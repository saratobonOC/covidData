import requests
from typing import List, Dict
from datetime import datetime

class CovidDataService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        
    def get_countries_data(self, countries: List[str]) -> List[Dict]:
        url = f"{self.base_url}/countries_data"
        response = requests.get(url, params={"countries": ",".join(countries)})
        
        if response.status_code != 200:
            raise Exception("Error al obtener los datos de los países")
        
        data = response.json()
        return data
    
    def get_countries_historic_data(self, countries: List[str], start_date: datetime, end_date: datetime) -> List[Dict]:
        url = f"{self.base_url}/countries_historic_data"
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")
        
        response = requests.get(url, params={
            "countries": ",".join(countries),
            "start_date": start_date_str,
            "end_date": end_date_str
        })
        
        if response.status_code != 200:
            raise Exception("Error al obtener los datos históricos de los países")
        
        data = response.json()
        return data
