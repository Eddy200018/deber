frase=input("ingrese una frase:")
for indice in range(len(frase)):
    print(indice,"-",frase[indice])
    for car in frase:
        if car in("a","e","i","o","u","Z","X","Y","V","W","N","F"):
            if car in ("Z","X","Y","V","W","N","F"):
                continue
            else:
                cvoc=cvoc+1
print("cantidad de vocales{}",format(cvoc))
[car for car in["a","e","i","o","u"]if car not in( "Z","X","Y","V","W","N","F")]