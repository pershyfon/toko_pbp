from django.shortcuts import render

def show_main(request):
    context = {
        'app name': 'main',
        'name': 'Sabrina Aviana Dewi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)