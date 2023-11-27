from models import db, connect_db, Cupcake
from app import app 

db.drop_all()
db.create_all()

Cupcakes = [
    Cupcake(flavor="vanila", size = 1, rating = 7, image= 'DEFUALT_URL_CUPCAKE')
]
