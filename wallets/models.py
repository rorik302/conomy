from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Wallet(models.Model):
    """Кошелек"""
    name = models.CharField('Название', max_length=150)
    balance = models.DecimalField('Баланс', max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wallets'


class Transaction(models.Model):
    """Транзакция"""
    wallet = models.ForeignKey(Wallet, verbose_name='Кошелек', on_delete=models.CASCADE, related_name='transactions')
    date = models.DateTimeField('Дата', default=timezone.now)
    amount = models.DecimalField('Сумма', max_digits=12, decimal_places=2)
    comment = models.TextField('Комментарий', blank=True)

    def __str__(self):
        return f'Транзакция от {self.date.strftime("%d.%m.%Y")} на сумму {self.amount} руб.'

    class Meta:
        db_table = 'transactions'


@receiver(post_save, sender=Transaction)
def update_balance(sender, instance, **kwargs):
    """Обновление баланса кошелька"""
    wallet = instance.wallet
    wallet_transactions = wallet.transactions.all()
    total_amount = wallet_transactions.aggregate(Sum('amount')).get('amount__sum')
    wallet.balance = total_amount
    wallet.save()
