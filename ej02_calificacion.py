nota = float(input("introduce tu nota(0-10): "))
if nota >= 5 and nota < 7:
    print("Calificacion: Aprobado")
elif nota >= 7 and nota < 9:
    print("Calificacion: notable")
elif nota > 9:
    print("Calificacion: sobresaliente")
else:
    print("Calificacion: Suspenso")
