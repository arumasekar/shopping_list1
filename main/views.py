from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Wahyu Aji Aruma Sekar Puri',
        'class': 'PBP B',
        'app name': 'shopping_list-1'
    }

    return render(request, "main.html", context)