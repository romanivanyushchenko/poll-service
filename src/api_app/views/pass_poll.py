from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api_app.models import PollModel
from api_app.serialisers.pass_poll import PassPollSerializer
from api_app.services.user_answers import create_user_answers


class PassPollViewSet(viewsets.GenericViewSet):
    """
    Прохождение опроса
    """
    queryset = PollModel.objects.none()
    serializer_class = PassPollSerializer
    permission_classes = (AllowAny,)

    def get_poll_id(self):
        try:
            return int(self.request.data['poll_id'])
        except:
            return None

    def get_serializer_context(self):
        context = super(PassPollViewSet, self).get_serializer_context()
        context['poll_id'] = self.get_poll_id()
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dtos = serializer.get_dto()
        create_user_answers(dtos)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
