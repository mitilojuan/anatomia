# anatomiaapp/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from .models import PDFDocument
import os
from django.views.decorators.clickjacking import xframe_options_exempt

@login_required
def home_view(request):
    return render(request, 'home.html') # <--- CHANGED (no 'anatomiaapp/')

@login_required
def pdf_list_view(request):
    pdfs = PDFDocument.objects.all().order_by('-uploaded_at')
    return render(request, 'pdf_list.html', {'pdfs': pdfs}) # <--- CHANGED (no 'anatomiaapp/')

@login_required
def pdf_detail_view(request, pk):
    pdf_doc = get_object_or_404(PDFDocument, pk=pk)
    return render(request, 'pdf_viewer.html', { # <--- CHANGED (no 'anatomiaapp/')
        'pdf_doc': pdf_doc,
    })

@login_required
@xframe_options_exempt
def serve_pdf_file(request, pk):
    pdf_doc = get_object_or_404(PDFDocument, pk=pk)

    if not os.path.exists(pdf_doc.pdf_file.path):
        raise Http404("PDF file not found locally.")

    try:
        pdf_file = open(pdf_doc.pdf_file.path, 'rb')
        response = FileResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(pdf_doc.pdf_file.name)}"'
        return response
    except Exception as e:
        raise Http404(f"Error serving PDF locally: {e}")