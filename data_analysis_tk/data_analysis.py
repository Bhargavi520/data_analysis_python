import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("Student_Grades.csv")
print(df.head(),"\n")
#selecting rows based on the condition
print("selecting rows where midterm is greater than or equal to 7")
print(df[df['MidTerm']>=7],"\n")
#printing scores acco. to midterm marks
print(df.loc[df['MidTerm']>=7,["Scores"]],"\n")
#print the groupby of grades 
grp=df.groupby(['Grade'])
print(grp.first())
print('\n')
#sorting values of hours columns
print(df.sort_values(by=['Hours']))
print('\n')

print(df.sort_values(by=['Grade','FinalExam']))
print('\n')
#bar graph between teamwork and midterm

x=df['Grade']
y=df['Scores']

plt.bar(x,y,color='g',edgecolor='w',linewidth=2,linestyle='--')
plt.xlabel("Grades")
plt.ylabel("Scores")
plt.show()
#histograph grade
plt.ylabel("frequency")
plt.hist(df['FinalExam'],bins=10,rwidth=0.8)
plt.title("Grades")
plt.show()

#pie chart
plt.title("DISTRIBUTION OF TEAMWORK")
occ = df.groupby('TeamWork').size()
occ.plot(kind='pie')
plt.show()


'''
print("STATISTICS OF NUMERIC VALUES")
print(df.describe())'''