import mysql.connector
import random
from datetime import datetime
import time 
from tkinter import *
from tkinter.ttk import *
from random import seed
from random import randint
seed(1)
import datetime
from timeit import default_timer as timer
import threading
from datetime import date




#Συνδεση με το phpmyadmin
def connect():
    try:

        cnx=mysql.connector.connect(user="db19_up1053652" , password= "up1053652", host="150.140.186.217", database="project_up1053652")

        if cnx.is_connected () :
            print("Σύνδεση με βάση δεδομένων ... " )
    except mysql.connector.Error as e :
        print(e)
        return False
    return cnx



#Ποιο κουμπι πατηθηκε στο gui 
def clicked():
    
 
    button = selected.get()
    
    if button==0 :
        print("------------------------------------------------------------------")
        print("Δεν πάτησες κανένα κουμπί")
        print("------------------------------------------------------------------")
        window.destroy()
    
    
# Κωδικας για τις ερωτησεις 
    
    cnx=connect()


    
    if  cnx.is_connected():
        print("Επιτυχής σύνδεση στη βάση δεδομένων ζωολογικός κήπος")
        print("Σύνδεση με γραφική διεπαφή")
        print("------------------------------------------------------------------")
        curs=cnx.cursor()

#----------------------------------------------------------------------------- GUI_ΕΠΙΣΚΕΠΤΗ---------------------------------------------------------------------------------------------------------------------#
        
        if button==1 and idiothta=="1" :
              
              fetch_the_animals (cnx,curs)
      
        
        elif button==2  and idiothta=="1":
            date=input("Δώσε έτος:")
            find_the_visitors(cnx,curs,date)

            

        elif  button==3 and idiothta=="1" :
            
            find_programms(cnx,curs)
            

        elif  button==4 and idiothta=="1":
            
            animal=input("Δώσε το όνομα του ζώου που ψάχνεις : ")
            find_the_animal(cnx,curs,animal) 
            

        elif  button==5 and idiothta=="1" :
        
            return_the_categories(cnx,curs)
            
       
        elif  button==6 and idiothta=="1" :
            wrario_leiourgias(cnx,curs)
         
        
        elif  button==7 and idiothta=="1" :
            age=input("Δώσε έτος : " )
            epikoinwnia (cnx ,curs,age)
           
        
        elif button==8 and idiothta=="1" :
            general_info(cnx,curs)
           

        elif  button==9 and idiothta=="1" :
            find_biggest_smallest_age(cnx,curs,0)
       

        elif  button==10 and idiothta=="1" :
            find_biggest_smallest_age(cnx,curs,-1)

#----------------------------------------------------------------------------- GUI_ΔΙΑΧΕΙΡΙΣΤΗ_ΒΑΣΗΣ_ΔΕΔΟΜΕΝΩΝ---------------------------------------------------------------------------------------------------------------------#

        elif button==1 and idiothta=="2":
            print("Ιστορικό κτηνιάτρων")
            print(" ")
            kthniatroi(cnx,curs)

        elif button==2  and idiothta=="2":
            print("Ιστορικό υπαλλήλων")
            print(" ")
            upallhloi(cnx,curs)

        elif button==3  and idiothta=="2":
            ktin(cnx,curs)
            
        elif button==4  and idiothta=="2":
            trwei(cnx,curs)

        elif button==5 and idiothta=="2":
            biotopoi_zwa(cnx,curs)

        elif button==6 and idiothta=="2":
            arithmoszwon(cnx,curs)
        elif button==7 and idiothta=="2":
            nekro_zwo(cnx,curs)
        elif button==8 and idiothta=="2":
            vale_zwo(cnx,curs)
        elif button==9 and idiothta=="2":
            vale_programmata(cnx,curs)
        elif button==10 and idiothta=="2":
            neos_ergazomenos(cnx,curs)
        elif button==11 and idiothta=="2":
            update_programma(cnx,curs)
        elif button==12 and idiothta=="2":
            allagi_misthou(cnx,curs)
            
            

        

        print("------------------------------------------------------------------")

    else:print("Συνέβη σφάλμα κατά την σύνδεση")

#-------------------------------------------------------------------------ΣΥΝΑΡΤΗΣΕΙΣ----------------------------------------------------------------------------------------------------------------------------------------------------#

#Ιστορικο κτηνιατρων
def kthniatroi(cnx,curs):
    try:
        curs.execute('SELECT * FROM ΚΤΗΝΙΑΤΡΟΣ  ORDER BY `ΚΤΗΝΙΑΤΡΟΣ`.`ημερομηνια_ληξης_εργασιας` ASC;')
        print("ΚΤΗΝΙΑΤΡΟΙ:  \n")
        les=curs.fetchall()
        
        for i in les:
            print(i)


    except mysql.connector.Error as e :
          print(e)  



#Ιστορικο υπαλληλων
def upallhloi(cnx,curs):
    try:
       
        curs.execute('SELECT * FROM ΥΠΑΛΛΗΛΟΣ  ORDER BY `ΥΠΑΛΛΗΛΟΣ`.`ημερομηνια_ληξης_εργασιας` ASC;')
        print("ΥΠΑΛΛΗΛΟΙ: \n \n")
        les=curs.fetchall()
        for i in les:
            print(i)

    except mysql.connector.Error as e :
          print(e)  



#Τελευταια  ζωα που εχoυν εξετασει οι κτηνιατροι
def ktin(cnx,curs):
    try:
        curs.execute('SELECT k.αφμ,k.ονομα,k.επωνυμο,e.id_ζωου,z.ονομα,f.ονομα_φαρμακου,l.ημερομηνια_εξετασης FROM ΚΤΗΝΙΑΤΡΟΣ as k join ΕΞΕΤΑΖΕΙ as e on k.αφμ=e.αφμ_κτηνιατρου join ΕΞΕΤΑΣΗ as l on e.id_εξετασης=l.id_εξετασης JOIN ΦΑΡΜΑΚΕΥΤΙΚΗ_ΑΓΩΓΗ as f on f.id_εξετασης=e.id_εξετασης join ΖΩΟ as z on z.id_ζωου=e.id_ζωου\
                     WHERE ημερομηνια_ληξης_εργασιας="NULL" ORDER BY `l`.`ημερομηνια_εξετασης` DESC ;')
        les=curs.fetchall()
        for i in les:
            print(i)

    except mysql.connector.Error as e :
            print(e)


#Συναρτηση που βρισκει τι τρωει το καθε ζωο
def trwei(cnx,curs):
    name=input("Δώσε όνομα ζώου:")
   
    try:
        curs.execute('SELECT DISTINCT ka.ονομα FROM ΤΡΩΕΙ as t join ΖΩΟ as z on z.id_ζωου=t.id_ζωου JOIN ΤΡΟΦΗ as ka on ka.`ID τροφής`=t.id_τροφης WHERE z.ονομα=(%s)   ;', (name,))
                     
        les=curs.fetchall()
        for i in les:
            print(i[0])

    except mysql.connector.Error as e :
            print(e)




###ΒΙΟΤΟΠΟΙ ΣΕ ΚΑΘΕ ΤΜΗΜΑ ΚΑΙ ΖΩΑ ΣΕ ΚΑΘΕ ΤΜΗΜΑ
def biotopoi_zwa(cnx,curs):
    try:
        curs.execute('SELECT t.id_τμηματος,COUNT(b.id_βιοτοπου) FROM ΤΜΗΜΑ as t join ΒΙΟΤΟΠΟΣ as b on t.id_τμηματος=b.id_τμηματος GROUP BY t.id_τμηματος;')
        les=curs.fetchall()
        curs.execute('SELECT COUNT(z.id_τμηματος) FROM ΖΩΟ as z JOIN ΤΜΗΜΑ as t on z.id_τμηματος=t.id_τμηματος GROUP BY z.id_τμηματος;')
        kar=curs.fetchall()
        kar=[list(i) for i in kar]
        j=0
        print("BIOTΟΠΟΙ---ΖΩΑ ΣΕ ΚΑΘΕ ΤΜΗΜΑ")
        for i in les:
                print(i,kar[j])
                j=j+1
               

    except mysql.connector.Error as e :
            print(e)

### ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΝΕΚΡΟ ΖΩΟ 
def nekro_zwo(cnx,curs):
    on=input('ΔΩΣΕ ΟΝΟΜΑ ΖΩΟΥ ΠΟΥ ΠΕΘΑΝΕ:')
    curs.execute('SELECT id_ζωου,ημερομηνια_γεννησης FROM ΖΩΟ WHERE ονομα="{}" and ημερομηνια_θανατου="NULL";'\
                 .format(on))
    kar=curs.fetchall()
    for i in kar:
        print(i)
    id_zwou=input('ΔΩΣΕ ΤΟ ID ΤΟΥ ΖΩΟΥ ΠΟΥ ΠΕΘΑΝΕ:')
    try:
        curs.execute('UPDATE ΖΩΟ SET ημερομηνια_θανατου=CURRENT_DATE WHERE id_ζωου={};'\
                     .format(id_zwou))
        cnx.commit()
        
    except mysql.connector.Error as e :
              print(e)



