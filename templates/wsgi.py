"""
WSGI config for do_ipam project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('{{ netbox_virtualenv_path }}/lib/python3.5/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('{{ netbox_path }}/netbox')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netbox.settings")

# Activate your virtual env
activate_env=os.path.expanduser("{{ netbox_virtualenv_path }}/bin/activate_this.py")
exec(open(activate_env).read())

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
