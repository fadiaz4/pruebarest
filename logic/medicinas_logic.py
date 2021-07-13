from core.pyba_logic import PybaLogic

class MedicinasLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # getmedicinas
    def getMedicinasById(self, idmedicinas):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_1e671166cbafeed.medicinas where idmedicinas={idmedicinas};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return {}

    #getallmedicinas
    def getAllMedicinas(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM heroku_1e671166cbafeed.medicinas;"
        results = database.executeQuery(sql)
        return results


    # post
    def getMedicinasByPreciosMed(self, preciosmed):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_1e671166cbafeed.medicinas where PreciosMed='{preciosmed}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []
