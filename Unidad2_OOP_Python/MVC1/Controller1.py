class DataController:


    def __init__(self, pModel, pView):
        self.model = pModel
        self.view = pView

    
    #método que va a ser consumido por la vista
    def consumeData(self):
        pass

    #método que va a notificar al modelo, generando cambios
    def changeData(self):
        pass
