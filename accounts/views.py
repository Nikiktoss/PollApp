from django.shortcuts import render


def enter(request):
    return render(request, "accounts/enter_page.html")
