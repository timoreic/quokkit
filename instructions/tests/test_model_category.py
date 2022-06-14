from django.test import TestCase
from django.contrib.auth import get_user_model
from instructions.models import Instruction, Category


class CategoryTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            email='user@email.com',
            password='testpass123'
        )
        self.instruction = Instruction.objects.create(
            title='Test Instruction',
            user=self.user
        )
        self.category = Category.objects.create(
            title='Test Category'
        )
        self.category.instructions.add(self.instruction)

    def test_category(self):
        self.assertEqual(self.category.title, 'Test Category')
        self.assertEqual(self.category.description, '')
        self.assertEqual(
            str(self.category.instructions.all()[0]),
            'Test Instruction')

    def test_string_representation(self):
        self.assertEqual(str(self.category), 'Test Category')
