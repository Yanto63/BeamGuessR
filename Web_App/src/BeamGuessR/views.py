from django.shortcuts import render
from .models import Guess

def index(request):
    guess_picture = Guess.objects.order_by('?').first()
    with open("static/guess_image.png","wb") as guess_image:
        guess_image.write(guess_picture.picture)
    context = {
        "guess_id": guess_picture.id,
        "map": str(guess_picture.map),
        "x_coord": guess_picture.x_coord,
        "y_coord": guess_picture.y_coord,
    }
    return render(request, "BeamGuessR/index.html", context)
