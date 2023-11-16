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
    date = models.CharField()



    def __str__(self):
        return self.name



class New(models.Model):
    Headline = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField(max_length= 100000)


    def __str__(self):
        return self.Headline
    





class contactform(models.Model):
    names = models.CharField(max_length=200)
    emails = models.EmailField()
    services = models.CharField(max_length=200)
    dates = models.CharField(max_length=200)
    messages = models.TextField()

    def __str__(self):
        return self.names
