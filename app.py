from flask import Flask
from flask_restful import Api
from resources.medicina_resource import Medicina
from resources.medicinas_resource import Medicinas


app = Flask(__name__)
api = Api(app)

api.add_resource(Medicina,"/medicinas/<int:idmedicinas>")

api.add_resource(Medicinas, "/medicinas")


if __name__ == "__main__":
    app.run(debug=True)
