from django.contrib import admin
from .models import Vent_Availability
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Vent_Availability)
class ViewAdmin(ImportExportModelAdmin):
    pass
