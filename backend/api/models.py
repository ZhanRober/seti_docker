import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'
    firstname = db.Column(db.String(100), primary_key=True, nullable=False)
    lastname = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Player {self.firstname} {self.lastname}>"

    def to_dict(self):
        """Converts the Player instance into a dictionary."""
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
        }

def to_dict(obj):
    """Converts a SQLAlchemy model instance into a dictionary."""
    if isinstance(obj.__class__, DeclarativeMeta):
        # Check if the object is an SQLAlchemy model
        fields = {}
        for field in dir(obj):
            # Skip internal properties and metadata
            if not field.startswith("_") and field != "metadata":
                data = getattr(obj, field)
                try:
                    json.dumps(data)  # Ensures the value is JSON serializable
                    if data is not None:
                        fields[field] = data
                except (TypeError, ValueError):
                    pass  # Skip non-serializable fields
        return fields
    return None  # Return None if the object is not an SQLAlchemy model