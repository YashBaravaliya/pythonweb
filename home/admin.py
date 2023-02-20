from django.contrib import admin
from home.models import subject,chapter,cheetsheet,Contact

# Register your models here.
admin.site.register([subject,chapter,cheetsheet,Contact])