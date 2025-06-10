from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Teste
import json

# GET all and POST (create)
@csrf_exempt
def teste_list(request):
    if request.method == 'GET':
        test_list = list(Teste.objects.values())
        return JsonResponse(test_list, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        teste = Teste.objects.create(nom=data.get('nom', ''))
        return JsonResponse({'id': teste.id, 'nom': teste.nom})