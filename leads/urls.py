from rest_framework import routers
from .api import LeadViewSet,ProjectViewSet
from . import views
from django.urls import path, include
from django.conf.urls import url


router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/projects', ProjectViewSet, 'projects')



# urlpatterns = [
#     # router.urls,
#     path('helloworld/',views.HelloWorld.as_view())

# ]
urlpatterns = [
    url(r'^hello-view/', views.HelloWorld.as_view()),
    url(r'', include(router.urls))
]