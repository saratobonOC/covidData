from abc import ABC, abstractmethod
from typing import Any

class IDataPlotter(ABC):
    @abstractmethod
    def plot_data(self, csv_data: str) -> Any:
        pass
