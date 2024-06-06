from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    homeworld = db.Column(db.String(256))
    current_location = db.Column(db.Integer, db.ForeignKey('planet.id'))
    

    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "homeworld": self.homeworld,
            "current_location": self.current_location,
            # do not serialize the password, its a security breach
        }
    

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    biome = db.Column(db.String(256), nullable=False)
    population = db.relationship('Person', backref='resident', lazy='dynamic')

    

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "biome": self.biome,
            # do not serialize the password, its a security breach
        }
    
    