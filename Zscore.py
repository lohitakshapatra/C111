import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df=pd.read_csv('studentMarks.csv')
data=df["Math_score"].to_list()

fig=ff.create_distplot([data],["Math Scores"],show_hist=False)
fig.show()
mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print(mean,std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)    
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)    
    mean_list.append(set_of_means)
mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list)
print(mean,std_deviation)

#plotting the mean of the sample data
fig=ff.create_distplot([mean_list],["studentMarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.show()

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)


fig=ff.create_distplot([mean_list],["studentMarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.20],mode="lines",name="standard deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.20],mode="lines",name="standard deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.20],mode="lines",name="standard deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.20],mode="lines",name="standard deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.20],mode="lines",name="standard deviation 3 start"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.20],mode="lines",name="standard deviation 3 end"))
fig.show()


df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()
mean_of_sample1=statistics.mean(data)
print("Mean of sample 1 ",mean_of_sample1)
fig=ff.create_distplot([mean_list],["studentMarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.20],mode="lines",name="Mean of using tech"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.20],mode="lines",name="standard deviation 1 start"))
fig.show()

df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()
mean_of_sample2=statistics.mean(data)
print("Mean of sample 2 ",mean_of_sample2)
fig=ff.create_distplot([mean_list],["studentMarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample2,mean_of_sample2],y=[0,0.20],mode="lines",name="Mean of students who got extra class"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.20],mode="lines",name="standard deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.20],mode="lines",name="standard deviation 2 end"))
fig.show()

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score=(mean_of_sample1-mean)/std_deviation
print(z_score)
z_score=(mean_of_sample2-mean)/std_deviation
print(z_score)
z_score=(mean_of_sample3-mean)/std_deviation
print(z_score)
