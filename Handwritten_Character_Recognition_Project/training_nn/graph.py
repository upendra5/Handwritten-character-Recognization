import matplotlib.pyplot as plt 
  
# x axis values 
x = [0,1,2] 
# corresponding y axis values 
y = [95.536,96.932,97.506] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Epochs') 
# naming the y axis 
plt.ylabel('Accuracy') 
  
# giving a title to my graph 
plt.title('Accuracy Plot') 
  
# function to show the plot 
plt.show() 

