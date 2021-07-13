from core.pyba_logic import PybaLogic

class EmpresasLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # getempresas
    def getEmpresasById(self, idempresas):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_1e671166cbafeed.empresas where idempresas={idempresas};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return {}

    #getallempresas
    def getAllEmpresas(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM heroku_1e671166cbafeed.empresas;"
        results = database.executeQuery(sql)
        return results


    # post
    def getEmpresasByServicioEmpre(self, servicioempre):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_1e671166cbafeed.empresas where ServicioEmpre='{servicioempre}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []
