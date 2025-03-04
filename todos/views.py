from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo

# Список TodoList
def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_list.html', {'todo_lists': todo_lists})


# Создание нового TodoList
def todo_list_add(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title:  # Проверка, что поле не пустое
            TodoList.objects.create(title=title, description=description)
    return redirect('todo_list')

# Главная страница
def home(request):
    return redirect('todo_list')

# Детальная информация о списке
def todo_list_detail(request, pk):
    todo_list = get_object_or_404(TodoList, id=pk)
    todos = todo_list.todos.all()  # Используем related_name="todos"
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})


# Удаление списка
def todo_list_delete(request, pk):  # Используем pk вместо id
    todo_list = get_object_or_404(TodoList, pk=pk)
    todo_list.delete()
    return redirect('todo_list')

# Редактирование списка
def todo_list_edit(request, pk):  # Используем pk вместо id
    todo_list = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        todo_list.title = request.POST.get('title', '').strip()
        todo_list.description = request.POST.get('description', '').strip()
        todo_list.save()
        return redirect('todo_list_detail', pk=pk)
    return render(request, 'todos/todo_list_edit.html', {'todo_list': todo_list})

# Удаление конкретного дела
def todo_delete(request, pk):  # Используем pk вместо id
    todo = get_object_or_404(Todo, pk=pk)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', pk=todo_list_id)

# Редактирование конкретного дела
def todo_edit(request, pk):  # Используем pk вместо id
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.title = request.POST.get('title', '').strip()
        todo.description = request.POST.get('description', '').strip()
        todo.due_date = request.POST.get('due_date', todo.due_date)  # Оставляет старое значение, если пустое
        todo.status = request.POST.get('status', 'off') == 'on'  # Фикс для чекбокса
        todo.save()
        return redirect('todo_list_detail', pk=todo.todo_list.id)
    return render(request, 'todos/todo_edit.html', {'todo': todo})
