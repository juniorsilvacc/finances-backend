from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from rest_framework.exceptions import ValidationError
from django.db.models import Sum
from django.shortcuts import get_object_or_404


class TransactionCreateView(APIView):

    def post(self, request):
        try:
            serializer = TransactionSerializer(data=request.data)

            if serializer.is_valid():
                value = serializer.validated_data.get('value')
                transaction_type = serializer.validated_data.get('type')

                if value <= 0:
                    raise ValidationError('O valor da transação deve ser maior que zero.')

                total = 0
                if transaction_type == 'income':
                    total += value
                elif transaction_type == 'outcome':
                    total -= value
                else:
                    raise ValidationError("O tipo de transação deve ser 'income' ou 'outcome'.")

                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Detail": "Erro inesperado: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TransactionListView(APIView):

    def get(self, request):
        try:
            transactions = Transaction.objects.all()

            # Filtrando transações de 'income' e 'outcome'
            income_transactions = transactions.filter(type='income')
            outcome_transactions = transactions.filter(type='outcome')

            # Somando os valores das transações de 'income'
            total_income = income_transactions.aggregate(total=Sum('value'))['total'] or 0

            # Somando os valores das transações de 'outcome'
            total_outcome = outcome_transactions.aggregate(total=Sum('value'))['total'] or 0

            # Calculando o saldo total (income - outcome)
            total_balance = total_income - total_outcome

            serializer = TransactionSerializer(transactions, many=True)

            return Response({
                'transactions': serializer.data,
                'total_income': total_income,
                'total_outcome': total_outcome,
                'total_balance': total_balance
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Detail": "Erro inesperado: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TransactionDeleteView(APIView):

    def delete(self, request, pk):
        try:
            # Busca a transação pelo ID ou retorna 404 se não existir
            transaction = get_object_or_404(Transaction, pk=pk)

            transaction.delete()

            return Response({"message": "Transação deletada com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"Detail": "Erro inesperado: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TransactionSummaryView(APIView):

    def get(self, request):
        try:
            summary = (
                Transaction.objects
                    # Utiliza 'iexact' para ignorar maiúsculas/minúsculas
                    .filter(type__iexact='outcome')
                    # Agrupa os resultados pela categoria da transação, acessando o título da categoria
                    .values('category__title')
                    # Realiza uma soma do valor ('value') das transações por categoria
                    .annotate(total_value=Sum('value'))
                    .order_by('-total_value')
            )

            # Cria um dicionário com o título da categoria como chave e o valor total como valor
            summary_data = {
                item['category__title']: float(item['total_value'] or 0)
                for item in summary
            }

            return Response(summary_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Detail": "Erro inesperado: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
