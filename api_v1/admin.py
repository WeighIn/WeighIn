from django.contrib import admin
from api_v1.models import *


class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Application, ApplicationAdmin)


class ResultAdmin(admin.ModelAdmin):
    pass
admin.site.register(Result, ResultAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)
