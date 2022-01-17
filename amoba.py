def kirajzol(lista):
  for sor in lista:
    for cella in sor:
        print(cella, end=' ')
    print()

def nyert(lista, jatekos):    
  for sor in lista:
    szamlalo = 0
    for cella in sor:
      if cella == jatekos["szimbolum"]:
        szamlalo += 1            
    if szamlalo == 3:
      return True
  for i in range(len(lista)):
    szamlalo = 0
    for j in range(len(lista)):
      if lista[j][i] == jatekos["szimbolum"]:
        szamlalo += 1
    if szamlalo == 3:
      return True
  szamlalo = 0    
  for i in range(len(lista)):    
    if lista[i][i] == jatekos["szimbolum"]:
      szamlalo += 1
  if szamlalo == 3:
    return True
  szamlalo = 0  
  for i in range(len(lista)):    
    if lista[i][-i-1] == jatekos["szimbolum"]:
      szamlalo += 1
  if szamlalo == 3:
    return True
  return False

def elfogyott(lista):
  for sor in lista:
    if '.' in sor:
      return False
  return True


palya=[['.','.','.'],['.','.','.'],['.','.','.']]

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
    while beker_sor < 0 or beker_sor > 2 or beker_oszlop < 0 or beker_oszlop > 2 or palya[beker_sor][beker_oszlop] != ".":
      print("ervenytelen koordinata")
      beker_sor=int(input('sor: ')) - 1         
      beker_oszlop=int(input('oszlop: ')) - 1
    palya[beker_sor][beker_oszlop]=jatekos["szimbolum"]
    kirajzol(palya)
    if nyert(palya, jatekos):
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

      