from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from hubs.models import UserProfile, Resource
from django.core.files.uploadedfile import SimpleUploadedFile


class TestCreateResource(APITestCase):

    def test_if_user_is_anonymous_returns_401(self):
        """Test creating a new resources as an anonymous user"""

        response = self.client.post('/hubs/resources/', {'title': 'a'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_if_user_is_authorized_returns_201(self):
        """Test creating new resources as an authorized user"""

        user = User.objects.create_user(username='test_user', password='test_pass')

        UserProfile.objects.create(user_name= "testing", user=user, role="staff")

        #Authenticate User
        self.client.force_authenticate(user=user)

        file_data = SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf")

        response = self.client.post(
                                '/hubs/resources/', 
                               {'title': 'a',
                                'description': 'new file',
                                'file': file_data,
                                'uploaded_by': user.id
                                },
                                format='multipart'
                                )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class TestGetResources(APITestCase):

    def test_user_is_anonymous_returns_200(self):
        """Test if anonymous users can get resources"""

        response = self.client.get('/hubs/resources/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestDeleteResources(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='test_user', password='test_pass')
        self.user_profile = UserProfile.objects.create(user=self.user, role='staff')

        self.resources = Resource.objects.create(
            title="testing_file",
            description="testing",
            file='file.pdf',
            uploaded_by=self.user_profile
        )

    def test_user_is_anonymous_returns_401(self):
        """Test if anonymous user can delete resources"""

        response = self.client.delete(f'/hubs/resources/{self.resources.id}/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_if_user_is_authorized_returns_204(self):
        """Delete resources as an authorized user"""

        #Authenticate User
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(f'/hubs/resources/{self.resources.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestUpdateResources(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='test_user', password='test_pass')
        self.user_profile = UserProfile.objects.create(user=self.user, role='staff')


        self.resources = Resource.objects.create(
            title="testing_file",
            description="testing",
            file="file.pdf",
            uploaded_by=self.user_profile
        )
         
        self.file_data = SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf")

    def test_user_is_anonymous_returns_401(self):
        """Test if anonymous users can't update resources"""

        response = self.client.put(f'/hubs/resources/{self.resources.id}/', {'title':'updated_file', 'description': 'test'})
        
        print(f"response: {response.content}")
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_if_user_is_authorized_returns_200(self):
        """Update resources as an authorized user"""

        #Authenticate User
        self.client.force_authenticate(user=self.user)

        response = self.client.put(f'/hubs/resources/{self.resources.id}/',
                                   {'title':'updated_file', 'description': 'test', 'file': self.file_data, 'uploaded_by': self.user_profile.id}, 
                                   format='multipart'
                                   )

        print(f"response: {response.content}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
