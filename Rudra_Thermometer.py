
print("The 7-Day Thermometer Program \n")
Celsius = []
weekDays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
# Constants = namedtuple('Constants', ['highest_Temperature', 'lowest_Temperature'])
# constants = Constants(0.0, 100.0)
# print(constants.lowest_Temperature)
i = 0

for i in range (7):
    Celsius.append(input("Please enter the temperature for " + weekDays[i]+ " in Celsius:"))


print("\nYou entered these Temperatures in Celsius and Fahrenheit.\n")
j=0
convertedcelcius = []
convertedcelcius = [float(item) for item in Celsius]
Fahrenheit = 0
Fahrenheitlist =[]

for i in range (7):
    Fahrenheit = convertedcelcius[i] * 1.8 + 32.0;
    Fahrenheit =round(Fahrenheit, 1)
    Fahrenheitlist.append(Fahrenheit)
    print(convertedcelcius[i]," C° is ",Fahrenheitlist[i]," F°")

average = 0

# Bubble Short for bonus
for i in range(0,len(convertedcelcius)-1):
    for j in range(len(convertedcelcius)-1):
        if(convertedcelcius[j]>convertedcelcius[j+1]):
            temp = convertedcelcius[j]
            convertedcelcius[j] = convertedcelcius[j+1]
            convertedcelcius[j+1] = temp

temp1 = 0
for i in range (7):
    average = convertedcelcius[i]+average;
    temp1 += 1


highest_Temperature = convertedcelcius[6]
lowest_Temperature =  convertedcelcius[0]
average = average / temp1
average =round(average, 1)
print("--------------------")
print("High Temp: ",highest_Temperature," C°, Low Temp: ",lowest_Temperature," C°","and Average Temp: ",average," C°")

