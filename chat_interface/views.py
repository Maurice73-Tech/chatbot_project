from django.shortcuts import render

def chat_view(request):
    return render(request, 'chat_interface/chat_interface.html')




