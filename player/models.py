from django.db import models


class PlayerRequests(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    service_used = models.CharField(max_length=20)
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.service_used} - {self.request_time}"

    class Meta:
        db_table = 'player_requests'
        indexes = [models.Index(fields=['username'], name='username')]
        managed = True
