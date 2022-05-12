# Importing Modules
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

# Initializing Data
df = pd.read_csv("data.csv")

# Reading And Storing Data
reading_data = df["reading score"].to_list()
math_data = df["math score"].to_list()

# Calculating The Mean And The Standard Deviation Of reading_data
reading_data_mean = statistics.mean(reading_data)
reading_data_median = statistics.median(reading_data)
reading_data_mode = statistics.mode(reading_data)
reading_data_std_deviation = statistics.stdev(reading_data)

# Calculating The Mean And The Standard Deviation Of math_data
math_data_mean = statistics.mean(math_data)
math_data_mode = statistics.mode(math_data)
math_data_median = statistics.median(math_data)
math_data_std_deviation = statistics.stdev(math_data)

# Finding Standard Deviation 1 & 2 Start And End Values Of reading_data
reading_data_first_std_deviation_start, reading_data_first_std_deviation_end = reading_data_mean - reading_data_std_deviation, reading_data_mean + reading_data_std_deviation
reading_data_second_std_deviation_start, reading_data_second_std_deviation_end = reading_data_mean - (2*reading_data_std_deviation), reading_data_mean + (2*reading_data_std_deviation)
reading_data_third_std_deviation_start, reading_data_third_std_deviation_end = reading_data_mean - (3*reading_data_std_deviation), reading_data_mean + (3*reading_data_std_deviation)

# Finding Standard Deviation 1 & 2 Start And End Values Of reading_data
math_data_first_std_deviation_start, math_data_first_std_deviation_end = math_data_mean - math_data_std_deviation, math_data_mean + math_data_std_deviation
math_data_second_std_deviation_start, math_data_second_std_deviation_end = math_data_mean - (2*math_data_std_deviation), math_data_mean + (2*math_data_std_deviation)
math_data_third_std_deviation_start, math_data_third_std_deviation_end = math_data_mean - (3*math_data_std_deviation), math_data_mean + (3*math_data_std_deviation)

# Plotting The Reading Chart, And Lines For Mean, 1 Standard Deviation and 2 Standard Deviations
fig = ff.create_distplot([reading_data], ["Reading Score"], show_hist=False)
fig.add_trace(go.Scatter(x=[reading_data_mean, reading_data_mean], y=[0, 0.17], mode="lines", name="Mean Of Reading"))
fig.add_trace(go.Scatter(x=[reading_data_first_std_deviation_start, reading_data_first_std_deviation_start], y=[0, 0.17], mode="lines", name="Reading Standard Deviation 1 Start"))
fig.add_trace(go.Scatter(x=[reading_data_first_std_deviation_end, reading_data_first_std_deviation_end], y=[0, 0.17], mode="lines", name="Reading Standard Deviation 1 End"))
fig.add_trace(go.Scatter(x=[reading_data_second_std_deviation_start, reading_data_second_std_deviation_start], y=[0, 0.17], mode="lines", name="Reading Standard Deviation 2 Start"))
fig.add_trace(go.Scatter(x=[reading_data_second_std_deviation_end, reading_data_second_std_deviation_end], y=[0, 0.17], mode="lines", name="Reading Standard Deviation 2 End"))

# Updating Layout
fig.layout.update({
                    "title": "Reading Score Of Students",
                    "xaxis": {"title": "Score"}
                 })

# Plotting The Math Chart, And Lines For Mean, 1 Standard Deviation and 2 Standard Deviations
figure = ff.create_distplot([math_data], ["Math Score"], show_hist=False)
figure.add_trace(go.Scatter(x=[math_data_mean, reading_data_mean], y=[0, 0.17], mode="lines", name="Mean Of Math"))
figure.add_trace(go.Scatter(x=[math_data_first_std_deviation_start, math_data_first_std_deviation_start], y=[0, 0.17], mode="lines", name="Math Standard Deviation 1 Start"))
figure.add_trace(go.Scatter(x=[math_data_first_std_deviation_end, math_data_first_std_deviation_end], y=[0, 0.17], mode="lines", name="Math Standard Deviation 1 End"))
figure.add_trace(go.Scatter(x=[math_data_second_std_deviation_start, math_data_second_std_deviation_start], y=[0, 0.17], mode="lines", name="Math Standard Deviation 2 Start"))
figure.add_trace(go.Scatter(x=[math_data_second_std_deviation_end, math_data_second_std_deviation_end], y=[0, 0.17], mode="lines", name="Math Standard Deviation 2 End"))

# Updating Layout
figure.layout.update({
                    "title": "Maths Score Of Students",
                    "xaxis": {"title": "Score"}
                 })

# Plotting Graphs
print("Plotting..")
fig.show()
figure.show()

# Printing The Results Of Reading Data
list_of_data_of_reading_within_1_std_deviation = [
    result for result in reading_data if result > reading_data_first_std_deviation_start and result < reading_data_first_std_deviation_end
]
list_of_data_of_reading_within_2_std_deviation = [
    result for result in reading_data if result > reading_data_second_std_deviation_start and result < reading_data_second_std_deviation_end
]
list_of_data_of_reading_within_3_std_deviation = [
    result for result in reading_data if result > reading_data_third_std_deviation_start and result < reading_data_third_std_deviation_end
]

print()
print("Mean Of Reading Data Is: {}".format(reading_data_mean))
print("Median Of Reading Data Is: {}".format(reading_data_median))
print("Mode Of Reading Data Is: {}".format(reading_data_mode))
print("Standard Deviation Of Reading Data Is: {}".format(reading_data_std_deviation))
print()
print("{}% Of Data Lies Within 1 Standard Deviation".format(len(list_of_data_of_reading_within_1_std_deviation)*100.0/len(reading_data)))
print("{}% Of Data Lies Within 2 Standard Deviations".format(len(list_of_data_of_reading_within_2_std_deviation)*100.0/len(reading_data)))
print("{}% Of Data Lies Within 3 Standard Deviations".format(len(list_of_data_of_reading_within_3_std_deviation)*100.0/len(reading_data)))

# Printing The Results Of Math Data
list_of_data_of_math_within_1_std_deviation = [
    result for result in math_data if result > math_data_first_std_deviation_start and result < math_data_first_std_deviation_end
]
list_of_data_of_math_within_2_std_deviation = [
    result for result in math_data if result > math_data_second_std_deviation_start and result < math_data_second_std_deviation_end
]
list_of_data_of_math_within_3_std_deviation = [
    result for result in math_data if result > math_data_third_std_deviation_start and result < math_data_third_std_deviation_end
]

print()
print("Mean Of Math Data Is: {}".format(math_data_mean))
print("Median Of Math Data Is: {}".format(math_data_median))
print("Mode Of Math Data Is: {}".format(math_data_mode))
print("Standard Deviation Of Math Data Is: {}".format(math_data_std_deviation))
print()
print("{}% Of Data Lies Within 1 Standard Deviation".format(len(list_of_data_of_math_within_1_std_deviation)*100.0/len(reading_data)))
print("{}% Of Data Lies Within 2 Standard Deviations".format(len(list_of_data_of_math_within_2_std_deviation)*100.0/len(reading_data)))
print("{}% Of Data Lies Within 3 Standard Deviations".format(len(list_of_data_of_math_within_3_std_deviation)*100.0/len(reading_data)))