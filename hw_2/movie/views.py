from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Movie


def movie_list(request):
    if request.method == "GET":
        movies = list(Movie.objects.values("id", "title", "description", "release_year"))
        return JsonResponse(movies, safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            movie = Movie.objects.create(
                title=data["title"],
                description=data["description"],
                release_year=data["release_year"],
            )
            return JsonResponse({"id": movie.id, "title": movie.title}, status=201)
        except (KeyError, json.JSONDecodeError):
            return HttpResponseBadRequest("Invalid data")

    return JsonResponse({"error": "Method not allowed"}, status=405)


def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        return JsonResponse({
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "release_year": movie.release_year
        })
    except Movie.DoesNotExist:
        return JsonResponse({"error": "Movie not found"}, status=404)

