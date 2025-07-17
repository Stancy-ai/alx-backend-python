#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock
from utils import memoize
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for utils.access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b"),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        expected_message = repr(path[-1])
        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """Unit tests for utils.get_json with mocked requests.get"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        with patch("utils.requests.get") as mock_get:
            # Configure the mock to return a response with the desired JSON payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            # Ensure requests.get was called exactly once with the correct URL
            mock_get.assert_called_once_with(test_url)

            # Ensure get_json returns the expected payload
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Unit tests for utils.memoize decorator"""

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            obj = TestClass()
            result1 = obj.a_property()
            result2 = obj.a_property()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
