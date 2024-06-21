from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    description = models.TextField(verbose_name="Описание")
    published = models.BooleanField(verbose_name="Опубликовано")
    creeate_date = models.DateTimeField(verbose_name="Дата и время", auto_now_add=True)

    def __str__(self) -> str:
        return self.title