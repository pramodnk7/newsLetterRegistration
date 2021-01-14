from django.urls import path
from .views import RegistrationListView, RegistrationDetailView

urlpatterns = [
	path('', RegistrationListView.as_view()),
	path('/<pk>', RegistrationDetailView.as_view())
]