#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_2.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_1.settings')
>>>>>>> e78adcc (Initial commit)
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cw_2.settings')
>>>>>>> c6dbf57 (Инициализация проекта cw_2)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
