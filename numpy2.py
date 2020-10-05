import matplotlib.pyplot as plot
import numpy as np 
val=[[5.,25.,45.,12.],[4., 28., 51.,16.],[6.,32.,47.,19.]]
x=np.arange(1,5)
plot.plot(x,val[0],color="b",label="range1",marker="o")
plot.plot(x,val[1],color="g",label="range2",marker="d")
plot.plot(x,val[2],color="r",label="range3",marker="x")
plot.legend(loc="upper left")
plot.title("Multirange line chart")
plot.xlabel("X")
plot.ylabel("Y")
plot.show()