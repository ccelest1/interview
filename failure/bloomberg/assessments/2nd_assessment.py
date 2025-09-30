# For a body of tasks that are either done or not done, implement a basic to-do list interface.

# You will be provided with an isDone function that takes a task id and checks whether or not the task is done. Tasks may change to done at any time.

# Your implementation should support the following methods:

# addTask - which takes in a task id and adds that task to the to-do list,
# deleteTask - which removes a task from the list by its id,
# getTasksToDo - which returns all tasks in the to-do list that are currently not done,
# getAllTasks - which returns all tasks in the to-do list, done or not done
# isDone(taskId) -> boolean
"""
implied task class, isDone
(1) class ToDoList
    tasks -> []
(2) def addTask - > appeding to tasks, accept param of id: int
(3) def deleteTask -> id param, ask what tasks pertaining to id (), preserve insertion order
(4) getTasksToDo -> iterate self.tasks, if not ISdoNE(TASK) -> APPEND done [], return done to user
(5) get allTasks -> return self.tasks
"""


class Task:
    def __init__(self, id):
        self.id = id
        self.isDone = None


class ToDoList:
    def __init__(self):
        # self.tasks = []
        """
        self.counter = 0
        """
        # could've been refactored to this
        self.tasks = {
            "byId": {
                1: {
                    # task1
                },
                2: {
                    # task2
                },
                3: {
                    # task3
                },
            },
            # ordering
            "allIds": [1, 2, 3],
        }
        """
        self.head = None
        self.tail = None
        self.length = 0
        """

    def markDone(self, id):
        counter = 0
        while counter <= self.tasks - 1:
            if self.tasks[counter].id is not id:
                if counter < len(self.tasks) - 1:
                    counter += 1
                if counter == len(self.tasks) - 1:
                    return f"tasks with id of {id} is not in db"
            if self.tasks[counter].id is id:
                self.tasks[counter].isDone = True
        return

    def addTask(self, id):
        if id in self.tasks:
            return f"task with {id} already exists, please enter a different id"
        # handling duplicates
        self.tasks.append(id)
        """
        if not self.head:
            self.head = Task
        if self.head and length==1:
            self.head.next = Task
        """

    def deleteTask(self, id):
        # conditional
        if not self.tasks:
            return
        if id not in self.tasks:
            return f"id not in tasks"
        for task in self.tasks:
            if task == id:
                index = self.tasks.index(task)
        self.tasks.pop(index)
        """
        tracker = 0 (understand insertion) +=1 (add tasks)
        tasks = {}
        ask if tasks[task] = [tracker, isDone(task)]
        if tasks[task] = id: del tasks[task]
        """
        return f"{prev} is now deleted"

    def getTasksToDo(self):
        """ """
        toDo = []
        # self.tasks = {}
        for task in self.tasks:
            if not self.markDone(task):
                toDo.append(task)
        return toDo

    def getAllTasks(self):
        """
        return sorted(self.tasks.keys, key=lambda x:x[1], reverse=True)
        """
        return sorted(self.tasks.keys(), key=lambda x: x, reverse=True)
