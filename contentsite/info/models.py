from django.db import models

class Infomation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    level_1 = models.CharField(max_length=255, blank=True, null=True)
    level_2 = models.CharField(max_length=255, blank=True, null=True)
    level_3 = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    target_post = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    edu_requirements = models.CharField(max_length=255, blank=True, null=True)
    exp_requirements = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    job_requirements = models.CharField(max_length=2000, blank=True, null=True)
    detail_url = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'info_infomation'