from app import create_app

app = create_app()
with app.app_context():
    from extensions import db
    db.create_all()
    print('Database tables created successfully')
