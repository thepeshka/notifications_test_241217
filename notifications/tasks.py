from celery import shared_task
from notifications.models import Supplier

@shared_task
def send_notifications(district_id=None):
    qs = Supplier.objects
    if district_id is not None:
        qs = qs.filter(district_id=district_id)
    for supplier in qs.iterator():
        print(f"Send notification to '{supplier.name}'")
