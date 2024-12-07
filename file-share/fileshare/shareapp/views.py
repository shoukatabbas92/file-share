from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import File
from .forms import FileUploadForm

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.save()
            file_link = request.build_absolute_uri(f'/download/{file.uuid}/')
            return render(request,'shareapp/upload_success.html',{'file_link': file_link})
    else:
        form = FileUploadForm()
    return render(request,'shareapp/upload.html',{'form':form})


def download_file(request, uuid):
    file = get_object_or_404(File, uuid=uuid)
    response = HttpResponse(file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response

