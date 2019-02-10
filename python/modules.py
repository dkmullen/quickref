# import classes, platform # platform is a built in module
from classes import Car # import just one thing from a module
import platform

newCar = Car("Chevy", "Silverado", "Silver")
print(newCar.model)

# classes.car1.printCar() 
x = platform.system()
print(x)
#print(dir(classes)) # dir is a built-in function
