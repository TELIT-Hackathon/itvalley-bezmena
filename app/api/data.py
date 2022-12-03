import requests


events = [{
        "EventName": "joga",
        "EventAddress": "Alpinka",
        "EventDescription": "Niekto na spoločné prevetranie mysle a tela?",
        "EventOwner": "Miska",
        "EventDateOfCreate": "2022-09-09",
        "EventDateOfEvent": "2022-09-19",
        "EventMaxUsers": 20,
        "EventSignedUsers": "Veronika,Anka,Sofia",
        "EventFilter": "sport"
    },{
        "EventName": "ComicCon",
        "EventAddress": "Belgium",
        "EventDescription": "Do u wanna meet with the stars and unforgettable weekend?",
        "EventOwner": "Diako",
        "EventDateOfCreate": "2022-09-08",
        "EventDateOfEvent": "2022-10-22",
        "EventMaxUsers": 4,
        "EventSignedUsers": "Laura,Tommy,Lea",
        "EventFilter": "entertainment"
    },{
        "EventName": "koncert",
        "EventAddress": "Steel Arena",
        "EventDescription": "Hľadám partiu na Stinga. Kto má chuť na dobrú hudbu?",
        "EventOwner": "Jozko",
        "EventDateOfCreate": "2022-09-09",
        "EventDateOfEvent": "2022-09-28",
        "EventMaxUsers": 6,
        "EventSignedUsers": "Peto,Jano,Adam",
        "EventFilter": "music"
    },{
        "EventName": "tura",
        "EventAddress": "Tatry",
        "EventDescription": "Milovníci hôr pridajte sa na Teryho chatu.",
        "EventOwner": "Biba",
        "EventDateOfCreate": "2022-09-15",
        "EventDateOfEvent": "2022-11-20",
        "EventMaxUsers": 5,
        "EventSignedUsers": "Miska,Laura,Adam",
        "EventFilter": "travelling"
    },
{
        "EventName": "streetfood",
        "EventAddress": "Kino Úsmev",
        "EventDescription": "Mám tu nejakých gurmánov?",
        "EventOwner": "Peto",
        "EventDateOfCreate": "2022-09-15",
        "EventDateOfEvent": "2022-09-18",
        "EventMaxUsers": 30,
        "EventSignedUsers": "Marko,Jano,Sofia",
        "EventFilter": "food"
    },{
        "EventName": "speak",
        "EventAddress": "Mlynska",
        "EventDescription": "Kto si chce precvičiť speakovanie pri káve?",
        "EventOwner": "Miso",
        "EventDateOfCreate": "2022-09-28",
        "EventDateOfEvent": "2022-10-10",
        "EventMaxUsers": 15,
        "EventSignedUsers": "Samo,Anka,David,Adam,Diako",
        "EventFilter": "education"
    },{
        "EventName": "lego",
        "EventAddress": "Hlavna",
        "EventDescription": "Hľadám partiu na stavanie Košíc z lega",
        "EventOwner": "Jozko",
        "EventDateOfCreate": "2022-11-06",
        "EventDateOfEvent": "2022-12-17",
        "EventMaxUsers": 10,
        "EventSignedUsers": "Kubo,Marek,Lea,Peto,Jano,Veronika,Adam",
        "EventFilter": "other"
    },{
        "EventName": "zipline",
        "EventAddress": "Beňatina",
        "EventDescription": "Fanúšikovia adrenalínu?",
        "EventOwner": "Samo",
        "EventDateOfCreate": "2022-09-18",
        "EventDateOfEvent": "2022-10-07",
        "EventMaxUsers": 5,
        "EventSignedUsers": "Kubo,Miso,David",
        "EventFilter": "entertainment"
    },
{
        "EventName": "tura",
        "EventAddress": "Dukla",
        "EventDescription": "Po stopách hrdinou cestou SNP",
        "EventOwner": "Jano",
        "EventDateOfCreate": "2022-09-06",
        "EventDateOfEvent": "2023-02-17",
        "EventMaxUsers": 20,
        "EventSignedUsers": "Marek,David,Peto,Jano,Daniel,Tommy,Adam",
        "EventFilter": "travelling"
    },{
        "EventName": "speak",
        "EventAddress": "Amfik",
        "EventDescription": "Alguien precvičiť si španielčinu pri premietaní Money Heist?",
        "EventOwner": "Natalia",
        "EventDateOfCreate": "2022-09-05",
        "EventDateOfEvent": "2022-09-20",
        "EventMaxUsers": 8,
        "EventSignedUsers": "Lea,Tommy,Biba",
        "EventFilter": "education"
    },{
        "EventName": "futbal",
        "EventAddress": "Futbalová aréna",
        "EventDescription": "Hľadám partiu, čo pôjde zahrať futbal.",
        "EventOwner": "Daniel",
        "EventDateOfCreate": "2022-09-23",
        "EventDateOfEvent": "2022-09-28",
        "EventMaxUsers": 20,
        "EventSignedUsers": "Marek,Peto,Jano,Marko,Adam,Tommy,Dávid",
        "EventFilter": "sport"
    },{
        "EventName": "concert",
        "EventAddress": "Portugal",
        "EventDescription": "Someone with a good taste? ",
        "EventOwner": "Marco",
        "EventDateOfCreate": "2022-10-10",
        "EventDateOfEvent": "2022-12-24",
        "EventMaxUsers": 5,
        "EventSignedUsers": "Anka,Lea,Jano",
        "EventFilter": "music"
    },
{
        "EventName": "tasting",
        "EventAddress": "Alžbetina",
        "EventDescription": "Coffee lovers???",
        "EventOwner": "Lea",
        "EventDateOfCreate": "2022-10-06",
        "EventDateOfEvent": "2022-09-17",
        "EventMaxUsers": 20,
        "EventSignedUsers": "Natalia,Janka,Brona",
        "EventFilter": "food"
    },{
        "EventName": "imagination",
        "EventAddress": "Hlavná",
        "EventDescription": "Kto chce zažiť čarovný večer v Živej galérii?",
        "EventOwner": "Biba",
        "EventDateOfCreate": "2022-09-09",
        "EventDateOfEvent": "2022-09-13",
        "EventMaxUsers": 5,
        "EventSignedUsers": "Miska,Janka,Peto,Jano",
        "EventFilter": "entertainment"
    },{
        "EventName": "volejbal",
        "EventAddress": "Čičky",
        "EventDescription": "Plážová partia?",
        "EventOwner": "Laura",
        "EventDateOfCreate": "2022-09-26",
        "EventDateOfEvent": "2022-09-30",
        "EventMaxUsers": 20,
        "EventSignedUsers": "Natalia,Lea,Tommy,Biba",
        "EventFilter": "sport"
    
    },
{
        "EventName": "party",
        "EventAddress": "staré mesto",
        "EventDescription": "Noc plná prekvapení?",
        "EventOwner": "Adam",
        "EventDateOfCreate": "2022-09-18",
        "EventDateOfEvent": "2022-09-29",
        "EventMaxUsers": 20,
        "EventSignedUsers": "David,Veronika,Jano,Janka",
        "EventFilter": "music"
    },{
        "EventName": "tanec",
        "EventAddress": "Jose Garcia Dance Company",
        "EventDescription": "Ak si chceš užiť atmosféru a iskry na parkete, pridaj sa!! ",
        "EventOwner": "Lea",
        "EventDateOfCreate": "2022-09-05",
        "EventDateOfEvent": "2022-09-20",
        "EventMaxUsers": 25,
        "EventSignedUsers": "Sofia,Anka,Tommy,Diako",
        "EventFilter": "education"
    },{
        "EventName": "karate",
        "EventAddress": "K2",
        "EventDescription": "dame bitku?",
        "EventOwner": "Natalia",
        "EventDateOfCreate": "2022-09-05",
        "EventDateOfEvent": "2022-09-20",
        "EventMaxUsers": 5,
        "EventSignedUsers": "Kubo,Daniel,Jozko,Biba",
        "EventFilter": "sport"
    },{
        "EventName": "deti",
        "EventAddress": "Anička",
        "EventDescription": "Niekto do partie zabaviť sa aj s celou rodinkou na Ceste okolo sveta?",
        "EventOwner": "Daniel",
        "EventDateOfCreate": "2022-09-10",
        "EventDateOfEvent": "2022-09-18",
        "EventMaxUsers": 15,
        "EventSignedUsers": "Lea,David,Veronika,Tommy,Jozko,Peto",
        "EventFilter": "entertainment"
    },{
        "EventName": "Riddikulus",
        "EventAddress": "Historická radnica",
        "EventDescription": "Mám tu aj ľudí z Rokfortu?",
        "EventO,wner": "Anka",
        "EventDateOfCreate": "2022-09-15",
        "EventDateOfEvent": "2022-10-22",
        "EventMaxUsers": 18,
        "EventSignedUsers": "Miska,David,Tommy,Biba,Marek",
        "EventFilter": "entertainment"
    },
{
        "EventName": "splav",
        "EventAddress": "Lodenica",
        "EventDescription": "Hladam partiu co pojde zahrat futbal",
        "EventOwner": "Kubo",
        "EventDateOfCreate": "2022-09-06",
        "EventDateOfEvent": "2022-09-11",
        "EventMaxUsers": 20,
        "EventSignedUsers": "Samo,Laura,Miso,Veronika",
        "EventFilter": "travelling"
    }
]
       

