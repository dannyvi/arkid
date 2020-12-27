'''
entrypoint of celery
'''

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# 此时显式声明，从当前目录导入；否则会从三方库中导入
import oauth2_provider    # pylint: disable=unused-import

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oneid.settings')
app = Celery(    # pylint: disable=invalid-name
    'oneid',
    # include={
    #     'tasksapp.tasks',
    #     'ldap.sql_backend.scripts',
    #     'plugins.crontab.tasks',
    # },
)
app.config_from_object(settings, namespace='CELERY')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(300, update_scim.s(),)


@app.task()
def update_scim():
    from scim.utils import sync_scim
    from scim.models import ScimApp
    print('sync scim:------')
    urls_list = ScimApp.objects.values_list('refresh_url', flat=True)
    print(urls_list)
    for url in urls_list:
        sync_scim(url)