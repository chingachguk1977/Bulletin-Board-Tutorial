from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Advert(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=128, verbose_name='Ad title')
    text = models.TextField(verbose_name='Ad body')
    CATS = (
        ('tanks', 'Tanks'),
        ('heals', 'Healers'),
        ('dd', "DD's"),
        ('traders', 'Traders'),
        ('givers', 'Quest Givers'),
        ('smiths', 'Smiths'),
        ('tanners', 'Tanners'),
        ('potions', 'Potion Makers'),
        ('spellcasters', 'Spell Casters')
    )
    category = models.CharField(
        max_length=12, choices=CATS, default='tanks', verbose_name='Category'
    )
    create = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    attach = models.FileField(
        upload_to='uploads/%Y/%m/%d/', blank=True, null=True, verbose_name='Attachment'
    )

    class Meta:
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'

    def get_absolute_url(self):
        return reverse('bill_board:detail', args=[str(self.pk)])

    def __str__(self):
        return f'{self.title}'


class Resp(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='User'
    )
    post = models.ForeignKey(Advert, on_delete=models.CASCADE, verbose_name='Advertisement')
    text = models.TextField(verbose_name='Response body')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Response Date')
    status = models.BooleanField(default=False, verbose_name='Accepted')

    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'

    def get_absolute_url(self):
        return reverse('bill_board:detail', args=[str(self.post.pk)])

    def __str__(self):
        return f'{self.text[:64]}' if len(self.text > 64) else f'{self.text}'
