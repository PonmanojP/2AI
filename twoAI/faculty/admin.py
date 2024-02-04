from django.contrib import admin
from .models import Faculty

admin.site.site_header = "2AI - Administration"
admin.site.site_title = "2AI Admin Portal"
admin.site.index_title = "Welcome to 2AI Admin Portal"
admin.site.register(Faculty)

