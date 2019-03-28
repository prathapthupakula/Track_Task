from django.urls import path,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router=routers.DefaultRouter()
router.register("track",views.TrackViewSet)
router.register("question",views.QuestionViewSet)
router.register("choice",views.ChoiceViewSet)
# router.register("test1",views.QuestionData2ViewSet)

urlpatterns =[
    # path('', views.index, name='index'),
    path('',include(router.urls)),
    # path('track/',views.TrackData),
    # path("test/",views.TestCRED.as_view())
    # path('postquestion/<int:pk>',views.QuestionData2)
]
# urlpatterns = format_suffix_patterns(urlpatterns)