from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='ФИО')
    phone = models.CharField(max_length=11, null=False, verbose_name='Номер телефона')
    systems = models.ManyToManyField('System', verbose_name='Системы', blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['name']

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(
        max_length=200,
        db_index=True,
        null=False,
        verbose_name="Информационная система"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Система'
        verbose_name_plural = 'Системы'
        ordering = ['name']


class Message(models.Model):
    '''
    Таблица для сохранения результатов выполненной рассылки.
    '''
    text = models.TextField(max_length=60, null=False, verbose_name='Текст')
    system = models.ForeignKey('System', on_delete=models.DO_NOTHING)
    sended_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Отправлено')
    status = models.TextField(max_length=20, default='unknown', verbose_name='Статус')
