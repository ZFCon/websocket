import os
import django
from channels.routing import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ws.settings')
# django.setup()
application = get_wsgi_application()