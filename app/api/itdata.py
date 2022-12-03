import requests


events = [{
        "EventName": "MedicalHistory",
        "EventAddress": "bart.sk",
        "EventDescription": "Create a sustainable blockchain project that is applicable within the context of securing, storing, and sharing medical data and the patient being the main actor in control.",
        "EventOwner": "bart.sk",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 10,
        "EventSignedUsers": "Jakub,Marek,Monika",
        "EventFilter": "sport"
    },{
        "EventName": "UpTimeBot",
        "EventAddress": "bart.sk",
        "EventDescription": "Celé zle! Namiesto obľúbenej stránky sa objaví len dinosaurus. ",
        "EventOwner": "bart.sk",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 2,
        "EventSignedUsers": "Nina",
        "EventFilter": "education"
    },{
        "EventName": "MobilnyBodovaci",
        "EventAddress": "Blue Lemons s.r.o.",
        "EventDescription": "Cieľom projektu je naprogramovať mobilnú aplikáciu pre bodovanie súťaží Slovenskej Lukostreleckej Asociácie 3D. Aplikácia bude spravovať zoznam lukostrelcov a súťaží a sumarizovať výsledky jednotlivých kôl. Navrhnutá aplikácia má byť prístupná aj offline.",
        "EventOwner": "Blue Lemons s.r.o.",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 6,
        "EventSignedUsers": "Katka,Adam",
        "EventFilter": "other"
    },{
        "EventName": "BlueSpace",
        "EventAddress": "Blue Lemons s.r.o.",
        "EventDescription": "Cieľom projektu je vytvoriť platformu k efektívnemu manažmentu ľuskych zdojov v spoločnosti. Vizualizácia alokácie jednotlivých zamestnancov ako aj reporting prebiehajúcich projektov. Zabezpečiť prepojenie medzi platformou a nástrojmi použivanými na projektoch (Jira).",
        "EventOwner": "Blue Lemons s.r.o.",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 4,
        "EventSignedUsers": "",
        "EventFilter": "food"
    },{
        "EventName": "PersonalDataCleaner",
        "EventAddress": "Deutsche Telekom IT",
        "EventDescription": "Aplikacia na vyhladavnie svojich zaznamov na slovenskych weboch za ucelom ziadania vymazu.",
        "EventOwner": "Deutsche Telekom IT",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 16,
        "EventSignedUsers": "",
        "EventFilter": "other"
    },{
        "EventName": "HateChecker",
        "EventAddress": "Deutsche Telekom IT",
        "EventDescription": "Browser plugin na kontrolu vlastnych prispevkov na hate speech na socialne siete.",
        "EventOwner": "Deutsche Telekom IT",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 10,
        "EventSignedUsers": "Marek,Jakub",
        "EventFilter": "music"
    },{
        "EventName": "Sprava3D",
        "EventAddress": "Deutsche Telekom IT",
        "EventDescription": "Vytvorenie webového portálu pre nahrávanie a správu 3D modelov a sprostretkovanie týchto modelov v mobilnej aplikácií pre kreatívnu formu vzdelávania.",
        "EventOwner": "Deutsche Telekom IT",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 7,
        "EventSignedUsers": "Tomas,Matus",
        "EventFilter": "other"
    },{
        "EventName": "FyzickaAktivita",
        "EventAddress": "FPT Slovakia",
        "EventDescription": "Navrhnutie a vytvorenie virtuálnych prostredí so stupňujúcou sa obtiažnosťou na prekonávanie fóbií za použitia interakcie vo virtuálnej realite.",
        "EventOwner": "FPT Slovakia",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 8,
        "EventSignedUsers": "Marek,Jakub,Adam",
        "EventFilter": "sport"
    },{
        "EventName": "Majetok",
        "EventAddress": "FPT Slovakia",
        "EventDescription": "Vytvorenie tréningového prostredia vo virtuálnej realite za využitia interakcie pre seniorov v sociálnych zariadeniach a stacionároch",
        "EventOwner": "FPT Slovakia",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 9,
        "EventSignedUsers": "Marek,Andrej,Petra",
        "EventFilter": "sport"
    },{
        "EventName": "VyuzitieRPA",
        "EventAddress": "GlobalLogic",
        "EventDescription": "Vývoj WEB aplikácie pre správu majetku spoločnosti s možnosťou zatriedenia majetku do kategórií, sledovania jeho histórie, odpisovania, vyradenia a možnosťou pravidelnej inventarizácie. Aplikácia umožní taktiež import dát cez REST API, majetok importovaný daným API bude potrebné schváliť a zatriediť užívateľom s adekvátnou rolou. Súčasťou riešenia budú aj včasné notifikácie o blížiacich sa termínoch odpísania majetku, splatenia majetku na lízing/úver a vytváranie reportu o aktuálnom stave majetku spoločnosti.",
        "EventOwner": "GlobalLogic",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 5,
        "EventSignedUsers": "Adam,Katka,Monika",
        "EventFilter": "music"
    },{
        "EventName": "AutomatizovanyZberDat",
        "EventAddress": "GlobalLogic",
        "EventDescription": "V čase COVID a post COVID situácie, keď došlo vo firmách ku viacerým zmenám, dostáva čoraz viac zelenú automatizácia a robotizácia procesov. Táto téma využíva nové RPA technológie, na rýchle a efektívne spracovanie vybraných procesov, ich vizualizáciu a automatický reporting.",
        "EventOwner": "GlobalLogic",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 3,
        "EventSignedUsers": "Tomas",
        "EventFilter": "travelling"
    },{
        "EventName": "PodpornaAplikacia",
        "EventAddress": "HOTOVO s.r.o.",
        "EventDescription": "Cieľom projektu je navrhnúť automatizovaný system schopný spracúvavať dáta z kamery umiestnenej v aute za účelom rozpoznávania viacerých informácii o komunikácii a tvorbe passportu. Systém by mal plniť v zásade dve konkrétne úlohy:",
        "EventOwner": "HOTOVO s.r.o.",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 6,
        "EventSignedUsers": "Nina,Katka",
        "EventFilter": "food"
    },{
        "EventName": "3DSimulaciaPremavky",
        "EventAddress": "HOTOVO s.r.o.",
        "EventDescription": "Cieľom projektu je uľahčiť servisné práce na bežných zariadeniach vďaka rozšírenej realite. Koncový užívateľ aplikácie by mal byť servisný pracovník spotrebičov, ako sú práčka, umývačka, televízia, výťah atp. Ich práca je špecifická v tom, že chodia k rôznym zákazníkom s rôznymi spotrebičmi. Každé zariadenie je pritom trochu iné a má iné umiestnenie komponentov a senzorov. Dokumentácia nie je vždu k dispozícii priamo pri zásahu u zákazníka, a ak áno, je komplikované v nej vyhľadávať počas zásahu. Aplikácia by mala používať kameru tabletu a na displeji tabletu vykresľovať rozšírenú realitu v ktorej by zobrazovala:",
        "EventOwner": "HOTOVO s.r.o.",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 8,
        "EventSignedUsers": "Adam,Petra",
        "EventFilter": "food"
    },{
        "EventName": "SpravaNapajania",
        "EventAddress": "Ness Košice",
        "EventDescription": "Navrhnite a implementujte správu napájania pre Raspberry Pi, Navrhnite a vytvorte si vlastný serverový kryt  pre RPi pomocou 3D tlaciarne. Navrhnite a implementujte ovládanie robotického ramena pomocou Raspberry Pi.",
        "EventOwner": "Ness Košice",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 4,
        "EventSignedUsers": "Marek,Jakub",
        "EventFilter": "sport"
    },{
        "EventName": "SmartData",
        "EventAddress": "Ness Košice",
        "EventDescription": "Služba pre automatizáciu dataflowu (dodávatelia, zákazníci, produkty, ponúkané služby). Za pomoci ML a data processing vygeneruje ďalšie parametre pre katagolizáciu.",
        "EventOwner": "Ness Košice",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 5,
        "EventSignedUsers": "Nina,Monika",
        "EventFilter": "music"
    },{
        "EventName": "IndexFund",
        "EventAddress": "Ness Košice",
        "EventDescription": "Fungujúci projekt Šport Košice (www.sportkosice.sk) potrebuje rozšírenie funkcionality. Táto unikátna webová stránka administrovaná pracovníkmi magistrátu združuje informácie o akciách, športových kluboch a športoviskách.",
        "EventOwner": "Ness Košice",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 6,
        "EventSignedUsers": "Katka,Adam",
        "EventFilter": "food"
    },{
        "EventName": "NaucnyChodnik",
        "EventAddress": "Siemens Healthcare s.r.o.",
        "EventDescription": "Fungujúci projekt Šport Košice (www.sportkosice.sk) potrebuje rozšírenie funkcionality. Táto unikátna webová stránka administrovaná pracovníkmi magistrátu združuje informácie o akciách, športových kluboch a športoviskách.",
        "EventOwner": "Siemens Healthcare s.r.o.",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 8,
        "EventSignedUsers": "",
        "EventFilter": "sport"
    },{
        "EventName": "BlackMirror",
        "EventAddress": "Siemens Healthcare s.r.o.",
        "EventDescription": "Pokúste sa čo najvernejšie zreplikovať technológiu z ľubovoľného futuristického seriálu (e.g. Black Mirror)",
        "EventOwner": "Siemens Healthcare s.r.o.",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 15,
        "EventSignedUsers": "Jakub,Andrej,Marek,Adam,Monika,Petra",
        "EventFilter": "other"
    },{
        "EventName": "OpenOfficeDesk",
        "EventAddress": "Siemens Healthcare s.r.o.",
        "EventDescription": "Úlohou riešiteľou je vytvoriť webovú aplikáciu, v ktorej uzivatel vytvorí priestor Open Officu kde naznačí stoly/meetingovky/stoličky. Nasledne si užívatelia môžu rezervovať stôl, meetingovku, ... na určitý čas/deň. Výsledkom je prehľadný dochádzkový systém s prehľadom voľných stolov na daný deň. Užívateľ môže aj prehliadať obsadenosť priestorov v kalendáry a rezervovať si stol na ktorýkoľvek deň. Taktiež pomocou webapp može nájsť svojho kolegu, v ktoré dni je v práci a  rezervovať si stol v ten istý deň pri nom ak potrebuju spoluparcovat. Aplikácia umôžní vytváranie aj prehľadných reportov s obsadenosťou priestorov dochádzkov zamestnancov a pod. pomocou aplikacie moze uzivatel zadefinovat ktore dni je v praci a ktoré doma a nasledne system zasle ziadost na pracu z domu nadriadenemu.",
        "EventOwner": "Siemens Healthcare s.r.o.",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 10,
        "EventSignedUsers": "Adam",
        "EventFilter": "food"
    },{
        "EventName": "JednoducheEKG",
        "EventAddress": "TUKE",
        "EventDescription": "Jednoduchý vývoj HW platformy pre zobrazenie EKG.  Možnosť získať cenné znalosti v rámci projektu , mentor projektu bude usmerňovať vývoj a nápomocný pri vývoji.",
        "EventOwner": "TUKE",
        "EventDateOfCreate": "2022-03-12",
        "EventDateOfEvent": "2022-03-12",
        "EventMaxUsers": 5,
        "EventSignedUsers": "Matus,Nina,Katka",
        "EventFilter": "sport"
    }
]
       

