from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadExcelForm
from .models import CleanedFile
import pandas

def clean_excel_data(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_file = form.save()
            excel_file_path = cleaned_file.excel_file.path

            df = pandas.read_excel(excel_file_path)
            
            # cleaning duplicate records
            df.drop_duplicates(inplace=True)
            
            # cleaning records with na field(s)
            df.dropna(inplace=True)
            
            # saving cleaned data to new file
            cleaned_file_path = 'media/' + cleaned_file.excel_file.name

            df.to_excel(cleaned_file_path, index=False)
            
            cleaned_file.cleaned_file = cleaned_file_path
            cleaned_file.save()

            # return cleaned file to user
            with open(cleaned_file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename=cleaned_file.xlsx'
                return response
    else:
        form = UploadExcelForm()

    context = {'form': form}
    return render(request, 'clean_excel.html', context)
