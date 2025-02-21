from flask import Blueprint, request, jsonify
import pandas as pd
import numpy as np
from backend.models.dataset_model import DataSet

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/analyze', methods=['POST'])
def analyze_data():
    try:
        dataset_id = request.json.get('dataset_id')
        if not dataset_id:
            return jsonify({'error': 'Dataset ID is required'}), 400
            
        dataset = DataSet.query.get(dataset_id)
        if not dataset:
            return jsonify({'error': 'Dataset not found'}), 404
            
        df = pd.read_json(dataset.data)
        
        # Basic statistics
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        stats = {
            'summary': df[numeric_cols].describe().to_dict(),
            'correlations': df[numeric_cols].corr().to_dict(),
            'missing_values': df.isnull().sum().to_dict(),
            'column_types': df.dtypes.astype(str).to_dict(),
            'unique_values': {col: df[col].nunique() for col in df.columns}
        }
        
        # Time series analysis if date columns exist
        date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
        if date_cols:
            stats['time_series'] = {
                col: {
                    'min_date': df[col].min().isoformat(),
                    'max_date': df[col].max().isoformat(),
                    'date_range': (df[col].max() - df[col].min()).days
                } for col in date_cols
            }
        
        return jsonify(stats), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500