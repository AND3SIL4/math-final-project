# El usuario ingresa al sistema con 3 vidas
# 1. El sistema genera una funcion de manera aleatoria
# 2. El sistema grafica la funcion.
# 3. El sistema imprime el rango y el dominio
# 4. El sistema pregunta al usuario que tipo de funcion es?
# 3.1 Que tipo de funcion es?
# a) Cuadratica
# b) Exponencial
# c) Lineal
# 5. El sistema evalua la respuesta del usuario
# 6. Si la respuesta es INCORRECTA le resta una vida
# 7. Si es CORRECTA suma 10 puntos y avanza a la siguiente
# 8. El flujo se iterará en los pasos anteriores en un total de 5 veces
# 9. El juego finaliza si el usuario pierde todas las vidas o
# Lográ conservar al menos una vida cuando termine el juego
# 10. Al finalizar el sistema imprime el puntaje del jugador

# Import dependencies
import numpy as np
import matplotlib.pyplot as plt
import random
import os


def show_function(function, x_min, x_max, points=1000):
    """This method get a function and use matplotlib to show visually"""
    x = np.linspace(x_min, x_max, points)

    # Calculate values
    y = function(x)

    # Create a shapes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Graphic function
    ax.plot(x, y, 'b-', label='f(x)')

    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)

    # Add styles
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Gráfica de la función')
    ax.legend()

    # Show dasboard
    ax.grid(True, linestyle=':', alpha=0.7)

    # Show result
    plt.savefig("img.png")
    plt.close()
    plt.show()


"""This code contains all the differents function types"""

# Funciones cuadraticas


def cuadratica_1(x):
    return x**2


def cuadratica_2(x):
    return -x**2 + 2*x + 5

# Funciones lineales


def lineal_1(x):
    return 3*x


def lineal_2(x):
    return x+2

# Funciones logaritmicas


def logaritmica_1(x):
    return np.log(x)


def logaritmica_2(x):
    return np.log(3*x) + 2

# Funciones cubicas


def cubica_1(x):
    return x**3


def cubica_2(x):
    return 5*x**3 + 2*x + 10

# Racionales


def racional_1(x):
    return 1/(2*x)

# raíz


def raiz(x):
    return np.sqrt(x)


"""Method to get the correct answer"""


def menu(option: str) -> bool:
    # global lifes
    # global points
    options: list = [
        "cuadratica", "logaritmica", "cubica", "lineal", "raíz", "racional"
    ]

    options.remove(option)
    option_2 = random.choices(options)[0]
    options.remove(option_2)
    option_3 = random.choices(options)[0]
    options.remove(option_3)

    correct_options: list[str] = []
    # Append the 3 possible options
    correct_options.append(option)
    correct_options.append(option_2)
    correct_options.append(option_3)

    uno: str = random.choices(correct_options)[0]
    correct_options.remove(uno)
    dos: str = random.choices(correct_options)[0]
    correct_options.remove(dos)
    tres: str = random.choices(correct_options)[0]
    correct_options.remove(tres)

    print("¿Que tipo de función es?")
    print(f"""
    a) {uno}
    b) {dos}
    c) {tres}
    """)

    response: str = input("Escribe tu respuesta: ")
    if response.lower() == option.lower():
        return True
    else:
        return False


def calculate_score(response: bool, lifes: int, points: int) -> None:
    if response:
        points += 10
    else:
        lifes -= 1
    return lifes, points


def game():
    function: dict = {
        1: cuadratica_1,
        2: cuadratica_2,
        3: lineal_1,
        4: lineal_2,
        5: cubica_1,
        6: cubica_2,
        7: logaritmica_1,
        8: logaritmica_2,
        9: racional_1,
        10: raiz
    }

    # Local variables
    used_functions: list[int] = []
    counter = 0  # Loop iterator
    lifes = 3
    points = 0

    # Show function in graphic
    while counter < 5 and lifes > 0:
        os.system("clear")
        random_number = random.randint(1, 10)
        if random_number in used_functions:
            continue
        result = function.get(random_number)
        used_functions.append(random_number)  # Avoid duplicated functions

        show_function(result, -100, 100)  # Show the graphic

        # Show gamer score
        print(f"Vidas: {lifes}")
        print(f"Puntos: {points}")

        if random_number == 1 or random_number == 2:
            response = menu("cuadratica")
            lifes, points = calculate_score(response, lifes, points)
        elif random_number == 3 or random_number == 4:
            response = menu("lineal")
            lifes, points = calculate_score(response, lifes, points)
        elif random_number == 5 or random_number == 6:
            response = menu("cubica")
            lifes, points = calculate_score(response, lifes, points)
        elif random_number == 7 or random_number == 8:
            response = menu("logaritmica")
            lifes, points = calculate_score(response, lifes, points)
        elif random_number == 9:
            response = menu("racional")
            lifes, points = calculate_score(response, lifes, points)
        elif random_number == 10:
            response = menu("raíz")
            lifes, points = calculate_score(response, lifes, points)
        else:
            menu("No es")

        counter += 1
  
    print("El juego ha terminado :)")
    print(f"Tu puntaje final es: {points} has {"aprobado" if points >= 30 else "perdido"}")
game()
