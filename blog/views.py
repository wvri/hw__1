from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Article

def article_list(request):
    if request.method == "GET":  # Фильтруем только GET-запросы
        articles = list(Article.objects.values())  
        return JsonResponse(articles, safe=False, json_dumps_params={"ensure_ascii": False})
    return JsonResponse({"error": "Method not allowed"}, status=405)

def article_detail(request, article_id):
    if request.method == "GET":  # Обрабатываем только GET
        article = get_object_or_404(Article, id=article_id)
        return JsonResponse({
            "title": article.title,
            "text": article.text,
            "author": article.author,
        }, json_dumps_params={"ensure_ascii": False})
    return JsonResponse({"error": "Method not allowed"}, status=405)
