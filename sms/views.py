from sms.models import Student, School
from rest_framework import viewsets, filters
from sms.serializers import StudentSerializer, SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('-name')
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'age']


class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


