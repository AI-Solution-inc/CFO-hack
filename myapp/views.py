from django.shortcuts import render, redirect
from .forms import TextForm, PDFForm, InputForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404, JsonResponse
from .models import PDFModel
from .processing import process_doc_file


import datetime
import os

def add_text_and_pdf(request):
    if request.method == "POST" and request.FILES.get('file'):
        file = request.FILES['file']

        unix_timestamp = int(datetime.datetime.now().timestamp())
        filename, file_extension = os.path.splitext(file.name)
        filename = f"{unix_timestamp}_inputfile{file_extension}"
        file.name = filename
        pdf_model_instance = PDFModel.objects.create(pdf_file=file)

        file_location = pdf_model_instance.pdf_file.path
        process_doc_file(file_location)
        return redirect('complite')

    return render(request, 'text_box.html')

def pages (request):
    test_json ={'data':
                    {'key1':'asdas., dzxc'
                    ,'key2':'asf.,asmfфывфывфывфывыфвфывфывфывфывыфв.'
                    ,'key3':'lksdaflask'
                    ,'key4':'ывжэда'
                    ,'key5':'zxc,mas dfna,mфывпфриттьф ырпвфыодвлфывлф'},
                'Название': 'Аналитика'}
                
    page_key = test_json['Название']  # Get the first key from the test_json dictionary
    if page_key == 'Аналитика':
        return render(request, 'slides/page2.html', {'data':test_json['data'], 'Название':test_json['Название']})
    elif page_key == 'Другое':
        return render(request, 'slides/page3.html', {'data':test_json['data'], 'Название':test_json['Название']})
    else :
        return render(request, 'text_box.html')


def complite(request):
    return render(request, 'complite.html')


def main_page (request):
    return render(request, 'main_page.html')