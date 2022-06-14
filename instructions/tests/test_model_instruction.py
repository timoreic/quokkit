from django.test import TestCase
from django.contrib.auth import get_user_model
from instructions.models import Instruction


class InstructionTests(TestCase):

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

    def test_instruction(self):
        self.assertEqual(self.instruction.title, 'Test Instruction')
        self.assertEqual(self.instruction.subtitle, '')
        self.assertEqual(self.instruction.description, '')
        self.assertTrue(self.instruction.is_public)
        self.assertEqual(self.instruction.user, self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.instruction), 'Test Instruction')
