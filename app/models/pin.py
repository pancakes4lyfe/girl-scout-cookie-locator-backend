from flask import current_app
from app import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class Pin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lat_lon = db.Column(db.String)
    pinned_at = db.Column(db.DateTime, nullable=True)
    hours = db.Column(db.String, nullable=True)
    cookies_available = db.Column(db.String, nullable=True)
    notes = db.Column(db.String, nullable=True)
    upvote_count = db.Column(db.Integer, nullable=True)
    __tablename__ = "pins"

    def to_json(self):
        cookie_types = self.cookies_available
        upvotes = self.upvote_count
        if not self.cookies_available:
            cookie_types = "N/A"
        if not self.upvote_count:
            upvotes = 0

        json_data = {
            "id": self.id,
            "lat_lon": self.lat_lon,
            "pinned_at": self.pinned_at,
            "hours": self.hours,
            "cookies_available": cookie_types,
            "notes": self.notes,
            "upvote_count": upvotes
        }
        return json_data

    def to_string(self):
        return f"{self.id}: Coordinates: {self.lat_lon}"