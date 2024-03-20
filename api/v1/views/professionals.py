#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.professional import Professional
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from models.city import City
from flask import current_app


@app_views.route('/professionals', methods=['GET'], strict_slashes=False)
@swag_from('documentation/professional/all_professionals.yml')
def get_professionals():
    """
    Retrieves the list of all professional objects
    or a specific user
    """
    all_professionals = storage.all(Professional).values()
    list_professionals = []
    for professional in all_professionals:
        list_professionals.append(professional.to_dict())
    return jsonify(list_professionals)


@app_views.route('/professionals/<professional_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/professional/get_professional.yml', methods=['GET'])
def get_professional(professional_id):
    """ Retrieves an professional """
    professional = storage.get(Professional, professional_id)
    if not professional:
        abort(404)

    return jsonify(professional.to_dict())

@app_views.route('/professionals/city/<city_name>', methods=['GET'], strict_slashes=False)
def get_professionals_by_city_name(city_name):
    current_app.logger.info(f"Recherche de professionnels pour la ville : {city_name}")

    city = next((city_obj for city_obj in storage.all(City).values() if city_obj.name.lower() == city_name.lower()), None)

    if city is None:
        current_app.logger.error(f"Ville non trouvée : {city_name}")
        return jsonify({"error": "City not found"}), 404

    current_app.logger.info(f"Ville trouvée : {city.name} avec ID {city.id}")

    professionals_in_city = []
    for professional in storage.all(Professional).values():
        current_app.logger.info(f"Vérification du professionnel : {professional.first_name}, City ID: {professional.city_id}")
        if str(professional.city_id) == str(city.id):  # Convertit en chaîne pour une comparaison sûre
            professionals_in_city.append(professional.to_dict())

    if not professionals_in_city:
        current_app.logger.error(f"Aucun professionnel trouvé pour la ville : {city_name}")
        return jsonify({"error": "No professionals found for the given city name"}), 404

    return jsonify(professionals_in_city)




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
    data = request.get_json()

    if not data:
        abort(400, description="Not a JSON")

    for field in ['email', 'password', 'city_id']:
        if field not in data:
            abort(400, description=f"Missing {field}")

    if not storage.get(City, data['city_id']):
        abort(404, description="City not found")
        
    instance = Professional(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/professionals/exist', methods=['POST'], strict_slashes=False)
def check_professional_existence():
    """
    Check if a professional exists by email
    """
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({"error": "Missing email"}), 400

    email = data['email']
    all_professionals = storage.all(Professional).values()
    for professional in all_professionals:
        if professional.email == email:
            # Found a professional with the given email
            return jsonify({"exists": True, "professional_id": professional.id}), 200

    # No professional found with the given email
    return jsonify({"exists": False}), 404


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

    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(professional, key, value)
    storage.save()
    return make_response(jsonify(professional.to_dict()), 200)