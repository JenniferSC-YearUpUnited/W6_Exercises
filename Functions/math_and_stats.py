import random
import math
import statistics

vals_100 = range(1,100)
# print(vals_100)
vals_sample = random.sample(vals_100, 75)
# print(vals_sample)
sum = math.fsum(vals_sample)
# print(sum)
average = statistics.mean(vals_sample)
# print(average)
median = statistics.median(vals_sample)
# print(median)
# use a combination of functions from all three models to create calculations that will support the following output:
print(f'''_Experimenting with a subset of integers 1-100:
Sum of 75 sample values from 1 to 100: {sum}
Average of 75 sample values: {average}
Median of 75 sample values: {median} ''')



vals_choices = random.choices(vals_100, k = 200)
# print(vals_choices)
average200 = statistics.mean(vals_choices)
# print(average200)
median200 = statistics.median(vals_choices)
# print(median200)
mode200 = statistics.mode(vals_choices)
# print(mode200)
standard_dev = statistics.pstdev(vals_choices)
# print(standard_dev)
variance = statistics.pvariance(vals_choices)
# print(variance)
# use a combination of functions from all three models to create calculations that will support the following output:
print(f'''_Experimenting with a superset of 200 values, integers 1-100:
Average of 200 values: {average200}
Median of 200 values: {median200}
Mode of 200 values: {mode200}
Standard deviation of 200 values: {standard_dev}
Variance of 200 values: {variance}''')


radius = random.randint(3,10)
# print(radius)
squared_radius = radius**2
# print(squared_radius)
pi = math.pi
# print(pi)
area = squared_radius * pi
# print(area)
areaup = math.ceil(area)
# print(areaup)
areadown = math.floor(area)
# print(areadown)

# rounded up to the nearest integer then rounded down to the nearest integer
print(f'''_Modeling a random circle:
Radius = {squared_radius}, area = {areaup}
Radius = {squared_radius}, area = {areadown}''')
