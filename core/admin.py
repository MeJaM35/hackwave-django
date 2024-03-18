from django.contrib import admin
from . import models
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from import_export import resources, fields


class TeamAdmin(ExportActionMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    list_filter = ('domain',)
    

admin.site.register(models.User)
admin.site.register(models.Team, TeamAdmin)




# Register your models here.
