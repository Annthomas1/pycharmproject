from django.contrib import admin
from .models import myapp
# Register your models here.
class MyappAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
admin.site.register(myapp,MyappAdmin)
