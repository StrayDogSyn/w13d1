# Create a more sophisticated temperature chart with weather styling
def create_styled_temperature_chart(dates, temperatures):
    """Create a professional-looking temperature chart"""
    
    plt.figure(figsize=(12, 7))
    
    # Create the line chart with weather-appropriate styling
    plt.plot(dates, temperatures, 
            color='#FF6B35',  # Weather orange color
            marker='o', 
            linewidth=3, 
            markersize=10,
            markerfacecolor='#FF6B35',
            markeredgecolor='white',
            markeredgewidth=2,
            label='Temperature')
    
    # Add temperature value labels on each point
    for i, (date, temp) in enumerate(zip(dates, temperatures)):
        plt.annotate(f'{temp}°F', 
                    (date, temp), 
                    textcoords="offset points", 
                    xytext=(0,15), 
                    ha='center',
                    fontsize=10,
                    fontweight='bold',
                    color='#333333')
    
# Styling improvements
    plt.title('Weekly Temperature Forecast', 
              fontsize=18, 
              fontweight='bold', 
              color='#2C3E50',
              pad=20)
    
    plt.xlabel('Date', fontsize=14, fontweight='bold', color='#34495E')
    plt.ylabel('Temperature (°F)', fontsize=14, fontweight='bold', color='#34495E')
    
    # Format dates on x-axis
    plt.xticks(rotation=45, fontsize=11)
    plt.yticks(fontsize=11)
    
    # Add background grid
    plt.grid(True, linestyle='--', alpha=0.4, color='#BDC3C7')
    
    # Set background color
    plt.gca().set_facecolor('#F8F9FA')
    
    # Add legend
    plt.legend(fontsize=12, loc='upper left')
    
    # Adjust layout
    plt.tight_layout()
    plt.show()

# Create our styled temperature chart
create_styled_temperature_chart(dates, temperatures)
print("Styled temperature chart created!")

