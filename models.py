from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFUALT_URL_CUPCAKE = 'https://tinyurl.com/demo-cupcake'

class Cupcake(db.Model):

    __tablename__ = 'cupcakes'
    id = db.Column(db.Integer, autoincrement = True, nullable = False, primary_key = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Integer, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, nullable = False, default = DEFUALT_URL_CUPCAKE)

    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image 
        }
    def __repr__(self):
        return f"<Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating} image={self.image}>"