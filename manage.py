#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Set the default Django settings module for the project
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netfix.settings")
    
    try:
        # Attempt to import the command-line utility for managing the Django project
        from django.core.management import execute_from_command_line
    except ImportError:
        # Handle the case where Django is not installed
        try:
            import django
        except ImportError:
            # Raise a detailed error if Django is missing
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    
    # Execute the command-line arguments using Django's management utility
    execute_from_command_line(sys.argv)
