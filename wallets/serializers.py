from rest_framework import serializers

from wallets.models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    balance = serializers.FloatField(read_only=True)

    class Meta:
        model = Wallet
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=False, format='%d.%m.%Y')
    amount = serializers.FloatField()

    class Meta:
        model = Transaction
        fields = '__all__'
