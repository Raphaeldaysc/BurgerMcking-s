from django.shortcuts import render
from . import models

def home(request):
    cliente = models.Cliente.objects.all().first()
    
    return render(request, 'core/index.html', {'cliente': cliente})

def about(request):
    return render(request, 'core/sobre.html')

def jobs(request):
    staff = models.Crew.objects.all().first()
    return render(request, 'core/trabalhe-conosco.html', {"staff": staff}) # type: ignore

def franchises(request):
    franchises = models.Cliente.objects.all().last()
    
    return render(request, 'core/franquias.html', {"franchises": franchises}) # type: ignore

def investors(request):
    analista = models.Cliente.objects.all().last()
    return render(request, 'core/relacoes-investidores.html', {"analista": analista}) # type: ignore

def contact(request):
    return render(request, 'core/fale-conosco.html') # type: ignore

def satisfation(request):
    cliente = models.Cliente.objects.all().first()
    return render(request, 'core/pesquisa-satisfacao.html', {"cliente":cliente}) # type: ignore

def privacy_policy(request):
    return render(request, 'core/politica-privacidade.html') # type: ignore

def devolution(request):
    return render(request, 'core/politica-troca-devolucao.html') # type: ignore

def cookies_policy(request):
    return render(request, 'core/politica-cookies.html') # type: ignore

def coupons(request):
    return render(request, 'core/cupons.html') # type: ignore

def menu(request):
    hamburgers = models.Hamburgers.objects.all()
    fries = models.SideDishes.objects.all().all()
    sobremesas = models.SweetsTreats.objects.all()
    return render(request, 'core/cardapio.html', {"hmb": hamburgers, "fries": fries, "sobremesas":sobremesas}) # type: ignore

def app(request):
    return render(request, 'core/app-mckings.html') # type: ignore

def club(request):
    usuario = models.Cliente.objects.all().last()
    clube = models.Clube.objects.get(Cliente=usuario)
    return render(request, 'core/clube-mckings.html', {"usuario": usuario, "clube": clube}) # type: ignore

def delivery(request):
    return render(request, 'core/delivery.html') # type: ignore