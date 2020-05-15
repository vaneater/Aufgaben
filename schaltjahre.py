# Hierzu muss ich sagen, dass ich Schwierigkeiten mit der 400 und 100 Jahr Problematik hatte,
# weshalb ich dazu im Internet etwas recherchiert habe

def schaltjahr(jahr):
    # Alle 4 Jahre ist ein Schaltjahr
    if (jahr%4 == 0):
        #Alle 100 Jahre kein Schaltjahr, aber ..
        if (jahr%100 == 0):
            # alle 400 Jahre ist ein Schaltjahr
            if (jahr%400 ==0):
                print("Dieses Jahr ist ein Schaltjahr. ")
            else:
                print("Dieses Jahr ist kein Schaltjahr. ")
        else:
            print("Dieses Jahr ist ein Schaltjahr. ")
    else:
        print("Dieses Jahr ist kein Schaltjahr. ")
