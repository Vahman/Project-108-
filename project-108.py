import plotly.figure_factory as ff
import pandas as pd
import random
import plotly_express as px
dice_result=[]
count=[]

for i in range(0, 100):
  dice1=random.randint(1,6)
  dice2=random.randint(1,6)
  dice_result.append(dice1+dice2)
  count.append(i)

print(count,dice_result)

fig=px.bar(x=dice_result,y=count)
fig.show


for i in range(0,100):
  dice1=random.randint(1,6)
  dice2=random.randint(1,6)
  dice_result.append(dice1+dice2)

print(count,dice_result)

df = pd.read_csv("data3.csv")
data=df["Avg Rating"].to_list()
fig=ff.create_distplot([data], ["Avg Rating"])
fig.show()