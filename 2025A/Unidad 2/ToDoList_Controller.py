from ToDoList_Model import TaskModel
from ToDoList_View import TaskView

class TaskController:

    def __init__(this, model:TaskModel, view:TaskView):
        this._model = model
        this._view = view

    def addTask(this):
        #captura información de la vista:
        newTask = this._view.promptForAdd()
        #actualiza el modelo con lo que la vista devuelve:
        this._model.addTask(newTask)
        this._view.showMessage("La tarea ha sido agregada")

    #Completar:
    def removeTask(this):
        pass

    #Completar:
    def showTasks(this):
        pass

    #Menú del controlador
    def runController(self):
        while True:
            self._view.showAllTasks(self._model.listTasks())
            action = input("\n[1] Agregar  [2] Eliminar  [3] Salir\n> ")
            if action == '1':
                self.addTask()
            elif action == '2':
                self.removeTask()
            elif action == '3':
                self._view.showMessage("¡Adiós!")
                break
            else:
                self._view.showMessage("Opción no válida.")
