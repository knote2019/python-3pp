import matplotlib.pyplot as plot

val1 = ["{:X}".format(i) for i in range(10)]
val2 = ["{:02X}".format(10 * i) for i in range(10)]
val3 = [["" for c in range(10)] for r in range(10)]

fig, ax = plot.subplots()
ax.set_axis_off()
table = ax.table(cellText=val3,
                 rowLabels=val2,
                 colLabels=val1,
                 rowColours=["palegreen"] * 10,
                 colColours=["palegreen"] * 10,
                 cellLoc='center',
                 loc='upper left')

ax.set_title('matplotlib.axes.Axes.table() function Example',
             fontweight="bold")

plot.show()

fig_background_color = 'skyblue'
fig_border = 'steelblue'
