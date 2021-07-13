from core.pyba_logic import PybaLogic

class HospitalesLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # get hospitales por id
    def getHospitalesById(self, idhospital):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_1e671166cbafeed.hospitales where idhospital={idhospital};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return {}

    #getallhospitales
    def getAllHospitales(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM heroku_1e671166cbafeed.hospitales;"
        results = database.executeQuery(sql)
        return results


    # post
    def getHospitalesByMunicipio(self, municipiohosp):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_1e671166cbafeed.hospitales where municipiohosp='{municipiohosp}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []
