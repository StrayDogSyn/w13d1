import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random
from datetime import datetime, timedelta

class WeatherVisualizationApp:
    """Weather application with integrated data visualization"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather Data Visualization App")
        self.root.geometry("1000x700")
        
        # Generate sample data
        self.generate_sample_data()
        
        # Set up the GUI
        self.setup_gui()
        
        print("Weather Visualization App initialized!")
    
    def generate_sample_data(self):
        """Generate sample weather data for visualization"""
        start_date = datetime.now()
        
        self.dates = []
        self.temperatures = []
        self.humidity = []
        self.precipitation = []
        
        for i in range(7):
            current_date = start_date + timedelta(days=i)
            self.dates.append(current_date.strftime("%m/%d"))
            
            # Generate realistic weather data
            temp = 70 + random.randint(-10, 15)
            self.temperatures.append(temp)
            
            humid = random.randint(30, 90)
            self.humidity.append(humid)
            
            precip = random.uniform(0, 2.0) if humid > 60 else 0
            self.precipitation.append(precip)
    
    def setup_gui(self):
        """Set up the GUI layout with embedded charts"""
        
        # Title
        title_label = tk.Label(self.root, 
                              text="Weather Data Visualization Dashboard", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Control panel
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        # Buttons to switch between different visualizations
        temp_btn = tk.Button(control_frame, 
                            text="Temperature Chart", 
                            command=self.show_temperature_chart,
                            bg="#E74C3C", 
                            fg="white",
                            font=("Arial", 10, "bold"))
        temp_btn.pack(side=tk.LEFT, padx=5)
        
        humidity_btn = tk.Button(control_frame, 
                                text="Humidity Chart", 
                                command=self.show_humidity_chart,
                                bg="#3498DB", 
                                fg="white",
                                font=("Arial", 10, "bold"))
        humidity_btn.pack(side=tk.LEFT, padx=5)
        
        precip_btn = tk.Button(control_frame, 
                              text="Precipitation Chart", 
                              command=self.show_precipitation_chart,
                              bg="#2980B9", 
                              fg="white",
                              font=("Arial", 10, "bold"))
        precip_btn.pack(side=tk.LEFT, padx=5)
        
        dashboard_btn = tk.Button(control_frame, 
                                 text="Full Dashboard", 
                                 command=self.show_dashboard,
                                 bg="#27AE60", 
                                 fg="white",
                                 font=("Arial", 10, "bold"))
        dashboard_btn.pack(side=tk.LEFT, padx=5)
        
        # Chart display area
        self.chart_frame = tk.Frame(self.root)
        self.chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Show initial chart
        self.show_temperature_chart()
    
    def clear_chart_frame(self):
        """Clear the current chart from display"""
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
    
    def show_temperature_chart(self):
        """Display temperature line chart in the GUI"""
        self.clear_chart_frame()
        
        # Create matplotlib figure
        fig = Figure(figsize=(10, 6), dpi=80)
        ax = fig.add_subplot(111)
        
        # Create the temperature chart
        ax.plot(self.dates, self.temperatures, 
               color='#E74C3C', 
               marker='o', 
               linewidth=3,
               markersize=8)
        
        # Customize the chart
        ax.set_title('7-Day Temperature Forecast', 
                    fontsize=14, 
                    fontweight='bold')
        ax.set_ylabel('Temperature (°F)')
        ax.grid(True, alpha=0.3)
        
        # Add temperature labels
        for i, (date, temp) in enumerate(zip(self.dates, self.temperatures)):
            ax.annotate(f'{temp}°F', 
                       (i, temp), 
                       textcoords="offset points", 
                       xytext=(0,10), 
                       ha='center',
                       fontweight='bold')
        
        # Embed the chart in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_humidity_chart(self):
        """Display humidity line chart in the GUI"""
        self.clear_chart_frame()
        
        fig = Figure(figsize=(10, 6), dpi=80)
        ax = fig.add_subplot(111)
        
        ax.plot(self.dates, self.humidity, 
               color='#3498DB', 
               marker='s', 
               linewidth=3,
               markersize=8)
        
        ax.set_title('7-Day Humidity Levels', 
                    fontsize=14, 
                    fontweight='bold')
        ax.set_ylabel('Humidity (%)')
        ax.grid(True, alpha=0.3)
        
        # Add humidity labels
        for i, (date, humid) in enumerate(zip(self.dates, self.humidity)):
            ax.annotate(f'{humid}%', 
                       (i, humid), 
                       textcoords="offset points", 
                       xytext=(0,10), 
                       ha='center',
                       fontweight='bold')
        
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_precipitation_chart(self):
        """Display precipitation bar chart in the GUI"""
        self.clear_chart_frame()
        
        fig = Figure(figsize=(10, 6), dpi=80)
        ax = fig.add_subplot(111)
        
        bars = ax.bar(self.dates, self.precipitation, 
                     color='#2980B9', 
                     alpha=0.8)
        
        ax.set_title('7-Day Precipitation Forecast', 
                    fontsize=14, 
                    fontweight='bold')
        ax.set_ylabel('Precipitation (inches)')
        ax.grid(axis='y', alpha=0.3)
        
        # Add precipitation labels
        for bar, precip in zip(bars, self.precipitation):
            if precip > 0:
                ax.text(bar.get_x() + bar.get_width()/2, 
                       bar.get_height() + 0.05,
                       f'{precip:.1f}"', 
                       ha='center', 
                       va='bottom',
                       fontweight='bold')
        
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_dashboard(self):
        """Display multi-panel dashboard in the GUI"""
        self.clear_chart_frame()
        
        fig = Figure(figsize=(12, 8), dpi=80)
        
        # Create subplots
        ax1 = fig.add_subplot(221)  # Top left
        ax2 = fig.add_subplot(222)  # Top right
        ax3 = fig.add_subplot(223)  # Bottom left
        ax4 = fig.add_subplot(224)  # Bottom right
        
        # Temperature chart
        ax1.plot(self.dates, self.temperatures, 
                color='#E74C3C', 
                marker='o', 
                linewidth=2)
        ax1.set_title('Temperature', fontweight='bold')
        ax1.set_ylabel('°F')
        ax1.grid(True, alpha=0.3)
        
        # Humidity chart
        ax2.plot(self.dates, self.humidity, 
                color='#3498DB', 
                marker='s', 
                linewidth=2)
        ax2.set_title('Humidity', fontweight='bold')
        ax2.set_ylabel('%')
        ax2.grid(True, alpha=0.3)
        
        # Precipitation chart
        ax3.bar(self.dates, self.precipitation, 
               color='#2980B9', 
               alpha=0.8)
        ax3.set_title('Precipitation', fontweight='bold')
        ax3.set_ylabel('inches')
        ax3.grid(axis='y', alpha=0.3)
        
        # Combined chart
        ax4_temp = ax4
        ax4_precip = ax4.twinx()
        
        ax4_temp.plot(self.dates, self.temperatures, 
                     color='#E74C3C', 
                     marker='o', 
                     linewidth=2,
                     label='Temp')
        ax4_precip.bar(self.dates, self.precipitation, 
                      color='#3498DB', 
                      alpha=0.6,
                      label='Precip')
        
        ax4.set_title('Combined View', fontweight='bold')
        ax4.grid(True, alpha=0.3)
        
        fig.suptitle('Weather Dashboard', fontsize=16, fontweight='bold')
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def run(self):
        """Start the weather visualization application"""
        print("Starting Weather Visualization App...")
        self.root.mainloop()

# Create and run the weather visualization app
if __name__ == "__main__":
    app = WeatherVisualizationApp()
    app.run()
