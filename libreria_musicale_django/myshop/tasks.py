from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta

from .models import Order, Notification


@shared_task(
    autoretry_for=(Exception,),
    max_retries=3,
    default_retry_delay=60,
    retry_backoff=True
)
def send_order_confirmation():
    # """
    # Invia email di conferma ordine in modo asincrono.
    # """

    # try:
    #     order = Order.objects.get(id=order_id)

    #     send_mail(
    #         subject="Conferma ordine",
    #         message=f"Grazie {order.user.username}, ordine {order.id} confermato!",
    #         from_email="noreply@shop.com",
    #         recipient_list=[order.user.email],
    #         fail_silently=False,
    #     )

    #     return f"Email ordine {order.id} inviata"

    # except Order.DoesNotExist:
        return f"Ordine  non trovato"


@shared_task
def cleanup_old_notifications():
    """
    # Cancella notifiche più vecchie di 30 giorni.
    # """

    # limit_date = timezone.now() - timedelta(days=30)

    # deleted, _ = Notification.objects.filter(
    #     created_at__lt=limit_date
    # ).delete()

    return f"Eliminate  notifiche vecchie"
#docker compose -d
   
# per invocare il task:
# python manage.py shell
# from myshop.tasks import send_order_confirmatio
# send_order_confirmation.delay()

#tre shell diverse:
# celery -A config worker -l info --pool=solo avvio celery windows
# celery -A config beat -l info
# celery -A config flower --port=5555