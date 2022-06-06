from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import SignupPageView


class SignupPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_home_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_template(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')

    def test_home_url_resolves_signuppageview(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )
