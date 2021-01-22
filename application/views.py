from django.shortcuts import render


def initial_page(request):
    """ Представление первоначальной страницы """
    return render(request, 'application/initial_page.html', {})
