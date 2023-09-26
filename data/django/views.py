from django.shortcuts import render

def djangodemo_UI(request):
    return render(request, 'hello_world.html', {})