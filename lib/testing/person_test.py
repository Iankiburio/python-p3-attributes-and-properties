#!/usr/bin/env python3

from person import Person

import sys
import io

class Person:
    APPROVED_JOBS = ['Engineer', 'Developer', 'QA', 'Sales', 'ITC']

    def __init__(self, name, job):
        self._name = name
        self._job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print("Name must be a string.")
        elif not (1 <= len(value) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in self.APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = value

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person".'''
        guido = Person(name='Guido', job='Sales')
        assert type(guido) == Person
        
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="Guido", job="Sales")
        person.name = ""
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n"

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="Guido", job='Sales')
        person.name = 123
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string.\n"

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="Guido", job='Sales')
        person.name = "What do Persons do on their day off? Can't lie around - that's their job."
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n"

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        guido = Person("Guido", "Sales")
        guido.name = "Guido"
        assert guido.name == "Guido"

    def test_valid_name_title_case(self):
        '''converts name to title case and saves if between 1 and 25 characters'''
        guido = Person(name="guido van rossum", job='Sales')
        guido.name = "guido van rossum"
        assert guido.name == "Guido Van Rossum"

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="Guido", job='Sales')
        person.job = "Benevolent dictator for life"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() =="Job must be in the list of approved jobs.\n"

    def test_job_in_list(self):
        '''saves job if in job list.'''
        guido = Person(name="Guido", job='Sales')
        guido.job = "ITC"
        assert guido.job == "ITC"
