from django.db import models
from django.contrib.auth.models import User
from isicwebdatabase.models import AuthUser

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    organization = models.CharField(max_length=255, default="N/A")

    def __str__(self):
        return 'User:  {} LEVEL: {} \
                Organization: {}'.format(self.user, self.level,\
                        self.organization )


    class Meta:
        managed = False
        db_table = 'users_profile'
