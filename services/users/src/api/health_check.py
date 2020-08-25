from flask import current_app as app
from flask import jsonify


@app.route('/users/healthcheck', methods=['GET'])
def health_check():
    return jsonify({"status_code": 200, "message": "OK"})
