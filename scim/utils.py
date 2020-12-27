import os
import threading
import requests
from oneid_meta.models import User, Dept
from siteapi.v1.serializers.dept import DeptSerializer, DeptDetailSerializer
from siteapi.v1.serializers.user import UserSerializer

def _sync_scim(url):
    users = User.objects.all()
    user_srl = UserSerializer(users, many=True)
    print('---user data', user_srl.data)
    user_resp = requests.post(os.path.join(url, 'users'), json=user_srl.data)
    depts = Dept.objects.all()
    dept_srl = DeptDetailSerializer(depts, many=True)
    print('---user data', dept_srl.data)
    dept_resp = requests.post(os.path.join(url, 'groups'), json=dept_srl.data)

def sync_scim(url):
    threading.Thread(target=_sync_scim, args=(url, )).start()