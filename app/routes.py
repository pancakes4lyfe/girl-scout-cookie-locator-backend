from flask import Blueprint, request, jsonify
from app import db
from .models.pin import Pin
from datetime import datetime
import requests
import os

pins_bp = Blueprint("pins", __name__, url_prefix="/pins")

#---------------------# HELPER FUNCTIONS #---------------------#

def invalid_input():
    return jsonify({"details":"Invalid data"}), 400


#---------------------# DECORATORS #---------------------#

def pin_not_found(func):
    def inner(pin_id):
        if Pin.query.get(pin_id) is None:
            return jsonify(None), 404
        return func(pin_id)
    #renames the function for each wrapped endpoint to avoid endpoint conflict
    inner.__name__ = func.__name__
    return inner


#---------------------# PIN ENDPOINTS #---------------------#

@pins_bp.route("", methods=["GET"], strict_slashes=False)
def pins_index():
    pins = Pin.query.all()
    pins_response = [pin.to_json() for pin in pins]
    return jsonify(pins_response), 200

@pins_bp.route("/<pin_id>", methods=["GET"], strict_slashes=False)
@pin_not_found
def single_pin(pin_id):
    pin = Pin.query.get(pin_id)
    return jsonify(pin.to_json()), 200


@pins_bp.route("", methods=["POST"], strict_slashes=False)
def create_pin():
    request_body = request.get_json()

    # if "hours" not in request_body:
    #     request_body["hours"] = "Unknown"
    # if "cookies_available" not in request_body:
    #     request_body["cookies_available"] = "Unknown"
    # if "notes" not in request_body:
    #     request_body["notes"] = ""

    new_pin = Pin(lat_lon = request_body["lat_lon"] 
                    # pinned_at = request_body["pinned_at"], 
                    # hours = request_body["hours"],
                    # cookies_available = request_body["cookies_available"],
                    # notes = request_body["notes"],
                    # upvote_count = 0
                )
    db.session.add(new_pin)
    db.session.commit()

    return jsonify(new_pin.to_json()), 201

@pins_bp.route("/<pin_id>", methods=["PUT"], strict_slashes=False)
@pin_not_found
def update_pin(pin_id):
    pin = Pin.query.get(pin_id)
    response_body = request.get_json()
    pin.lat_lon = response_body["lat_lon"]

    db.session.commit()
    return jsonify(pin.to_json()), 200

@pins_bp.route("/<pin_id>", methods=["DELETE"], strict_slashes=False)
@pin_not_found
def delete_pin(pin_id):
    pin = Pin.query.get(pin_id)
    db.session.delete(pin)
    db.session.commit()
    return jsonify({"details":f'pin {pin.id} "{pin.lat_lon}" successfully deleted'}), 200