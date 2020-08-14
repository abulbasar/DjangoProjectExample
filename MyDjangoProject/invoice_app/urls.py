from django.urls import path
from invoice_app import views

urlpatterns = [
    path("dashboard/", views.dashboard, name = "dashboard"),
    path("", views.dashboard, name = "dashboard2"),
    path("customers/", views.customers, name = "customers"),
    path("invoices/", views.invoices, name = "invoices"),
    path("invoice/<int:id>", views.invoice_details, name = "invoice_details"),
    path("invoice/<int:id>/edit", views.invoice_edit, name = "invoices_edit"),
    path("customer/<int:id>", views.customer_details, name = "customer_details"),
    path("customer/<int:id>/edit", views.customer_edit, name = "customer_edit")
]