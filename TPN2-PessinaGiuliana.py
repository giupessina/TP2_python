# Trabajo Práctico Número 2 - Pessina Giuliana - Ingeniería del conocimiento

# 1. Crea un código que imprima en pantalla la expresión:
#    "Mi Primer Código En Python."
print("\n\n")
print("Mi Primer Código En Python")
print("\n")

# 2. Crea un código que le permita ingresar una respuesta al usuario haciéndole la siguiente pregunta:
#    "¿Qué estás estudiando?"
#    El código debe poder imprimir en pantalla lo ingresado por el usuario.
response = input("¿Qué estás estudiando? (responde a continuación): ")
print(response)
print("\n")

# 3. Crea un código que le permita ingresar una respuesta al usuario haciéndole la siguiente pregunta:
#    "¿En qué país vives?"
#    El código debe poder imprimir en pantalla lo ingresado por el usuario.
country = input("¿En qué país vives? (responde a continuación): ")
print(country)
print("\n")

# 4. Declara dos variables llamadas `nombre` y `edad`.
#    Asigna a `nombre` el valor "David Bowman" y a `edad` el valor 51.
nombre = "David Bowman"
edad = 51
print("nombre: "+nombre)
print("\n")
print("edad: "+str(edad))
print("\n")

# 5. Crea tres variables: `nombre`, `apellido`, `nombrecompleto`.
#    A `nombre` asígnale el valor "Julia" y en `apellido` el valor "Roberts".
#    Finalmente construye `nombrecompleto` concatenando las variables (recuerda sumar un espacio intermedio).
nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido
print("nombrecompleto: "+nombrecompleto)
print("\n")

# 6. Declara la variable `materia` y asígnale el valor "Ingeniería del conocimiento".
#    Muestra en pantalla la frase: "Estás estudiando 'materia'" (concatenando).
subject = "Ingeniería del conocimiento"
print("(hardcoded) Estás estudiando " + subject)
print("\n")

# 7. Convierte el valor de `num1` (num1=35) en un int e imprime el tipo de dato que resulta.
num1 = 35
num1 = int(num1)
print("the int type is: ")
print(type(num1))
print("\n")

# 8. Imprime el nombre y número de asociado dentro de la siguiente frase:
#    "Estimado/a (nombre_asociado) su número de asociado es: (numero_asociado)".
member_name = "John Doe"
member_number = 12345
print(f"Estimado/a {member_name}, su número de asociado es: {member_number}")
print("\n")

# 9. Muestra en pantalla el cociente (división al piso) de los siguientes dos números:
#    874 dividido entre 27. Debes mostrar solo el valor numérico que resulta de esta operación.
result = 874 // 27 # <- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
print(result)
print("\n")

# 10. Redondea el número 10.676767 al entero más próximo y muestra en pantalla el resultado.
rounded_number = round(10.676767)
print("rounded number is: "+str(rounded_number))
print("\n")

# 11. Gestión de inventario con tuplas:
#     Una tienda tiene un inventario de productos. Cada producto tiene un nombre, precio y cantidad disponible.
#     Representa cada producto como una tupla (nombre, precio, cantidad).
#     Escribe una función que reciba una lista de productos (tuplas) y devuelva el producto más caro.
productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

# with initial data, each prod is defined array in the form of touples, 
# meaning we can iter through and get the `max` of the second index

def getMaxPriceFrom(productos):
    newMax = 0
    for prod in productos:
        if(newMax<prod[1]): newMax = prod[1] 
    return newMax

print(f"Productos precio maximo: {getMaxPriceFrom(productos)}")
print("\n")


# 12. Registro de estudiantes con diccionarios:
#     Una escuela lleva un registro de estudiantes donde la clave es el número de matrícula y el valor es un diccionario con nombre, edad y calificaciones.
#     Escribe una función que reciba el registro de estudiantes y devuelva el promedio de calificaciones de un estudiante dado su número de matrícula.
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def getEstudianteAverageFor(estudiantes, enrollmentId):
    # Check if the enrollment ID exists in the dictionary
    if enrollmentId in estudiantes:
        calificaciones = estudiantes[enrollmentId]["calificaciones"]
        promedio = sum(calificaciones.values()) / len(calificaciones)
        return promedio
    else:
        return "Student not found"

enrollmentId = 102
print(f"Promedio del estudiante {enrollmentId} es {getEstudianteAverageFor(estudiantes, enrollmentId)}")
print("\n")


# 13. Análisis de datos meteorológicos con arrays:
#     Un meteorólogo registra las temperaturas diarias durante un mes. Escribe una función que reciba este array y devuelva la temperatura media, la máxima y la mínima.
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def processTemperatureData(temperatures):
    # Calculate the average, max, and min temperatures
    average = sum(temperatures) / len(temperatures)
    maximum = max(temperatures)
    minumum = min(temperatures)
    
    return average, maximum, minumum

