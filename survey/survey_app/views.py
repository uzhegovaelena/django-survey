from django.shortcuts import render

import datetime
import logging

from rest_framework import viewsets, decorators, response, permissions
from .serializers import SurveySerializer, QuestionSerializer
from .models import Survey, Question
from .permissions import SurveyPermission, QuestionPermission


logger = logging.getLogger(__name__)


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (permissions.IsAdminUser, )


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (QuestionPermission, )


# class VoteViewSet(viewsets.ModelViewSet):
#     queryset = Vote.objects.all()
#     serializer_class = VoteSerializer
#     http_method_names = ('get', 'post')
#
#     def perform_create(self, serializer):
#         if self.request.user.is_authenticated:
#             return serializer.save(user=self.request.user)
#
#         return super().perform_create(serializer)
