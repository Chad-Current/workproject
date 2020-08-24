# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Interoperability(models.Model):
    primary_key = models.BigIntegerField(primary_key=True)
    county_no = models.CharField(max_length=20, blank=True, null=True)
    county = models.CharField(max_length=45, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    user_lvl = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    cell_or_alternate = models.CharField(max_length=35, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return 'County Number:  {} County: {} \
                Organization: {}  User Level: {}\
                Name: {}  phone: {}  job title: {}\
                Cell Phone or Alternate: {}\
                E-mail: {}\
                notes: {}'\
                .format(self.county_no, self.county,\
                        self.organization, self.user_lvl,\
                        self.name, self.phone, self.job_title,\
                        self.cell_or_alternate, self.email, \
                        self.notes )


    class Meta:
        managed = False
        db_table = 'interoperability '


class IsicApplicant(models.Model):
    primary_key = models.BigIntegerField(primary_key=True)
    applicant = models.CharField(max_length=255, null=False)
    loi = models.BooleanField(default=False)
    moa = models.BooleanField(default=False)
    part_pl = models.BooleanField(default=False)
    ugc = models.BooleanField(default=False)
    isicsb_approved = models.BooleanField(default=False)
    user_level = models.SmallIntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'applicants'

class Site(models.Model):
    primary_key = models.BigIntegerField(primary_key=True)
    site_name = models.CharField(max_length=255, default='Unknown')
    # site_alias = models.CharField(max_length=255, default='Unknown')
    site_id = models.DecimalField(max_digits=5, decimal_places=2)
    site_asr = models.CharField(max_length=20, default='Unknown')
    site_location = models.CharField(max_length=255, default='Unknown')
    site_gps_coord = models.CharField(max_length=255, default='Unknown')
    state_owned = models.BooleanField(default=False)

    def __str__(self):
        return 'Site Name: {}    Site Alias: {}    Site Id: {} \
                Site ASR: {}     Site Location: {} Site GPS: {}'.format(
                                                                self.site_name,
                                                                self.site_alias,
                                                                self.site_id,
                                                                self.site_asr,
                                                                self.site_location,
                                                                self.site_gps_coord,
                                                                self.site_state_owned,
                                                                )
    class Meta:
        managed = False
        db_table = 'site'

class RenderPDF(models.Model):
    primary_key = models.BigIntegerField(primary_key=True)
    pdf_file = models.ForeignKey('Site',on_delete=models.CASCADE,)

    def __str__(self):
        return 'PDF : {}'.format(self.pdf_file)

    class Meta:
        managed = False
        db_table = 'pdf'

# https://gendpdc/iVista/Account/Login?ReturnUrl=%2fiVista%2fError%3faspxerrorpath%3d%2fiVista%2fAccount%2f&aspxerrorpath=/iVista/Account/
# GenWatch3 {'name':'username'}
# {'type':'password','name':'password'}
