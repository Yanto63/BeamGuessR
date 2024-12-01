from json import loads

from django.http import JsonResponse
from .models import Guess

# def guess(request):
#     request_data = loads(request.body.decode('utf-8'))
#     guess = Guess.objects.get(id=request_data["guess_id"])
#     win = guess.x_coord == request_data["x"] and guess.y_coord == request_data["y"]
#     data = {
#         "win": win
#     }
#     return JsonResponse(data)