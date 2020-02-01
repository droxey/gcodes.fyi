from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Firmware(models.Model):
    name = models.CharField(
        _("Firmware Name"), max_length=50, help_text="Example: Marlin")

    class Meta:
        verbose_name = _('Firmware')
        verbose_name_plural = _('Firmware')


class FirmwareVersion(models.Model):
    firmware = models.ForeignKey(
        Firmware, on_delete=models.CASCADE, verbose_name=_("Firmware"))
    version = models.CharField(
        _("Version Name/Number"), max_length=20, help_text="Example: bugfix-1.1.9")

    class Meta:
        verbose_name = _('Firmware Version')
        verbose_name_plural = _('Firmware Versions')


class Command(models.Model):
    code = models.CharField(_("Code"), max_length=64,
                            help_text="Example: M500")
    description = models.TextField(
        _("Description"), help_text="Example: Saves settings to memory.")
    firmware_support = models.ManyToManyField(
        FirmwareVersion, verbose_name=_("Firmware Support"))
    created_by = models.ForeignKey("django.contrib.auth.models.User", verbose_name=_(
        "Added By"), on_delete=models.CASCADE)
    created_date = models.DateField(_("Creation Date"), default=timezone.now())
    updated_by = models.ForeignKey("django.contrib.auth.models.User", verbose_name=_(
        "Updated By"), on_delete=models.CASCADE)
    updated_date = models.DateField(_("Updated Date"), default=timezone.now())

    class Meta:
        verbose_name = _('Command')
        verbose_name_plural = _('Commands')
