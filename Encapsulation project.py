

#here we are defining our class and setting up some variables with initial values.
# These are private and protected variables, respectively.

#Next we are setting up some print and value-setting functions for use
# later on when we call them.

class Private:
    def __init__(self):
        self.__private = 30
        self._protected = 0

    def getitprivate(self):
        print(self.__private)

    def getitprotected(self):
        print(self._protected)

    def setit(self, priv):
        self.__private = priv

    def setit2(self, priv):
        self._protected = priv









# All the below is doing is instantiating an object(instance2, which is from the Private class)
# it is then calling a couple print functions.
# Then it is changing the values of some variables with set functions.
# Then it is printing the new values after having been reset

# This is an instantiation of a class which is utilizing both
# the private and protected aspects.

instance2 = Private()
instance2.getitprivate()
instance2.getitprotected()

instance2.setit(39)
instance2.getitprivate()

instance2.setit2(399)
instance2.getitprotected()

