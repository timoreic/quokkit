from django.contrib.auth import get_user_model
from django.test import TestCase


class UserTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='user@email.com',
            handle='testuser',
            password='testpass123'
        )
        self.superuser = User.objects.create_superuser(
            email='superuser@email.com',
            handle='testsuperuser',
            password='testpass123'
        )

    def test_user(self):
        self.assertEqual(self.user.email, 'user@email.com')
        self.assertEqual(self.user.handle, 'testuser')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_superuser(self):
        self.assertEqual(self.superuser.email, 'superuser@email.com')
        self.assertEqual(self.superuser.handle, 'testsuperuser')
        self.assertTrue(self.superuser.is_active)
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)
