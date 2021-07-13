from flask_restful import Resource, reqparse
from logic.medicinas_logic import MedicinasLogic


class Medicina(Resource):
    def __init__(self):
        self.medicinas_put_args = self.createParser()
        self.logic = MedicinasLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombremed", type=str, help="nombre de la medicina")
        args.add_argument("preciosmed", type=str, help="precio de la medicina")
        args.add_argument("casa farmaceutica", type=str, help="casa farmaceutica de la medicina")
        args.add_argument("principio activo", type=str, help="principio activo de la medicina")
        return args

    def get(self, idmedicinas):
        result = self.logic.getMedicinasById(idmedicinas)
        return result, 200

    def post(self, idmedicinas):
        medicinasDict = self.logic.getMedicinasById(idmedicinas)
        preciosMed = medicinasDict["preciosmed"]
        result = self.logic.getMedicinasByPreciosMed(preciosMed)
        return result, 200