# Call the function and unpack the results
average, maximum, minimum = processTemperatureData(temperaturas)
print(f"Temperatura media: {average}")
print(f"Temperatura máxima: {maximum}")
print(f"Temperatura mínima: {minimum}")
print("\n")

# 14. Manejo de parámetros variables con *args:
#     Escribe una función que reciba un número variable de notas de estudiantes y devuelva la nota promedio. Utiliza *args.
def calculateAverage(*grades):
    return sum(grades) / len(grades)

print(calculateAverage(85, 90, 78, 92)) 
print("\n")


# 15. Creación de un perfil de usuario con **kwargs:
#     Escribe una función que reciba datos de un usuario como nombre, edad, correo electrónico, y cualquier otro dato adicional usando **kwargs. 
#     La función debe devolver un diccionario con toda la información del usuario.
def createUserProfile(name, age, **kwargs):
    profile = {"name": name, "age": age}
    profile.update(kwargs)
    return profile

userProfile = createUserProfile("Luis", 25, email="luis@example.com", city="Mendoza")
print(userProfile)
print("\n")


# 16. Administración de empleados con tuplas y diccionarios:
#     Una empresa quiere administrar la información de sus empleados, donde cada empleado se representa como una tupla (nombre, edad, salario).
#     Escribe una función que reciba un diccionario donde la clave es el ID del empleado y el valor es la tupla con su información.
#     La función debe devolver un diccionario con los empleados que ganan más de un salario dado.

employees = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

def filterEmployeesBySalary(employees, minSalary):
    filteredEmployees = {
        id: info for id, 
        info in employees.items() if info[2] >= minSalary # <- returns the data of the employee based on salary threshold
    }
    return filteredEmployees

highEarners = filterEmployeesBySalary(employees, 3000)
print(highEarners)
print("\n")

# 17. Procesamiento de ventas con arrays:
#     Una tienda quiere procesar sus ventas diarias almacenadas en un array. 
#     Escribe una función que reciba el array de ventas diarias y devuelva el total de ventas y el promedio de ventas por día.
dailySales = [200, 450, 300, 400, 350, 500, 600]

def processSales(sales):
    totalSales = sum(sales)
    averageSales = totalSales / len(sales)
    return totalSales, averageSales

total, average = processSales(dailySales)
print(f"Total sales: {total}, Average sales per day: {average}")
print("\n")


# 18. Análisis de resultados deportivos con diccionarios:
#     Un club deportivo registra los resultados de sus partidos en un diccionario, donde la clave es el nombre del equipo rival y el valor es una tupla con los goles anotados y recibidos.
#     Escribe una función que calcule el total de goles anotados y recibidos en la temporada.
matchResults = {
    "Team A": (3, 2),
    "Team B": (1, 1),
    "Team C": (4, 0)
}

def calculateGoals(results):
    totalScored = sum([goals[0] for goals in results.values()])
    totalConceded = sum([goals[1] for goals in results.values()])
    return totalScored, totalConceded

scored, conceded = calculateGoals(matchResults)
print(f"Total goals scored: {scored}, Total goals conceded: {conceded}")
print("\n")


# 19. Configuración de una aplicación con **kwargs:
#     Escribe una función que reciba configuraciones opcionales para una aplicación (modo oscuro, idioma, notificaciones, etc.) usando **kwargs.
#     La función debe devolver un diccionario con las configuraciones aplicadas.
def configureApp(**kwargs): # <- kwargs automatically forms a dictionary
    return kwargs

appConfig = configureApp(darkMode=True, language="es", notifications=False)
print(appConfig)
print("\n")

# 20. Ordenamiento de datos con tuplas:
#     Escribe una función que reciba una lista de tuplas donde cada tupla contiene un nombre y una puntuación. 
#     La función debe devolver la lista ordenada por puntuación de mayor a menor.
scores = [("Ana", 85), ("Luis", 90), ("María", 78)]

def sortScores(scores):
    sortedList = []
    while scores:
        # find the tuple with the highest score
        highest = scores[0]
        for score in scores:
            if score[1] > highest[1]:
                highest = score
        # add the highest score to the sorted list and remove it from the original list
        sortedList.append(highest)
        scores.remove(highest)

    return sortedList

sortedScores = sortScores(scores)
print(sortedScores)
print("\n")


# 21. Planificación de viajes con tuplas y diccionarios:
#     Escribe una función que reciba una lista de estos paquetes y devuelva un diccionario con los destinos como claves 
#     y el precio total (precio por día * duración) como valor.
packages = [("Paris", 200, 5), ("Roma", 150, 4), ("London", 180, 3)]

