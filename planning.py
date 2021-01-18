import numpy as np
import time

import utils


class Task:
    """Task class to help run methods at specified times.
    Tasks have a target 'action' - a method to be called - which should be run at or after due_at, and a 'completed'
    flag, indicating whether the task has run."""

    def __init__(self, action, due_at):
        self.action = action
        self.due_at = due_at
        self.completed = False

    def run_if_due(self):
        """Run action if it's later than due_at."""
        now = time.time()
        due = now >= self.due_at
        if due and not self.completed:
            self.action()
            self.completed = True
        #

    def __str__(self):
        timestring = utils.format_epoch_time(self.due_at)
        funcstring = self.action.__name__
        s = "At time %s, run %s" % (timestring, funcstring)
        return s


class Agenda:
    """Agenda class to create and organize tasks."""

    def __init__(self):
        self.tasks = []

    def remove_completed_tasks(self):
        """Remove from agenda tasks that have run."""
        for i in range(len(self.tasks) - 1, -1, -1):
            if self.tasks[i].completed:
                del self.tasks[i]
            #
        #

    def __str__(self):
        s = "Agenda consisting of %d tasks." % len(self.tasks)
        if self.tasks:
            s += "\n" + "\n".join([str(task) for task in self.tasks[:5]])
        return s

    def add_task(self, task):
        """Adds a task to the agenda."""
        self.tasks.append(task)
        self.tasks.sort(key=lambda t: t.due_at)

    def run_due_tasks(self):
        """Runs all tasks that are past their due_at."""
        for task in self.tasks:
            task.run_if_due()
        self.remove_completed_tasks()

    def schedule_random(self, action, timespan_hours, n_events=1):
        """Schedules the input action to be called n_events times, distributed uniformly at random between now and
        timespan_hours hours into the future.
        for instance, schedule_random(somefun, 8, 10) schedules somefun to be called 10 times over the next 8 hours."""

        now = time.time()
        deadline = now + 3600*timespan_hours
        for _ in range(n_events):
            due_at = np.random.uniform(low=now, high=deadline)
            task = Task(action=action, due_at=due_at)
            self.add_task(task)
