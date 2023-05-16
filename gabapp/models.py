from django.db import models

# Definição do modelo de dados para uma tarefa
class Task(models.Model):
    # Campo de caractere para o título da tarefa
    title = models.CharField(max_length=50)
    # Campo de texto para a descrição da tarefa
    description = models.TextField()
    # Campo de data para a data de vencimento da tarefa
    due_date = models.DateField()
    # Campo booleano para indicar se a tarefa foi concluída ou não
    done = models.BooleanField()