#ΠΡΟΣΘΗΚΗ ΖΩΟΥ
def vale_zwo(cnx,curs):
    curs.execute('SELECT COUNT(*) FROM ΖΩΟ;')
    id_zwou=curs.fetchone()[0]+1
    onoma=input('ΔΩΣΕ ΟΝΟΜΑ ΖΩΟΥ:')
    curs.execute('SELECT DISTINCT ειδος FROM ΖΩΟ;')
    kar=curs.fetchall()
    for i in kar:
        print(i)
    eidos=input('ΔΩΣΕ ΕΙΔΟΣ ΖΩΟΥ:')
    hmerominia_gen=input('ΔΩΣΕ ΗΜΕΡΟΜΗΝΙΑ ΓΕΝΝΗΣΗΣ YYYY-MM-DD:')
    curs.execute('SELECT * from ΤΡΟΦΗ')
    les=curs.fetchall()
    for i in les:
        print(i)
    trofi=int(input('ΔΩΣΕ ID ΤΡΟΦΗΣ:'))
    onoma=str(onoma)
    onoma_neo='{}'\
           .format(onoma)
    onoma_neo=[onoma_neo]
    curs.execute('SELECT DISTINCT ονομα FROM ΖΩΟ WHERE ημερομηνια_θανατου="NULL";')
    les=curs.fetchall()
    lista=[list(i) for i in les]
    
       
    if onoma_neo in lista:
        curs.execute('SELECT DISTINCT id_τμηματος FROM ΖΩΟ WHERE ονομα="{}";'\
                     .format(onoma))
        id_tmim=curs.fetchone()[0]
        id_tmim=int(id_tmim)
        print('ΟΡΙΣΤΗΚΕ ID_ΤΜΗΜΑΤΟΣ:',id_tmim)
        curs.execute('SELECT DISTINCT id_βιοτοπου FROM ΖΩΟ WHERE ονομα="{}";'\
                     .format(onoma))
        id_biot=curs.fetchone()[0]
        id_biot=int(id_biot)
        print('ΟΡΙΣΤΗΚΕ ID_ΒΙΟΤΟΠΟΥ:',id_biot)
    
         
        try:
             
             curs.execute('INSERT INTO ΖΩΟ VALUES({},"{}","{}","NULL","{}",{},{});'\
                          .format(id_zwou,onoma,hmerominia_gen,eidos,id_biot,id_tmim))
             cnx.commit()
             curs.execute('INSERT INTO ΤΡΩΕΙ VALUES({},{});'\
                          .format(trofi,id_zwou))
             cnx.commit()
        except mysql.connector.Error as e :
              print(e)
        
    elif onoma_neo not in lista:
        curs.execute('SELECT COUNT(*) FROM ΒΙΟΤΟΠΟΣ;')
        id_biotopou=curs.fetchone()[0]+1
        
        curs.execute('SELECT id_τμηματος,ονομα FROM ΤΜΗΜΑ')
        an=curs.fetchall()
        for i in an:
            print(i)
        id_tmimat=input('ΔΙΑΛΕΞΕ ΤΟ ΣΩΣΤΟ ID ΤΜΗΜΑΤΟΣ:')
        perigr=input('ΔΩΣΕ ΠΕΡΙΓΡΑΦΗ ΒΙΟΤΟΠΟΥ ΠΟΥ ΖΕΙ:')
        try:
             curs.execute('INSERT INTO ΒΙΟΤΟΠΟΣ VALUES({},{},"{}");'\
                          .format(id_biotopou,id_tmimat,perigr))
             curs.execute('INSERT INTO ΖΩΟ VALUES({},"{}","{}","NULL","{}",{},{});'\
                          .format(id_zwou,onoma,hmerominia_gen,eidos,id_biotopou,id_tmimat))
             cnx.commit()
             curs.execute('INSERT INTO ΤΡΩΕΙ VALUES({},{});'\
                          .format(trofi,id_zwou))
             cnx.commit()
        except mysql.connector.Error as e :
              print(e)









#ΕΙΣΑΓΩΓΗ ΠΡΟΓΡΑΜΜΑΤΩΝ
def vale_programmata(cnx,curs):
    curs.execute('SELECT COUNT(*) FROM ΠΡΟΓΡΑΜΜΑ;')
    idprogr=curs.fetchone()[0]+1
    on_progr=input('ΔΩΣΕ ΟΝΟΜΑ ΠΡΟΓΡΑΜΜΑΤΟΣ:')
    timi=input('ΔΩΣΕ ΤΙΜΗ ΠΡΟΓΡΑΜΜΑΤΟΣ:')
    timi=int(timi)
    curs.execute('SELECT αφμ,ονομα,επωνυμο FROM ΥΠΑΛΛΗΛΟΣ WHERE ημερομηνια_ληξης_εργασιας="NULL";')
    les=curs.fetchall()
    print("ΔΙΑΘΕΣΙΜΑ αφμ ΥΠΑΛΛΗΛΩΝ")
    for i in les:
        print(i)    
    afm_ipal=input('ΔΩΣΕ ΑΦΜ ΥΠΑΛΛΗΛΟΥ ΠΟΥ ΘΑ ΤΡΕΧΕΙ ΤΟ ΠΡΟΓΡΑΜΜΑ:')
    afm_ipal=int(afm_ipal)
    hmer_liks=input('ΔΩΣΕ ΗΜΕΡΟΜΗΝΙΑ ΛΗΞΗΣ ΠΡΟΓΡΑΜΜΑΤΟΣ YEAR-MONTH-DAY:')
    today=date.today()
    try:
        curs.execute('INSERT INTO ΠΡΟΓΡΑΜΜΑ VALUES({},"{}",{});'\
                     .format(idprogr,on_progr,timi))
        cnx.commit()
        curs.execute('INSERT INTO ΤΡΕΧΕΙ VALUES({},"{}","{}",{});'\
                     .format(afm_ipal,today,hmer_liks,idprogr))
        cnx.commit()
    except mysql.connector.Error as e :         
         print(e)

         
#ΑΝΑΝΕΩΣΗ ΠΡΟΓΡΑΜΜΑΤΟΣ
def update_programma(cnx,curs):
    print('ΘΕΛΕΙΣ ΝΑ \n 1.ΤΕΡΜΑΤΙΣΕΙΣ ΚΑΠΟΙΟ ΠΡΟΓΡΑΜΜΑ \n 2.ΑΛΛΑΞΕΙΣ ΥΠΑΛΛΗΛΟ ΠΟΥ ΤΡΕΧΕΙ ΤΟ ΠΡΟΓΡΑΜΜΑ:')
    timi=input('ΔΙΑΛΕΞΕ 1 η 2: ')
    timi=int(timi)
    today=date.today()
    while timi!=1 or timi!=2:
        if timi==1:
            print("\n ΔΙΑΘΕΣΙΜΑ ΠΡΟΓΡΑΜΜΑΤΑ \n")
            curs.execute('SELECT t.id_προγραμματος,p.ονομα,t.αφμ_υπαλληλου,t.ημερομηνια_εναρξης FROM ΤΡΕΧΕΙ as t join ΠΡΟΓΡΑΜΜΑ as p on t.id_προγραμματος=p.id_προγραμματος WHERE t.ημερομηνια_ληξης>CURRENT_DATE ;')
            les=curs.fetchall()
            for i in les:
                print(i)
            id_progr=input("ΔΙΑΛΕΞΕ id προγραμματος (1η στηλη): ")
            id_progr=int(id_progr)
            afm_ipal=input("ΔΙΑΛΕΞΕ αφμ υπαλληλου(3η στηλη): ")
            afm_ipal=int(afm_ipal)
            try:
                curs.execute('UPDATE ΤΡΕΧΕΙ SET ημερομηνια_ληξης=CURRENT_DATE WHERE αφμ_υπαλληλου={} and id_προγραμματος={};'\
                             .format(afm_ipal,id_progr))
                cnx.commit()
            except mysql.connector.Error as e :
                print(e)
            break

        elif timi==2:
            print("\n ΔΙΑΘΕΣΙΜΑ ΠΡΟΓΡΑΜΜΑΤΑ \n")
            curs.execute('SELECT t.id_προγραμματος,p.ονομα,t.αφμ_υπαλληλου,t.ημερομηνια_εναρξης FROM ΤΡΕΧΕΙ as t join ΠΡΟΓΡΑΜΜΑ as p on t.id_προγραμματος=p.id_προγραμματος WHERE t.ημερομηνια_ληξης>CURRENT_DATE ;')
            les=curs.fetchall()
            for i in les:
                print(i)
            id_progr=input("ΔΙΑΛΕΞΕ id προγραμματος (1η στηλη): ")
            id_progr=int(id_progr)
            afm_ipal=input("ΔΙΑΛΕΞΕ αφμ υπαλληλου(3η στηλη): ")
            afm_ipal=int(afm_ipal)
            curs.execute('SELECT αφμ,ονομα,επωνυμο FROM ΥΠΑΛΛΗΛΟΣ WHERE ημερομηνια_ληξης_εργασιας="NULL";')
            les=curs.fetchall()
            print("ΔΙΑΘΕΣΙΜΑ αφμ ΥΠΑΛΛΗΛΩΝ \n")
            for i in les:
                print(i)    
            neo_afm=input("ΔΙΑΛΕΞΕ αφμ αλλου υπαλληλου:")
            neo_afm=int(neo_afm)
            try:
                curs.execute('UPDATE ΤΡΕΧΕΙ SET αφμ_υπαλληλου={},id_προγραμματος={} WHERE αφμ_υπαλληλου={} and id_προγραμματος={};'\
                             .format(neo_afm,id_progr,afm_ipal,id_progr))
                cnx.commit()
            except mysql.connector.Error as e :
                print(e)
            
            break


        else:
            timi=input('ΕΙΠΑΜΕ 1 η 2:')
            timi=int(timi)
            


