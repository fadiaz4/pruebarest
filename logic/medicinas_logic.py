from core.pyba_logic import PybaLogic

class MedicinasLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # get
    def getMedicinasById(self, idmedicinas):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_1e671166cbafeed.medicinas where idmedicinas={idmedicinas};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return {}

    # post
    def getMedicinasByPreciosMed(self, preciosmed):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_1e671166cbafeed.medicinas where PreciosMed='{preciosmed}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []
