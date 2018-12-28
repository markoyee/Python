#program tworzenie list plikow w folderach,
import os

#ustalam srodowisko (1. sciezka 2. srodowisko)
print ('ustawiam sciezke dostepu do danych')
path = r'D:\BDL 2018\BDL 2018\BDL\BDL_01_01_AUGUSTOW_2018'


#wyswietlanie zawartosci folderu - funcja do tego jest z biblioteki os
lista_plikow = os.listdir(path) #podgladam zawartosc
for obiekt_zagniezdzony in lista_plikow:
        # warunek zeby wczytywac pliki o okreslonej nazwie
        if obiekt_zagniezdzony.endswith('species.txt'):
            plik = open(path+'\\'+obiekt_zagniezdzony)

            linie = [linia.split('\t') for linia in plik]

            plik.close()

            #print(lines[0], lines[-2]) #to ma byc zapisane


print ('zakonczono' )
