#!/usr/bin/env python3
class Person:
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
        if value not in APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = value
