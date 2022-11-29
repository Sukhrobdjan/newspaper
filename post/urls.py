from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UsersListView,UserDetailView

urlpatterns = [
    path('users/', UsersListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)


