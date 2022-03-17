from . import db
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    allergy = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.firstname}'


class Medicine(db.Model):
    __tablename__ = 'medicine'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    manufacturer = db.Column(db.String(255))
    description = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))


    def __repr__(self):
        return f'Medicine {self.name}'
    
class Category(db.Model):
    __tablename__ = 'category'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    medicine = db.relationship('Medicine', backref='category', lazy="dynamic")
    
    def __repr__(self):
        return f'Category {self.name}'

