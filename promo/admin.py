from django.contrib import admin

from promo.models import RequestInfo


class RequestInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'children_name', 'children_birthday', 'created_at')


admin.site.register(RequestInfo, RequestInfoAdmin)
