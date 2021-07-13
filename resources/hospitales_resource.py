from flask_restful import Resource, reqparse
from logic.hospitales_logic import HospitalesLogic
class Hospitales(Resource):
    def get(self):
        logic = HospitalesLogic()
        result = logic.getAllHospitales()
        return result
