<<<<<<< HEAD
# manage.py (правильная версия)
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cw_2.settings')
=======
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_4.settings')
>>>>>>> abc4b35 (Первый коммит)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

<<<<<<< HEAD
=======

>>>>>>> abc4b35 (Первый коммит)
if __name__ == '__main__':
    main()
