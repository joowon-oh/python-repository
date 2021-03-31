# importing bokeh
 #from bokeh.plotting import figure
 #from bokeh.io import output_file, show
# preparing data

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

# read data from csv file
# (sample) http://pythonhow.com/data/bachelors.csv # the ratio of women who got bachelor degree in the fields
# import pandas as pd
# df = pd.read_csv("file.csv" or url)
# x = df[x]
# y = df[y]

# preparing the output file (plot1.html) output_file("plot1.html")

# create a figure object f = figure()

# plot a line
#f.line(x, y)
#f.triangle(x, y)
#show(f)

# preparing the output notebook
from bokeh.plotting import output_notebook

output_notebook()

# prepare some data
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y = [i**2 for i in x]

# create a new plot

'fig = figure(
    tools="pan,box_zoom,wheel_zoom,zoom_in,zoom_out,reset,save",
    title="Example Bokeh plot",
    y_axis_type="log",
    y_range=[0.001, 10**3],
    x_axis_label='Sections',
    y_axis_label='Particles (log)',
    plot_width=600, plot_height=400,
)

# plot some data ('renderers' in Bokeh)
fig.circle(x, x, legend_label="y=x", fill_color="white", size=8)
fig.line(x, y, legend_label="y=x^2", line_width=3, line_color="red")

# show the results
show(fig)

from bokeh.models import Legend, LegendItem
from bokeh.plotting import figure, show

output_notebook()

p = figure()
r = p.multi_line([[1,2,3], [1,2,3]], [[1,3,2], [3,4,3]],
                 color=["orange", "red"], line_width=4)

legend = Legend(items=[
    LegendItem(label="orange", renderers=[r], index=0),
    LegendItem(label="red", renderers=[r], index=1),
])
p.add_layout(legend)

show(p)

from bokeh.models import Legend, LegendItem
from bokeh.plotting import figure, show

output_notebook()

p = figure()
r = p.multi_line([[1,2,3], [1,2,3]], [[1,3,2], [3,4,3]],
                 color=["orange", "red"], line_width=4)

legend = Legend(items=[
    LegendItem(label="orange", renderers=[r], index=0),
    LegendItem(label="red", renderers=[r], index=1),
])
p.add_layout(legend)

show(p)

