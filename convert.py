#This program will take a number from the user
#and convert it from degrees fahrenheit to degrees celcius
# (F - 32)/1.8
fNum = float(input("Please give me a number to convert from degrees fahrenheit to degrees celcius: "))
cNum = (fNum - 32)/1.8
print("The result is " + str(cNum) + ".")