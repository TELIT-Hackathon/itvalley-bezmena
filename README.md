Zakladne info o projekte, Stack - Django, Postgres, Vue
Full stack developer - Marek Horvath
Front end developer - Diana Orsolyova 

[Link na jiru](https://brofinder.atlassian.net/jira/software/projects/BROF/boards/1)


# Dependencies 

| Program      | Version |
| :---        |    :----:   |
| [Node.js](https://nodejs.org/en/)     |  16.6.1 |
| [Visual Studio Code](https://code.visualstudio.com/)     | -  |
| [Postman](https://www.postman.com/)     |  - |
| [Python](https://www.python.org/)     |  3.9.2 |
| [PGAdmin](https://www.pgadmin.org/)     |  4 |
| [Postgresql](https://www.postgresql.org/)     | -  |

## PIP installations 

pip install psycopg2 django djangorestframework django-cors-headers

## NODE installations

npm install 

# BroFinderAPI

API ku projektu\

[Link na api](https://git.kpi.fei.tuke.sk/brofinder/brofinderapi)

## Kroky ku spusteniu API
1. Prepisanie credentials v DjangoAPI/settings.py riadok 89
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'brofinder',
            'USER': 'postgres',
            'PASSWORD': 'marecek'
        }
    }

2. Vytvorenie tabuliek, cez terminal zadat prikazy 
python manage.py makemigrations BroFinderApp\
python manage.py makemigrations \
python manage.py migrate BroFinderApp\
python manage.py migrate \

3. Optional - Nahratie dat 
python data.py

4. Spustenie serveru 
python manage.py runserver

## Vytvorenie projektu

django-admin startproject DjangoAPI\

python manage.py startapp BroFinderApp

## Dolezite komponenty

### BroFinderApp/serializers.py
Serializuje modely na objekt 

### BroFinderApp/models.py
Modely pre vytvorenie databazy 
Zoznam endpointov
| Nazov      | Popis |
| :---        |    :----:   |
| [Node.js](https://nodejs.org/en/)     |  16.6.1 |

### BroFinderApp/urls.py
Zoznam endpointov
| Nazov      | Popis |
| :---        |    :----:   |
| [Node.js](https://nodejs.org/en/)     |  16.6.1 |
### BroFinderApp/views.py
Funkcionalita API
### DjangoAPI/urls.py
Admin cast pre Django 

### Photos
Tu sa ukladaju fotky o eventoch a profiloch

# BroFinderUI

Vue3 appka

[Link na ui](https://git.kpi.fei.tuke.sk/brofinder/brofinderui)

## Spustenie projektu
npm run serve
url - localhost:8080/


## Dolezite komponenty 

### Locales
JSON subory, umoznuju menenie jazyka 
### Router/index.js
Zoznam vsetkych url ciest
| Nazov      | Popis |
| :---        |    :----:   |
| /   | Uvitacia stranka |
| mainpage   | Hlavna stranka |
|  detailevent/:id  | zobrazenie konkretneho eventu |
|  profile/:name  | zobrazenie konkretneho profilu |
|  registration  | registracia |
|   singup | prihlasenie |
|  favorites  | oblubene eventy |

### views/AddNewEventModal.vue
Formular na vytvorenie noveho eventu 
| Metody      | Popis |
| :---        |    :----:   |
|   closemodal   |   |
|   createEvent   |   |
|   onFileChange(e)   |   |

### views/DetailEvent.vue
Otvorenie jedneho konkretneho eventu
| Metody      | Popis |
| :---        |    :----:   |
|  onFileChange(e)    |   |
|   editEvent   |   |
|    resetNotif  |   |
|    addLike(id)  |   |
|  deleteComment(id)    |   |
|   addToFavorite   |   |
|    removeFromFavorite  |   |
|    AddComment  |   |
|   deleteEvent   |   |
|  redirecteditevent    |   |
|    replaceByDefault(e)  |   |
|   deleteUserFromEvent(item)   |   |
|  subUserToEvent    |   |
|    getEventInfo  |   |


### views/FavoriteEvents.vue
Oblubene Eventy
| Metody      | Popis |
| :---        |    :----:   |
|   replaceByDefault(e)   |   |
|  getEvents    |   |

### views/LanguageSwitcher.vue
Komponent sluziaci na menenie jazyku 

### views/MainPage.vue
Hlavna stranka programu 
| Metody      | Popis |
| :---        |    :----:   |
|   resetNotif   |   |
|   getUsersCount(abc)   |   |
|    searchBar  |   |
|    addFavorite(id)  |   |
|    sortEvents2(type)  |   |
|   sortEvents(type)   |   |
|    onClickHandler(a)  |   |
|  redirectFavorite()    |   |
|   replaceByDefault(e)   |   |
|   getEvents   |   |
|   getUsers   |   |
|     showModal |   |
|   closeModal   |   |


### views/Notification.vue
Komponent pre notifikacie 

### views/Profile.vue
Profil pouzivatela
| Metody      | Popis |
| :---        |    :----:   |
|  editProfile    |   |
|   onFileChange(e)   |   |
|   onClickHandler(a)   |   |
|   onClickHandler2(a)   |   |
|  addFriend    |   |
|   removeFriend   |   |
|     owned |   |
|    joined  |   |
|   friends   |   |
|   redirecteditprofile   |   |
|    replaceByDefault(e)  |   |
|   formatDate(value)   |   |
|    getUserInfo  |   |
|    getEvents  |   |
|   checkAdded   |   |


### views/Registration.vue
Registracia pouzivatela
| Metody      | Popis |
| :---        |    :----:   |
|   registerUser   |   |
|   onFileChange(e)   |   |

### views/SingUp.vue
Prihlasenie pouzivatela
| Metody      | Popis |
| :---        |    :----:   |
|   loginUser   |   |

## Vytvorenie projektu
vue create BroFinderUI
