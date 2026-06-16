'''
Data Analysis
--->This is process of inspecting,cleaning,transforming, and modelling
    data to discover useful insights.

Types of DA:
-------------------------------------------------------------------
1)Descriptive analysis
{Summarizes historical data}
-------------------------------------------------------------------
2)Diagnostic analysis
{Understanding Causes} or {Investigates causes behind outcomes}
-------------------------------------------------------------------
3)Predective analysis
{Forecasting future outcomes}
-------------------------------------------------------------------
4)prescriptive analysis
{Suggesting actins based on data}
-------------------------------------------------------------------

Why DA:
-->To improve decision making
-->Detects trends and patterns




Numpy(Numerical python)(Array concept in python)
-------------------------------------------------------------------
--->This Python library fo numerical computing.it provides support for
    multi-dimensional arrays, and linear algebra operations,making it essential
    for data analysis...


Using numpy in DA
------------------
-->Improved performance
-->Simplifies complex operations
-->Easy data manipulation


import numpy as np
arr_1=np.array([[1,2,3,4],[5,6,7,8],[3,4,5,6]])
print(arr_1)

import numpy as np
arr_1=np.array([[2,3,4],[3,6,5]])
print(arr_1)
print(arr_1.shape)


import numpy as np
arr_1=np.array([2,3,4,3,6,5])
print(arr_1[2])



import numpy as np
arr_1=np.array([2,3,4,3,6,5])
print(arr_1+5)



import numpy as np
arr_1=np.array([[2,3],[3,4]])
arr_2=np.array([[1,3],[2,4]])
print(np.dot(arr_1,arr_2))



import numpy as np
arr1=np.array([10,20,30])
nrm_copy=arr1.view()
arr1[0]=100
print(nrm_copy)
print(arr1)


copy_dee=arr1.copy()
arr1[1]=400
print(copy_dee)
print(arr1)




Pandas
------
--->The pandas is a powerful data manipulation and analysis library.
--->Where it provides data structure like series and dataframe for efficiently data handling



import pandas as pd
any_=pd.Series([2999,15999,52999,4999,1999],
               index=['Earbuds','Smartphones','Laptop','Watch','Footwear'])
print(any_)



DATAFRAME
---------

'''
import pandas as pd
data={
    'Product':['Earbuds','smartphones','Laptop','Watch','Footwear'],
    'Brand':['JBL','Samsung','Mac','Titan','Nike'],
    'price':[1999,85000,120000,4000,4500],
    'Stock':[50,15,34,54,18]
    }

dip=pd.DataFrame(data)
print(dip)



























