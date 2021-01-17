import time


class Task:
    """Task class to help run methods at specified times.
    Tasks have a target 'action' - a method to be called - which should be run at or after due_at."""

    def __init__(self, action, due_at):
        self.action = action
        self.due_at = due_at
        self.completed = False

    def run_if_due(self):
        now = time.time()
        due = now >= self.due_at
        if due and not self.completed:
            self.action()
            self.completed = True


class Schedule:
    """Schedule class to create and organize tasks."""

    def __init__(self):
        self.tasks = []

    def remove_completed_tasks(self):
        """Remove from schedule tasks that have run."""
        for i in range(len(self.tasks) - 1, -1, -1):
            if self.tasks[i].completed:
                del self.tasks[i]
            #
        #

    def run_due_tasks(self):
        for task in self.tasks:
            task.action()
        self.remove_completed_tasks()