# WeatherChartComponent.py

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class WeatherChartComponent:
    """Reusable component for creating weather charts in GUI applications"""

    @staticmethod
    def create_embedded_chart(parent_frame, chart_type, dates, data,
                              title, ylabel, color, figsize=(8, 5)):
        # Clear previous content
        for widget in parent_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=figsize, dpi=80)
        ax = fig.add_subplot(111)

        if chart_type == 'line':
            ax.plot(dates, data, color=color, marker='o', linewidth=3, markersize=8)
            for i, (date, value) in enumerate(zip(dates, data)):
                ax.annotate(f'{value}', (i, value), textcoords="offset points",
                            xytext=(0, 10), ha='center', fontweight='bold', fontsize=9)

        elif chart_type == 'bar':
            bars = ax.bar(dates, data, color=color, alpha=0.8)
            for bar, value in zip(bars, data):
                if value > 0:
                    ax.text(bar.get_x() + bar.get_width() / 2,
                            bar.get_height() + max(data) * 0.01,
                            f'{value:.1f}', ha='center', va='bottom',
                            fontweight='bold', fontsize=9)

        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_ylabel(ylabel, fontsize=10)
        ax.grid(True, alpha=0.3)

        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        return canvas
