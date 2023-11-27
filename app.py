from flask import Flask, request, render_template, jsonify, redirect
from  models import db, Cupcake, connect_db
import requests

app  = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SERVER_NAME']= 'http://localhost:5000'
app.config['SECRET_KEY'] = 'userisactivated'
app.app_context().push()

connect_db(app)


@app.route('/')
def list_page():
    cupcakes = Cupcake.query.all()
    return render_template('create.html', cupcakes=cupcakes)

#############################################################################
# This line allows us to collect all of the cupcakes and returns them into Json #  
#############################################################################

@app.route('/api/cupcakes')
def all_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

#############################################################################
# This line of code is sellecting a todo by id(returning 1 todo)
#############################################################################

@app.route('/api/cupcake/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

#############################################################################
# This line of code allows us to use the HTTP method "PATCH" to update a cupcake
#############################################################################

@app.route('/api/cupcake/<int:id>/update', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
# This line of code is reteriving JSON by using the method get from the key value "flavor". This effectively updates the flavor of the existing todo object.
    cupcake.flavor = request.json.get('flavor',cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating= request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    create = jsonify(cupcake=cupcake.serialize())
    return redirect(create)

#########################################################################################
# This line of code allows us to delete a cupcake, we will also use javaScript to delete.
#########################################################################################

@app.route('/api/cupcake/<int:id>/delete', methods=['DELETE'])
def delete_cupcake(id):
    delete_cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(delete_cupcake)
    db.session.commit()
    return jsonify(message="DELETED")

#############################################################################
# This line of code allows us to create a todo 
#############################################################################

@app.route('/api/cupcake/create', methods=['POST'])
def create_cupcake():
# this line we are creating a new instance(new object) of Cupcake class.
# Then we are providing the values in the Cupcake class to create a new cupcake.
# lastly, taking we are taking the key values from the JSON data and adding the new key values like flavor, size, rating, and image.    
    new_cupcake = Cupcake(flavor=request.json["flavor"],
                          size=request.json["size"],
                          rating=request.json["rating"],
                          image=request.json["image"]
                          )
# This line of code is now adding the new_cupcake instance to the data_bases session   
    db.session.add(new_cupcake)
    db.session.commit()
# we are now responding back with JSON.     
    respond_back_json = jsonify(cupcake=new_cupcake.serialize())
# we are returning the information and also makign sure our status code is 201 when using the method "POST".
    return render_template(respond_back_json, 201)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)