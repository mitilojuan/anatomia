# anatomiapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), # Home page after login
    path('pdfs/', views.pdf_list_view, name='pdf_list'), # List of PDFs
    path('pdfs/<int:pk>/', views.pdf_detail_view, name='pdf_detail'), # View a specific PDF
    path('pdfs/serve/<int:pk>/', views.serve_pdf_file, name='serve_pdf_file'), # View to serve the actual PDF file
]
