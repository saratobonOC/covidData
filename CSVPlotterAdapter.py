from typing import Any

class CSVPlotterAdapter(IDataPlotter):
    def __init__(self, csv_plotter: CSVPlotter):
        self.csv_plotter = csv_plotter
        
    def plot_data(self, csv_data: str) -> Any:
        return self.csv_plotter.plot_data(csv_data)
