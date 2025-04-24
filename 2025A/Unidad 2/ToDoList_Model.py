class TaskModel:

    def __init__(this):
        this._tasks = []

    def addTask(this,task):
        this._tasks.append(task)

    def remove(this, index):
        #el índice la tarea a remover es válido:
        if  0 <=  index < len(this._tasks):
            return this._tasks.pop(index)
        return None

    def listTasks(this):
        return this._tasks