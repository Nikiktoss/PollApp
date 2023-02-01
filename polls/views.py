from django.shortcuts import render


def main(request):
    return render(request, 'polls/main_page.html')
