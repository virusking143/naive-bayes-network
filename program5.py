"""@author: VIRUSKING"""
import pandas as pd
import numpy as np
import csv
data1 = pd.read_csv('trainingexample.csv')
df1 = data1[data1['class'] == 'Yes']
df2 = data1[data1['class'] == 'No']
inputlist1=[]
head=['Outlook','Temperature','Humidity','Wind','class']
inputlist1.append(head)
count=0
def counting(inputlist1,j,str1,count):
    if(inputlist1[j][4]==str1):
        count=count+1
    return count
with open('trainingexample.csv','r') as csv_file1:
              csv_reader1=csv.reader(csv_file1)
              for i in range(11):
                  next(csv_reader1)              
              for line1 in csv_reader1:
                  inputlist1.append(line1)
              for j in range(1,len(inputlist1)):  
                  print("\nThe ",j,"Test data IS:\n",head[0]," = ",inputlist1[j][0],", ",head[1]," = ",inputlist1[j][1],", ",head[2]," = ",inputlist1[j][2],", ",head[3]," = ",inputlist1[j][3])
                  listyes=list()
                  listno=list()
                  resultyes=0.0
                  resultno=0.0
                  for d in range(4):
                      listyes.append(df1.loc[df1[head[d]]==inputlist1[j][d],head[d]].count()/len(df1))
                      listno.append(df2.loc[df2[head[d]]==inputlist1[j][d],head[d]].count()/len(df2))
                  resultyes = np.prod(np.array(listyes))*(len(df1)/len(data1))
                  resultno = np.prod(np.array(listno))*(len(df2)/len(data1))
                  print("Probability of Yes: ",resultyes,"\nProbability of No: ",resultno)                  
                  if resultyes>resultno:
                     print("Classified as YES\n")
                     count=counting(inputlist1,j,'Yes',count)                    
                  else:
                     print("Classified as NO\n")
                     count=counting(inputlist1,j,'No',count)                    
print("\nAccuracy for the Given Test Data Set is:\n",count/(len(inputlist1)-1) )            