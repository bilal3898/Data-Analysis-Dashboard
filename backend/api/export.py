from flask import Blueprint, request, jsonify, send_file
import pandas as pd
from io import BytesIO
from backend.models.dataset_model import DataSet

export_bp = Blueprint('export', __name__)

@export_bp.route('/export', methods=['POST'])
def export_data():
    try:
        data = request.get_json()
        dataset_id = data.get('dataset_id')
        export_format = data.get('format', 'csv')
        
        if not dataset_id:
            return jsonify({'error': 'Dataset ID is required'}), 400
            
        dataset = DataSet.query.get(dataset_id)
        if not dataset:
            return jsonify({'error': 'Dataset not found'}), 404
            
        df = pd.read_json(dataset.data)
        buffer = BytesIO()
        
        if export_format == 'csv':
            df.to_csv(buffer, index=False)
            mimetype = 'text/csv'
            filename = f'export_{dataset_id}.csv'
        elif export_format == 'json':
            df.to_json(buffer, orient='records')
            mimetype = 'application/json'
            filename = f'export_{dataset_id}.json'
        elif export_format == 'excel':
            df.to_excel(buffer, index=False)
            mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            filename = f'export_{dataset_id}.xlsx'
        else:
            return jsonify({'error': 'Unsupported export format'}), 400
            
        buffer.seek(0)
        return send_file(
            buffer,
            mimetype=mimetype,
            as_attachment=True,
            download_name=filename
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500