for i in events:       
    response = requests.post('http://127.0.0.1:8000/events', json=i)
    
    
users = [
        {
        "UserName": "Kubo",
        "UserAddress": "Bruselska",
        "UserDescription": "Cau ja som kubo",
        "UserEvents": "",
        "UserFavorites": "",
        "UserFriends": "",
        "UserOwnedEvents": ""
    },
    {
        "UserName": "Samo",
        "UserAddress": "Atenska",
        "UserDescription": "Serus volam sa samo a mam 20 rokov",
        "UserEvents": "",
        "UserFavorites": "",
        "UserFriends": "",
        "UserOwnedEvents": ""
    },
        {
        "UserName": "Laura",
        "UserAddress": "Madridska",
        "UserDescription": "Ahoj ako sa mas?",
        "UserEvents": "",
        "UserFavorites": "",
        "UserFriends": "",
        "UserOwnedEvents": ""
    },
            {
        "UserName": "Miso",
        "UserAddress": "Popradska",
        "UserDescription": "Idem do prveho rocnika na TUKE",
        "UserEvents": "",
        "UserFavorites": "",
        "UserFriends": "",
        "UserOwnedEvents": ""
    },    {
        "UserName": "Veronika",
        "UserAddress": "Hanojska",
        "UserDescription": "Idem na kazdy event",
        "UserEvents": "",
        "UserFavorites": "",
        "UserFriends": "",
        "UserOwnedEvents": ""
    }
        ,    {
        "UserName": "Miska",
        "UserAddress": "Havanska",
        "UserDescription": "Blondinka",
        "UserEvents": "",
        "UserFavorites": "",
        "UserFriends": "",
        "UserOwnedEvents": ""
    }
        ,    {
        "UserName": "David",
        "UserAddress": "Belehradska",
        "UserDescription": "Futbalista",
        "UserEvents": "",
        "UserFavorites": "",
        "UserFriends": "",
        "UserOwnedEvents": ""
    }
        ,    {
        "UserName": "Marek",
        "UserAddress": "Bukurestska",
        "UserDescription": "CEO of Brofinder",
        "UserEvents": "",
        "UserFavorites": "",
        "UserFriends": "",
        "UserOwnedEvents": ""
    }
        
    
    ]
        
        
for i in users:       
    response = requests.post('http://127.0.0.1:8000/users', json=i)
    
    
user = [    {
        "UserName": "Kubo",
        "UserPassword": "heslo",
        "UserEmail": ""
    },
        {
        "UserName": "Samo",
        "UserPassword": "heslo",
        "UserEmail": ""
    },
        {
        "UserName": "Laura",
        "UserPassword": "heslo",
        "UserEmail": ""
    },
        {
        "UserName": "Miso",
        "UserPassword": "heslo",
        "UserEmail": ""
    },
        {
        "UserName": "Veronika",
        "UserPassword": "heslo",
        "UserEmail": ""
    },
        {
        "UserName": "Miska",
        "UserPassword": "heslo",
        "UserEmail": ""
    },
        {
        "UserName": "David",
        "UserPassword": "heslo",
        "UserEmail": ""
    },
        {
        "UserName": "Marek",
        "UserPassword": "heslo",
        "UserEmail": ""
    }
       ]

for i in user:       
    response = requests.post('http://127.0.0.1:8000/register', json=i)
    
    
print("hotovo")