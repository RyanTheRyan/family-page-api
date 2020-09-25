from . import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    banner_image_url = db.Column(db.String())
    content = db.Column(db.String())
    status = db.Column(db.String(10))
    published_date = db.Column(db.String(50))
    
class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(250))