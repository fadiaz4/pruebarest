from flask_restful import Resource, reqparse
from logic.medicinas_logic import MedicinasLogic
class Medicinas(Resource):
    def get(self):
        logic = MedicinasLogic()
        result = logic.getAllMedicinas()
        return result
