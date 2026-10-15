nota = float(input("introduce tu nota(0-10): "))
if nota < 0 or nota > 10:
    calificacion = "Nota no válida"
elif nota < 5:
    calificacion = "Suspenso"
elif nota < 6:
    print("Calificacion: Bien")
elif nota >= 7 and nota < 9:
    print("Calificacion: notable")
elif nota > 9:
    print("Calificacion: sobresaliente")
else:
    print("Calificacion: Insuficiente")
