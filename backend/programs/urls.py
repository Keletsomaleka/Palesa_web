from django.urls import path
from .views import WellnessProgramListview,WellnessProgramView,ActiveView

urlpatterns = [
    path('',WellnessProgramListview.as_view()),
    path('active',ActiveView.as_view()),
    path('<pk>',WellnessProgramView.as_view())
]