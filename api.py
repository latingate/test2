# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    # use the line below to run flask server directly (not recommended for production)
    app.run(host='0.0.0.0', port=5000, debug=True)
    # , use_reloader=False
    # , ssl_context = 'adhoc'
    # , ssl_context=('cert.pem', 'key.pem'))

    # use the line below to run flask through waitress server, and than run waitress_server.py from pycharm or directly from command line using: python waitress_server.py
    # app = Flask(__name__)

