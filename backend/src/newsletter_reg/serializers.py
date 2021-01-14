from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Registration
		fields = ('name', 'email_id', 'phone_number')
