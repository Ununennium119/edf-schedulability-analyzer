import math

from schedulability_analyze_report import ReportTable, ReportRow
from task import Task

from math import lcm
from functools import reduce


class EdfAnalyzer:
    def analyze_schedulability(self, tasks: list[Task]) -> ReportTable:
        hyper_period = self._calculate_hyper_period(tasks)
        max_deadline = max(tasks, key=lambda task: task.deadline).deadline
        l_star = self._calculate_l_star(tasks)
        max_time_to_check = min(float(hyper_period), max(float(max_deadline), l_star))

        # Check schedulability
        report_table = ReportTable()
        times_to_check: list[int] = self._get_times_to_check(tasks, max_time_to_check)
        for time in times_to_check:
            demand_function = self._calculate_demand_function(tasks, time)
            report_row = ReportRow(
                time=time,
                demand_function=demand_function,
                is_ok=demand_function <= time
            )
            report_table.add_row(report_row)

        return report_table

    def _calculate_hyper_period(self, tasks: list[Task]) -> int:
        periods: list[int] = [task.period for task in tasks]
        return int(reduce(lcm, periods))

    def _calculate_l_star(self, tasks: list[Task]) -> float:
        utilization = sum([task.execution_time / task.period for task in tasks])
        l_star: float = sum([(task.period - task.deadline) * task.execution_time / task.period for task in tasks])
        l_star /= (1 - utilization)
        return l_star

    def _get_times_to_check(self, tasks: list[Task], max_time_to_check: float) -> list[int]:
        times_to_check: list[int] = []
        for task in tasks:
            current_deadline = task.deadline
            while current_deadline <= max_time_to_check:
                times_to_check.append(current_deadline)
                current_deadline += task.period
        times_to_check = list(set(times_to_check))
        times_to_check.sort()
        return times_to_check

    def _calculate_demand_function(self, tasks: list[Task], time: int) -> int:
        demand_function = 0
        for task in tasks:
            demand_function += math.floor((time + task.period - task.deadline) / task.period) * task.execution_time
        return demand_function
