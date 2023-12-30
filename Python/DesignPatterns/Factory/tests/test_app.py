import unittest

from DesignPatterns.Factory.src.app import BurgerFactory


class TestBurgerFactory(unittest.TestCase):
    def test_building_cheesebuger(self):
        # Arrange
        burger_factory = BurgerFactory()
        # Act
        actual = burger_factory.create_cheese_burger()
        # Assert
        assert actual.print() == ["bun", "cheese", "beef-patty"]

    def test_building_hamburger(self):
        # Arrange
        burger_factory = BurgerFactory()
        # Act
        actual = burger_factory.create_ham_burger()
        # Assert
        assert actual.print() == ["bun", "beef-patty"]
