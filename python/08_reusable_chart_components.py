class WeatherChartComponent:
    """Reusable component for creating weather charts in GUI applications"""
    
    @staticmethod
    def create_embedded_chart(parent_frame, chart_type, dates, data, 
                             title, ylabel, color, figsize=(8, 5)):
        """
        Create an embedded matplotlib chart for GUI applications
        
        Args:
            parent_frame: Tkinter frame to embed the chart in
            chart_type: 'line' or 'bar'
            dates: List of date labels
        data: List of data values
            title: Chart title
            ylabel: Y-axis label
            color: Chart color
            figsize: Figure size tuple
        """
        
        # Clear any existing widgets in the frame
        for widget in parent_frame.winfo_children():
            widget.destroy()
        
        # Create matplotlib figure
        fig = Figure(figsize=figsize, dpi=80)
        ax = fig.add_subplot(111)
        
        # Create chart based on type
        if chart_type == 'line':
            ax.plot(dates, data, 
                   color=color, 
                   marker='o', 
                   linewidth=3,
                   markersize=8)
            
            # Add data labels for line charts
            for i, (date, value) in enumerate(zip(dates, data)):
                ax.annotate(f'{value}', 
                           (i, value), 
                           textcoords="offset points", 
                           xytext=(0,10), 
                           ha='center',
                           fontweight='bold',
                           fontsize=9)
        
        elif chart_type == 'bar':
            bars = ax.bar(dates, data, 
                         color=color, 
                         alpha=0.8)
            
            # Add data labels for bar charts
            for bar, value in zip(bars, data):
                if value > 0:
                    ax.text(bar.get_x() + bar.get_width()/2, 
                           bar.get_height() + max(data) * 0.01,
                           f'{value:.1f}', 
                           ha='center', 
                           va='bottom',
                           fontweight='bold',
                           fontsize=9)
        
        # Customize chart
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_ylabel(ylabel, fontsize=10)
        ax.grid(True, alpha=0.3)
        
        # Embed in Tkinter
        canvas = FigureCanvasTkinter(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        return canvas

print("Reusable chart component created!")
print("This component can be easily integrated into any weather application GUI.")


