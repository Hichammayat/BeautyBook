#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Professionals """
from models.professional import Professional
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/professionals', methods=['GET'], strict_slashes=False)
@swag_from('documentation/professional/all_prodfessionals.yml')
def get_professionals():
    """
    Retrieves the list of all professionals objects
    """
    all_professionals = storage.all(Professional).values()
    list_professionals = []
    for professional in all_professionals:
        list_professionals.append(professional.to_dict())
    return jsonify(list_professionals)


@app_views.route('/professionals/<professional_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/professional/get_professional.yml', methods=['GET'])
def get_professional(professional_id):
    """ Retrieves a professional """
    professional = storage.get(Professional, professional_id)
    if not professional:
        abort(404)

    return jsonify(professional.to_dict())


@app_views.route('/professionals/<professional_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/professional/delete_professional.yml', methods=['DELETE'])
def delete_professional(professional_id):
    """
    Deletes a professional Object
    """

    professional = storage.get(Professional, professional_id)

    if not professional:
        abort(404)

    storage.delete(professional)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/professionals', methods=['POST'], strict_slashes=False)
@swag_from('documentation/professional/post_professional.yml', methods=['POST'])
def post_professional():
    """
    Creates a professional
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'biography' not in request.get_json():
        abort(400, description="Missing biography")
    if 'work_hours' not in request.get_json():
        abort(400, description="Missing work_hours")

    data = request.get_json()
    instance = Professional(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/professionals/<professional_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/professional/put_professional.yml', methods=['PUT'])
def put_professional(professional_id):
    """
    Updates a professional
    """
    professional = storage.get(Professional, professional_id)

    if not professional:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)