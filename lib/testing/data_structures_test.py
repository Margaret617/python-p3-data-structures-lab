# lib/testing/data_structures_test.py

import pytest
from data_structures import get_names, get_spiciest_foods, print_spicy_foods, get_spicy_food_by_cuisine, print_spiciest_foods, get_average_heat_level, create_spicy_food


class TestDataStructures:
    SPICY_FOODS = [
        {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9,
        },
        {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        },
        {
            "name": "Mapo Tofu",
            "cuisine": "Sichuan",
            "heat_level": 6,
        },
    ]
    
    def test_get_names(self):
        assert get_names(self.SPICY_FOODS) == ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

    def test_get_spiciest_foods(self):
        assert get_spiciest_foods(self.SPICY_FOODS) == [
            {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
            {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
        ]

    def test_print_spicy_foods(self):
        # Test implementation

        def test_get_spicy_food_by_cuisine(self):
            assert get_spicy_food_by_cuisine(self.SPICY_FOODS, "American") == {
               "name": "Buffalo Wings",
               "cuisine": "American",
               "heat_level": 3
            }
        assert get_spicy_food_by_cuisine(self.SPICY_FOODS, "Thai") == {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9
        }

    def test_print_spiciest_foods(self):
        # Test implementation

        def test_get_average_heat_level(self):
            assert get_average_heat_level(self.SPICY_FOODS) == 6

    def test_create_spicy_food(self):
        new_food = {
            'name': 'Griot',
            'cuisine': 'Haitian',
            'heat_level': 10,
        }
        expected = self.SPICY_FOODS + [new_food]
        assert create_spicy_food(self.SPICY_FOODS, new_food) == expected
