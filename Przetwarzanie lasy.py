#program do tworzenia jednego pliku tekstowego na bazie innych plikow tekstowych w tym konkretnym przypadku z LMN
import os

print ('ustawiam sciezke dostepu do danych')
path = r'D:\BDL 2018\BDL 2018\BDL'
mass = r'D:\BDL 2018\BDL 2018\mass.txt'
#otwarcie pliku w trybie dodawania na koncu pliku
mass_plik = open(mass, "a")

#wyswietlanie zawartosci folderu - funcja do tego jest z biblioteki os
lista_plikow = os.listdir(path) #podgladam zawartosc

#petla po obiektach w katalotu
for obiekt in lista_plikow:
    path_x= path+'\\'+obiekt
    #petla po podkatalogach
    lista_plikow_wewnetrzna = os.listdir(path_x)
    for obiekt_zagniezdzony in lista_plikow_wewnetrzna:
        # warunek zeby wczytywac pliki o okreslonej nazwie konczacej sie na jakies slowo
        if obiekt_zagniezdzony.endswith('species.txt'):
            plik = open(path_x+'\\'+obiekt_zagniezdzony)

            #generator po liniach z pliku na okreslonych warunkach
            # zmienna = row[1]+row[2] for row in file if row[1]!="" and row[2]!="tekst"
            linie = [linia.split('\t')[0]+"\t"+linia.split('\t')[-2]+"\n" for linia in plik if (linia.split('\t')[-2]!="") and (linia.split('\t')[0]!="arodes_int_num") ]
            #zapis do pliku
            for i in range(len(linie)):

                        mass_plik.write(linie[i])
            plik.close()

mass_plik.close()

print ('zakonczono' )
#brakuje nag?owkow trzeba dodac pojedyncza linie na koniec petli przed zamknieciem ostaniego pliku lub podczas rozpoczecia
#trzeba jeszcze dorobic kawalek z arcgisa