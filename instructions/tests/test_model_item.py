from django.test import TestCase
from django.contrib.auth import get_user_model
from instructions.models import Instruction, Item


class ItemTests(TestCase):

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
        self.item = Item.objects.create(
            title='Test Item',
            amount='2g',
            instruction=self.instruction
        )

    def test_step(self):
        self.assertEqual(self.item.title, 'Test Item')
        self.assertEqual(self.item.description, '')
        self.assertEqual(self.item.amount, '2g')
        self.assertEqual(self.item.instruction, self.instruction)

    def test_string_representation(self):
        self.assertEqual(str(self.item), 'Test Item')
