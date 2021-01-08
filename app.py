from flask import Flask, request, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Strain

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///strains_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'weed'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/api/strains')
def list_strains():
    all_strains = [strain.serialize() for strain in Strain.query.all()]
    return jsonify(all_strains)

@app.route('/api/strains', methods=['POST'])
def create_strain():
    new_strain = Strain(name=request.json["name"], variety=request.json["variety"], thc_content=request.json["thc_content"], description=request.json["description"])
    db.session.add(new_strain)
    db.session.commit()
    resp_json = jsonify(strain=new_strain.serialize())
    return (resp_json, 201)

@app.route('/api/strains/<int:s_id>')
def get_strain(s_id):
    strain = Strain.query.get_or_404(s_id)
    return jsonify(strain=strain.serialize())

@app.route('/api/strains/<int:s_id>', methods=["PATCH"])
def update_strain(s_id):
    strain = Strain.query.get_or_404(s_id)
    
    strain.name = request.json.get('name', strain.name)
    strain.variety = request.json.get('variety', strain.variety)
    strain.thc_content = request.json.get('thc_content', strain.thc_content)
    strain.description = request.json.get('description', strain.description)
    resp_json = jsonify(strain=strain.serialize())
    return resp_json

@app.route('/api/strains/<int:s_id>', methods=["DELETE"])
def delete_strain(s_id):
    strain = Strain.query.get_or_404(s_id)
    db.session.delete(strain)
    db.session.commit()
    return jsonify(message="deleted")

