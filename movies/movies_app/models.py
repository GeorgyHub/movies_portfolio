from django.db import models

# Create your models here.
class Movies(models.Model):
    class Meta:
        verbose_name = "Фильмы"
        verbose_name_plural = "Фильм"
        ordering = ["-created_at"]

    name = models.CharField(max_length=50, null=True, verbose_name = "Имя")
    image = models.ImageField(upload_to='media/image/%Y/%M/%D', verbose_name = "Изображение")
    text = models.TextField(max_length=300, null=True, verbose_name = "Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Создан")