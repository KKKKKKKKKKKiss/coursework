from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from users.forms import UserCreationForm
User = get_user_model()



class TestRegisterView(TestCase):

    def test_get(self):
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], UserCreationForm)


    def test_post_ok(self):
        email = 'test_email@mail.ru'

        payload = {
            'username': 'userr',
            'email': email,
            'password1': '12345678u',
            'password2': '12345678u',
        }

        response = self.client.post(reverse('register'), data=payload)

        user = User.objects.get(email=email)

        self.assertEqual(user.email, email)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(user.is_authenticated)


