from flask_restful import Resource, reqparse
from logic.empresas_logic import EmpresasLogic


class Empresa(Resource):
    def __init__(self):
        self.empresas_put_args = self.createParser()
        self.logic = EmpresasLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombreempre", type=str, help="nombre de la empresa asociada")
        args.add_argument("servicioempre", type=str, help="servicios que ofrece la empresa asociada")
        args.add_argument("direccionempre", type=str, help="dirección de la empresa asociada")
        args.add_argument("telefonoempre", type=str, help="teléfono de la empresa asociada")
        return args

    def get(self, idempresas):
        result = self.logic.getEmpresasById(idempresas)
        return result, 200

    def post(self, idempresas):
        empresasDict = self.logic.getEmpresasById(idempresas)
        servicioEmpre = empresasDict["servicioempre"]
        result = self.logic.getEmpresasByServicioEmpre(servicioEmpre)
        return result, 200
