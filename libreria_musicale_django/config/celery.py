import os
from celery import Celery

# Imposta il settings module di Django per Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Crea l'app Celery
app = Celery('config')

# Carica la configurazione da settings.py con prefisso CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Scopre automaticamente i task nelle app installate
app.autodiscover_tasks()