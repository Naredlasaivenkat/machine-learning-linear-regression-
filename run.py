# IMPORTING MY MODULE WHICH I USED FOR LINEAR REGRESSION
import lin as ml2


from pandas import *
 
#IMPORTED CSV DATA FILE
data = read_csv("Salary_Data.csv")
 

x= data['YearsExperience'].tolist()

y=data['Salary'].tolist()
q="experiance"
w="salary"
#SCATTERD DATA POINTS IN GRAPH
ml2.sct(x, y,q,w)
#BY SEEING GRAPH I TAKEN LINEAR REGRESSION MODELWHAT I BUIT
# BY USING MY MDULE I TRAINED MY DATASET BBY PASSING XAND Y
a,b=ml2.train(x, y)
#AFTER TRAINIG I FITTED STRAIGHT LINE WITH LEAST ERRORS
ml2.fit(a, b, x, y,q,w)
#BY PASSING YEAER OF EXPERIAANCE IN FUNCTION I PREDICTED SALARY
s=ml2.predict(10.5,a,b)
print(s)

