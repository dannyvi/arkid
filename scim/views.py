from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from scim.models import ScimApp
from scim.serializers import ScimAppSerializer
from scim.utils import sync_scim


class ScimAppViewset(ModelViewSet):
    queryset = ScimApp.objects.all()
    serializer_class = ScimAppSerializer
    permission_classes = [AllowAny, ]


    @action(methods=['get'], detail=True, url_path='doSync', permission_classes=[permissions.AllowAny])
    def do_sync(self, request, *args, **kwargs):
        app = self.get_object()
        url = app.refresh_url
        sync_scim(url)
        return Response()


    @action(methods=['post', 'delete'], detail=False, url_path='users', permission_classes=[permissions.AllowAny])
    def users(self, request, *args, **kwargs):
        print('sync users called')
        return Response()

    @action(methods=['post', 'delete'], detail=False, url_path='groups', permission_classes=[permissions.AllowAny])
    def groups(self, request, *args, **kwargs):
        print('sync groups called')
        return Response()
