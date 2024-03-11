from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def pagina_inicial(request):
  return HttpResponse('Printo para investir')

def contato(request):
  return HttpResponse('Para dúvidas, enviar um e-mail para contato@suporte.com')

def minha_historia(request):
  pessoa = {
    'nome': 'Jeff',
    'idade': 28,
    'hobby': 'Games'
  }
  return render(request, 'investimentos/minha_historia.html', pessoa)