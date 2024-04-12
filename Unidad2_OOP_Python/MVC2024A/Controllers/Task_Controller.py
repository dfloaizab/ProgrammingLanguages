from Views import Task_View
from Models import Task_Model

class TaskController:

    def __init__(self):

        #referencia al modelo:
        self.tasks = []

        #referencia a la vista 
        self.view = Task_View()

    def add_task(self, task):
        pass

    def toggle_task_fin(self, taskIndex):
        pass

    def showAllTasks(self):
        #llamar método en la vista:
        pass

    def runController(self):
        #mostrar todas las tareas en la vista:
        self.view.showAllTasks(self.tasks)

        #capturar entrada de la vista

        #actualizar el modelo

    

        

