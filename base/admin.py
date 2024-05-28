from django.contrib import admin

# Register your models here.
from .models import User
from .models import Status
from .models import Report

admin.site.register(User)
admin.site.register(Status)
admin.site.register(Report)
