from app import db, create_user, app

with app.app_context():
    db.create_all()
    create_user('shetyebhakti', 'shetye@1234', is_admin=True)