import json

import requests
from flask import Flask, Response

airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "14MI":{"Name": "East-West Paris Airport", "Location": "Dutton"},
    "CLC2": {"Name": "London / Chapeskie Field Airport", "Location": "London"},
    "ESKN": {"Name": "Stockholm Skavsta Airport", "Location": "Stockholm / Nykoping"},
}
app = Flask(__name__)
@app.route('/airport/<iCAO>')
def c(iCAO):
    try:
        response = {
            "ICAO" : iCAO,
            "Name": airport_database[iCAO]["Name"],
            "Location": airport_database[iCAO]["Location"],
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)