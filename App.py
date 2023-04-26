from typing import List, Tuple, Any
from datetime import datetime

class App:
    def __init__(self, data_service: CovidDataService, plotter: IDataPlotter):
        self.data_service = data_service
        self.plotter = plotter
        
    def get_countries_data(self, countries: List[str]) -> List[Tuple[str, Any]]:
        data = self.data_service.get_countries_data(countries)
        images = []
        
        for country_data in data:
            csv_data = self.convert_to_csv(country_data)
            image = self.plotter.plot_data(csv_data)
            images.append((country_data['country'], image))
            
        return images
    
    def get_countries_historic_data(self, countries: List[str], start_date: datetime, end_date: datetime) -> List[Tuple[str, Any]]:
        data = self.data_service.get_countries_historic_data(countries, start_date, end_date)
        images = []
        
        for country_data in data:
            csv_data = self.convert_to_csv(country_data)
            image = self.plotter.plot_data(csv_data)
            images.append((country_data['country'], image))
            
        return images
    
    def convert_to_csv(self, data: dict) -> str:
        # Aquí se implementaría la conversión de los datos JSON a formato CSV.
        pass
