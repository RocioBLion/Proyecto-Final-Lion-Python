import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from computer.models import Computer


class ComputerTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="Holahola12",
        )
        Computer.objects.create(brand="Apple", owner=self.test_user)
        Computer.objects.create(brand="Acer", owner=self.test_user)

        computer_test_num = 20
        self.mock_brands = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(2, 6))
                ]
            )
            for _ in range(computer_test_num)
        ]

        for mock_brand, in zip(self.mock_brands):
            Computer.objects.create(brand=mock_brand, owner=self.test_user)

    def test_computer_brand(self):
        """Computers creation are correctly identified"""
        apple_computer = Computer.objects.get(brand="Apple")
        acer_computer = Computer.objects.get(brand="Acer")
        self.assertEqual(apple_computer.owner.username, "testuser")
        self.assertEqual(acer_computer.owner.username, "testuser")

    def test_computer_list(self):
        for mock_brand, in zip(self.mock_brands):
            computer_test = Computer.objects.get(brand=mock_brand)
            self.assertEqual(computer_test.owner.username, "testuser")