# ΕΙΣΑΓΩΓΗ ΝΕΟΥ ΕΡΓΑΖΟΜΕΝΟΥ

def neos_ergazomenos(cnx,curs):
    print("ΘΕΛΕΙΣ ΝΑ ΒΑΛΕΙΣ \n 1.ΥΠΑΛΛΗΛΟΣ \n 2.ΚΤΗΝΙΑΤΡΟΣ \n")
    timi=input('ΔΙΑΛΕΞΕ 1 η 2: ')
    timi=int(timi)
    today=date.today()
    afm=int(input("ΔΩΣΕ ΑΦΜ:"))
    onoma=input("ΔΩΣΕ ΟΝΟΜΑ:")
    epitheto=input("ΔΩΣΕ ΕΠΙΘΕΤΟ:")
    dieuthinsi=input("ΔΩΣΕ ΔΙΕΥΘΥΝΣΗ:")
    kinito=int(input("ΔΩΣΕ ΚΙΝΗΤΟ:"))
    email=input("ΔΩΣΕ email:")
    misthos=int(input("ΑΡΧΙΚΟΣ ΜΙΣΘΟΣ:"))
               
    while timi!=1 or timi!=2:
        if timi==1:
            try:
                curs.execute('INSERT INTO ΥΠΑΛΛΗΛΟΣ VALUES({},"{}","{}","{}",{},"{}",CURRENT_DATE,"NULL",{});'\
                             .format(afm,onoma,epitheto,dieuthinsi,kinito,email,misthos))
                cnx.commit()
            except mysql.connector.Error as e :
                print(e)    
            break
        elif timi==2:
            try:
                curs.execute('INSERT INTO ΚΤΗΝΙΑΤΡΟΣ VALUES({},"{}","{}","{}",{},"{}",CURRENT_DATE,"NULL",{});'\
                             .format(afm,onoma,epitheto,dieuthinsi,kinito,email,misthos))
                cnx.commit()
            except mysql.connector.Error as e :
                print(e) 
            break
        else:
            timi=input('ΔΕΝ ΔΙΑΛΕΞΕΣ ΣΩΣΤΑ ΟΜΩΣ 1.ΥΠΑΛΛΗΛΟΣ Η 2.ΚΤΗΝΙΑΤΡΟΣ :')
            timi=int(timi)


    
def ergazomeno_eixame(cnx,curs):
    curs.execute('SELECT αφμ,ονομα,επωνυμο FROM ΥΠΑΛΛΗΛΟΣ WHERE ημερομηνια_ληξης_εργασιας="NULL";')
    les=curs.fetchall()
    print("ΔΙΑΘΕΣΙΜΟΙ ΥΠΑΛΛΗΛΟΙ")
    for i in les:
        print(i)
    curs.execute('SELECT αφμ,ονομα,επωνυμο FROM ΚΤΗΝΙΑΤΡΟΣ WHERE ημερομηνια_ληξης_εργασιας="NULL";')
    le=curs.fetchall()
    print("\nΔΙΑΘΕΣΙΜΟΙ ΚΤΗΝΙΑΤΡΟΙ")
    for i in le:
        print(i)     
    afm=int(input("\nΔΙΑΛΕΞΕ ΑΦΜ ΕΡΓΑΖΟΜΕΝΟΥ ΠΟΥ ΘΕΣ ΝΑ ΔΙΩΞΕΙΣ:"))
    try:
        curs.execute('UPDATE ΥΠΑΛΛΗΛΟΣ SET ημερομηνια_ληξης_εργασιας=CURRENT_DATE WHERE αφμ={};'\
                     .format(afm))
        cnx.commit()
        curs.execute('UPDATE ΚΤΗΝΙΑΤΡΟΣ SET ημερομηνια_ληξης_εργασιας=CURRENT_DATE WHERE αφμ={};'\
                     .format(afm))
        cnx.commit()
    except mysql.connector.Error as e :
        print(e)



# ΣΥΝΑΡΤΗΣΗ ΑΛΛΑΓΗΣ ΜΙΣΘΟΥ        
def allagi_misthou(cnx,curs):
    curs.execute('SELECT αφμ,ονομα,επωνυμο,μισθος FROM ΥΠΑΛΛΗΛΟΣ WHERE ημερομηνια_ληξης_εργασιας="NULL";')
    les=curs.fetchall()
    print("ΔΙΑΘΕΣΙΜΟΙ ΥΠΑΛΛΗΛΟΙ")
    for i in les:
        print(i)
    curs.execute('SELECT αφμ,ονομα,επωνυμο,μισθος FROM ΚΤΗΝΙΑΤΡΟΣ WHERE ημερομηνια_ληξης_εργασιας="NULL";')
    le=curs.fetchall()
    print("\nΔΙΑΘΕΣΙΜΟΙ ΚΤΗΝΙΑΤΡΟΙ")
    for i in le:
        print(i)     
    afm=int(input("\nΔΙΑΛΕΞΕ ΑΦΜ ΕΡΓΑΖΟΜΕΝΟΥ ΠΟΥ ΘΕΣ ΝΑ ΑΛΛΑΞΕΙΣ ΜΙΣΘΟ:"))
    neos_mis=int(input("ΔΩΣΕ ΝΕΟ ΜΙΣΘΟ:"))
    try:
        curs.execute('UPDATE ΥΠΑΛΛΗΛΟΣ SET μισθος={} WHERE αφμ={};'\
                     .format(neos_mis,afm))
        cnx.commit()

        curs.execute('UPDATE ΚΤΗΝΙΑΤΡΟΣ SET μισθος={} WHERE αφμ={};'\
                     .format(neos_mis,afm))
        cnx.commit()

    except mysql.connector.Error as e :
        print(e)









def arithmoszwon(cnx,curs):
    try:
        curs.execute('SELECT id_βιοτοπου,ονομα,COUNT(id_βιοτοπου) FROM ΖΩΟ GROUP BY id_βιοτοπου;')
        les=curs.fetchall()
        print("Ιd βιοτοπου--Όνομα ζώου--Πλήθος")
        print(" ")
        for i in les:
            print(i)

    except mysql.connector.Error as e :
            print(e)




#Επιστρεφει τα ζωα που εχουν πεθανει στον ζωολογικο κηπο.     
def dead_animals(cnx,curs):
        try :
            curs.execute('SELECT ημερομηνια_θανατου,ονομα,ειδος,id_βιοτοπου FROM ΖΩΟ WHERE ημερομηνια_θανατου  NOT IN("NULL")ORDER BY ημερομηνια_θανατου ;')
    
            rows = curs.fetchall()
            for i in rows:
                print(i)
 
                     
        except mysql.connector.Error as e :
            print(e)

        

 
#Επιστρεφει ολα τα ζωντανα ζωα στον ζωολογικο κηπο
def fetch_the_animals (cnx,curs):
    try :
            curs.execute('SELECT COUNT(*) FROM ΖΩΟ WHERE ημερομηνια_θανατου="NULL" ;')
    
            rows = curs.fetchall()
            data=rows[0]
 
            
            print("Στον ζωολογικό κήπο υπάρχουν", data[0],"ζώα")
                       
    except mysql.connector.Error as e :
            print(e)




