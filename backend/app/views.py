from flask import Blueprint, jsonify, request, session
from app.models import Medicine, User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras


views = Blueprint('views', __name__)


conn = psycopg2.connect(
    'dbname=quickmed user=brian password=12345 host=localhost')

@views.route('/')
def home():
    secure_password = generate_password_hash('123456')
    print(secure_password)
    if 'email' in session:
        email = session['email']
        return jsonify({'message' : 'You are already logged in', 'email' : email})
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp
    
@views.route('/register', methods=["POST"])
def sign_up():
    user_data = request.get_json()
    user = User(firstname=user_data['firstname'], lastname=user_data['lastname'], email=user_data['email'],
                allergy=user_data['allergy'], pass_secure=generate_password_hash(user_data['pass_secure']))
    db.session.add(user)
    db.session.commit()
    return jsonify(user_data)


@views.route('/login', methods=["POST"])
def login():
    _json = request.json
    _email = _json['email']
    _password = _json['password']
    if _email and _password:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "SELECT * FROM users WHERE email=%s"
        sql_where = (_email,)

        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        email = row['email']
        password = row['pass_secure']
        if row:
            if check_password_hash(password, _password):
                session['email'] = email
                cursor.close()
                return jsonify({'message' : 'You are logged in successfully'})
            else:
                resp = jsonify({'message' : 'Wrong password '})
                resp.status_code = 400
                return resp
        else:
            resp = jsonify({'message' : 'invalid details'})
            resp.status_code = 400
            return resp
    
@views.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
    return jsonify({'message' : 'You successfully logged out'})
        
        


@views.route('/medicine', methods=["GET"])
def get_medicine():

    all_medicine = Medicine.query.all()
    output = []
    for medicine in all_medicine:
        currMedicine = {}
        currMedicine['id'] = medicine.id
        currMedicine['name'] = medicine.name
        currMedicine['price'] = medicine.price
        currMedicine['manufacturer'] = medicine.manufacturer
        currMedicine['description'] = medicine.description
        currMedicine['category_id'] = medicine.category_id
        output.append(currMedicine)
    return jsonify(output)


@views.route('/medicine', methods=["POST"])
def put_medicine():
    med_data = request.get_json()
    medicine = Medicine(name=med_data['name'], price=med_data['price'], manufacturer=med_data['manufacturer'],
                        description=med_data['description'], category_id=med_data['category_id'])
    db.session.add(medicine)
    db.session.commit()
    return jsonify(med_data)


@views.route('/medicine/prescription', methods=["GET"])
def pres_medicine():
    prescription = Medicine.query.filter_by(category_id=1).all()
    output = []
    for medicine in prescription:
        currMedicine = {}
        currMedicine['id'] = medicine.id
        currMedicine['name'] = medicine.name
        currMedicine['price'] = medicine.price
        currMedicine['manufacturer'] = medicine.manufacturer
        currMedicine['description'] = medicine.description
        currMedicine['category_id'] = medicine.category_id
        output.append(currMedicine)
    return jsonify(output)


@views.route('/medicine/otc', methods=["GET"])
def otc_medicine():
    otc = Medicine.query.filter_by(category_id=2).all()
    output = []
    for medicine in otc:
        currMedicine = {}
        currMedicine['id'] = medicine.id
        currMedicine['name'] = medicine.name
        currMedicine['price'] = medicine.price
        currMedicine['manufacturer'] = medicine.manufacturer
        currMedicine['description'] = medicine.description
        currMedicine['category_id'] = medicine.category_id
        output.append(currMedicine)
    return jsonify(output)
