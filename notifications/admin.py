from django.contrib.admin import register, ModelAdmin

from notifications.models import Supplier, Area, District

@register(Area)
class AreaAdmin(ModelAdmin):
    pass

@register(District)
class DistrictAdmin(ModelAdmin):
    pass

@register(Supplier)
class SupplierAdmin(ModelAdmin):
    pass