for i in events:       
    response = requests.post('http://127.0.0.1:8000/events', json=i)
    
    
users = [
        {
        "UserName": "Jakub",
        "UserAddress": "Bruselska",
        "UserDescription": "Student",
        "UserEvents": "OpenOfficeDesk",
        "UserFavorites": "OpenOfficeDesk",
        "UserFriends": "Andrej,Marek",
        "UserOwnedEvents": "MedicalHistory,FyzickaAktivita,OpenOfficeDesk"
    },{
        "UserName": "Marek",
        "UserAddress": "Bruselska",
        "UserDescription": "Student",
        "UserEvents": "MedicalHistory,FyzickaAktivita,OpenOfficeDesk",
        "UserFavorites": "MedicalHistory,FyzickaAktivita,OpenOfficeDesk",
        "UserFriends": "Nina,Katka",
        "UserOwnedEvents": "OpenOfficeDesk"
    },{
        "UserName": "Andrej",
        "UserAddress": "Bruselska",
        "UserDescription": "Lector",
        "UserEvents": "OpenOfficeDesk",
        "UserFavorites": "OpenOfficeDesk",
        "UserFriends": "Nina",
        "UserOwnedEvents": "MedicalHistory,PersonalData,FyzickaAktivita"
    },{
        "UserName": "Tomas",
        "UserAddress": "Bruselska",
        "UserDescription": "Lector",
        "UserEvents": "MedicalHistory,PersonalData,FyzickaAktivita",
        "UserFavorites": "MedicalHistory,PersonalData,FyzickaAktivita",
        "UserFriends": "",
        "UserOwnedEvents": "PersonalData,IndexFund"
    },{
        "UserName": "Matus",
        "UserAddress": "Bruselska",
        "UserDescription": "Mentor",
        "UserEvents": "PersonalData,IndexFund",
        "UserFavorites": "PersonalData,IndexFund",
        "UserFriends": "Andrej",
        "UserOwnedEvents": "FyzickaAktivita,SpravaNapajania"
    },{
        "UserName": "Adam",
        "UserAddress": "Bruselska",
        "UserDescription": "Student",
        "UserEvents": "FyzickaAktivita,SpravaNapajania",
        "UserFavorites": "FyzickaAktivita,SpravaNapajania",
        "UserFriends": "Marek,Petra",
        "UserOwnedEvents": "PersonalData,SpravaNapajania,IndexFund"
    },{
        "UserName": "Katka",
        "UserAddress": "Bruselska",
        "UserDescription": "Expert",
        "UserEvents": "PersonalData,SpravaNapajania,IndexFund",
        "UserFavorites": "PersonalData,SpravaNapajania,IndexFund",
        "UserFriends": "Nina",
        "UserOwnedEvents": "MedicalHistory,SpravaNapajania"
    },{
        "UserName": "Nina",
        "UserAddress": "Bruselska",
        "UserDescription": "Lector",
        "UserEvents": "MedicalHistory,SpravaNapajania",
        "UserFavorites": "MedicalHistory,SpravaNapajania",
        "UserFriends": "Tomas",
        "UserOwnedEvents": "IndexFund,OpenOfficeDesk"
    },{
        "UserName": "Petra",
        "UserAddress": "Bruselska",
        "UserDescription": "Mentor",
        "UserEvents": "IndexFund,OpenOfficeDesk",
        "UserFavorites": "IndexFund,OpenOfficeDesk",
        "UserFriends": "Matus",
        "UserOwnedEvents": "PersonalData,SpravaNapajania,IndexFund"
    },{
        "UserName": "Monika",
        "UserAddress": "Bruselska",
        "UserDescription": "Student",
        "UserEvents": "PersonalData,SpravaNapajania,IndexFund",
        "UserFavorites": "PersonalData,SpravaNapajania,IndexFund",
        "UserFriends": "Marek",
        "UserOwnedEvents": "MedicalHistory,PersonalData"
    }
    
    ]
        
        
