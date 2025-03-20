import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar sidos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo ordenque las preguntas

answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas

correct_answers_index = [1, 2, 0, 3, 1]

# El usuario deberá contestar 3 preguntas
puntos = 0
for _ in range(3):

    # Se selecciona una pregunta aleatoria
    question_index = random.sample(questions, 5)

    # Se muestra la pregunta y las respuestas posibles

    questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = int(input("Respuesta: ")) - 1
        # Verifico si la respuesta del usuario está dentro de las opciones
        if user_answer < 1 or user_answer > 5
            print("Respuesta no valida")
            sys.exit(1)
        else:
            for 
            # Se verifica si la respuesta es correcta
            if user_answer == correct_answers_index[question_index]:
                print("¡Correcto!")
                # Suma puntos por cada acierto
                puntos = puntos + 1
                break
            else:
                # Resta puntos por cada error
                puntos = puntos - 0.5
        else:
            # Si el usuario no responde correctamente después de 2 intentos,
            # se muestra la respuesta correcta
            print("Incorrecto. La respuesta correcta es:")
            print(answers[question_index] [correct_answers_index[question_index]])

#imprime la cantidad de puntos obtenida

print(f"Obtuvo {puntos} puntos")

    # Se imprime un blanco al final de la pregunta
    print()