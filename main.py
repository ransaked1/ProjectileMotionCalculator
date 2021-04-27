from src.AngleHeightTimeCalc import AngleHeightTimeCalc
from src.HeightTimeDistanceCalc import HeightTimeDistanceCalc
from src.VelocityHeightAngleCalc import VelocityHeightAngleCalc
from src.HeightTimeCalc import HeightTimeCalc

from graphics.graphics_handler import MainGraphics

from ttkthemes import themed_tk as tk
import tkinter.ttk as ttk
import tkinter
import pygubu

# Adding create_circle to the tkinter.Canvas module
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tkinter.Canvas.create_circle = _create_circle

if __name__ == '__main__':
    # Setting up tk object
    root = tk.ThemedTk()

    # Setting app title
    root.title("Projectile Motion Calculator and Visualizer")

    # Setting app icon
    img = tkinter.PhotoImage(file='graphics/icon.png')
    root.iconphoto(False, img)

    # Setting app theme
    style = ttk.Style(root)
    style.theme_use('yaru')

    # Starting app
    app = MainGraphics(root)
    app.run()
