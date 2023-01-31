from django.db import models


class Newsletter(models.Model):
    """database model of e-mails subscribers to the newsletter"""

    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Підписки'
        ordering = ('date', )

    def __str__(self):
        return self.email