#Επιστρεφει τον αριθμο ανθρωπων που επισκεφθηκαν τον ζωολογικο κηπο μια συγκεκριμενη χρονια
def find_the_visitors(cnx,curs,date):
      try :
            or_date=date
            date= date+"%"
            curs.execute('SELECT COUNT(*) FROM ΕΠΙΣΚΕΠΤΗΣ WHERE ημερομηνια_επισκεψης LIKE (%s)  ;',(date,))
            rows = curs.fetchall()
            data=rows[0]
 
            
            print("Το ",or_date," επισκέφτηκαν τον ζωολογικό κήπο ", data[0],"άτομα")
                       
      except mysql.connector.Error as e :
            print(e)



#Επιστρεφει ολα τα δυνατα προγραμματα του ζωολογικου κηπου   
def find_programms(cnx,curs):
     try :
           
            curs.execute('SELECT ονομα,τιμη FROM ΠΡΟΓΡΑΜΜΑ WHERE TRUE  ;')
            rows = curs.fetchall()
            for row in rows :
                print(row[0]," Tιμή:" ,row[1]," ευρω ")
            
          
                       
     except mysql.connector.Error as e :
            print(e)




#Επιστρεφει την τοποθεσια του ζωου που επιλεχθηκε απο τον χρηστη στον ζωολογικο κηπο
def find_the_animal(cnx,curs,name ):
      try :
           
            
            curs.execute('SELECT id_τμηματος,id_βιοτοπου FROM ΖΩΟ  WHERE ονομα= (%s) AND ημερομηνια_θανατου="NULL";', (name,))
            print()
            print("ΤΜΗΜΑ,ΒΙΟΤΟΠΟΣ,ΠΕΡΙΓΡΑΦΗ")
            print("------------------------")
            rows = curs.fetchall()
            counter=0
            for row in rows :
                if(row[0]==1):
                    print(row[0],row[1],"ΠΡΟΣΤΑΤΕΥΟΜΕΝΟΣ ΧΩΡΟΣ")
                    counter=counter+1
                elif(row[0]==2):
                    print(row[0],row[1],"ΚΕΛΙ")
                    counter=counter+1
                elif(row[0]==3):
                    print(row[0],row[1],"ΛΙΜΝΗ-ΕΝΥΔΡΙΟ")
                    counter=counter+1
                elif(row[0]==4):
                    print(row[0],row[1],"ΚΛΟΥΒΙ")
                    counter=counter+1
            print("Βρεθηκαν ",counter," αποτελεσματα" )
                
                    
                       
      except mysql.connector.Error as e :
            print(e)


#Επιστρεφει τα ειδη των ζωων που υπαρχουν στον ζωολογικο κηπο 
def return_the_categories(cnx,curs):
     try :
           
            
            curs.execute('SELECT DISTINCT ειδος , ονομα FROM ΖΩΟ   ;')
            rows = curs.fetchall()
            for row in rows:
                print("Eίδος:",row[0],"  Zώο:",row[1])
            
                       
     except mysql.connector.Error as e :
            print(e)




#Επιστρεφει τα ωραρια λειτουργιας των τμηματων του ζωολογικου κηπου
def wrario_leiourgias(cnx,curs):
      try :
           
            
            curs.execute('SELECT ονομα,id_τμηματος,ωραριο_λειτουργιας FROM ΤΜΗΜΑ   ;')
            rows = curs.fetchall()
            print("ωραρίο λειτουργίας (κάθε μέρα εκτός κυριακής) ")
            print()
            for row in rows:
                print(row[0],row[2])
            
                       
      except mysql.connector.Error as e :
            print(e)



#Επιστρεφει τους υπευθυνους των προγραμματων σε ενα συγκεκριμενο ετος
def epikoinwnia (cnx ,curs,date ) :
    try :
           
            datee= date+ "%"
            curs.execute('SELECT ΥΠΑΛΛΗΛΟΣ.ονομα,ΥΠΑΛΛΗΛΟΣ.επωνυμο,ΥΠΑΛΛΗΛΟΣ.κινητο,ΠΡΟΓΡΑΜΜΑ.ονομα FROM ΥΠΑΛΛΗΛΟΣ JOIN ΤΡΕΧΕΙ JOIN ΠΡΟΓΡΑΜΜΑ WHERE ΥΠΑΛΛΗΛΟΣ.αφμ=ΤΡΕΧΕΙ.αφμ_υπαλληλου AND ΠΡΟΓΡΑΜΜΑ.id_προγραμματος=ΤΡΕΧΕΙ.id_προγραμματος\
                         AND ΤΡΕΧΕΙ.ημερομηνια_εναρξης LIKE (%s) ORDER BY ΠΡΟΓΡΑΜΜΑ.ονομα  ;',(datee,))   
            rows = curs.fetchall()
            for row in rows :
                print("Υπεύθυνος: ",row[0]," ",row[1]," Tηλέφωνο: ",row[2],"Πρόγραμμα: ",row[3])
           
            
                       
    except mysql.connector.Error as e :
            print(e)

#Γενικες πληροφοριες του ζωολογικου κηπου
def general_info(cnx,curs):
      try :
            curs.execute('SELECT COUNT(*) FROM ΖΩΟ WHERE ημερομηνια_θανατου="NULL" ;')
            rows = curs.fetchall()
            zwa=rows[0]
    
            curs.execute('SELECT COUNT(*) FROM ΥΠΑΛΛΗΛΟΣ WHERE ημερομηνια_ληξης_εργασιας ="NULL" ;')
            rows = curs.fetchall()
            upallhloi=rows[0]
            curs.execute('SELECT COUNT(*) FROM ΚΤΗΝΙΑΤΡΟΣ WHERE ημερομηνια_ληξης_εργασιας ="NULL" ;')
            rows = curs.fetchall()
            kthniatroi=rows[0]
            curs.execute('SELECT COUNT(*) FROM ΒΙΟΤΟΠΟΣ  ;')
            rows = curs.fetchall()
            biotopoi=rows[0]

            print("Γενικές πληροφορίες για τον ζωολογικό κήπο")
            print("Το Ζωολογικό Πάρκο, ένα αυτοχρηματοδοτούμενο δημιούργημα που ιδρύθηκε το 2010, εκτείνεται σε μια συνολική έκταση 200 στρεμμάτων, φιλοξενώντας περισσότερα από ",zwa[0]," ζώα.")
            print("Η λειτουργία του ξεκίνησε τον Ιανουάριο του 2010, αρχικά ως Ορνιθολογικό Πάρκο με την πέμπτη μεγαλύτερη συλλογή πουλιών στην Ελλαδα , ζώα της φάρμας για τους μικρότερους επισκέπτες, και 3 πολύ εντυπωσιακούς μεγάλους χώρους – μικρογραφίες των 3 ηπείρων - στους οποίους οι επισκέπτες μπορούν να περπατήσουν και να θαυμάσουν την αντίστοιχη ορνιθολογική πανίδα και χλωρίδα")
            print("Από τον απρίλιο του 2010, όταν στο ζωολογικό κήπο  προστέθηκε Ο Κόσμος των Eρπετών, ξεκίνησαν οι συνεχείς επεκτάσεις και προσθήκες που περιλάμβαναν το έκθεμα Αφρικανική Πανίδα, με ζώα της Αφρικής  που δεν συναντάμε συχνά.Επίσης το 2010, άνοιξε το Τμήμα των Μαϊμούδων. Το 2010 ενα μηνα μετα την ιδρυση , ολοκληρώθηκε το τμήμα των αιλουροειδών και η επέκταση της Αφρικάνικής Σαβάνας.Ακόμα, άνοιξε το Δάσος των Πιθήκων, όπου οι επισκέπτες μπορούν να βρίσκονται στον ίδιο χώρο με τους πιθηκους. ")
            print("O αριθμός των υπαλλήλων που απασχολούνται στον ζωολογικό κήπο το 2019-2020  είναι ", upallhloi[0] )
            print("O αριθμός των κτηνιάτρων που απασχολούνται στον ζωολογικό κήπο το 2019-2020 είναι ", kthniatroi[0] )
            print("Στον ζωολογικό κήπο υπάρχουν ",biotopoi[0],"βιότοποι και 4 τμήματα που διαχειρίζουν τους βιότοπους")
                 
      except mysql.connector.Error as e :
            print(e)

    
