from rest_framework import mixins
from rest_framework import viewsets

from api_app.models import PollModel
from api_app.serialisers.polls import PollSerializer

class PollsViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Просмотр созданных опросов
    """
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer
