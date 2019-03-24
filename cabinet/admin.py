from django.contrib import admin

from cabinet import models

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Place, PlaceAdmin)
