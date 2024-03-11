from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def pagina_inicial(request):
  return HttpResponse('Printo para investir')

def novo_investimento(request):
  return render(request, 'investimentos/novo_investimento.html')

def investimento_registrado(request):
  investimento = {
    'tipo_investimento': request.POST.get('TipoInvestimento')
  }
  return render(request, 'investimentos/investimento_registrado.html', investimento)