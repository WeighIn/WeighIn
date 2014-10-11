from django.contrib import admin
from api.models import *


class ApplicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Application, ApplicationAdmin)


class ResultAdmin(admin.ModelAdmin):
    pass
admin.site.register(Result, ResultAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
