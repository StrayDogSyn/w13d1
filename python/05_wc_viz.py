# Create visualizations for weather conditions
def create_weather_conditions_chart():
    """Create charts showing weather condition distributions"""
    
    # Sample weather conditions data
    conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Rainy', 'Stormy']
    condition_counts = [45, 30, 15, 8, 2]  # Percentage of days
    condition_colors = ['#F39C12', '#F7DC6F', '#BDC3C7', '#3498DB', '#8E44AD']
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Panel 1: Pie Chart
    wedges, texts, autotexts = ax1.pie(condition_counts, 
                                      labels=conditions,
                                      colors=condition_colors,
                                      autopct='%1.1f%%',
                                      startangle=90,
                                      explode=(0.05, 0, 0, 0, 0))  # Explode the sunny slice
    
    ax1.set_title('Weather Conditions Distribution', 
                  fontsize=14, 
                  fontweight='bold')
    
    # Panel 2: Horizontal Bar Chart
    bars = ax2.barh(conditions, condition_counts, 
                    color=condition_colors,
                    alpha=0.8)
    
    # Add percentage labels
    for i, (bar, count) in enumerate(zip(bars, condition_counts)):
        ax2.text(bar.get_width() + 1, 
                bar.get_y() + bar.get_height()/2,
                f'{count}%', 
                va='center',
                fontweight='bold')
    
    ax2.set_title('Weather Conditions Frequency', 
                  fontsize=14, 
                  fontweight='bold')
    ax2.set_xlabel('Percentage of Days')
    ax2.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Create weather conditions charts
create_weather_conditions_chart()
print("Weather conditions visualization created!")
