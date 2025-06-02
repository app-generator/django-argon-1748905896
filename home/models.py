# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Empleado(models.Model):

    #__Empleado_FIELDS__
    cedula = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    salario mensual = models.BooleanField()
    iban = models.CharField(max_length=255, null=True, blank=True)
    fecha de ingreso = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha de salida = models.DateTimeField(blank=True, null=True, default=timezone.now)
    vacaciones = models.IntegerField(null=True, blank=True)
    incapacidades = models.DateTimeField(blank=True, null=True, default=timezone.now)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)

    #__Empleado_FIELDS__END

    class Meta:
        verbose_name        = _("Empleado")
        verbose_name_plural = _("Empleado")


class Sucursal(models.Model):

    #__Sucursal_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Sucursal_FIELDS__END

    class Meta:
        verbose_name        = _("Sucursal")
        verbose_name_plural = _("Sucursal")


class Puesto(models.Model):

    #__Puesto_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Puesto_FIELDS__END

    class Meta:
        verbose_name        = _("Puesto")
        verbose_name_plural = _("Puesto")



#__MODELS__END
