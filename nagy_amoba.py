def feltolt(szam):
    lista = []
    for i in range(szam):
        lista.append([])
        for _ in range(szam):
            lista[i].append(".")
    return lista

def kirajzol(lista):
  for sor in lista:
    for cella in sor:
        print(cella, end=' ')
    print()

def nyert(lista, jatekos, sor, osz):
    if nyert_sor(lista[sor], jatekos, osz):
      return True
    if nyert_osz(lista, jatekos, sor, osz):
      return True
    return False

def nyert_sor(sorlista, jatekos, osz):
  szamol = 1
  o = osz - 1
  while(sorlista[o] == jatekos["szimbolum"] and o >= 0):
    o -= 1
    szamol += 1
  o = osz + 1
  while(sorlista[o] == jatekos["szimbolum"] and o < len(sorlista)):
    o += 1
    szamol += 1
  if(szamol == 5):
    return True
  return False

def nyert_osz(lista, jat, sor, osz):
  szamol = 1
  s = sor - 1
  while(s >= 0 and lista[s][osz] == jat["szimbolum"]):
    s -= 1
    szamol += 1
  s = sor + 1
  while(s < len(lista) and lista[s][osz] == jat["szimbolum"]):
    s += 1
    szamol += 1
  if(szamol == 5):
    return True
  return False

def elfogyott(lista):
  for sor in lista:
    if '.' in sor:
      return False
  return True


# palya=[['.','.','.'],['.','.','.'],['.','.','.']]

palya = feltolt(10)
# print(palya)

print("Amőba (by:Szeszko egyetem)")
print("A megadott értékek, csak '0' és '2' között érvényesek sorban és oszlopban is")
player_x=input("Add meg az 1. játékos nevét: ")
player_o=input("Add meg a 2. játékos nevét: ")
kirajzol(palya)
print(player_x,", a szimbólumod a(z) 'x'",sep='')
print(player_o,", a szimbólumod a(z) 'o'",sep='')

jatekosok = [{'nev': player_x, "szimbolum": "x"}, {'nev': player_o, "szimbolum": "o"}]
vege=False
while not vege:
  for jatekos in jatekosok:
    print(jatekos["nev"], ", te következel!",sep='')
    beker_sor=int(input('sor: ')) - 1
    beker_oszlop=int(input('oszlop: ')) - 1
    while beker_sor < 0 or beker_sor > len(palya) - 1 or beker_oszlop < 0 or beker_oszlop > len(palya) - 1  or palya[beker_sor][beker_oszlop] != ".":
      print("ervenytelen koordinata")
      beker_sor=int(input('sor: ')) - 1         
      beker_oszlop=int(input('oszlop: ')) - 1
    palya[beker_sor][beker_oszlop]=jatekos["szimbolum"]
    kirajzol(palya)
    if nyert(palya, jatekos, beker_sor, beker_oszlop):
      gyoztes = jatekos
      vege = True
      break
    if elfogyott(palya):
      gyoztes = {}
      vege = True
      break
    # gyoztes = kiertekel(palya, jatekos) 
    # if gyoztes:            
    #     vege = True
    #     break
if gyoztes: 
  print(gyoztes["nev"], "nyertel") 
else:
  print("Elfogytak a mezők, döntetlen!")       

      