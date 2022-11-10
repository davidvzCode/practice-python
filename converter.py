
def print_message(country ,value_dollar):
    pesos = input("How much "+ country +"pesos have you?:")
    pesos = float(pesos)
    value_dollar = value_dollar
    dolares =  pesos / value_dollar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    return("I have you $" + dolares + " dollars")

menu = """
Welcome to the conversore coins 💰

1 - Colombian pesos
2 - Argentines pesos
3 - Mexicans pesos

Chose a optional : """

opcion = int(input(menu))

if (opcion == 1):
    res = print_message("Colombian",3575)
elif (opcion == 2):
    res = print_message("Argentines",65)
elif (opcion == 3):
    res = print_message("Mexicans",24)
else:
    res = "Invalid opcion" + opcion
    
print(res);
