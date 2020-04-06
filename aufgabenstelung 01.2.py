
def eingabe_pruefen(name, einzelpreis , gesamtpreis , menge):
    kriterien ={}
    
    try:
        ep1 = float(einzelpreis)
        kriterien.update({'einzelpreis':True})
    except:
        ep1 = einzelpreis
        kriterien.update({'einzelpreis':False})

    try:
        gp1 = float(gesamtpreis)
        kriterien.update({'gesamtpreis':True})
    except:
        gp1 = gesamtpreis
        kriterien.update({'gesamtpreis':False})

    #print(type(ep1))    
    #print(type(gp1))
    #print(type('a'))    

    if menge > 0:
        kriterien.update({'menge': True})
    else:
        kriterien.update({'menge':False})

    if name != '' and len(name) < 128:
         kriterien.update({'name': True})
    else:
        kriterien.update({'name':False})

    if kriterien['name'] and kriterien['einzelpreis'] and kriterien['gesamtpreis'] and kriterien['menge']:
        #print('asdf')
        if gp1/ menge == ep1:
            #print('ok')
            kriterien.update({'gesamtpreis': True})
            
        else:
            #print('not ok')
            kriterien.update({'gesamtpreis':False})
    
    #print(menge)
    #RED   = "\033[1;31m"  
    #print(kriterien)
    if  False in kriterien.values():
        print('ERROR!!! \nMindestens eine Eingabe erfüllt nicht die Kriterien! \n'
              ,kriterien,'\n\n')
    else:
        print('All good - Die Eingaben waren alle erfolgreich! :) \n')
        
max_goods = 10
counter = 0
while counter != max_goods:
            menge =''
            while type(menge) != type(0):
                try:
                    print('Geben Sie die Artikel-Menge ein!')
                    menge = int(input())
                except:
                    pass    
         
            print('Geben Sie den Artikel-Namen ein!')
            name = input()
            
            print('Geben Sie den Artikel-Einzelpreis ein!')
            einzel_preis = input()  
            
            print('Geben Sie den Gesamtpreis ein!')
            gesamtpreis =input()

            if ',' in einzel_preis:
                einzel_preis = einzel_preis.replace(',','.')

            if ',' in gesamtpreis:
                gesamtpreis = gesamtpreis.replace(',','.')

            #print(einzel_preis, gesamtpreis)
            eingabe_pruefen(name, einzel_preis, gesamtpreis, menge)

            
            counter +=1

