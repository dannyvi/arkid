from django.db import models

from oneid_meta.models.app import APP

class ScimApp(APP):
    refresh_url = models.CharField('地址', max_length=255, default=None, null=True, blank=True)
    inteval = models.SmallIntegerField('间隔', default=5)