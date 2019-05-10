#!/usr/bin/env python3
import datetime
import os
from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file((os.path.abspath(__file__))+"line.html")

p = figure(plot_width=400, plot_height=400)

# add a circle renderer with a size, color, and alpha
p.circle([1, 1,2, 3, 4, 5], [6,1, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

# show the results
show(p)