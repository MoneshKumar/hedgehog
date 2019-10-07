from sms.models import Student, School
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Student
		fields = ['url', 'name', 'age', 'is_adult', 'school']


class SchoolSerializer(serializers.HyperlinkedModelSerializer):

	students = serializers.HyperlinkedRelatedField(many=True,
		read_only=True,
		view_name='student-detail'
	)

	class Meta:
		model = School
		fields = ['url', 'name', 'students']
