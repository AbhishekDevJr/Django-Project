from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExpenseSerializer
from rest_framework import status
from .models import Expense
from .serializers import ExpenseSerializer
import uuid
import datetime

# Create your views here.

@api_view(['POST'])
def create_expense(request):
    try:
        if request.data:
            expense = request.data.copy()
            expense['expenseId'] = uuid.uuid4()
            expense['creationDate'] = datetime.datetime.now()
            serializedData = ExpenseSerializer(data = expense)
            
            if serializedData.is_valid():
                serializedData.save()
                return Response({
                    "title" : "Expense Created",
                    "message" : "Expense Record created in DataBase.",
                    "data" : serializedData.data
                }, status = status.HTTP_201_CREATED)
            else:
                return Response({
                    "title" : "Request Data is Invalid",
                    "message" : "Requested expense data Invalid."
                }, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "title" : "Bad Request",
                "message" : "Bad Request Payload."
            }, status = status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "title" : "Server Error",
            "message" : "Unhandled Server Error",
            "error" : str(e)
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['GET', 'POST'])
def get_expense(request):
    try:
        if request.data:
            pass
        else:
            expenses = Expense.objects.all()
            if expenses:
                return Response({
                    "title" : "Total Expenses",
                    "message" : "Total Expense on the Server.",
                    "data" : ExpenseSerializer(expenses, many = True).data
                }, status = status.HTTP_200_OK)
            else:
                return Response({
                    "title" : "No Expense Found",
                    "message" : "No Expense Found"
                }, status = status.HTTP_200_OK)
    except Exception as e:
        return Response({
             "title" : "Server Error",
            "message" : "Unhandled Server Error",
            "error" : str(e)
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
