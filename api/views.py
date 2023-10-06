from json import JSONDecodeError
from django.http import JsonResponse, HttpResponse
from .serializers import LetterSerializer, WordrulerSerializer, StudentSerializer, LessonSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status, authentication, permissions
from rest_framework.response import Response
from wordruler.models import Letter, Wordruler
from students.models import Student
from teachers.models import Teacher
from lessons.models import Lesson
from django.views.decorators.csrf import csrf_exempt



# API VIEWS

class LetterAPIView(views.APIView):
    """
    A simple APIView for creating letter entires.
    """
    serializer_class = LetterSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request) # Get JSON data from frontend and parse it
            serializer = LetterSerializer(data=data) # Serialize the JSON into an Model Object
            if serializer.is_valid(raise_exception=True):
                serializer.save() # Save to Database
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
        
class WordRulerAPIView(views.APIView):
    """
    A simple APIView for creating wordruler entires.
    """
    serializer_class = WordrulerSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request) # Get JSON data from frontend and parse it
            serializer = WordrulerSerializer(data=data) # Serialize the JSON into an Model Object
            if serializer.is_valid(raise_exception=True):
                serializer.save() # Save to Database
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)


class ListLetters(views.APIView):
    """
    View to list all letters in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        letters = Letter.objects.all()
        serializer = LetterSerializer(letters, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = LetterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=400)
    
class ListWordrulers(views.APIView):
    """
    View to list all Wordrulers in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        wordrulers = Wordruler.objects.all()
        serializer = WordrulerSerializer(data=wordrulers)
        return Response(serializer)

class ListStudents(views.APIView):
    """
    View to list all Student in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all Students.
        """

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

@csrf_exempt
def letter_detail(request, pk):
    """
    Retrieve, update or delete a letter.
    """
    try:
        letter = Letter.objects.get(pk=pk)
    except Letter.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LetterSerializer(letter)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LetterSerializer(letter, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        letter.delete()
        return HttpResponse(status=204)
    

@csrf_exempt
def create_letter_dict_by_student(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request) # Get JSON data from frontend and parse it
            if not 'pk' in data.keys():
                return JsonResponse("Student ID was not provided.", status= 400) 
            
            curr_student = Student.objects.get(pk=data['pk'])
            curr_teacher = Teacher.objects.first() # Hard coded, change later

            wordruler_by_student, wr_created = Wordruler.objects.get_or_create(
                student = curr_student,
                teacher = curr_teacher
            )

            letters = wordruler_by_student.letters.all()
            
            # Create dict that maps every existing letter to a key, null if student doesn't have letter
            letter_dict = {}

            for l in letters:
                serializer = LetterSerializer(l)
                letter_dict.setdefault(l.letter, serializer.data)
            
            for c in 'abcdefghijklmnopqrstuvwxyz':
                letter_dict.setdefault(c)

            # Sort dict alphabetically
            letter_dict = dict(sorted(letter_dict.items()))
            
            return JsonResponse(letter_dict)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
        

class ListLessons(views.APIView):
    """
    View to list all Lessons in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all Students.
        """

        lesson = Lesson.objects.all()
        serializer = LessonSerializer(lesson, many=True)
        return Response(serializer.data)


@csrf_exempt
def lesson_get_by_student(request, student_pk):
    """
    Retrieve, update or delete a lesson.
    """
    try:
        lesson = Lesson.objects.filter(student = student_pk).first()
        if not lesson:
            raise Lesson.DoesNotExist
    except Lesson.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LessonSerializer(lesson)
        return JsonResponse(serializer.data)