#Επιστρεφει το μεγαλυτερο και το μικροτερο  σε ηλικια ζωο (με 0 βρισκω το max με -1 το min λογω λιστας)
def find_biggest_smallest_age(cnx,curs,num):
     try :
            curs.execute('SELECT ημερομηνια_γεννησης,ονομα FROM ΖΩΟ JOIN ΒΙΟΤΟΠΟΣ WHERE ΖΩΟ.id_βιοτοπου=ΒΙΟΤΟΠΟΣ.id_βιοτοπου AND ΖΩΟ.ημερομηνια_θανατου="NULL" ORDER BY ημερομηνια_γεννησης  ;')
            rows = curs.fetchall()
            age=rows[num]
            curs.execute('SELECT id_βιοτοπου FROM ΖΩΟ  WHERE  ημερομηνια_γεννησης=(%s);', (age[0],))
            rows = curs.fetchall()
            id_bio=rows[0]
            animal_age_in_years=find_age(age[0],2019)
            print(age[0],age[1],"Id_βιοτοπου:",id_bio[0]," Years:",animal_age_in_years)
            
     except mysql.connector.Error as e :
            print(e)



#Επιστρεφει την ηλικια των ζωων σε χρονια (πχ ΑΛΟΓΟ 26 χρονων )
def find_age(string,today_year):
    L=string.split('-')
    return today_year-int(L[0])
    
    
    
#Συναρτηση για το exit
def endProgam():
   
    window.destroy()
   

#Επιστρεφει τυχαια ημερομηνια
def randomDate(start, end):
    
   
    frmt = '%d-%m-%Y %H:%M'

    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))

    ptime = stime + random.random() * (etime - stime)
    dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
    return dt

#Περιστροφη της ημερομηνιας ετσι ωστε να συμβαδιζει με τα προτυπα συναρτησεων χρονου της SQL (πχ 2011-11-22)
def rotate_string(str):
    new_string=""
    my_rotate_list=[]
    my_rotate_list= str.split('/')
    paula="-"
    new_string=my_rotate_list[2]+paula + my_rotate_list[0]+paula +my_rotate_list[1]
    return new_string 


#Συναρτηση που γεμιζει με τυχαιες τιμες τον πινακα ΕΠΙΣΚΕΠΤΗΣ
def episkepths(cnx,curs):
    i=0
    programmata =  [ 1,2,3,4,5,6,7,8,9,10,11,12 ]



    counter= int(input("Δώσε τον αριθμό των επισκεπτών που θες να προσθέσω:"))
    while True :
        if i== counter : break
        random_program = programmata[random.randint(0,len(programmata)-1)]
        L= randomDate("20-01-2010 13:30", "23-12-2019 04:50").strftime("%m/%d/%Y, %H:%M:%S").split(',')
        random_date= rotate_string(L[0])
       
        try :
            curs.execute('INSERT INTO ΕΠΙΣΚΕΠΤΗΣ VALUES ({},"{}",{});'\
                         .format(random_program,random_date,i))
            i=i+1
            cnx.commit()
        except mysql.connector.Error as e :
            print(e)


def delete_data_from_episkepths (cnx , curs ) :
       try :
            curs.execute('DELETE FROM ΕΠΙΣΚΕΠΤΗΣ WHERE TRUE')
                         
            cnx.commit()
       except mysql.connector.Error as e :
            print(e)
    

#Συναρτηση που γεμιζει με συγκεκριμενες τιμες τον πινακα ΠΡΟΓΡΑΜΜΑ
def programma (cnx,curs):

    id_programmatos= [1,2,3,4,5,6,7,8,9,10,11,12]
    onoma_programmatos=["ΠΡΟΓΡΑΜΜΑ ΓΙΑ ΑΝΗΛΙΚΑ ΠΑΙΔΙΑ","ΚΑΝΟΝΙΚΟ ΠΡΟΓΡΑΜΜΑ","ΣΧΟΛΙΚΑ ΠΡΟΓΡΑΜΜΑΤΑ","ΠΡΟΓΡΑΜΜΑ ΓΙΑ ΕΦΗΒΟΥΣ","ΔΡΑΣΤΗΡΙΟΤΗΤΕΣ ΜΕ ΤΗΝ ΟΙΚΟΓΕΝΕΙΑ","ΕΙΔΙΚΑ ΔΙΑΜΟΡΦΩΜΕΝΟ ΠΡΟΓΡΑΜΜΑ ΓΙΑ ΑΜΕΑ",
                        "ONLINE ΠΡΟΓΡΑΜΜΑΤΑ","ZOO CAMPS","ΠΑΝΕΠΙΣΤΗΜΙΑΚΑ ΠΡΟΓΡΑΜΜΑΤΑ","ΕΜΠΕΙΡΙΑ ΣΑΦΑΡΙ","ΚΑΤΑΔΥΣΗ ΜΕ ΚΕΛΙ","ΤΑΙΣΜΑ ΠΤΗΝΩΝ"]
    timh=[0,10,7,8,9,3,5,15,12,10,20,3]
    for j in range(len(timh)):
        try:
             curs.execute('INSERT INTO ΠΡΟΓΡΑΜΜΑ VALUES ({},"{}",{});'\
                         .format(id_programmatos[j],onoma_programmatos[j],timh[j]))

             cnx.commit()
        except mysql.connector.Error as e :
            print(e)

#Συναρτηση που διαγραφει τιμες απο τον πινακα ΠΡΟΓΡΑΜΜΑ
def delete_data_from_programma (cnx , curs ) :
       try :
            curs.execute('DELETE FROM ΠΡΟΓΡΑΜΜΑ WHERE TRUE')
                         
            cnx.commit()
       except mysql.connector.Error as e :
            print(e)

#Ελεγχος αν η λιστα ειναι αδεια
def empty_list (L) :
    M=[]
    return M

