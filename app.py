from flask import Flask
from flask_restful import Api
from resources.medicina_resource import Medicina
from resources.medicinas_resource import Medicinas
from resources.hospital_resource import Hospital
from resources.hospitales_resource import Hospitales


app = Flask(__name__)
api = Api(app)

api.add_resource(Medicina,"/medicinas/<int:idmedicinas>")

api.add_resource(Medicinas, "/medicinas")

api.add_resource(Hospital,"/hospitales/<int:idhospital>")

api.add_resource(Hospitales, "/hospitales")


if __name__ == "__main__":
    app.run(debug=True)
