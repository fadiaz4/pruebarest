from flask_restful import Resource, reqparse
from logic.empresas_logic import EmpresasLogic

class Empresas(Resource):
    def get(self):
        logic = EmpresasLogic()
        result = logic.getAllEmpresas()
        return result
