#!/usr/bin/env python3
"""
module
"""
import unittest
from utils import *
from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase, mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Class to test
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Method to test
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Method to test that test_access_nested_map
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """
    Class testGetJson
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Method to test
        """
        mock_instance = Mock()
        mock_instance.json.return_value = test_payload
        with patch('requests.get', return_value=mock_instance):
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock_instance.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    Class to test TestMemoize
    """

    def test_memoize(self):
        """
        Method to test test_memoize
        """
        class TestClass:
            """
            Class TestClass
            """

            def a_method(self):
                """
                method to test a_method
                """
                return 42

            @memoize
            def a_property(self):
                """
                Method a_property
                """
                return self.a_method()
        with patch.object(TestClass, 'a_method') as test_method:
            class_instance = TestClass()
            class_instance.a_property
            class_instance.a_property
            test_method.assert_called_once
