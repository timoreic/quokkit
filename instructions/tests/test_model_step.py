from django.test import TestCase
from django.contrib.auth import get_user_model
from instructions.models import Instruction, Step


class StepTests(TestCase):

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
        self.step = Step.objects.create(
            title='Test Step',
            number=1,
            instruction=self.instruction
        )

    def test_step(self):
        self.assertEqual(self.step.title, 'Test Step')
        self.assertEqual(self.step.description, '')
        self.assertEqual(self.step.number, 1)
        self.assertEqual(self.step.instruction, self.instruction)

    def test_string_representation(self):
        self.assertEqual(str(self.step), 'Test Step')
