###Method 1###
# with open("weather_data.csv") as wdata:
#     weather_data = wdata.readlines()
#     print(weather_data)

### Metho 2 with csv object
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#     print(temperatures)

##Method 3 Panadas the Master kungfu
import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# avg = round(sum(temp_list) / len(temp_list))
# print(f"Temp series is\n {data["temp"]}")
# print(f"Average temp is {data["temp"].mean()}.")
# print(f"Max temp is {data["temp"].max()}")
# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"])
# monday = data[data.day == "Monday"]
# #°F = (9/5 × °C) + 32.
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(type(monday.temp))
# print(f"Temp C is {monday_temp} \nTemp F is {monday_temp_F}.")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240321.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)
data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



