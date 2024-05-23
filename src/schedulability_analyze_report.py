class ReportRow:
    def __init__(self, time: int, demand_function: float, is_ok: bool):
        self.time: int = time
        self.demand_function: float = demand_function
        self.is_ok: bool = is_ok

    def __repr__(self):
        return f"{self.time:<6}\t|{self.demand_function:<12}\t|{'OK' if self.is_ok else 'FAILED':<12}"


class ReportTable:
    def __init__(self):
        self.rows: list[ReportRow] = list()

    def add_row(self, row: ReportRow):
        self.rows.append(row)

    def __repr__(self):
        return f"{'L':<6}\t|{'g(0, L)':<12}\t|{'Result':<12}\n" + "\n".join([str(row) for row in self.rows])
