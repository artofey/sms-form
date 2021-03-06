from django.db import models


class Contact(models.Model):
    """
    Таблица со списком контактов для оповещения
    """
    name = models.CharField(max_length=100, db_index=True, verbose_name='ФИО')
    phone = models.CharField(max_length=11, null=False, unique=True, verbose_name='Номер телефона')
    systems = models.ManyToManyField('System', verbose_name='Системы')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['name']

    def __str__(self):
        return self.name


class System(models.Model):
    """
    Таблица со списком информационных систем
    """
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
    """
    Таблица для сохранения результатов выполнения рассылки
    """
    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['-sended_time']

    text = models.TextField(max_length=200, null=False, verbose_name='Текст')
    systems = models.ManyToManyField('System', verbose_name='Системы')
    sended_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Отправлено')
    status = models.CharField(max_length=20, default='unknown', verbose_name='Статус')
