from django.db import models
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class Article(models.Model):

    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    category = models.CharField(max_length=40, null=False, blank=False,  choices=status_choices, default='Новая',
                              verbose_name='категория')
    created_at = models.DateTimeField(auto_now=False, verbose_name='Время изменения')

    def __str__(self):
        return self.title