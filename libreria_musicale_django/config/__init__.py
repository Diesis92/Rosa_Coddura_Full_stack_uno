# Importa l'istanza Celery e la espone come 'celery_app'
from .celery import app as celery_app

# Garantisce che celery_app sia importabile da questo pacchetto
__all__ = ('celery_app',)