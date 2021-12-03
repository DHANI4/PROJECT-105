import csv
from numpy import shares_memory
with open("Data.csv",newline='') as F:
    reader=csv.reader(F)
    fileData=list(reader)

fileData.pop(0)
totalMarks=0
n=len(fileData)

for i in fileData:
    totalMarks=totalMarks+float(i[1])

mean=totalMarks/n
print("mean="+str(mean))

import pandas as pd
import plotly_express as px

df=pd.read_csv("Class1.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[
    dict(
        type="line",
        y0=mean,
        y1=mean,
        x0=0,
        x1=n
      )
])
fig.update_yaxes(rangemode="tozero")
fig.show()