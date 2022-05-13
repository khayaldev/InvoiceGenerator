from django.urls import path
from .views import (InvoiceListView,
                    InvoiceFormView, 
                    InvoiceRedirectView ,
                    InvoiceTemplateView,
                    InvoiceUpdateView, 
                    PositionFormView,
                    PositionDeleteView,
                    render_pdf_view)

app_name='invoices'

urlpatterns = [
    path('',InvoiceListView.as_view(),name="main"),
    path('new/',InvoiceFormView.as_view(),name="create"),
    path('invoice/<pk>/',InvoiceTemplateView.as_view(),name="invoice-template"),
    path('update/<pk>/',InvoiceUpdateView.as_view(),name="update"),
    path('details/<pk>/',PositionFormView.as_view(),name="details"),
    path('closed/<pk>/',InvoiceRedirectView.as_view(),name="closed"),
    path('delete/<pk>/<int:position_pk>',PositionDeleteView.as_view(),name="delete-pos"),
    path('pdf/<pk>/',render_pdf_view,name="export"),
]
