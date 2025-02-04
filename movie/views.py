from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Movie

def movie_list(request):
    if request.method == "GET":  # Защита от других методов
        movies = list(Movie.objects.values())  # Получаем все фильмы
        return JsonResponse(movies, safe=False, json_dumps_params={"ensure_ascii": False})
    return JsonResponse({"error": "Method not allowed"}, status=405)

def movie_detail(request, movie_id):
    if request.method == "GET":  # Обрабатываем только GET
        movie = get_object_or_404(Movie, id=movie_id)
        return JsonResponse({
            "title": movie.title,
            "description": movie.description,
            "producer": movie.producer,
            "duration": movie.duration,
        }, json_dumps_params={"ensure_ascii": False})  # Чтобы не было проблем с кодировкой
    return JsonResponse({"error": "Method not allowed"}, status=405)
