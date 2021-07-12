from flask import Flask
from flask_restful import Api
from resources.medicinas_resource import Medicinas

app = Flask(__name__)
api = Api(app)

api.add_resource(Medicinas, "/medicinas/<int:idmedicinas>")

if __name__ == "__main__":
    app.run(debug=True, port=23512)
