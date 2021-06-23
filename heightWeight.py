import csv 
import plotly.express as px
import pandas as pd 
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import numpy as np 


df = pd.read_csv("./HeightWeightData.csv")
height = df["Height"].tolist()
weight = df["Weight"].tolist()
fig = px.scatter(x = height, y = weight)
fig.show()
#from the scatter plot we can see that the height and weight are correlated so as the height increases the weight also increases
#add a line using the line equation on the plot 
#y = mx + c
#where m =  slope and c = intersect on y axis and x = height and y = weight a
#we already know the values of x and y let's assume the values of m and c (We will use hit and try method to plot the graph)
#Guess a solution and see if it is valid or not.. We will do this until we get proper values for slope and intersect 

#m = 1
#c = 0
#Here we have a close line that covers all the scatter plots in our graph 
m = 0.95
c = -93
y = []
for x in height:
    y_value = m*x + c
    y.append(y_value)

#ploting the points 

fig = px.scatter(x = height,y = weight)
fig.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = min(y),y1 = max(y),
        x0 = min(height),x1 = max(height)
    )
])

fig.show()

#Can we predict the weight of someone if his height is 250 using the formula 
x = 250
y = m*x + c
print(f"weight of someine with height {x} is {y}")

#let's find the slope and intersect of the data using computer algorithm and plot again with new values of m and c
 
import numpy as np
height_array = np.array(height)
weight_array = np.array(weight)

#slope and intercept using prebuild function of numpy 

m,c = np.polyfit(height_array,weight_array,1)
print(m,c)
y = []
for x in height_array:
    y_value = m*x + c
    y.append(y_value)

#Plotting the graph 

fig = px.scatter(x = height_array, y = weight_array)
fig.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = min(y), y1 = max(y),
        x0 = min(height_array), x1 = max(height_array)
    )
])

fig.show()
#This is the best fit ine for the data that the computer algorithm has provided us with
#Let's see the weight of someone who's height is 250 using the new values of slope and intercept 

x = 250
y = m*x + c
print(f"weight of someone with height {x} is {y}")
#we earlier got the values 144.5 and the computer provided the best fot line and we got the value 144.34