from flask import Blueprint, request, jsonify
from app import db
from .models.pin import Pin
from datetime import datetime
import requests
import os

pins_bp = Blueprint("pins", __name__, url_prefix="/pins")

@pins_bp.route("", methods=["GET"], strict_slashes=False)
def pins_index():
    pins = Pin.query.all()
    pins_response = [pin.to_json() for pin in pins]
    return jsonify(pins_response), 200


@pins_bp.route("", methods=["POST"], strict_slashes=False)
def create_pin():
    request_body = request.get_json()

    if "hours" not in request_body:
        request_body["hours"] = "Unknown"
    if "cookies_available" not in request_body:
        request_body["cookies_available"] = "Unknown"
    if "notes" not in request_body:
        request_body["notes"] = ""

    new_pin = Pin(lat_lon = request_body["lat_lon"], 
                    pinned_at = datetime.utcnow, 
                    hours = request_body["hours"],
                    cookies_available = request["cookies_available"],
                    notes = request_body["notes"],
                    upvote_count = 0)
    db.session.add(new_pin)
    db.session.commit()

    return jsonify(new_pin.to_json()), 201