from django.shortcuts import redirect, render
from .forms import ImgForm
from .models import Gallery

# Create your views here.
def home(request):
    form=ImgForm()
    gallerys=Gallery.objects.all()
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('home')
    return render(request,'index.html',{'form':form,'gal':gallerys})



