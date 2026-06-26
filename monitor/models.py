from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, default='Unknown')
    response_time = models.FloatField(null=True, blank=True)
    last_checked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class MonitorLog(models.Model):
    website = models.ForeignKey(
        Website,
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=10)
    status_code = models.IntegerField(null=True)
    response_time = models.FloatField(null=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.website.name} - {self.status}"


class Notification(models.Model):
    website = models.ForeignKey(
        Website,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    message = models.CharField(max_length=255)
    type = models.CharField(max_length=20, default='INFO')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.message