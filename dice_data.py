import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics

dice_result = []
#count = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    #count.append(i)

print(dice_result)

#calculating mean
mean = sum(dice_result)/len(dice_result)
print(mean)
#generating standard deviation
std_deviation = statistics.stdev(dice_result)
print(std_deviation)
#fig = px.bar(x = dice_result, y = count)
#fig = ff.create_distplot([dice_result],["Result"])
#fig.show()

#calculating median
median = statistics.median(dice_result)
print(median)

#calculating mode
mode = statistics.mode(dice_result)
print(mode)
#plotting bell curve
fig = ff.create_distplot([dice_result],["Result"], show_hist= False)
fig.show()

#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))


second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))


third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))
