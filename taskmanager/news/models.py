from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата и время публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)
    is_featured = models.BooleanField('Важная статья', default=False)
    image = models.ImageField('Изображение', upload_to='articles/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'