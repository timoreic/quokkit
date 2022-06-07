from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignupTests(TestCase):

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_template(self):
        self.assertTemplateUsed(self.response, 'account/signup.html')

    def test_signup_form(self):
        get_user_model().objects.create_user(
            'newuser',
            'newuser@email.com'
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'newuser')
        self.assertEqual(
            get_user_model().objects.all()[0].email, 'newuser@email.com')
