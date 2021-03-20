from django.urls import path
from rest_framework.routers import SimpleRouter

from wallets.views import WalletViewSet, TransactionListCreateAPIView, TransactionDestroyAPIView

router = SimpleRouter()
router.register('wallets', WalletViewSet)

urlpatterns = [
    path('transactions/<int:id>/', TransactionDestroyAPIView.as_view()),
    path('transactions/', TransactionListCreateAPIView.as_view()),
]
urlpatterns += router.urls
