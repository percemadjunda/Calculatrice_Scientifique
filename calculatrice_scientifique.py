import math
import sympy as sp

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : division par zéro"

def sinus(angle):
    return math.sin(math.radians(angle))

def cosinus(angle):
    return math.cos(math.radians(angle))

def tangente(angle):
    return math.tan(math.radians(angle))

def racine_carree(nombre):
    return math.sqrt(nombre)

def puissance(base, exposant):
    return base ** exposant

def logarithme(nombre):
    return math.log10(nombre)

def logarithme_naturel(nombre):
    return math.log(nombre)

def exponentielle(nombre):
    return math.exp(nombre)

def valeur_absolue(nombre):
    return abs(nombre)

def arrondi(nombre, decimales):
    return round(nombre, decimales)

def factorielle(nombre):
    if nombre < 0:
        return "Erreur: impossible de calculer la factorielle d'un nombre négatif."
    elif nombre == 0:
        return 1
    else:
        return nombre * factorielle(nombre - 1)

def degres_vers_radians(degres):
    return math.radians(degres)

def radians_vers_degres(radians):
    return math.degrees(radians)

def radians_vers_dms(radians):
    degres = math.degrees(radians)
    degres_entiers = int(degres)
    minutes = (degres - degres_entiers) * 60
    minutes_entiers = int(minutes)
    secondes = (minutes - minutes_entiers) * 60
    return degres_entiers, minutes_entiers, secondes

def dms_vers_radians(degres, minutes, secondes):
    degres_decimaux = degres + (minutes / 60) + (secondes / 3600)
    return math.radians(degres_decimaux)

def logarithme_neperien(nombre):
    return math.log(nombre, math.e)

def celsius_vers_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_vers_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def calculer_integrale(expression, variable, limite_inf, limite_sup):
    x = sp.Symbol(variable)
    f = sp.sympify(expression)
    integrale = sp.integrate(f, (x, limite_inf, limite_sup))
    return integrale

def calculer_derivee(expression, variable):
    x = sp.Symbol(variable)
    f = sp.sympify(expression)
    derivee = sp.diff(f, x)
    return derivee

