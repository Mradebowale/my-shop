from django.db import models
# Create your models here.

# class Services(models.Model):
#     name = models.CharField(max_length= 200)
#     description = models.TextField(max_length=100000)
    

#     class Meta:
#         verbose_name_plural = "Services"

#     def __str__(self):
#         return self.name




SERVICE_TYPE = (
    ("1", "service 1"),
    ("2", "service 2"),
    ("3", "service 3")
)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(help_text="Insert a valid email")
    type = models.CharField(max_length=10, choices= SERVICE_TYPE)
    message = models.TextField(max_length=7000)
    date = models.DateField()



    def __str__(self):
        return self.name



