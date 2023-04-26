import matplotlib.pyplot as plt
import pandas as pd
import io
from typing import Any

class CSVPlotter:
    def plot_data(self, csv_data: str) -> Any:
        data = io.StringIO(csv_data)
        df = pd.read_csv(data)
        
        plt.figure()
        plt.plot(df['date'], df['cases'], label='Casos confirmados')
        plt.plot(df['date'], df['deaths'], label='Muertes')
        plt.xlabel('Fecha')
        plt.ylabel('Cantidad')
        plt.title('Evolución del COVID-19')
        plt.legend()
        
        image = io.BytesIO()
        plt.savefig(image, format='png')
        plt.close()
        
        image.seek(0)
        return image
