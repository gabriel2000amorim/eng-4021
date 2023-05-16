from django.shortcuts import render, redirect
from .models import Task

# Função para exibir a página inicial (home)
def home(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "home.html", context=context)

# Função para listar todas as tarefas
def list_tasks(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "list_tasks.html", context=context)

# Função para criar uma nova tarefa
def create_task(request):
    if request.method == "POST":
        if "done" not in request.POST:
            done = False
        else:
            done = True
        Task.objects.create(title=request.POST["title"],
                            description=request.POST["description"],
                            due_date=request.POST["due-date"],
                            done=done)
        return redirect("tasks-list")

    return render(request, "task_form.html")

# Função para atualizar uma tarefa existente
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.due_date = task.due_date.strftime('%Y-%m-%d')
    if request.method == "POST":
        task.title = request.POST["title"]
        task.description = request.POST["description"]
        task.due_date = request.POST["due-date"]
        if "done" not in request.POST:
            task.done = False
        else:
            task.done = True
        task.save()
        return redirect("tasks-list")

    return render(request, "task_form.html", context={"task": task})

# Função para excluir uma tarefa existente
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
      if "confirm" in request.POST:
        task.delete()

      return redirect("tasks-list")

    return render(request, "delete_form.html", context={"task": task})
