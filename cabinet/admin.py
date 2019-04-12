from django.contrib import admin

from cabinet import models

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)

class LessonInline(admin.TabularInline):
    model = models.Lesson
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    inlines = (LessonInline,)
    list_display = ('course',)

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Place, PlaceAdmin)
admin.site.register(models.Group, GroupAdmin)
