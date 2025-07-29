# anatomiapp/models.py

from django.db import models
from django.urls import reverse # Required for get_absolute_url

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    # FileField will store files in MEDIA_ROOT/pdfs/
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the URL to the detail view of this PDF."""
        return reverse('pdf_detail', args=[str(self.pk)])

    class Meta:
        verbose_name = "PDF Document"
        verbose_name_plural = "PDF Documents"