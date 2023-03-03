from django.urls import path
from .models import Profile
from .views import ProfilesListView,ProfileView

urlpatterns = [
    path('',ProfilesListView.as_view()),
    path('<slug>',ProfileView.as_view())
]