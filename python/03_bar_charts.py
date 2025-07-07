# Create a precipitation bar chart
def create_precipitation_chart(dates, precipitation):
    """Create a bar chart showing daily precipitation"""
    
    plt.figure(figsize=(12, 6))
    
    # Create bar chart
    bars = plt.bar(dates, precipitation, 
                   color='#3498DB',  # Blue for water/rain
                   alpha=0.8,
                   edgecolor='#2980B9',
                   linewidth=2)
    
    # Add value labels on top of bars
    for bar, precip in zip(bars, precipitation):
        if precip > 0:  # Only show label if there's precipitation
            plt.text(bar.get_x() + bar.get_width()/2, 
                    bar.get_height() + 0.02,
                    f'{precip:.1f}"', 
                    ha='center', 
                    va='bottom',
                    fontweight='bold',
                    fontsize=10)
    
    # Chart styling
    plt.title('Daily Precipitation Forecast', 
              fontsize=24, 
              fontweight='bold',
              color='#2C3E50')
    
    plt.xlabel('Date', fontsize=24, fontweight='bold')
    plt.ylabel('Precipitation (inches)', fontsize=24, fontweight='bold')
    
    # Format x-axis dates
    plt.xticks(rotation=45)
    
    # Add horizontal grid lines
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    
    # Set y-axis to start at 0
    plt.ylim(bottom=0)
    
    plt.tight_layout()
    plt.show()

# Create precipitation chart
create_precipitation_chart(dates, precipitation)
print("Precipitation bar chart created!")

