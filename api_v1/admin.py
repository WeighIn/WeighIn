from django.contrib import admin
from api_v1.models import *


class ResultAdmin(admin.ModelAdmin):
    pass
admin.site.register(Result, ResultAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)
