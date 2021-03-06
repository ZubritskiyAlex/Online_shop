from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter
from .serializers import CategorySerializer, SmartphoneSerializer, NotebookSerializer
from ..models import Category, Smartphone, Notebook, Customer


class CategoryAPIView(ListAPIView, RetrieveUpdateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

class SmartphoneListAPIView(ListAPIView):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price','title']


class CustomersListAPIView(ListAPIView):

    serializer_class = None
    queryset = Customer.objecs.all()




class NotebookListAPIView(ListAPIView):

    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price','title']

class SmartphoneDetailAPIView(RetrieveAPIView):

    serializer_class =SmartphoneSerializer
    queryset = Smartphone.objects.all()
    lookup_field = 'id'




