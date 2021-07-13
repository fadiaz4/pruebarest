from flask_restful import Resource, reqparse
from logic.hospitales_logic import HospitalesLogic


class Hospital(Resource):
    def __init__(self):
        self.hospitales_put_args = self.createParser()
        self.logic = HospitalesLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombrehosp", type=str, help="Nombre del Hospital")
        args.add_argument("municipiohosp", type=str, help="Municipio donde se encuentra el Hospital")
        args.add_argument("direccionhosp", type=str, help="Dirección exacta del Hospital")
        args.add_argument("telefonohosp", type=str, help="Telefono del Hospital")
        args.add_argument("especialidadeshosp", type=str, help="Especialidades que ofrece el Hospital")
        return args

    def get(self, idhospital):
        result = self.logic.getHospitalesById(idhospital)
        return result, 200

    def post(self, idhospital):
        hospitalesDict = self.logic.getHospitalesById(idhospital)
        municipioHosp = hospitalesDict["municipiohosp"]
        result = self.logic.getHospitalesByMunicipio(municipioHosp)
        return result, 200
