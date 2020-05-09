from api.utils.database import db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from passlib.hash import pbkdf2_sha256 as sha256
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    username = db.Column(db.String(120), nullable=False,unique=True)
    password = db.Column(db.String(120),nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password,hash):
        return sha256.verify(password,hash)
class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String()