import pandas as pd
a=pd.read_csv("Universities.csv")
df1 = a[a["country"].str.contains('United States of America') ] 
print(df1) 
print("total number of usa universities=" ,len(df1))  #Question 1
print("max number of students is in=""\n",a[["university_name","num_students"]][a.num_students==a["num_students"].max()]) #Question 2
print("max number of citations is in=""\n",a[["university_name","citations"]][a.citations==a["citations"].max()])  #Question 3
g= a[a["country"].str.contains('Canada') ] 
print(g)
h=g[["num_students"]]
k=[h.sum(axis = 0, skipna = False) ]
print("total number of students in all canada universities=",k)  #Question 4