def calculatePackageCost(packages):
    packageCosts = {destination: price * duration for destination, price, duration in packages}
    return packageCosts

packageCosts = calculatePackageCost(packages)
print(packageCosts)
print("\n")


# 22. Gestión de inventario con arrays:
#     Escribe una función que reciba el array de inventario y un número de productos vendidos (otro array) y devuelva el inventario actualizado.
inventory = [50, 30, 20, 10]
sales = [5, 10, 5, 2]

def updateInventory(inventory, sales):
    updatedInventory = [inventory[i] - sales[i] for i in range(len(inventory))]
    return updatedInventory

updatedInventory = updateInventory(inventory, sales)
print(updatedInventory)
print("\n")


# 23. Organización de eventos con *args:
#     Escribe una función que reciba un número variable de nombres de eventos y los imprima en un formato de lista numerada. Utiliza *args para recibir los nombres de los eventos.
def organizeEvents(*events):
    for idx, event in enumerate(events, 1):
        print(f"{idx}. {event}")

organizeEvents("Concert", "Art Exhibition", "Tattooing")
print("\n")
print("\n")


# 24. Análisis financiero con **kwargs:
#     Escribe una función que reciba diferentes tipos de ingresos y gastos como **kwargs y calcule el balance final. 
#     La función debe manejar ingresos como positivos y gastos como negativos.
def analyzeFinances(**kwargs):
    balance = sum(kwargs.values())
    return balance

balance = analyzeFinances(
    salary=2000, 
    rent=-800, 
    food=-300, 
    transport=-150, 
    freelance=500
)
print(balance)
print("\n")

# 25. Registro de empleados con tuplas y **kwargs:
#     Escribe una función que reciba el nombre, edad y salario de un empleado como parámetros obligatorios y otros datos como dirección, número de teléfono, etc. como **kwargs.
#     La función debe devolver un diccionario con toda la información del empleado.
def registerEmployee(name, age, salary, **kwargs):
    employee = {
        "name": name, 
        "age": age, 
        "salary": salary
    }
    employee.update(kwargs)
    return employee

employeeData = registerEmployee(
    "Ana", 
    30, 
    3000,
    address="111 Fake Address", 
    phone="123456789"
)
print(employeeData)
print("\n")

# 26. Estadísticas de ventas con arrays:
#     Escribe una función que reciba un array con las ventas de cada mes y devuelva un diccionario con el total de ventas, el promedio mensual y el mes con mayores ventas.
ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def salesStatistics(sales):
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    highest_sales = max(sales)
    month_highest_sales = sales.index(highest_sales) + 1  # Add 1 to get the month number (1-based index)
    
    return {
        "total": total_sales,
        "average": average_sales,
        "highest_month": month_highest_sales
    }

stats = salesStatistics(ventas_mensuales)
print(stats)
print("\n")

# 27. Organización de una biblioteca con diccionarios:
#     Escribe una función que reciba un diccionario de libros y devuelva una lista de todos los libros publicados después del año 2000.
biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def booksAfter2000(library):
    books = []
    for title, info in library.items():
        if info["año"] > 2000:
            books.append(title)
    return books

books = booksAfter2000(biblioteca)
print(books)
print("\n")

# 28. Registro de notas con tuplas y arrays:
#     Escribe una función que reciba una lista de tuplas donde cada tupla contiene el nombre de un estudiante y sus calificaciones en un array. 
#     La función debe devolver un diccionario con el nombre del estudiante como clave y su promedio de calificaciones como valor.
notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def studentGradesAverage(students):
    averages = {}
    for name, grades in students:
        averages[name] = sum(grades) / len(grades)
    return averages

averages = studentGradesAverage(notas_estudiantes)
print(averages)
print("\n")

# 29. Configuración de perfiles de usuario con **kwargs y arrays:
#     Escribe una función que reciba una lista de usuarios y sus preferencias de configuración como **kwargs.
#     La función debe devolver un diccionario donde la clave es el nombre del usuario y el valor es un array con las configuraciones aplicadas.
usuarios = ["Ana", "Luis", "María"]

def configureProfiles(users, **kwargs):
    profiles = {}
    for user in users:
        profiles[user] = list(kwargs.items())  # Convert to list of key-value pairs (array)
    return profiles

profiles = configureProfiles(usuarios, language="es", dark_mode=True, notifications=False)
print(profiles)
print("\n")

# 30. Gestión de una red social con **kwargs y arrays:
#     Escribe una función que administre publicaciones de una red social.
#     La función debe recibir el nombre del usuario, el texto de la publicación y un número variable de etiquetas usando **kwargs y arrays.
#     Además debe manejar opciones adicionales como visibilidad pública o privada. La función debe devolver un diccionario con todos los detalles de la publicación.
def publicar(usuario, texto, **kwargs):
    post = {"usuario": usuario, "texto": texto}
    post.update(kwargs)
    return post

