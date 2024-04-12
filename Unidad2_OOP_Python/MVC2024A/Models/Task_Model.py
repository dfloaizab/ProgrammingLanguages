class Task:

    def __init__(self, description, duration, project, developer):
        self.description = description
        self.duration = duration 
        self.project = project
        self.developer = developer
        self.finished = False

    def changeDuration(self, newDuration):
        self.duration = newDuration
        
    def finishTask(self):
        self.finished = True

    def toggleFinished(self):
        self.finished = not self.finished

    def getFinished(self):
        return self.finished
    
    def getDescription(self):
        return self.description

