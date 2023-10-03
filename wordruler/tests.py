from . models import Letter
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status



class LetterTestCase(APITestCase):

    """
    Test suite for Letter
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "letter": "a",
            "letter_name": "This is a test letter"
        }
        self.url = "/api/addletter/"

    def test_create_letter(self):
        '''
        test LetterViewSet create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Letter.objects.count(), 1)
        self.assertEqual(Letter.objects.get().letter, "a")

    def test_create_letter_without_letter(self):
        '''
        test LetterViewSet create method when letter is not in data
        '''
        data = self.data
        data.pop("letter")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_letter_when_letter_equals_blank(self):
        '''
        test LetterViewSet create method when letter is blank
        '''
        data = self.data
        data["letter"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_letter_without_letter_name(self):
        '''
        test LetterViewSet create method when letter_name is not in data
        '''
        data = self.data
        data.pop("letter_name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_letter_when_letter_name_equals_blank(self):
        '''
        test LetterViewSet create method when letter_name is blank
        '''
        data = self.data
        data["letter_name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)