
# Create a program that converts fahrenheight to degrees

print("Hello, this program will take an input of the fahrenheight and output the celcius.")
fahrenheight = float(input("Input the degrees in fahrenheight: "))
celcius = round((fahrenheight-32)*0.5555555555, 2)
print(f"The degrees in celcius is: {celcius} ")