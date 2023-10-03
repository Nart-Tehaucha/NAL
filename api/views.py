from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import LetterSerializer, WordrulerSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response


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


