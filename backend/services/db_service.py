from backend.models.dataset_model import db, Dataset

def add_dataset(name, file_path):
    dataset = Dataset(name=name, file_path=file_path)
    db.session.add(dataset)
    db.session.commit()
    return dataset.to_dict()

def get_all_datasets():
    return [dataset.to_dict() for dataset in Dataset.query.all()]
