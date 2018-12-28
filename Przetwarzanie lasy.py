#program tworzenie list plikow w folderach,
import os

#ustalam srodowisko (1. sciezka 2. srodowisko)
print ('ustawiam sciezke dostepu do danych')
path = r'D:\BDL 2018\BDL 2018\BDL'
mass = r'D:\BDL 2018\BDL 2018\mass.txt'
mass_plik = open(mass, "a")

#wyswietlanie zawartosci folderu - funcja do tego jest z biblioteki os
lista_plikow = os.listdir(path) #podgladam zawartosc

for obiekt in lista_plikow:
    path_x= path+'\\'+obiekt
    #print path_x
    lista_plikow_wewnetrzna = os.listdir(path_x)
    for obiekt_zagniezdzony in lista_plikow_wewnetrzna:
        # warunek zeby wczytywac pliki o okreslonej nazwie
        if obiekt_zagniezdzony.endswith('species.txt'):
            plik = open(path_x+'\\'+obiekt_zagniezdzony)

            linie = [linia.split('\t')[0]+" "+linia.split('\t')[-2]+"\n" for linia in plik]
            for i in range(len(linie)):
                        mass_plik.write(linie[i])


            plik.close()
            print(obiekt_zagniezdzony)

mass_plik.close()

print ('zakonczono' )
