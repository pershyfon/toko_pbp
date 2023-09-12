from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'main',
        'name': 'Sabrina Aviana Dewi',
        'class': 'PBP C',
        'item_name': 'Bubbly Eau de Toilette',
        'amount': '30',
        'price': '300000',
        'description': 'Experience the light, powdery, and clean scent of freshly laundered linens in a bottle.',
    }

    return render(request, "main.html", context)