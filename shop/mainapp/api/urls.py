from django.urls import path

from .api_views import CategoryAPIView, SmartphoneListAPIView, NotebookListAPIView, CustomersListAPIView



urlpatterns = [
    path('categories/<str:id>', CategoryAPIView.as_view(), name='categories_list'),
    path('customers/', CustomersListAPIView.as_view(), name='customers_list'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones'),
    path('smartphones/<str:id>', SmartphoneListAPIView.as_view(), name='smartphone_detail'),
    path('notebooks/', NotebookListAPIView.as_view(), name='notebooks'),

]