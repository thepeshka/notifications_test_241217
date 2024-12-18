from datetime import datetime, timedelta, timezone

from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from notifications.models import Supplier
from notifications.tasks import send_notifications
from notifications.consts import DISTRICT_ID_TO_UTC_OFFSET_MAP

class NotificationViewSet(GenericViewSet):
    @action(["POST"], False)
    def schedule(self, request, *args, **kwargs):
        today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        district_id = None
        for supplier in Supplier.objects.filter(district_id__isnull=False).iterator():
            if district_id is None:
                district_id = supplier.district_id
            if district_id != supplier.district_id:
                utc_offset = DISTRICT_ID_TO_UTC_OFFSET_MAP[district_id]
                send_notifications.apply_async(eta=today + timedelta(hours=10 + utc_offset), args=(district_id,))
                district_id = supplier.district_id
        utc_offset = DISTRICT_ID_TO_UTC_OFFSET_MAP[district_id]
        send_notifications.apply_async(eta=today + timedelta(hours=10 + utc_offset), args=(district_id,))
        return Response()
    
    @action(["POST"], False)
    def run_now(self, request, *args, **kwargs):
        send_notifications.apply_async()
        return Response()
