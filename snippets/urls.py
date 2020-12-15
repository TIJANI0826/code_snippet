from django.urls import include, path
from django.contrib.auth.models import User

from snippets import views
from snippets.serializers import UserSerializer, SnippetSerializer

from rest_framework import routers
from rest_framework import permissions ,viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.urlpatterns import format_suffix_patterns



router = routers.DefaultRouter()
router.register(r'snipes', views.SnippetListViewSet)
# router.register(r'posts', views.snippet_detail)

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    # path('',include(router.urls)),
    # path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
