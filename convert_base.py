chiffres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base_to_int(nombre,base):
    liste = []
    txt = reverse_str(str(nombre))
    for i in range(len(txt)):
        v = txt[i]
        index = chiffres.index(v)*base**i
        liste += [index]
        print(str(v)+" = "+str(chiffres.index(v))+"*"+str(base)+"^"+str(i)+" = "+str(index))
    print("+".join([str(x) for x in liste])+" = "+str(sum(liste)))
    print("donc le nombre "+str(nombre)+" de base "+str(base)+" = "+str(sum(liste))+" de base 10")
    return sum(liste)

def int_to_base2(nombre, base):
    if base < 2 or base > 36:
        raise ValueError("La base doit être comprise entre 2 et 36")
    
    if nombre == 0:
        return "0"

    resultat = ""
    
    signe = ""
    if nombre < 0:
        signe = "-"
        nombre = abs(nombre)

    while nombre > 0:
        reste = nombre % base
        resultat = chiffres[reste] + resultat
        nombre = nombre // base
    return signe + resultat

def int_to_base(nombre, base):
    if base < 2 or base > 36:
        raise ValueError("La base doit être comprise entre 2 et 36")
    
    if nombre == 0:
        return "0"
    
    resultat = ""
    
    signe = ""
    if nombre < 0:
        signe = "-"
        nombre = abs(nombre)
    nb2 = nombre
    while nombre > 0:
        reste = nombre % base
        resultat = chiffres[reste] + resultat
        print(str(nombre)+" = "+str(nombre//base)+"*"+str(base)+" + "+str(reste)+":"+str(int_to_base2(reste,base)))
        nombre = nombre // base
    result = str(signe + resultat)
    print("donc le nombre "+str(nb2)+" de base 10 = "+result+" de base "+str(base))
    return signe + resultat

def reverse_str(chaine):
    chaine_inverse = ""
    for caractere in chaine:
        chaine_inverse = caractere + chaine_inverse
    return chaine_inverse

def base_to_base(nb,base_from,base_to):
    print(str(nb)+" base "+str(base_from)+" en base "+str(base_to)+":")
    return itb(bti(nb,base_from),base_to)

itb = ITB = int_to_base
bti = BTI = base_to_int
btb = BTB = base_to_base
btb("1100110011",2,10)
