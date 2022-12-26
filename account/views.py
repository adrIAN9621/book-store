from django.shortcuts import render

def make_ac(request):
    return render (request, 'account/account.html')