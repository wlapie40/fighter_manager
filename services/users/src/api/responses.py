def response(status_code: int, message: str):
    return jsonify({"status_code": status_code, "message": message})
