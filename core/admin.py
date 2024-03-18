from django.contrib import admin
from . import models
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from import_export import resources, fields


class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", 'id')}
    

admin.site.register(models.User)
admin.site.register(models.College)
admin.site.register(models.Team)




# Register your models here.
