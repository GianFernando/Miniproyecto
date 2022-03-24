import datetime, random
from gzip import READ
from tracemalloc import start
from urllib import response


def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        # El año no es importante para nuestra simulación, 
        # siempre y cuando todos los cumpleaños tienen el mismo año.
        startOfYear = datetime.date(2001, 1, 1)

        # Obtenga un día aleatorio en el año:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # Todos los cumpleaños son únicos, así que devuelva Ninguno


    # Compare cada cumpleaños con cualquier otro cumpleaños:
    for a, birthdayA in enumerate (birthdays):
        for b, birthdayB in enumerate (birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # Devuelve el cumpleaños correspondiente.

# Configure una tupla de nombres de meses en orden:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # Sigue preguntando hasta que el usuario ingrese una cantidad válida.
    print('¿Cuántos cumpleaños debo generar? (Máx. 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # El usuario ha ingresado una cantidad válida
print()

# Generar y mostrar los cumpleaños:
print('Aquí están', numBDays, 'Cumpleaños:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Muestra una coma para cada cumpleaños después del primer cumpleaños.
        print(' , ' , end='') 
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# Determine si hay dos cumpleaños que coincidan.
match = getMatch(birthdays)

# Mostrar los resultados:
print('En esta simulacion, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('varias personas tienen un cumpleaños en', dateText)
else:
    print('no hay cumpleaños coincidentes.')
print()

# Ejecute 100,000 simulaciones:
print('Generating', numBDays, 'cumpleaños aleatorios 100.000 veces...')
input('Presiona Enter para comenzar...')

print('Hagamos otras 100.000 simulaciones.')
simMatch = 0 # Cuántas simulaciones tenían cumpleaños coincidentes en ellos.
for i in range(100_000):
    # Informe sobre el progreso cada 10.000 simulaciones:
    if i % 10_000 == 0:
        print(i, 'las simulaciones se ejecutan...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100.000 simulaciones ejecutadas.')

# Muestra los resultados de la simulación:
probabilidad = round(simMatch / 100_000 * 100, 2)
print('De 100.000 simulaciones de', numBDays, 'personas, que tiene')
print('cumpleaños coincidentes en ese grupo es de', simMatch, 'veces. Esto significa')
print('que', numBDays, 'de las personas tiene un', probabilidad, '% Probabilidades de')
print('tener un cumpleaños coincidente en su grupo.')
print('Eso es más probablemente de lo que piensas')
