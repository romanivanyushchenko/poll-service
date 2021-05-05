from rest_framework import mixins
from rest_framework import viewsets

from api_app.models import PollModel
from api_app.serialisers import PollSerializer


class PollListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer
