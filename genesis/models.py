from django.db import models

# instantiate this model portion later
# def user_directory_path(instance, filename):
#     return 'userGen_{0}/{1}'.format(instance.user.id, filename)

class UserGenesisReport(models.Model):
    userGen = models.CharField(max_length=255, default='Username')
    userOrg = models.CharField(max_length=255, default='Organization')
    # userFile = models.FileField(upload_to=user_directory_path)
    userFile = models.CharField(max_length=255, default='None')

    def __str__(self):
        return 'User:  {} OrganizationL: {} \
                Filename: {}'.format(self.userGen, self.userOrg,\
                        self.userFile)
