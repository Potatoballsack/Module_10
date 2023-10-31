"""
Program: test.py
Author: Guyver Baccam
Last date modified: 10/31/2023
Write unit tests to test the Student class:
"""

import unittest
from student import Student

class TestStudent(unittest.TestCase):
    # Tests for the Student class. 
    def setUp(self):
        # Create a student for use in all test methods.
        self.student = Student('Bob', 'Marley', 'Engineering', 3.5)

    def tearDown(self):
        # Tears down the student created.
        self.student = None

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Bob')
        self.assertEqual(self.student.first_name, 'Marley')
        self.assertEqual(self.student.major, 'Engineering')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.gpa, 3.5)

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Bob, Marley has major Engineering with gpa: 3.5') # Calls the returning value of __str__.

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = Student('', 'Marley', 'Engineering', 3.5)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = Student('Bob', '', 'Engineering', 3.5)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = Student('Bob', 'Marley', '', 3.5)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = Student('Bob', 'Marley', 'Engineering', '')
        with self.assertRaises(ValueError):
            s = Student('Bob', 'Marley', 'Engineering', -1)
        with self.assertRaises(ValueError):
            s = Student('Bob', 'Marley', 'Engineering', 5.1)

if __name__ == '__main__':
    unittest.main()