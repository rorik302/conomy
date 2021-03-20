from django.db import models


class Wallet(models.Model):
    """Кошелек"""
    name = models.CharField('Название', max_length=150)
    balance = models.DecimalField('Баланс', max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wallets'


class Transaction(models.Model):
    """Транзакция"""
    wallet = models.ForeignKey(Wallet, verbose_name='Кошелек', on_delete=models.CASCADE)
    date = models.DateField('Дата', auto_now_add=True)
    amount = models.DecimalField('Сумма', max_digits=12, decimal_places=2)
    comment = models.TextField('Комментарий', blank=True)

    def __str__(self):
        return f'Транзакция от {self.date} на сумму {self.amount}'

    class Meta:
        db_table = 'transactions'
