#program tworzenie list plikow w folderach,
import os

#ustalam srodowisko (1. sciezka 2. srodowisko)
print ('ustawiam sciezke dostepu do danych')
path = r'D:\BDL 2018\BDL 2018\BDL\BDL_01_01_AUGUSTOW_2018\f_storey_species.txt'
plik = open(path)
linie = [(linia.split('\t')[0]+" "+linia.split('\t')[-2]+"\n") for linia in plik if linia.split('\t')[-2]!=""]

mass = r'D:\BDL 2018\BDL 2018\mass.txt'
mass_plik = open(mass, "a")
for i in range(len(linie)):
    mass_plik.write(linie[i])

#for i in range(len(linie)):
#        print(linie[i][0], linie[i][-2])

plik.close()
mass_plik.close()

            #print(lines[0], lines[-2]) #to ma byc zapisane

print ('zakonczono' )
