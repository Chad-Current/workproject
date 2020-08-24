from django.db import models

class Tickets(models.Model):
    primary_key = models.BigIntegerField(primary_key=True)
    badge_identifier = models.SmallIntegerField(null=False)
    location = models.TextField()
    talkgroup_assoc = models.CharField(max_length=255)
    rssi = models.IntegerField()
    mobile = models.BooleanField(default=False)
    portable = models.BooleanField(default=False)
    desc_issue = models.TextField()
    issue_resolve = models.BooleanField(default=False)
    desc_resolve = models.TextField()
    # time_stamp = models.DateTimeField(auto_now=True)
    time_stamp = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tickets'
