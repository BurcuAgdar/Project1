from django.contrib import admin
from .models import School
# Register your models here.


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display= ["name","adress"]

    search_fields = ["title"]
    class Meta:
        model = School