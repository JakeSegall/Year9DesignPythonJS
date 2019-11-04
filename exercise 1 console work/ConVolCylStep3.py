import math
print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")

print("Step 2")
#Input
#What inputs are needed to calculate the volume of a cylinder?
print("Volume of a Cylinder Formula: ")


name = input("\n\tWhat is your name: ")   #takes users name

height = 1
radius = 1

while (radius != 0 or height != 0):

	radius = input("\n\tInput radius(cm): ")  #input
	radius = xint(radius)    #cast to int

	height = input("\n\tInput height(cm): ") #input
	height = int(height)     #cast to int
	#Process 
	#What formula is used to calculate the volume of a cylinder?

if (radius >= 0 and height >= 0):

	volume = math.pi*radius*radius*height 
	volume = round(volume,2)
	#Output
	#What is important about the output?
	print("\n\t\tHi "+name+"!")
	print("\n\t\tGive a cylinder with:")
	print("\t\tRadius = "+str(radius))
	print("\t\tHeight = "+str(height))
	print("\t\tThe volume is: "+str(volume))  


