import json

from task import Task
from edf_analyzer import EdfAnalyzer


def main():
    tasks: list[Task] = list()
    with open('input.json', 'r') as file:
        data = json.load(file)
        for row in data:
            task = Task(
                task_id=row['id'],
                execution_time=row['execution_time'],
                deadline=row['deadline'],
                period=row['period'],
            )
            tasks.append(task)
    edf_analyzer = EdfAnalyzer()
    report_table = edf_analyzer.analyze_schedulability(tasks)
    print(report_table)


if __name__ == '__main__':
    main()
