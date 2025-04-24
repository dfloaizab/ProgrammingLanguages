from ToDoList_Model import TaskModel
from ToDoList_Controller import TaskController
from ToDoList_View import TaskView

if __name__ == "__main__":
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model=model,view=view)
    controller.runController()