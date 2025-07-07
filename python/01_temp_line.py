import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import random

# Create sample weather data for visualization
def create_sample_weather_data():
    """Generate sample weather data for the next 7 days"""
    
    # Start from today
    start_date = datetime.now()
    
    # Generate 7 days of weather data
    dates = []
    temperatures = []
    humidity = []
    precipitation = []
    
    for i in range(7):
        current_date = start_date + timedelta(days=i)
        dates.append(current_date)
        
        # Simulate realistic temperature patterns
        base_temp = 70 + (i * 2) + random.randint(-5, 5)  # Slight warming trend with variation
        temperatures.append(base_temp)
        
        # Simulate humidity (higher when it might rain)
        base_humidity = random.randint(40, 80)
        humidity.append(base_humidity)
        
        # Simulate precipitation (chance of rain)
        precip = random.uniform(0, 1.5) if base_humidity > 65 else 0
        precipitation.append(precip)
    
    return dates, temperatures, humidity, precipitation

# Generate our sample data
dates, temperatures, humidity, precipitation = create_sample_weather_data()

print("Sample weather data created!")
print("Let's create our first temperature chart...")

# Create a basic temperature line chart
plt.figure(figsize=(10, 6))  # Set chart size
plt.plot(dates, temperatures, marker='o', linewidth=2, markersize=8)

# Add chart customization
plt.title('7-Day Temperature Forecast', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)

# Improve date display on x-axis
plt.xticks(rotation=45)

# Add grid for easier reading
plt.grid(True, alpha=0.3)

# Make layout tight so nothing gets cut off
plt.tight_layout()

# Display the chart
plt.show()

print("Basic temperature chart created!")

