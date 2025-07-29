# anatomiapp/admin.py

from django.contrib import admin
from .models import PDFDocument

@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'pdf_file') # Added pdf_file for convenience
    search_fields = ('title',)
    # Removed Cloudinary-specific save_model method
