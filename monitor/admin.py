from django.contrib import admin
from .models import Website, MonitorLog, Notification

admin.site.register(Website)
admin.site.register(MonitorLog)
admin.site.register(Notification)
