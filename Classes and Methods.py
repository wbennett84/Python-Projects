

# This sets up a car class with a couple properties and a couple methods that take
# in info and print out results
class Car:
    def __init__(self, color, top_speed):
        self.color = color
        self.top_speed = top_speed

    

    def information(self):
        msg = ("You\'re about to drive a {} car with a top speed of {}MPH!!!".format(car1.color,car1.top_speed))
        return msg

    def survey(self):
        question1 = input("You like cars? Y/N \n>>> ").lower()
        if (question1) == ("y"):
            print ("You definitely belong in the club!")
        if (question1) == ("n"):
            print ("You might not be interested in this subject!")

#This sets up a child class and gives it a couple more properties as well as
# a polymorphic method based on the Car class. 

class Body(Car):
    def __init__(self, doors, bed):
        self.doors = doors
        self.bed = bed
    def information(self):
        msg = ("It has {} doors and {} bed...".format(body1.doors,body1.bed))
        return msg

    def survey(self):
        question1 = input("You ready for the next line? Y/N \n>>> ").lower()
        if (question1) == ("y"):
            print ("Here it comes!")
        if (question1) == ("n"):
            print ("Then get ready!")



#This sets up another child class and gives it a couple more properties as well as
# a polymorphic method based on the Car class. 


class Brand(Car):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def information(self):
        msg = ("And it\'s a {} {}!".format(cartype1.make,cartype1.model))
        return msg

    def survey(self):
        question1 = input("Did you enter the car giveaway contest? Y/N \n>>> ").lower()
        if (question1) == ("y"):
            print ("Then you have won! Collect your new car just outside the doors!")
        if (question1) == ("n"):
            print ("I'm sorry, but someone else won the car")



# This basically is the code that will run as long as all this is contained
# in the main .py file. This sequence allows for a program with a basic flow.

if __name__ == "__main__":
    car1 = Car("Red", 155)
    print (car1.information())
    body1 = Body(2, "no")
    print (body1.information())
    cartype1 = Brand("Ford", "Mustang")
    print (cartype1.information())
    car1.survey()
    body1.survey()
    cartype1.survey()
    
    
    
    


