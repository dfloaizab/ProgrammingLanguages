class TaskView:

    def __init__(self):
        pass

    def showAllTasks(self, tasks:list):
        pass

    def showFinishedTasks(self, tasks: list):
        for e in tasks:
            if e.getFinished():
                print(e.getDescription())
            

    def showUnfinishedTasks(self, tasks):
        for e in tasks:
            if not e.getFinished():
                print(e.getDescription())

    def getUserInput(self):
        return input("Ingrese el índice de la tarea:")

    def finishTask(self, numTask):
        pass

    def addTask(self, newTask):
        pass

    