#Συναρτηση που γεμιζει τον ΠΙΝΑΚΑ ΖΩΑ
def final_zwa(cnx,curs):
              zwa=["ΠΑΝΘΗΡΑΣ","ΠΙΘΗΚΟΣ","ΥΔΡΟΧΕΙΡΟΣ","ΧΙΜΠΑΤΖΗΣ","ΚΟΑΤΙ","ΚΡΙ-ΚΡΙ","ΛΑΜΑ","ΛΕΜΟΥΡΙΟΣ","ΙΠΠΟΠΟΤΑΜΟΣ","ΣΕΡΒΑΛ","ΠΛΑΤΩΝΙ","ΣΙΤΑΤΟΥΝΓΚΑ","ΣΑΙΜΙΡΙ","ΡΙΝΟΚΕΡΟΣ","ΟΡΥΞ","ΜΑΡΑ","ΜΑΚΑΚΟΣ","ΟΥΑΛΑΜΠΙ","ΑΓΡΙΟΓΟΥΡΟΥΝΟ",
                   "ΑΝΤΙΛΟΠΗ","ΕΛΕΦΑΝΤΑΣ","ΤΑΜΑΡΙΝΟΣ","ΚΑΜΗΛΑ","ΓΙΒΒΩΝΑΣ","ΜΥΡΜΗΓΚΟΦΑΓΟΣ","ΖΕΒΡΑ","ΚΑΜΗΛΟΠΑΡΔΑΛΗ","ΑΡΚΟΥΔΑ","ΑΛΟΓΟ","ΤΣΙΤΑΧ","ΠΟΥΜΑ","ΛΙΟΝΤΑΡΙ","ΤΙΓΡΗΣ",
                   "ΑΛΙΓΑΤΟΡΑΣ","ΠΥΘΩΝΑΣ","ΒΟΑΣ","ΔΡΑΚΟΣ","ΓΚΕΚΟ","ΑΝΑΚΟΝΤΑ","ΚΡΟΚΟΔΕΙΛΟΣ","ΙΓΚΟΥΑΝΑ","ΛΟΦΙΟΦΟΡΟΣ","ΣΑΜΙΑΜΙΔΙ","ΦΡΥΝΟΣ","ΧΑΜΑΙΛΕΟΝΤΑΣ","ΤΕΡΑΣΓΚΙΛΑ","ΠΟΝΤΙΚΟΦΙΔΟ",
                   "ΔΕΛΦΙΝΙ","ΦΩΚΙΑ","ΚΑΡΧΑΡΙΑΣ","ΙΠΠΟΚΑΜΠΟΣ","ΚΑΡΕΤΑ-ΚΑΡΕΤΑ","ΦΑΛΑΙΝΑ","ΦΥΣΗΤΗΡΑΣ","ΦΩΚΑΙΝΑ","ΖΙΦΙΟΣ","ΘΑΛΛΑΣΙΟ-ΛΙΟΝΤΑΡΙ","ΜΑΝΑΤΟΣ","ΘΑΛΑΣΣΙΑ-ΑΓΕΛΑΔΑ","ΘΑΛΑΣΣΙΟΣ-ΙΠΠΟΣ",
                   "ΑΓΑΠΟΡΝΙΣ","ΑΕΤΟΣ","ΑΗΔΟΝΙ","ΧΗΝΑ","ΑΜΑΖΟΝΑ","ΒΟΥΚΕΡΟΣ","ΦΑΣΙΑΝΟΣ","ΙΒΙΣ","ΓΥΠΑΣ","ΦΡΟΥΤΟΦΑΣΑ","ΤΟΥΡΑΚΟ","ΚΥΚΝΟΣ","ΚΑΛΑΟ","ΚΑΖΟΥΑΡΙΟΣ","ΚΕΑ","ΜΠΟΥΛΜΠΟΥΛ","ΛΟΡΙ","ΤΟΥΚΑΝΟΣ","ΚΟΡΑΚΙ","ΚΡΑΧΤΗΣ","ΤΡΥΓΟΝΙ",
                   "ΚΙΣΣΑ","ΥΦΑΝΤΗΣ","ΜΕΛΙΤΟΦΑΓΟΣ","ΜΠΟΥΦΟΣ","ΜΠΟΥΜΠΟΥΚ","ΝΑΝΟΧΗΝΑ","ΟΡΝΙΟ","ΠΕΛΑΡΓΟΣ","ΠΙΓΚΟΥΙΝΟΣ","ΜΑΚΑΟ","ΣΤΡΟΥΘΟΚΑΜΗΛΟΣ","ΦΛΑΜΙΝΓΚΟ" 
                  ]
              
              id_zwou=0
              i=1
              counter=-1
              department=1
              eidos="ΘΗΛΑΣΤΙΚΟ"
              for k in range(0,len(zwa)):
                    counter=counter+1
                    random_date_die=[]
                    tazwamou=zwa[counter]
                    print(tazwamou)
                    if(k==33):
                        department=2
                        eidos="ΕΡΠΕΤΟ"
                    if(k==47):
                        department=3
                        eidos="ΘΑΛΑΣΣΙΟ ΘΗΛΑΣΤΙΚΟ"
                    if(k==60):
                        department=4
                        eidos="ΠΤΗΝΟ"
                    
                    
                    
                    for j in range (0,random.randint(2,8)):
                            
                            L= randomDate("20-01-1990 13:30", "23-12-2015 04:50").strftime("%m/%d/%Y, %H:%M:%S").split(',')
                            birth= rotate_string(L[0])
                            D= randomDate("20-01-2010 13:30", "23-12-2019 04:50").strftime("%m/%d/%Y, %H:%M:%S").split(',')
                            random_date_die.append(rotate_string(D[0]))
                            random_date_die.append("NULL")
                            random_date_die.append("NULL")
                            random_date_die.append("NULL")
                            random_date_die.append("NULL")
                            random_date_die.append("NULL")
                            die=random_date_die[random.randint(0,len(random_date_die)-1)]
                            try :
                           
                            
                                curs.execute('INSERT INTO ΖΩΟ VALUES ({},"{}","{}","{}","{}","{}",{});'\
                                 .format(i,tazwamou,birth,die,eidos,k,department))
                                
                                cnx.commit()
                                i=i+1
     
            
                            except mysql.connector.Error as e :
                                       print(e)
    

def delete_zwa (cnx,curs):
       try :
            curs.execute('DELETE FROM ΖΩΟ WHERE TRUE')
                         
            cnx.commit()
       except mysql.connector.Error as e :
            print(e)

      

#Συναρτηση δημιουργιας του πινακα ΕΞΕΤΑΣΗ
def exetash ( cnx,curs ) :
     for i in range (1,150):
         L= randomDate("01-01-2010 13:30", "23-12-2019 04:50").strftime("%m/%d/%Y, %H:%M:%S").split(',')
         hmeromhnia_eksetashs= rotate_string(L[0])
         try :
                curs.execute('INSERT INTO ΕΞΕΤΑΣΗ VALUES ({},"{}");'\
                             .format(i,hmeromhnia_eksetashs))
                    
                cnx.commit()
            
         except mysql.connector.Error as e :
                print(e)
    

#Διαγραφη στοιχειων του πινακα EΞΕΤΑΣΗ
def delete_exetash (cnx,curs):
    try :
            curs.execute('DELETE FROM ΕΞΕΤΑΣΗ WHERE TRUE')
                         
            cnx.commit()
    except mysql.connector.Error as e :
            print(e)

    
    


#Επιστρεφει το μεγιστο αριθμο id_ζωου για καθε ειδος
def max_id_thilastika(cnx,curs,eidos_zwou):
    try :
            curs.execute('SELECT COUNT(*) FROM ΖΩΟ WHERE  ειδος=(%s) ;', (eidos_zwou,))
    
            rows = curs.fetchall()
            number=rows[0]
            print(int(number[0]))
            return int(number[0])
                             
    except mysql.connector.Error as e :
            print(e)



#Συναρτηση δημιουργιας του πινακα ΤΡΩΕΙ
def trwei_update(cnx,curs):
    number_of_thilastika=max_id_thilastika(cnx,curs,"ΘΗΛΑΣΤΙΚΟ")
    number_of_erpeta=max_id_thilastika(cnx,curs,"ΕΡΠΕΤΟ")
    number_of_thzwa=max_id_thilastika(cnx,curs,"ΘΑΛΑΣΣΙΟ ΘΗΛΑΣΤΙΚΟ")
    number_of_pthna=max_id_thilastika(cnx,curs,"ΠΤΗΝΟ")


    
    idtrofh_gia_agria_zwa=[1,2,3,4,5,6,7,8,9,11,12,14,15]
    
    idtrofh_gia_pthna=[4,13,15,18]
    idtrofh_gia_thalassia_thilastika=[4,15]
    idtrofh_gia_erpeta=[8,10,13,14,16,19]

    len1=number_of_thilastika+1 # μηκος θηλαστικων id
    for i in range(1,len1):
        random_food=idtrofh_gia_agria_zwa[random.randint(0,len(idtrofh_gia_agria_zwa)-1)]
        
        try :
                curs.execute('INSERT INTO ΤΡΩΕΙ VALUES ({},{});'\
                             .format(random_food,i))
                    
                cnx.commit()
            
        except mysql.connector.Error as e :
                print(e)

    
    len2=len1+1+number_of_erpeta
    for i in range(len1,len2):
        random_food=idtrofh_gia_erpeta[random.randint(0,len(idtrofh_gia_erpeta)-1)]
        try :
                curs.execute('INSERT INTO ΤΡΩΕΙ VALUES ({},{});'\
                             .format(random_food,i))
                    
                cnx.commit()
            
        except mysql.connector.Error as e :
                print(e)

    len3=len2+1+number_of_thzwa
    for i in range(len2,len3):
        random_food=idtrofh_gia_thalassia_thilastika[random.randint(0,len(idtrofh_gia_thalassia_thilastika)-1)]
        try :
                curs.execute('INSERT INTO ΤΡΩΕΙ VALUES ({},{});'\
                             .format(random_food,i))
                    
                cnx.commit()
            
        except mysql.connector.Error as e :
                print(e)
    len4=len3+1+number_of_pthna
    for i in range(len3,len4):
        random_food=idtrofh_gia_pthna[random.randint(0,len(idtrofh_gia_pthna)-1)]
        try :
                curs.execute('INSERT INTO ΤΡΩΕΙ VALUES ({},{});'\
                             .format(random_food,i))
                    
                cnx.commit()
            
        except mysql.connector.Error as e :
                print(e)
    
        
#Διαγραφη στοιχειων του πινακα ΤΡΩΕΙ
def delete_trwei (cnx,curs):
    try :
            curs.execute('DELETE FROM ΤΡΩΕΙ WHERE TRUE')
                         
            cnx.commit()
    except mysql.connector.Error as e :
            print(e)




