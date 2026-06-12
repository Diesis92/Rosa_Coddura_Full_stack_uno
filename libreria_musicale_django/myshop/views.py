from django.db import transaction
from django.http import JsonResponse

from .models import Order
from myshop.task import send_order_confirmation


def place_order(request):
    order = Order.objects.create(
        user=request.user,
        total=100
    )

    def trigger_task():
        send_order_confirmation.delay(order.id)

    transaction.on_commit(trigger_task)

    return JsonResponse({
        "status": "success",
        "order_id": order.id
    })
