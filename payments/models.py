from django.core.validators import MinValueValidator
from django.db import models


class Users(models.Model):
    user_name = models.CharField(blank=False, unique=True, max_length=255)
    user_password = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return f'{self.user_name} ({self.user_password})'


class Wallets(models.Model):
    wallet_num = models.CharField(blank=False, unique=True, max_length=16)
    wallet_sum = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False,
                                related_name='wallets')

    def __str__(self):
        return f'[{self.wallet_num}]: {self.wallet_sum}'


class Transactions(models.Model):
    sum = models.IntegerField(blank=False)
    source_wallet_id = models.ForeignKey(Wallets, on_delete=models.CASCADE, blank=False, related_name='source_wallet')
    destination_wallet_id = models.ForeignKey(Wallets, on_delete=models.CASCADE, blank=False,
                                              related_name='destination_wallet')

    def __str__(self):
        return f'Transfer [{self.sum}]'
