def create_custom_weather_chart(chart_type, data_type):
    """
    Create custom weather charts based on user preferences
    This function demonstrates how to make visualization flexible
    """
    
    if data_type == "temperature":
        data = temperatures
        color = '#E74C3C'
        ylabel = 'Temperature (°F)'
        title = 'Temperature Data'
    elif data_type == "humidity":
        data = humidity
        color = '#3498DB'
        ylabel = 'Humidity (%)'
        title = 'Humidity Data'
    else:  # precipitation
        data = precipitation
        color = '#2980B9'
        ylabel = 'Precipitation (inches)'
        title = 'Precipitation Data'
    
    plt.figure(figsize=(10, 6))
    
    if chart_type == "line":
        plt.plot(dates, data, 
                color=color, 
                marker='o', 
                linewidth=3,
                markersize=8)
    else:  # bar chart
        plt.bar(dates, data, 
               color=color, 
               alpha=0.8)
    
    plt.title(f'{title} - {chart_type.title()} Chart', 
              fontsize=16, 
              fontweight='bold')
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# Demonstrate custom chart creation
print("Creating custom temperature line chart...")
create_custom_weather_chart("line", "temperature")

print("Creating custom precipitation bar chart...")
create_custom_weather_chart("bar", "precipitation")

