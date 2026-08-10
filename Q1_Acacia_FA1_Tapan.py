import math

#input variables
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))

#distance formula
distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))


#answer
print(f"\n The distance between the two points is :{distance:.2f}")

#REFLECTION :  Making a library is more practical because it provides ready made tested functions that save time and reduce errors in coding, for example, our distance calculator activity, using the math library's sqrt() and pow() functions made it easy to calculate the distance between two points without writing those calculations from scratch, making the program simpler and more reliable.