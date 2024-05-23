class Task:
    def __init__(self, task_id: str, execution_time: int, deadline: int, period: int):
        self.task_id: str = task_id
        self.execution_time: int = execution_time
        self.deadline: int = deadline
        self.period: int = period

    def __repr__(self):
        return self.task_id
