from django.db import models


class Test(models.Model):

    POSITIVE = 'Pos'
    NEGATIVE = 'Neg'
    INVALID = 'Inv'
    results = [
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
        (INVALID, 'Invalid'),
    ]

    result = models.CharField(
        max_length=8,
        choices=results,
        default='Negative',
    )

    def __str__(self):
        return self.result
