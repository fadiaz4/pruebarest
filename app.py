from flask import Flask
from flask_restful import Api
from resources.medicinas_resource import Medicinas
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Medicinas, "/medicinas/<int:idmedicinas>")

if __name__ == "__main__":
    app.run(debug=True)
