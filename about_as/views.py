from django.shortcuts import render


def about_as_view(request):
    return render(request, 'about_as.html')