#Συναρτηση δημιουργιας του πινακα ΒΙΟΤΟΠΟΣ
def create_biotopos(cnx,curs):
              thilastika=["ΣΟΥΡΙΚΑΤΑ","ΠΙΘΗΚΟΣ","ΥΔΡΟΧΕΙΡΟΣ","ΧΙΜΠΑΤΖΗΣ","ΚΟΑΤΙ","ΚΡΙ-ΚΡΙ","ΛΑΜΑ","ΛΕΜΟΥΡΙΟΣ",
                "ΙΠΠΟΠΟΤΑΜΟΣ","ΣΕΡΒΑΛ","ΠΛΑΤΩΝΙ","ΣΙΤΑΤΟΥΝΓΚΑ","ΣΑΙΜΙΡΙ","ΡΙΝΟΚΕΡΟΣ","ΟΡΥΞ","ΜΑΡΑ","ΜΑΚΑΚΟΣ","ΟΥΑΛΑΜΠΙ","ΑΓΡΙΟΓΟΥΡΟΥΝΟ",
                "ΑΝΤΙΛΟΠΗ","ΕΛΕΦΑΝΤΑΣ","ΤΑΜΑΡΙΝΟΣ","ΚΑΜΗΛΑ","ΓΙΒΒΩΝΑΣ","ΜΥΡΜΗΓΚΟΦΑΓΟΣ","ΖΕΒΡΑ","ΚΑΜΗΛΟΠΑΡΔΑΛΗ","ΑΡΚΟΥΔΑ","ΑΛΟΓΟ","ΤΣΙΤΑΧ","ΠΟΥΜΑ","ΛΙΟΝΤΑΡΙ","ΤΙΓΡΗΣ",]
    
              erpeta=["ΑΛΙΓΑΤΟΡΑΣ","ΠΥΘΩΝΑΣ","ΒΟΑΣ","ΔΡΑΚΟΣ","ΓΚΕΚΟ","ΑΝΑΚΟΝΤΑ","ΚΡΟΚΟΔΕΙΛΟΣ","ΙΓΚΟΥΑΝΑ","ΛΟΦΙΟΦΟΡΟΣ","ΣΑΜΙΑΜΙΔΙ","ΦΡΥΝΟΣ","ΧΑΜΑΙΛΕΟΝΤΑΣ","ΤΕΡΑΣΓΚΙΛΑ","ΠΟΝΤΙΚΟΦΙΔΟ"]

              thalassia_thilastika=["ΔΕΛΦΙΝΙ","ΦΩΚΙΑ,ΚΑΡΧΑΡΙΑΣ","ΙΠΠΟΚΑΜΠΟΣ","ΚΑΡΕΤΑ-ΚΑΡΕΤΑ","ΦΑΛΑΙΝΑ","ΦΥΣΗΤΗΡΑΣ","ΦΩΚΑΙΝΑ","ΖΙΦΙΟΣ","ΘΑΛΛΑΣΙΟ-ΛΙΟΝΤΑΡΙ","ΜΑΝΑΤΟΣ","ΘΑΛΑΣΣΙΑ-ΑΓΕΛΑΔΑ","ΘΑΛΑΣΣΙΟΣ-ΙΠΠΟΣ"]
              pthna=["ΑΓΑΠΟΡΝΙΣ","ΑΕΤΟΣ","ΑΗΔΟΝΙ","ΧΗΝΑ","ΑΜΑΖΟΝΑ","ΒΟΥΚΕΡΟΣ","ΦΑΣΙΑΝΟΣ","ΙΒΙΣ","ΓΥΠΑΣ","ΦΡΟΥΤΟΦΑΣΑ","ΤΟΥΡΑΚΟ","ΚΥΚΝΟΣ","ΚΑΛΑΟ","ΚΑΖΟΥΑΡΙΟΣ","ΚΕΑ","ΜΠΟΥΛΜΠΟΥΛ","ΛΟΡΙ"
                        ,"ΤΟΥΚΑΝΟΣ","ΚΟΡΑΚΙ","ΚΡΑΧΤΗΣ","ΤΡΥΓΟΝΙ","ΚΙΣΣΑ","ΥΦΑΝΤΗΣ","ΜΕΛΙΤΟΦΑΓΟΣ","ΜΠΟΥΦΟΣ","ΜΠΟΥΜΠΟΥΚ","ΝΑΝΟΧΗΝΑ","ΟΡΝΙΟ","ΠΕΛΑΡΓΟΣ","ΠΙΓΚΟΥΙΝΟΣ","ΜΑΚΑΟ","ΣΤΡΟΥΘΟΚΑΜΗΛΟΣ","ΦΛΑΜΙΝΓΚΟ"]

              zwa=["ΣΟΥΡΙΚΑΤΑ","ΠΙΘΗΚΟΣ","ΥΔΡΟΧΕΙΡΟΣ","ΧΙΜΠΑΤΖΗΣ","ΚΟΑΤΙ","ΚΡΙ-ΚΡΙ","ΛΑΜΑ","ΛΕΜΟΥΡΙΟΣ",
                "ΙΠΠΟΠΟΤΑΜΟΣ","ΣΕΡΒΑΛ","ΠΛΑΤΩΝΙ","ΣΙΤΑΤΟΥΝΓΚΑ","ΣΑΙΜΙΡΙ","ΡΙΝΟΚΕΡΟΣ","ΟΡΥΞ","ΜΑΡΑ","ΜΑΚΑΚΟΣ","ΟΥΑΛΑΜΠΙ","ΑΓΡΙΟΓΟΥΡΟΥΝΟ",
                "ΑΝΤΙΛΟΠΗ","ΕΛΕΦΑΝΤΑΣ","ΤΑΜΑΡΙΝΟΣ","ΚΑΜΗΛΑ","ΓΙΒΒΩΝΑΣ","ΜΥΡΜΗΓΚΟΦΑΓΟΣ","ΖΕΒΡΑ","ΚΑΜΗΛΟΠΑΡΔΑΛΗ","ΑΡΚΟΥΔΑ","ΑΛΟΓΟ","ΤΣΙΤΑΧ","ΠΟΥΜΑ","ΛΙΟΝΤΑΡΙ","ΤΙΓΡΗΣ",
                "ΑΛΙΓΑΤΟΡΑΣ","ΠΥΘΩΝΑΣ","ΒΟΑΣ","ΔΡΑΚΟΣ","ΓΚΕΚΟ","ΑΝΑΚΟΝΤΑ","ΚΡΟΚΟΔΕΙΛΟΣ","ΙΓΚΟΥΑΝΑ","ΛΟΦΙΟΦΟΡΟΣ","ΣΑΜΙΑΜΙΔΙ","ΦΡΥΝΟΣ","ΧΑΜΑΙΛΕΟΝΤΑΣ","ΤΕΡΑΣΓΚΙΛΑ","ΠΟΝΤΙΚΟΦΙΔΟ",
                "ΔΕΛΦΙΝΙ","ΦΩΚΙΑ","ΚΑΡΧΑΡΙΑΣ","ΙΠΠΟΚΑΜΠΟΣ","ΚΑΡΕΤΑ-ΚΑΡΕΤΑ","ΦΑΛΑΙΝΑ","ΦΥΣΗΤΗΡΑΣ","ΦΩΚΑΙΝΑ","ΖΙΦΙΟΣ","ΘΑΛΛΑΣΙΟ-ΛΙΟΝΤΑΡΙ","ΜΑΝΑΤΟΣ","ΘΑΛΑΣΣΙΑ-ΑΓΕΛΑΔΑ","ΘΑΛΑΣΣΙΟΣ-ΙΠΠΟΣ",
                "ΑΓΑΠΟΡΝΙΣ","ΑΕΤΟΣ","ΑΗΔΟΝΙ","ΧΗΝΑ","ΑΜΑΖΟΝΑ","ΒΟΥΚΕΡΟΣ","ΦΑΣΙΑΝΟΣ","ΙΒΙΣ","ΓΥΠΑΣ","ΦΡΟΥΤΟΦΑΣΑ","ΤΟΥΡΑΚΟ","ΚΥΚΝΟΣ","ΚΑΛΑΟ","ΚΑΖΟΥΑΡΙΟΣ","ΚΕΑ","ΜΠΟΥΛΜΠΟΥΛ","ΛΟΡΙ",
                "ΤΟΥΚΑΝΟΣ","ΚΟΡΑΚΙ","ΚΡΑΧΤΗΣ","ΤΡΥΓΟΝΙ","ΚΙΣΣΑ","ΥΦΑΝΤΗΣ","ΜΕΛΙΤΟΦΑΓΟΣ","ΜΠΟΥΦΟΣ","ΜΠΟΥΜΠΟΥΚ","ΝΑΝΟΧΗΝΑ","ΟΡΝΙΟ","ΠΕΛΑΡΓΟΣ","ΠΙΓΚΟΥΙΝΟΣ","ΜΑΚΑΟ","ΣΤΡΟΥΘΟΚΑΜΗΛΟΣ","ΦΛΑΜΙΝΓΚΟ"]
              tmhma=1
              perigrafh="ΠΡΟΣΤΑΤΕΥΟΜΕΝΟΣ ΧΩΡΟΣ"
              for i in range(len(zwa)):
                  if(i==33):
                      tmhma=2
                      perigrafh="ΚΕΛΙ"
                  if(i==47):
                      tmhma=3
                      perigrafh="ΛΙΜΝΗ_ΕΝΥΔΡΙΟ"
                  if(i==60):
                      tmhma=4
                      perigrafh="ΚΛΟΥΒΙ"

                  try :
                        curs.execute('INSERT INTO ΒΙΟΤΟΠΟΣ VALUES ({},{},"{}");'\
                             .format(i+1,tmhma,perigrafh))
                         
                        cnx.commit()
                  except mysql.connector.Error as e :
                        print(e)

                  
                  
                
