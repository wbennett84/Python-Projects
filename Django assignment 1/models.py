from django.db import models




# This is defining the class/model
class djangoClasses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    coursenumber = models.IntegerField()
    instructorname = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField()
# puts in the object manager
    objects = models.Manager()

    def __str__(self):
        return self.title
#instantiates the class and saves to the dB
class1 = djangoClasses(
    1, "Painting 101", 1, "Robert Frost", 10
)
class1.save()
class1.__str__()

#instantiates the class and saves to the dB
class2 = djangoClasses(
    2, "Painting 102", 2, "Robert Frosting", 12
)
class2.save()
class2.__str__()

#instantiates the class and saves to the dB
class3 = djangoClasses(
    3, "Painting 103", 3, "Robert Frosted", 10
)
class3.save()
class3.__str__()


