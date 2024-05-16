from django.db import models

# Create your models here.
# Company Model
class  Company(models.Model):
    Company_id=models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(
            ('IT','IT'),
            ('Non IT','Non IT'),
            ("Mobiles Phones","Mobiles Phones")
     )
     )
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    def __str__(self) :
        return self.name  + " - " + self.location
         


#create Employee Model

class  Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    Phones=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=6, choices=(('male', 'Male'),
                                                ('female', 'female'),
                                                ('other', 'Other')),)
    address=models.TextField()
    position=models.CharField(max_length=15, choices=(('Manager','manager'),
                                                ('developer','developer'),
                                                ('Project Leader', 'PL')
                                                ))


    Company=models.ForeignKey(Company, on_delete=models.CASCADE)









