from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin,ExportActionModelAdmin
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from unfold.contrib.filters.admin import RangeDateFilter, MultipleChoicesDropdownFilter


@admin.register(Local)
class localJobAdmin(ModelAdmin, ExportActionModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    
    list_display = ['title', 'company', 'location',"date_posted" , "deadline","employment_type", 'action']
    search_fields = ['title', 'company', 'location', ]
    list_filter = [("employment_type",MultipleChoicesDropdownFilter),

                   ("deadline",RangeDateFilter),
                   'source',    
                   ]
    list_filter_submit = True 
    list_filter_sheet= False
    list_editable   = ["action"]
    

@admin.register(International)
class InterationalJobAdmin(ModelAdmin):
    pass