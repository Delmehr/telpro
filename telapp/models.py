from django.db import models
from django.forms import ModelForm

# Create your models here.
class Person(models.Model):
    f_name= models.CharField(max_length=25, null=True)
    l_name= models.CharField(max_length=25, null=True)
    #l_name= models.CharField(max_length=25, null=True)

    def __str__(self):

        return self.f_name.capitalize()  + "     " +    format(self.l_name).capitalize()
    #def __str__(self):
    #    return self.l_name
#that capitalize is a test!



class Telnum(models.Model):
    tel_num= models.CharField(max_length=13, null=True)
    #mob_num= models.CharField(max_length=13)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.tel_num

class TelForm(ModelForm):
    class Meta:
        model = Telnum
        fields = '__all__'
class ContactForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
