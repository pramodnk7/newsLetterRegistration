from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Registration
from .serializers import RegistrationSerializer


class RegistrationListView(ListAPIView):
	queryset = Registration.objects.all()
	serializer_class = RegistrationSerializer


class RegistrationDetailView(RetrieveAPIView):
	queryset = Registration.objects.all()
	serializer_class = RegistrationSerializer