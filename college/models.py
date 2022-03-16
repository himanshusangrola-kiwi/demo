from django.db import models

# declare a new model with a name "Collegemodel"
class CollegeModel(models.Model):
 
    # fields of the model
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length= 10)
    address = models.CharField(max_length= 200)
    
    # renames the instances of the model with their  name
    def __str__(self):
        return self.name