from django.contrib import admin

# Register your models here.
from . models import Person, Telnum





class PersonAdmin(admin.ModelAdmin):
    list_display = ('f_name')
    ordering = ('f_name',)
    search_fields = ('f_name')

admin.site.register(Person)
admin.site.register(Telnum)
