from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Strain(db.Model):
    """Weed instance"""
    
    __tablename__ = "strains"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    variety = db.Column(db.String, unique=False, nullable=False)
    thc_content = db.Column(db.Float, unique=False, nullable=False, default=0.00)
    description = db.Column(db.String, unique=False, nullable=False, default="More details coming soon!")
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'variety': self.variety,
            'thc_content': self.thc_content,
            'description': self.description
        }
    
    def __repr__(self):
        return f"<Strain {self.id} name={self.name} variety={self.variety} thc content={self.thc_content} description={self.description}"
    
