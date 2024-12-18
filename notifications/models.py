from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, BooleanField, CharField, TextField, SET_NULL


class District(Model):
    name = CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"


class Area(Model):
    name = CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Supplier(Model):
    name = CharField("Название", max_length=255)
    contact_person = TextField("Контактное лицо", null=True, blank=True)
    inn = CharField("ИНН", max_length=15, null=True, blank=True)
    storage_address = TextField("Адрес склада", null=True, blank=True)
    phone = CharField("Номер телефона", max_length=255)
    subscription_cancelled = BooleanField("Отписан ли от рассылки", default=False)
    subscription_admin = BooleanField("Отписан ли от рассылки админом", default=False)
    district = ForeignKey(District, verbose_name="Область", on_delete=SET_NULL, null=True, blank=True, related_name="suppliers")
    area = ForeignKey(Area, verbose_name="Район", on_delete=SET_NULL, null=True, blank=True)
    manager = ForeignKey(User, verbose_name="Менеджер", on_delete=SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
