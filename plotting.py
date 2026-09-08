import matplotlib
matplotlib.use('TkAgg')  # try this instead of the default Qt backend
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["Ironman","Thor","Spidey","Hulk"])
y = np.array([20,40,60,100])
y1 = np.array([45,18,78,95])
y2 = np.array([75,89,64,31])
line_style = dict(marker = ".",ms = 20,markerfacecolor = "blue",mec = "blue",linestyle = "solid",linewidth= 4,color = "cyan")
plt.title("Toy sales",fontsize = 25,
                      family = "Arial",
                      fontweight = "bold",
                      color = "green")
plt.xlabel("Toys",fontsize = 25,
                      family = "Arial",
                      fontweight = "bold",
                      color = "green")
plt.ylabel("sales",fontsize = 25,
                      family = "Arial",
                      fontweight = "bold",
                      color = "green")
plt.yticks(y)
plt.tick_params(axis = "both",colors = "red")
plt.plot(x,y,**line_style)
plt.plot(x,y1,**line_style)
plt.plot(x,y2,**line_style)
plt.show()