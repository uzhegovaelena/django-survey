from rest_framework import routers
from survey_app.views import SurveyViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register('api/survey', SurveyViewSet, 'survey')
router.register('api/question', QuestionViewSet, 'survey')
# router.register('api/vote', VoteViewSet, 'survey')

urlpatterns = router.urls