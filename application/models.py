from . import db
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_col = db.Column(db.String(10000))
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    editing = db.Column(db.Boolean, default=False)  
    completed = db.Column(db.Boolean, default=False)  

    
