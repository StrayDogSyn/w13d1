import tkinter as tk
from datetime import datetime, timedelta
import random

from WeatherChartComponent import WeatherChartComponent  # assumes same folder

class SimpleWeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Weather Demo")
        self.root.geometry("800x600")

        # Dummy data
        start_date = datetime.today()
        self.dates = [(start_date + timedelta(days=i)).strftime("%m/%d") for i in range(7)]
        self.humidity = [random.randint(30, 90) for _ in range(7)]
        self.precipitation = [round(random.uniform(0, 2.5), 1) for _ in range(7)]

        # Chart frame
        self.chart_frame = tk.Frame(root)
        self.chart_frame.pack(fill=tk.BOTH, expand=True)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack()

        tk.Button(button_frame, text="Show Humidity Chart", command=self.show_humidity_chart).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Show Precipitation Chart", command=self.show_precipitation_chart).pack(side=tk.LEFT, padx=5)

        self.show_humidity_chart()  # default view

    def show_humidity_chart(self):
        WeatherChartComponent.create_embedded_chart(
            parent_frame=self.chart_frame,
            chart_type='line',
            dates=self.dates,
            data=self.humidity,
            title='7-Day Humidity Levels',
            ylabel='Humidity (%)',
            color='#3498DB'
        )

    def show_precipitation_chart(self):
        WeatherChartComponent.create_embedded_chart(
            parent_frame=self.chart_frame,
            chart_type='bar',
            dates=self.dates,
            data=self.precipitation,
            title='7-Day Precipitation Forecast',
            ylabel='Precipitation (inches)',
            color='#2980B9'
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleWeatherApp(root)
    root.mainloop()
