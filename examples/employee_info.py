"""Collect employee information into a dictionary from a directory of files."""

import sys
import os

DELIM = ': '


class Employee(object):
    """Information for an employee."""

    def __init__(self, emp_id, name, title):
        self.id = emp_id
        self.name = name
        self.title = title

    def __str__(self):
        return "{}, {} ({})".format(self.name, self.title, self.id)


def parse_file(dirname, filename):
    """Parse a file into an Employee object."""
    emp_id = filename.split('.')[0]
    path = os.path.join(dirname, filename)
    emp_file = open(path, 'U')
    name = next(emp_file).strip().split(DELIM)[1]
    title = next(emp_file).strip().split(DELIM)[1]
    return Employee(emp_id, name, title)


def main():
    """Parse arguments and build the dictionary from each file."""
    target_dir = sys.argv[1]
    employees = {}

    filenames = os.listdir(target_dir)
    for filename in filenames:
        emp = parse_file(target_dir, filename)
        employees[emp.id] = emp
    for emp_id, emp in employees.items():
        print '{}: {}'.format(emp_id, emp)


if __name__ == "__main__":
    main()
