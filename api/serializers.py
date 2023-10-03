from wordruler import models
from rest_framework import serializers



class LetterSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Letter
		fields = '__all__'
		

class WordrulerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Wordruler
		fields = '__all__'