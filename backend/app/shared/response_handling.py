
from flask import jsonify

def get_response(status = 404, error = "not found", message = "invalid resource URI"):
    response = jsonify({'status': status,'error': error,
                            'message': message})
    response.status_code = 404
    return response