import inquirer
from functools import lru_cache

@lru_cache
def question():
    questions = [
            inquirer.Checkbox('procesos',
            message="¿Que deseas hacer?",
            choices=['Verificar el estado de PostgreSQL', 'screenfetch', 'Verificar el estado de MongoDB'],
            ),
            ]
    answers = inquirer.prompt(questions)
    return answers