post = publicar("UsuarioPrueba", "primer post", tags=["#hola", "#prueba"], visibility="public")
print(post)
print("\n")

# 32. Simulación de ventas con tuplas, arrays, y *args:
#     Una empresa quiere simular las ventas de diferentes productos.
#     Escribe una función que reciba un número variable de ventas (tuplas) donde cada tupla contiene el producto, la cantidad vendida, y el precio por unidad.
#     La función debe devolver el total de ingresos generados por las ventas.
def simular_ventas(*ventas):
    total = sum([cantidad * precio for producto, cantidad, precio in ventas])
    return total

ventas = simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))
print(ventas)
print("\n")

# 33. Sistema de reservas con tuplas y diccionarios:
#     Escribe una función que permita hacer una nueva reserva verificando primero si la habitación está disponible en la fecha seleccionada.
reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

def hacer_reserva(fecha, nombre, habitacion, precio):
    if fecha in reservas:
        for reserva in reservas[fecha]:
            if reserva[1] == habitacion:
                return "Habitación no disponible"
        reservas[fecha].append((nombre, habitacion, precio))
    else:
        reservas[fecha] = [(nombre, habitacion, precio)]
    return "Reserva exitosa"

print(hacer_reserva("2024-08-16", "Carlos", 102, 180))
print("\n")

# 34. Análisis de resultados de encuestas con diccionarios y arrays:
#     Escribe una función que calcule la frecuencia de cada respuesta para cada pregunta y devuelva un diccionario con estos resultados.
encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

def analizar_encuestas(encuestas):
    resultados = {}
    for pregunta, respuestas in encuestas.items():
        resultados[pregunta] = {respuesta: respuestas.count(respuesta) for respuesta in set(respuestas)}
    return resultados

print(analizar_encuestas(encuestas))
print("\n")

# 35. Optimización de rutas con arrays y tuplas:
#     Escribe una función que reciba una lista de rutas y un array con las distancias máximas permitidas para cada ruta.
rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

def optimizar_rutas(rutas, distancias_max):
    rutas_permitidas = [ruta for ruta, dist_max in zip(rutas, distancias_max) if ruta[2] <= dist_max]
    return rutas_permitidas

print(optimizar_rutas(rutas, distancias_max))
print("\n")

# 36. Gestión de inventarios en múltiples tiendas con diccionarios y **kwargs:
#     Escribe una función que gestione el inventario de una cadena de tiendas.
inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def gestionar_inventario(tienda, **kwargs):
    if tienda in inventario:
        for producto, cantidad in kwargs.items():
            if producto in inventario[tienda]:
                inventario[tienda][producto] += cantidad
            else:
                inventario[tienda][producto] = cantidad
    else:
        inventario[tienda] = kwargs
    return inventario[tienda]

print(gestionar_inventario("Tienda A", producto_1=10, producto_3=15))
print("\n")

# 37. Análisis de tendencias en redes sociales con arrays y tuplas:
#     Escribe una función que devuelva los hashtags que han sido mencionados más de una cierta cantidad de veces.
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def analizar_tendencias(hashtags, threshold):
    return [hashtag for hashtag, count in tendencias if count > threshold]

print(analizar_tendencias(hashtags, 100))
print("\n")

# 38. Administración de suscripciones con diccionarios, arrays, y **kwargs:
#     Escribe una función que gestione las suscripciones a un servicio en línea.
suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def gestionar_suscripciones(usuario, tipo, **kwargs):
    if usuario in suscripciones:
        suscripciones[usuario].append(tipo)
    else:
        suscripciones[usuario] = [tipo]
    return suscripciones[usuario]

print(gestionar_suscripciones("Luis", "mensual"))
print("\n")

# 39. Simulación de mercado bursátil con arrays y tuplas:
#     Escribe una función que simule el comportamiento de acciones en un mercado bursátil.
precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

def simular_mercado(precios, operaciones):
    total = 0
    for operacion, dia in operaciones:
        if operacion == "compra":
            total -= precios[dia]
        elif operacion == "venta":
            total += precios[dia]
    return total

print(simular_mercado(precios_diarios, operaciones))
print("\n")

# 40. Análisis de rendimiento académico con diccionarios y arrays:
#     Escribe una función que reciba este diccionario y devuelva un ranking de estudiantes basado en su promedio general.
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def ranking_estudiantes(estudiantes):
    promedios = {}
    for id, materias in estudiantes.items():
        total = sum([sum(notas) / len(notas) for notas in materias.values()]) / len(materias)
        promedios[id] = total
    return sorted(promedios.items(), key=lambda x: x[1], reverse=True)

print(ranking_estudiantes(estudiantes))
print("\n\nFIN\n\n")