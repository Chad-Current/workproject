from django.contrib import admin
from .models import Interoperability, IsicApplicant, Site

admin.site.register(Interoperability)
admin.site.register(IsicApplicant)
admin.site.register(Site)
