from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from wallets.models import Wallet, Transaction
from wallets.serializers import WalletSerializer, TransactionSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    @action(methods=['GET'], detail=True)
    def transactions(self, request, *args, **kwargs):
        instance = self.get_object()
        transactions = instance.transactions.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class TransactionAPIView(GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionListCreateAPIView(ListCreateAPIView, TransactionAPIView):
    pass


class TransactionDestroyAPIView(DestroyAPIView, TransactionAPIView):
    lookup_field = 'id'