#Διαγραφη στοιχειων του πινακα ΒΙΟΤΟΠΟΣ  
def delete_biotopos (cnx,curs):
    try :
            curs.execute('DELETE FROM ΒΙΟΤΟΠΟΣ WHERE TRUE')
                         
            cnx.commit()
    except mysql.connector.Error as e :
            print(e)



#----------------------------------------------------------------------- MAIN PROGRAMM ------------------------------------------------------------------------------------------------------------------------------------------

            

while True :
    print("Πάτησε 1 αν είσαι επισκέπτης του ζωολογικού κήπου")
    print("Πάτησε 2 αν είσαι ο διαχειριστής του ζωολογικού κήπου")
    idiothta=input("Γραψε εδω:")
    
    if idiothta not in ["1","2"]:
        print("Λαθος πληκτρολογηση.Προσπαθησε ξανα.")
    
    else: break

if(idiothta=="2"):
    password=input("Δώσε κωδικό πρόσβασης:")
    

if(idiothta=="1"):
    window = Tk()
    window.title("Καλώς ήρθατε στη βάση δεδομένων του ζωολογικού κήπου")
    w = 1000 
    h = 1000 
    ws = window.winfo_screenwidth() 
    hs = window.winfo_screenheight() 
    x=900
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.configure(background='green')
    selected = IntVar()
    rad1 = Radiobutton(window,text='Ερώτηση_1', value=1, variable=selected).grid(column=0, row=0)
    rad2 = Radiobutton(window,text='Ερώτηση_2', value=2, variable=selected).grid(column=1, row=0)
    rad3 = Radiobutton(window,text='Ερώτηση_3', value=3, variable=selected).grid(column=2, row=0)
    rad4 = Radiobutton(window,text='Ερώτηση_4', value=4, variable=selected).grid(column=3, row=0)
    rad5 = Radiobutton(window,text='Ερώτηση_5', value=5, variable=selected).grid(column=4, row=0)
    rad6 = Radiobutton(window,text='Ερώτηση_6', value=6, variable=selected).grid(column=5, row=0)
    rad7 = Radiobutton(window,text='Ερώτηση_7', value=7, variable=selected).grid(column=6, row=0)
    rad8 = Radiobutton(window,text='Ερώτηση_8', value=8, variable=selected).grid(column=7, row=0)
    rad9 = Radiobutton(window,text='Ερώτηση_9', value=9, variable=selected).grid(column=8, row=0)
    rad10 = Radiobutton(window,text='Ερώτηση_10', value=10,variable=selected).grid(column=9,row=0)
    btn = Button(window, text="Aπαντηση", command=clicked).grid(column=5, row=2)
    exit_button=Button(window, text = "Εξοδος", command = endProgam).grid(column=10 ,row=0)
    Question1 = Label(window, text = "Ερώτηση_1:  Δες τον αριθμό των ζώων που υπάρχουν στο ζωολογικό κήπο.").place(x = 30,y = 100)
    Question2 = Label(window, text = "Ερώτηση_2:  Δες τον αριθμό των επισκεπτών οποιοδήποτε έτος μέχρι σήμερα.").place(x = 30,y = 180)
    Question3 = Label(window, text = "Ερώτηση_3:  Διαθέσιμα προγράμματα και τιμές.").place(x = 30,y = 260)
    Question4 = Label(window, text = "Ερώτηση_4: Bρες που βρίσκεται κάποιο ζώο στο ζωολογικό κήπο.").place(x = 30,y = 340)
    Question5 = Label(window, text = "Ερώτηση_5:  Βρες τις κατηγορίες ζώων που υπάρχουν στο ζωολογικό κήπο.").place(x = 30,y = 420)
    Question6 = Label(window, text = "Ερώτηση_6:  Ωράρια λειτουργίας των τμημάτων του ζωολογικού κήπου").place(x = 30,y = 500)
    Question7 = Label(window, text = "Ερώτηση_7:  Επικοινωνία με τους υπεύθυνους των προγραμμάτων").place(x = 30,y = 580)
    Question8 = Label(window, text = "Ερώτηση_8:  Γενικές πληροφορίες για το ζωολογικό κήπο").place(x = 30,y = 660)
    Question9 = Label(window, text = "Ερώτηση_9:  Βρες την ημερομηνία γέννησης του μεγαλύτερου ζώου σε ηλικία").place(x = 30,y = 740)
    Question10 = Label(window, text = "Ερώτηση_10: Βρες την ημερομηνία γέννησης του μικρότερου ζώου σε ηλικία ").place(x = 30,y = 820)   
    window.mainloop()

  
elif idiothta=="2" and password=="password":
    
    window = Tk()
    window.title("ΔΙΑΧΕΙΡΙΣΤΗΣ")
    w = 1000 
    h = 1000 
    ws = window.winfo_screenwidth() 
    hs = window.winfo_screenheight() 
    x=900
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  
    window.configure(background='blue')
    selected = IntVar()
    rad1 = Radiobutton(window,text='Ερώτηση_1', value=1, variable=selected).grid(column=0, row=0)
    rad2 = Radiobutton(window,text='Ερώτηση_2', value=2, variable=selected).grid(column=1, row=0)
    rad3 = Radiobutton(window,text='Ερώτηση_3', value=3, variable=selected).grid(column=2, row=0)
    rad4 = Radiobutton(window,text='Ερώτηση_4', value=4, variable=selected).grid(column=3, row=0)
    rad5 = Radiobutton(window,text='Ερώτηση_5', value=5, variable=selected).grid(column=4, row=0)
    rad6 = Radiobutton(window,text='Ερώτηση_6', value=6, variable=selected).grid(column=5, row=0)
    rad7 = Radiobutton(window,text='Ερώτηση_7', value=7, variable=selected).grid(column=6, row=0)
    rad8 = Radiobutton(window,text='Ερώτηση_8', value=8, variable=selected).grid(column=7, row=0)
    rad9 = Radiobutton(window,text='Ερώτηση_9', value=9, variable=selected).grid(column=8, row=0)
    rad10 = Radiobutton(window,text='Ερώτηση_10', value=10, variable=selected).grid(column=9, row=0)
    rad11 = Radiobutton(window,text='Ερώτηση_11', value=11, variable=selected).grid(column=10, row=0)
    rad12 = Radiobutton(window,text='Ερώτηση_12', value=12, variable=selected).grid(column=11, row=0)
    btn = Button(window, text="Aπάντηση", command=clicked).grid(column=5, row=2)
    exit_button=Button(window, text = "Έξοδος", command = endProgam).grid(column=12 ,row=0)
    Question1 = Label(window, text = "Ερώτηση_1: Ιστορικό κτηνιάτρων.").place(x = 30,y = 100)
    Question2 = Label(window, text = "Ερώτηση_2: Ιστορικό υπαλλήλων.").place(x = 30,y = 180)
    Question3 = Label(window, text = "Ερώτηση_3:  Ιστορικό ζώων σε ασθένειες.").place(x = 30,y = 260)
    Question4 = Label(window, text = "Ερώτηση_4: Τροφή κάθε ζώου.").place(x = 30,y = 340)
    Question5 = Label(window, text = "Ερώτηση_5:  Bιότοποι και ζώα.").place(x = 30,y = 420)
    Question6 = Label(window, text = "Ερώτηση_6:  Πλήθος ζώων σε κάθε βιότοπο.").place(x = 30,y = 500)
    Question7 = Label(window, text = "Ερώτηση_7:  Ενημέρωση για νεκρό ζώο.").place(x = 30,y = 580)
    Question8 = Label(window, text = "Ερώτηση_8:  Εισαγωγή νέου ζώου.").place(x = 30,y = 660)
    Question9 = Label(window, text = "Ερώτηση_9:  Εισαγωγή νέου προγράμματος.").place(x = 30,y = 740)
    Question10 = Label(window, text = "Ερώτηση_10:  Εισαγωγή νέου εργαζομενου.").place(x = 30,y = 820)
    Question11 = Label(window, text = "Ερώτηση_11:  Ανανέωση προγράμματος.").place(x = 30,y = 880)
    Question12 = Label(window, text = "Ερώτηση_12:  Αλλαγή μισθού εργαζομένου.").place(x = 30,y = 940)
    
    
     
    window.mainloop()

    
    

    
    
   









