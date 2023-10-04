from wordruler import models as wr_models
from lessons import models as l_models
from teachers import models as t_models
from students import models as s_models
from rest_framework import serializers



class LetterSerializer(serializers.ModelSerializer):
	class Meta:
		model = wr_models.Letter
		fields = '__all__'
		

class WordrulerSerializer(serializers.ModelSerializer):
	class Meta:
		model = wr_models.Wordruler
		fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
	class Meta:
		model = l_models.Lesson
		fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = t_models.Teacher
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = s_models.Student
		fields = '__all__'