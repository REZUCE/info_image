from django.shortcuts import render
from .forms import ImageForm
from PIL import Image


def image(request):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        image_ = form.cleaned_data['image']
        with Image.open(image_) as img:
            width, height = img.size
    else:
        form = ImageForm()
        width = None
        height = None
    context = {
        'form': form,
        'width': width,
        'height': height
    }
    template = 'image_recognition/image.html'
    return render(request, template, context)