while True:
    print("=== calculatrice scientifique ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Sinus")
    print("6. Cosinus")
    print("7. Tangente")
    print("8. Racine carrée")
    print("9. Puissance")
    print("10. Logarithme (base 10)")
    print("11. Logarithme naturel")
    print("12. Exponentielle")
    print("13. Valeur absolue")
    print("14. Arrondi")
    print("15. Factorielle")
    print("16. Conversion degrés vers radians")
    print("17. Conversion radians vers degrés")
    print("18. Conversion radians vers degrés, minutes, secondes")
    print("19. Conversion degrés, minutes, secondes vers radians")
    print("20. Logarithme néperien")
    print("21. Conversion Celsius vers Fahrenheit")
    print("22. Conversion Fahrenheit vers Celsius")
    print("23. Calculer l'intégrale")
    print("24. Calculer la dérivée")
    print("0. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "0":
        print("Au revoir !")
        break

    try:
        if choix in ["1", "2", "3", "4"]:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le deuxième nombre : "))

        elif choix == "5":
            angle = float(input("Entrez l'angle en degrés : "))
            resultat = sinus(angle)
            print("Le sinus de", angle, "degrés est", resultat)

        elif choix == "6":
            angle = float(input("Entrez l'angle en degrés : "))
            resultat = cosinus(angle)
            print("Le cosinus de", angle, "degrés est", resultat)

        elif choix == "7":
            angle = float(input("Entrez l'angle en degrés : "))
            resultat = tangente(angle)
            print("La tangente de", angle, "degrés est", resultat)

        elif choix == "8":
            nombre = float(input("Entrez un nombre : "))
            resultat = racine_carree(nombre)
            print("La racine carrée de", nombre, "est", resultat)

        elif choix == "9":
            base = float(input("Entrez la base : "))
            exposant = float(input("Entrez l'exposant : "))
            resultat = puissance(base, exposant)
            print(base, "élevé à la puissance", exposant, "est", resultat)

        elif choix == "10":
            nombre = float(input("Entrez un nombre : "))
            resultat = logarithme(nombre)
            print("Le logarithme (base 10) de", nombre, "est", resultat)

        elif choix == "11":
            nombre = float(input("Entrez un nombre : "))
            resultat = logarithme_naturel(nombre)
            print("Le logarithme naturel de", nombre, "est", resultat)

        elif choix == "12":
            nombre = float(input("Entrez un nombre : "))
            resultat = exponentielle(nombre)
            print("L'exponentielle de", nombre, "est", resultat)

        elif choix == "13":
            nombre = float(input("Entrez un nombre : "))
            resultat = valeur_absolue(nombre)
            print("La valeur absolue de", nombre, "est", resultat)

        elif choix == "14":
            nombre = float(input("Entrez le nombre : "))
            decimales = int(input("Entrez le nombre de décimales : "))
            resultat = arrondi(nombre, decimales)
            print("L'arrondi de", nombre, "avec", decimales, "décimales est", resultat)

        elif choix == "15":
            nombre = int(input("Entrez un nombre entier : "))
            resultat = factorielle(nombre)
            print("La factorielle de", nombre, "est", resultat)

        elif choix == "16":
            degres = float(input("Entrez l'angle en degrés : "))
            resultat = degres_vers_radians(degres)
            print(degres, "degrés équivaut à", resultat, "radians")

        elif choix == "17":
            radians = float(input("Entrez l'angle en radians : "))
            resultat = radians_vers_degres(radians)
            print(radians, "radians équivaut à", resultat, "degrés")

        elif choix == "18":
            Nombre = float(input("Entrez un nombre : "))
            Resultat = calculer_carre(Nombre)
            print("Le carré de", Nombre, "est", Resultat)
    
    

        elif choix == "19":
            Degres = float(input("Entrez les degrés : "))
            Minutes = float(input("Entrez les minutes : "))
            Secondes = float(input("Entrez les secondes : "))
            Resultat = dms_vers_radians(Degres, Minutes, Secondes)
            print(Degres, "degrés", Minutes, "minutes", Secondes, "secondes équivaut à", Resultat, "radians")

        elif choix == "20":
             Nombre = float(input("Entrez un nombre : "))
             Resultat = logarithme_neperien(Nombre)
             print("Le logarithme népérien de", Nombre, "est", Resultat)
                 
        elif choix == "21":
            Celsius = float(input("Entrez la température en degrés Celsius : "))
            Resultat = celsius_vers_fahrenheit(Celsius)
            print(Celsius, "degrés Celsius équivaut à", Resultat, "degrés Fahrenheit")

        elif choix == "22":
             Fahrenheit = float(input("Entrez la température en degrés Fahrenheit : "))
             Resultat = fahrenheit_vers_celsius(Fahrenheit)
             print(Fahrenheit, "degrés Fahrenheit équivaut à", Resultat, "degrés Celsius")

        elif choix == "23":
            Expression = input("Entrez l'expression mathématique : ")
            Variable = input("Entrez la variable d'intégration : ")
            Limite_inf = float(input("Entrez la limite inférieure : "))
            Limite_sup = float(input("Entrez la limite supérieure : "))
            Resultat = calculer_integrale(Expression, Variable, Limite_inf, Limite_sup)
            print("L'intégrale de", Expression, "par rapport à", Variable, "de", Limite_inf, "à", Limite_sup, "est", Resultat)

        elif choix == "24":
             Expression = input("Entrez l'expression mathématique : ")
             Variable = input("Entrez la variable de dérivation : ")
             Resultat = calculer_derivee(Expression, Variable)
             print("La dérivée de", Expression, "par rapport à", Variable, "est", Resultat)
   

        else:
             print("Option invalide. Veuillez choisir une option valide.")
   
    except ValueError:
        print("Erreur : Entree invalide. veuillez entrer des valeurs numeriques appropriees")

    print("\n")
   
    
        
        
    

           