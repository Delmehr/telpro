from django.db import models

# Create your models here.
class Person(models.Model):
    f_name= models.CharField(max_length=25, null=True)
    l_name= models.CharField(max_length=25, null=True)
    #l_name= models.CharField(max_length=25, null=True)

    def __str__(self):

        return self.f_name  + "     " +    format(self.l_name).capitalize()
    #def __str__(self):
    #    return self.l_name




class Telnum(models.Model):
    tel_num= models.CharField(max_length=13, null=True)
    #mob_num= models.CharField(max_length=13)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.tel_num
