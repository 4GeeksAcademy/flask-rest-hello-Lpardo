from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    favorites = db.relationship('Favorite', backref='user', lazy=True)
    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }
class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(20))
    gender = db.Column(db.String(50))
    favorites = db.relationship('Favorite', backref='character', lazy=True)
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender,
        }
    
class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    favorites = db.relationship('Favorite', backref='planet', lazy=True)
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
        }
class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
        }