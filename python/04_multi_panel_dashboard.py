def create_weather_dashboard(dates, temperatures, humidity, precipitation):
    """Create a multi-panel weather dashboard"""
    
    # Create figure with subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Panel 1: Temperature Line Chart
    ax1.plot(dates, temperatures, 
             color='#E74C3C', 
             marker='o', 
             linewidth=3, 
             markersize=8)
    ax1.set_title('Temperature Trend', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Temperature (°F)')
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(axis='x', rotation=45)
    
    # Panel 2: Humidity Line Chart
    ax2.plot(dates, humidity, 
             color='#3498DB', 
             marker='s', 
             linewidth=3, 
             markersize=8)
    ax2.set_title('Humidity Levels', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Humidity (%)')
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    # Panel 3: Precipitation Bar Chart
    bars = ax3.bar(dates, precipitation, 
                   color='#2980B9', 
                   alpha=0.8)
    ax3.set_title('Daily Precipitation', fontsize=14, fontweight='bold')
    ax3.set_ylabel('Precipitation (inches)')
    ax3.grid(axis='y', alpha=0.3)
    ax3.tick_params(axis='x', rotation=45)
    
    # Panel 4: Combined Overview
    # Create a dual-axis plot showing temperature and precipitation together
    ax4_temp = ax4
    ax4_precip = ax4.twinx()
    
    # Temperature line
    line1 = ax4_temp.plot(dates, temperatures, 
                         color='#E74C3C', 
                         marker='o', 
                         linewidth=2,
                         label='Temperature')
    ax4_temp.set_ylabel('Temperature (°F)', color='#E74C3C')
    ax4_temp.tick_params(axis='y', labelcolor='#E74C3C')
    
    # Precipitation bars
    bars = ax4_precip.bar(dates, precipitation, 
                         color='#3498DB', 
                         alpha=0.6,
                         label='Precipitation')
    ax4_precip.set_ylabel('Precipitation (inches)', color='#3498DB')
    ax4_precip.tick_params(axis='y', labelcolor='#3498DB')
    
    ax4.set_title('Temperature vs Precipitation', fontsize=14, fontweight='bold')
    ax4.tick_params(axis='x', rotation=45)
    ax4.grid(True, alpha=0.3)
    
    # Overall dashboard title
    fig.suptitle('7-Day Weather Dashboard', 
                 fontsize=18, 
                 fontweight='bold', 
                 y=0.95)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.subplots_adjust(top=0.90)
    plt.show()

# Create the weather dashboard
create_weather_dashboard(dates, temperatures, humidity, precipitation)
print("Multi-panel weather dashboard created!")
