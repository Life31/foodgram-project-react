from django.db import models


class CreatedModel(models.Model):
    """
    Кастомная модель. Добавляет дату создания сущности.
    """
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        abstract = True
