from django.db import models
from django.urls import reverse

class Shu(models.Model):
    """шахтоуправление"""
    name = models.CharField("Шахто-управление", max_length=150)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Шахто-управление"
        verbose_name_plural = "Шахто-управления"

class Prof(models.Model):
    """Прафесия"""
    name = models.CharField("Праффесия", max_length=150)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Праффесия"
        verbose_name_plural = "Праффесии"

class Pp(models.Model):
    """Дроизводственое подраздиление"""
    name = models.CharField("Дроизводственое подраздиление", max_length=150)
    shu = models.ForeignKey(
        Shu, verbose_name="Шахто-управление", on_delete=models.SET_NULL, null=True
    )
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Дроизводственое подраздиление"
        verbose_name_plural = "Дроизводственое подраздиления"
        ordering = ("name", "shu")

class Uch(models.Model):
    """Участок"""
    name = models.CharField("Участок", max_length=150)
    shu = models.ForeignKey(
        Shu, verbose_name="Шахто-управление", on_delete=models.SET_NULL, null=True
    )
    pp = models.ForeignKey(
        Pp, verbose_name="Дроизводственое подраздилени", on_delete=models.SET_NULL, null=True
    )
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Участок"
        verbose_name_plural = "Участки"
        ordering = ("name", "shu", "pp")

class Users(models.Model):
    """Люди"""
    name = models.CharField("Фамилия И.О.", max_length=150)
    nomer = models.PositiveIntegerField("Номер")
    prof = models.ForeignKey(
        Prof, verbose_name="Проффесия", on_delete=models.SET_NULL, null=True
    )
    shu = models.ForeignKey(
        Shu, verbose_name="Шахто-управление", on_delete=models.SET_NULL, null=True
    )
    pp = models.ForeignKey(
        Pp, verbose_name="Производственое подраздилени", on_delete=models.SET_NULL, null=True
    )
    uch= models.ForeignKey(
        Uch, verbose_name="Участок", on_delete=models.SET_NULL, null=True
    )
   # url = models.SlugField(max_length=130, unique=True)
    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("users_detail", kwargs={"slug": self.id})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"
        ordering = ("name", "nomer", "shu", "pp", "uch", "prof")


