'''
Matplotlib
----------------
---> This is a library in python for data visualization , allowing users
to create a veriety of plots..

Basic structure of matplotlib
-----------------------------
1.Figure
2.Axes
3.Grid
4.Title
5.Legend



import matplotlib.pyplot as plt
sales=['A','B','C']
values=[25,30,45]
plt.bar(sales,values)
plt.show()


import matplotlib.pyplot as plt
sales=["a","B","C"]
values=[25,30,45]
plt.bar(sales,values)
plt.xlabel('car model')
plt.ylabel('Values')
plt.title('BMW sales')
plt.show()

import matplotlib.pyplot as plt
sales=["a","B","C"]
values=[25,30,45]
plt.bar(sales,values,color="Blue",edgecolor="Black")
plt.xlabel('car model')
plt.ylabel('Values')
plt.title('BMW sales')
plt.show()



import matplotlib.pyplot as plt
subjects=["Python","Java","SQL"]
students=[24,43,55]
plt.pie(students,labels=subjects,autopct='%1.1f%%')
plt.legend(subjects)
plt.title('Students in courses')
plt.show()


import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,15,18,20,13]

plt.scatter(x,y)
plt.title('Scatter plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()
'''
import matplotlib.pyplot as plt
y = [10,15,18,20,13]

plt.hist(y)
plt.title('Histogram plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()










