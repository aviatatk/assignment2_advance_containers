from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class DatabaseConnectionTest(TestCase):
    def test_database_connection(self):
        # This test passes if we can create a user.
        user_count_before = User.objects.count()
        User.objects.create_user(username='testuser', password='testpass')
        user_count_after = User.objects.count()
        self.assertEqual(user_count_after, user_count_before + 1)

class JWTAuthenticationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_obtain_jwt_token(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_access_protected_endpoint_without_token(self):
        url = reverse('user_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_protected_endpoint_with_token(self):
        # Obtain JWT token.
        token_url = reverse('token_obtain_pair')
        token_response = self.client.post(token_url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        access_token = token_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        profile_url = reverse('user_profile')
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