for i in users:       
    response = requests.post('http://127.0.0.1:8000/users', json=i)
    
    
user = [    {
        "UserName": "Jakub",
        "UserPassword": "heslo",
        "UserEmail": "jakub@gmail.com"
    },
        {
        "UserName": "Marek",
        "UserPassword": "heslo",
        "UserEmail": "marek@gmail.com"
    },
        {
        "UserName": "Andrej",
        "UserPassword": "heslo",
        "UserEmail": "andrej@gmail.com"
    },
        {
        "UserName": "Tomas",
        "UserPassword": "heslo",
        "UserEmail": "tomas@gmail.com"
    },
        {
        "UserName": "Matus",
        "UserPassword": "heslo",
        "UserEmail": "matus@gmail.com"
    },
        {
        "UserName": "Adam",
        "UserPassword": "heslo",
        "UserEmail": "adam@gmail.com"
    },
        {
        "UserName": "Katka",
        "UserPassword": "heslo",
        "UserEmail": "katka@gmail.com"
    },
        {
        "UserName": "Nina",
        "UserPassword": "heslo",
        "UserEmail": "nina@gmail.com"
    },
        {
        "UserName": "Petra",
        "UserPassword": "heslo",
        "UserEmail": "petra@gmail.com"
    },
        {
        "UserName": "Monika",
        "UserPassword": "heslo",
        "UserEmail": "monika@gmail.com"
    }
       ]

for i in user:       
    response = requests.post('http://127.0.0.1:8000/register', json=i)
    

print("hotovo")