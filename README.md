# Venmurasu_django
API to get interesting facts about venmurasu novel.

Here we have used the data from venmurasu novel written by writer jeyamogan. 
Navel starting from https://venmurasu.in/2014/01/01/%E0%AE%B5%E0%AF%86%E0%AE%A3%E0%AF%8D%E0%AE%AE%E0%AF%81%E0%AE%B0%E0%AE%9A%E0%AF%81-%E0%AE%A8%E0%AF%82%E0%AE%B2%E0%AF%8D-%E0%AE%92%E0%AE%A9%E0%AF%8D%E0%AE%B1%E0%AF%81/

Deployed Web App:

https://venmurasu.herokuapp.com/

# Requirements
1)Python3


Previous work : https://github.com/naveeen684/Venmurasu-Final
Note: The previous work shows how the date is scrapped and stored in different files. We took the sort.txt from the previous work and used it in this django project. 


# To run the app locally,

1) git clone https://github.com/naveeen684/Venmurasu_django.git or directly download as zip file from this repo.
2) cd Venmurasu_django
3) pip install requirements.txt
4)python manage.py makemigrations
5)python manage.py migrate
To upload data to the database,
6)python manage.py shell
7)from home.upload import upload
8)upload()
It will take some time to upload the words from sort.txt to database, after completeion
9)exit()
10)python manage.py runserver


# API requests:
API URL : https://venmurasu.herokuapp.com
GET REQUESTS

## Getting all words

    GET:https://venmurasu.herokuapp.com/api/words/all

    RESPONSE :
    [
        {
            "id": 1,
            "word": "வெடிபடுமண்டலத்திருளலைவெடிபடநடமிடுதுடியெழுகடியொலிதாளம்",
            "length": 32,
            "frequency": 1
        },
        {
            "id": 2,
            "word": "மைந்தனுக்குப்பிடித்திருக்கிறதுஎத்தனைமுறை",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 3,
            "word": "இருந்துகொண்டிருந்தவர்களுக்குமட்டும்தான்",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 4,
            "word": "என்னைத்தேடிவருவதுண்டுதேவிபுராணசம்ஹிதையை",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 5,
            "word": "சர்வகல்விதமேவாஹம்சர்வகல்விதமேவாஹம்",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 6,
            "word": "உக்ரசேனன்சத்ருஞ்சயன்வியாஹ்ரதந்தன்",
            "length": 21,
            "frequency": 1
        },
        {
            "id": 7,
            "word": "நான்யாஸ்திசனாதனம்சர்வகல்விதமேவாஹம்",
            "length": 21,
            "frequency": 1
        },
        {
            "id": 8,
            "word": "அலங்கரிக்கப்பட்டிருக்கவேண்டுமல்லவா",
            "length": 21,
            "frequency": 1
        },
        {
            "id": 9,
            "word": "சேர்த்துவிடுவீர்கள்அஞ்சவேண்டியதில்லை",
            "length": 20,
            "frequency": 1
        },
        {
            "id": 10,
            "word": "பனங்கொட்டைத்துருவலைப்போட்டிருந்தனர்",
            "length": 20,
            "frequency": 1
        },
        {
            "id": 11,
            "word": "இறந்தவர்களுக்கும்தீராச்சினத்துடன்",
            "length": 20,
            "frequency": 1
        },
        {
            "id": 12,
            "word": "பிடிக்கிறதுசிங்கம்ஓடிவாருங்கள்கல்லை",
            "length": 20,
            "frequency": 1
        },
        {
            "id": 13,
            "word": "நினைவுபடுத்திக்கொள்ளவேண்டியிருக்கிறதே",
            "length": 20,
            "frequency": 1
        },
        {
            "id": 14,
            "word": "பிரித்துப்பரப்பிவிட்டிருக்கிறார்கள்",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 15,
            "word": "சந்தனத்தைலத்தையும்வேப்பெண்ணையையும்",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 16,
            "word": "அப்பெயர்களைச்சொல்லிக்கொண்டிருந்தன",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 17,
            "word": "எதிர்வினையாற்றாமலிருக்கமுடியவில்லை",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 18,
            "word": "ஏற்றுக்கொள்ளப்பழகிவிட்டிருந்தனர்",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 19,
            "word": "எதிர்பார்த்துக்கொண்டிருந்திருக்கிறது",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 20,
            "word": "மைந்தரைப்பெற்றுக்கொண்டிருப்பதாகவும்",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 21,
            "word": "அமரச்செய்யப்பட்டிருக்கின்றீர்கள்",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 22,
            "word": "அவருக்குத்தெரியவேண்டுமென்பதற்காக",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 23,
            "word": "ஒதுக்கப்பட்டவர்கள்அவர்களிடம்",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 24,
            "word": "பித்துப்பிடித்தவர்களாகிவிட்டார்கள்",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 25,
            "word": "இரண்டாகப்பகுக்கப்படவிருக்கிறது",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 26,
            "word": "போர்க்கூச்சலெழுப்பிக்கொண்டிருந்தனர்",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 27,
            "word": "காற்றில்படமெடுத்தாடிக்கொண்டிருந்தன",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 28,
            "word": "அழுத்தப்பட்டுக்கொண்டிருப்பதைப்போல்",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 29,
            "word": "அறிவிக்கப்பட்டிருக்கப்படவுமில்லை",
            "length": 19,
            "frequency": 1
        },
        {
            "id": 30,
            "word": "இருட்பெருங்குழிச்சுழியலைப்பெருக்கென",
            "length": 19,
            "frequency": 1
        },
        .
        .
        .
        .
    ]
   



## Getting 7 longest words

    GET:https://venmurasu.herokuapp.com/api/words/longest/7

    RESPONSE :
    [
        {
            "id": 1,
            "word": "வெடிபடுமண்டலத்திருளலைவெடிபடநடமிடுதுடியெழுகடியொலிதாளம்",
            "length": 32,
            "frequency": 1
        },
        {
            "id": 2,
            "word": "மைந்தனுக்குப்பிடித்திருக்கிறதுஎத்தனைமுறை",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 4,
            "word": "என்னைத்தேடிவருவதுண்டுதேவிபுராணசம்ஹிதையை",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 5,
            "word": "சர்வகல்விதமேவாஹம்சர்வகல்விதமேவாஹம்",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 3,
            "word": "இருந்துகொண்டிருந்தவர்களுக்குமட்டும்தான்",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 7,
            "word": "நான்யாஸ்திசனாதனம்சர்வகல்விதமேவாஹம்",
            "length": 21,
            "frequency": 1
        },
        {
            "id": 6,
            "word": "உக்ரசேனன்சத்ருஞ்சயன்வியாஹ்ரதந்தன்",
            "length": 21,
            "frequency": 1
        }
    ]


## Getting 8 smallest words

GET:https://venmurasu.herokuapp.com/api/words/smallest/8

RESPONSE :

    [
        {
            "id": 9966,
            "word": "ரத்தினகுண்டலங்களும்",
            "length": 12,
            "frequency": 1
        },
        {
            "id": 9969,
            "word": "புத்திரலாபத்துக்குரிய",
            "length": 12,
            "frequency": 1
        },
        {
            "id": 9964,
            "word": "கோட்டான்களிடமிருந்தும்",
            "length": 12,
            "frequency": 1
        },
        {
            "id": 9965,
            "word": "வெல்வதற்கரியதாயிற்று",
            "length": 12,
            "frequency": 1
        },
        {
            "id": 9967,
            "word": "மங்கலப்பொருட்களுடன்",
            "length": 12,
            "frequency": 6
        },
        {
            "id": 9968,
            "word": "பொறுப்பேற்கவிருக்கிறாய்",
            "length": 12,
            "frequency": 1
        },
        {
            "id": 9963,
            "word": "இணைக்கப்பட்டிருந்தது",
            "length": 12,
            "frequency": 6
        },
        {
            "id": 9970,
            "word": "ஒலித்துக்கொண்டிருந்தன",
            "length": 12,
            "frequency": 35
        }
    ]



## Getting 9 most frequent words

GET:https://venmurasu.herokuapp.com/api/words/most-frequent/9

RESPONSE :

    [
        {
            "id": 4778,
            "word": "நிகழ்ந்துகொண்டிருக்கிறது",
            "length": 13,
            "frequency": 110
        },
        {
            "id": 4749,
            "word": "இந்திரப்பிரஸ்தத்திற்கு",
            "length": 13,
            "frequency": 86
        },
        {
            "id": 9971,
            "word": "நிகழ்ந்துகொண்டிருந்தது",
            "length": 12,
            "frequency": 78
        },
        {
            "id": 4698,
            "word": "வந்துகொண்டிருக்கிறார்கள்",
            "length": 13,
            "frequency": 76
        },
        {
            "id": 4718,
            "word": "ஷண்முகவேல்பெரிதுபடுத்த",
            "length": 13,
            "frequency": 70
        },
        {
            "id": 9976,
            "word": "அமர்ந்திருக்கிறார்கள்",
            "length": 12,
            "frequency": 58
        },
        {
            "id": 5063,
            "word": "பேசிக்கொண்டிருக்கிறார்கள்",
            "length": 13,
            "frequency": 55
        },
        {
            "id": 10000,
            "word": "அதிர்ந்துகொண்டிருந்தது",
            "length": 12,
            "frequency": 53
        },
        {
            "id": 5263,
            "word": "சென்றுகொண்டிருக்கிறார்கள்",
            "length": 13,
            "frequency": 38
        }
    ]

## Getting 10 least frequent words

GET:https://venmurasu.herokuapp.com/api/words/least-frequent/10

RESPONSE :

    [
        {
            "id": 2,
            "word": "மைந்தனுக்குப்பிடித்திருக்கிறதுஎத்தனைமுறை",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 3,
            "word": "இருந்துகொண்டிருந்தவர்களுக்குமட்டும்தான்",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 4,
            "word": "என்னைத்தேடிவருவதுண்டுதேவிபுராணசம்ஹிதையை",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 5,
            "word": "சர்வகல்விதமேவாஹம்சர்வகல்விதமேவாஹம்",
            "length": 22,
            "frequency": 1
        },
        {
            "id": 6,
            "word": "உக்ரசேனன்சத்ருஞ்சயன்வியாஹ்ரதந்தன்",
            "length": 21,
            "frequency": 1
        },
        {
            "id": 7,
            "word": "நான்யாஸ்திசனாதனம்சர்வகல்விதமேவாஹம்",
            "length": 21,
            "frequency": 1
        },
        {
            "id": 8,
            "word": "அலங்கரிக்கப்பட்டிருக்கவேண்டுமல்லவா",
            "length": 21,
            "frequency": 1
        },
        {
            "id": 9,
            "word": "சேர்த்துவிடுவீர்கள்அஞ்சவேண்டியதில்லை",
            "length": 20,
            "frequency": 1
        },
        {
            "id": 10,
            "word": "பனங்கொட்டைத்துருவலைப்போட்டிருந்தனர்",
            "length": 20,
            "frequency": 1
        },
        {
            "id": 1,
            "word": "வெடிபடுமண்டலத்திருளலைவெடிபடநடமிடுதுடியெழுகடியொலிதாளம்",
            "length": 32,
            "frequency": 1
        }
    ]



## Getting exact word match

GET:https://venmurasu.herokuapp.com/api/words/search-with-word/வெடிபடுமண்டலத்திருளலைவெடிபடநடமிடுதுடியெழுகடியொலிதாளம்

RESPONSE :

    [
        {
            "id": 1,
            "word": "வெடிபடுமண்டலத்திருளலைவெடிபடநடமிடுதுடியெழுகடியொலிதாளம்",
            "length": 32,
            "frequency": 1
        }
    ]



## Getting word contains specific word/letter

For word

GET:https://venmurasu.herokuapp.com/api/words/word-contains/வெடி

RESPONSE :

    [
        {
            "id": 1,
            "word": "வெடிபடுமண்டலத்திருளலைவெடிபடநடமிடுதுடியெழுகடியொலிதாளம்",
            "length": 32,
            "frequency": 1
        },
        {
            "id": 1339,
            "word": "குமிழிவெடித்துக்கொண்டிருந்தது",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 2820,
            "word": "வெடித்துச்சிரித்துவிட்டனர்",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 4420,
            "word": "வெடித்துக்கொண்டிருக்கின்றன",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 5606,
            "word": "உலர்த்திவெடிக்கவைக்கும்",
            "length": 13,
            "frequency": 1
        },
        {
            "id": 6676,
            "word": "வெடித்துப்பரவியிருந்தது",
            "length": 13,
            "frequency": 1
        }
    ]



For letter

GET:https://venmurasu.herokuapp.com/api/words/word-contains/வெ

RESPONSE :

    [
        {
            "id": 1,
            "word": "வெடிபடுமண்டலத்திருளலைவெடிபடநடமிடுதுடியெழுகடியொலிதாளம்",
            "length": 32,
            "frequency": 1
        },
        {
            "id": 44,
            "word": "புடவிப்பெருவெளிப்பெருக்கலைகளெழும்",
            "length": 18,
            "frequency": 1
        },
        {
            "id": 61,
            "word": "இருள்விஷக்கருநீலப்பேரொளிவெள்ளம்",
            "length": 18,
            "frequency": 1
        },
        {
            "id": 189,
            "word": "வெளிப்படுத்தப்படுவதென்பதனால்",
            "length": 17,
            "frequency": 1
        },
        {
            "id": 196,
            "word": "கொலைவெறியாடிக்கொண்டிருக்கிறார்கள்",
            "length": 17,
            "frequency": 1
        },
        {
            "id": 215,
            "word": "முடிவெடுக்கப்பட்டுவிட்டதல்லவா",
            "length": 17,
            "frequency": 1
        },
        {
            "id": 216,
            "word": "வெளிப்பட்டுக்கொண்டிருக்கவேண்டும்",
            "length": 17,
            "frequency": 1
        },
        {
            "id": 223,
            "word": "ஓய்வெடுத்துக்கொண்டிருந்தவர்கள்",
            "length": 17,
            "frequency": 1
        },
        {
            "id": 314,
            "word": "ஓய்வெடுத்துக்கொண்டிருக்கும்போது",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 333,
            "word": "எண்ணிமுடிவெடுப்பதற்குள்ளாகவே",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 335,
            "word": "வெளியிட்டுக்கொண்டிருக்கவேண்டும்",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 420,
            "word": "வெற்றிலைபோட்டுக்கொண்டிருந்தனர்",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 475,
            "word": "வெண்சுண்ணத்தூண்கள்போலிருந்தன",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 509,
            "word": "வெறியாட்டுக்கொண்டதுபோலிருந்தது",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 525,
            "word": "வெளிறத்தொடங்குவதற்குள்ளாகவே",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 565,
            "word": "வெளிப்படுத்திக்கொண்டிருந்தனர்",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 590,
            "word": "வெளியேற்றப்பட்டிருக்கிறார்கள்",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 618,
            "word": "ஓய்வெடுத்துக்கொண்டிருந்தார்கள்",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 783,
            "word": "வெற்றிகொள்ளப்படமுடியாதவரே",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 834,
            "word": "முடிவெடுக்கவேண்டியிருக்கிறது",
            "length": 15,
            "frequency": 2
        },
        {
            "id": 872,
            "word": "வெல்லப்படாதவர்களென்றறிக",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 911,
            "word": "அடர்காட்டுச்சமவெளிகளையும்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 954,
            "word": "வெண்ணிறச்சுதைப்பரப்பின்மேல்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 965,
            "word": "வெண்தந்தங்களைப்பற்றியபடி",
            "length": 15,
            "frequency": 2
        },
        {
            "id": 1024,
            "word": "வெண்தோல்எலும்புதசைக்கூட்டம்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1111,
            "word": "பெரும்புல்வெளிகளைப்பற்றியும்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1126,
            "word": "வெளிப்படுத்திக்கொண்டிருப்பது",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1194,
            "word": "ஓய்வெடுத்துக்கொண்டிருக்கையில்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1308,
            "word": "வெளிப்படுத்திக்கொண்டிருந்தது",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1329,
            "word": "ஓய்வெடுத்துக்கொண்டிருந்தபோது",
            "length": 15,
            "frequency": 2
        },
        {
            "id": 1339,
            "word": "குமிழிவெடித்துக்கொண்டிருந்தது",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1342,
            "word": "உருவெடுத்துக்கொண்டிருக்கிறான்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1352,
            "word": "வெளிவரத்தொடங்கியிருப்பதைக்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1381,
            "word": "ஓய்வெடுத்துக்கொண்டிருந்தனர்",
            "length": 15,
            "frequency": 2
        },
        {
            "id": 1392,
            "word": "வெளியேறிக்கொண்டிருக்கிறார்கள்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1412,
            "word": "வெட்டிக்குவிக்கப்பட்டதுபோல்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1428,
            "word": "வெளிப்படுத்திக்கொண்டிருப்பவை",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1558,
            "word": "வெல்லப்படமுடியாதவர்களாக",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1578,
            "word": "ஓய்வெடுத்துக்கொண்டிருக்கிறார்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1596,
            "word": "வெண்பஞ்சுகளாகிவிட்டிருந்தன",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1623,
            "word": "அவ்வெறுப்புக்குரியவர்களாக",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1734,
            "word": "வெறியாட்டெழுந்திருப்பதைப்போல்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1792,
            "word": "வெளிவந்துகொண்டிருக்கிறார்கள்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1812,
            "word": "வென்றுகொண்டிருந்தபோதிலும்கூட",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1856,
            "word": "முடிவெடுக்கப்பட்டிருக்கிறது",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1903,
            "word": "முடிவெடுத்துக்கொண்டவர்களின்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1921,
            "word": "வெண்ணிறம்கொண்டவர்களாதலால்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1954,
            "word": "வெளியேறிக்கொண்டிருக்கின்றன",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 2071,
            "word": "வெட்டச்சென்றிருந்தபோதுதான்",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 2074,
            "word": "உருவெடுத்துவிட்டிருக்கிறார்",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 2107,
            "word": "வெறுக்கப்படுபவர்கள்கூட",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 2179,
            "word": "வெண்குதிரைகளுக்குப்பின்னால்",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 2184,
            "word": "மலப்புழுவென்றாக்கிவிட்டீர்",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 2324,
            "word": "அளவெடுத்துக்கொண்டிருந்தன",
            "length": 14,
            "frequency": 1
        },
        .
        .
        .
    ]

## Getting word starts with specific word/letter

For word

GET:https://venmurasu.herokuapp.com/api/words/start-with/வெடி

RESPONSE :

    [
        {
            "id": 1,
            "word": "வெடிபடுமண்டலத்திருளலைவெடிபடநடமிடுதுடியெழுகடியொலிதாளம்",
            "length": 32,
            "frequency": 1
        },
        {
            "id": 2820,
            "word": "வெடித்துச்சிரித்துவிட்டனர்",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 4420,
            "word": "வெடித்துக்கொண்டிருக்கின்றன",
            "length": 14,
            "frequency": 1
        },
        {
            "id": 6676,
            "word": "வெடித்துப்பரவியிருந்தது",
            "length": 13,
            "frequency": 1
        }
    ]

For letter

GET:https://venmurasu.herokuapp.com/api/words/start-with/வெ

RESPONSE :

    [
        {
            "id": 1,
            "word": "வெடிபடுமண்டலத்திருளலைவெடிபடநடமிடுதுடியெழுகடியொலிதாளம்",
            "length": 32,
            "frequency": 1
        },
        {
            "id": 189,
            "word": "வெளிப்படுத்தப்படுவதென்பதனால்",
            "length": 17,
            "frequency": 1
        },
        {
            "id": 216,
            "word": "வெளிப்பட்டுக்கொண்டிருக்கவேண்டும்",
            "length": 17,
            "frequency": 1
        },
        {
            "id": 335,
            "word": "வெளியிட்டுக்கொண்டிருக்கவேண்டும்",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 420,
            "word": "வெற்றிலைபோட்டுக்கொண்டிருந்தனர்",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 475,
            "word": "வெண்சுண்ணத்தூண்கள்போலிருந்தன",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 509,
            "word": "வெறியாட்டுக்கொண்டதுபோலிருந்தது",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 525,
            "word": "வெளிறத்தொடங்குவதற்குள்ளாகவே",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 565,
            "word": "வெளிப்படுத்திக்கொண்டிருந்தனர்",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 590,
            "word": "வெளியேற்றப்பட்டிருக்கிறார்கள்",
            "length": 16,
            "frequency": 1
        },
        {
            "id": 783,
            "word": "வெற்றிகொள்ளப்படமுடியாதவரே",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 872,
            "word": "வெல்லப்படாதவர்களென்றறிக",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 954,
            "word": "வெண்ணிறச்சுதைப்பரப்பின்மேல்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 965,
            "word": "வெண்தந்தங்களைப்பற்றியபடி",
            "length": 15,
            "frequency": 2
        },
        {
            "id": 1024,
            "word": "வெண்தோல்எலும்புதசைக்கூட்டம்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1126,
            "word": "வெளிப்படுத்திக்கொண்டிருப்பது",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1308,
            "word": "வெளிப்படுத்திக்கொண்டிருந்தது",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1352,
            "word": "வெளிவரத்தொடங்கியிருப்பதைக்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1392,
            "word": "வெளியேறிக்கொண்டிருக்கிறார்கள்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1412,
            "word": "வெட்டிக்குவிக்கப்பட்டதுபோல்",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1428,
            "word": "வெளிப்படுத்திக்கொண்டிருப்பவை",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1558,
            "word": "வெல்லப்படமுடியாதவர்களாக",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1596,
            "word": "வெண்பஞ்சுகளாகிவிட்டிருந்தன",
            "length": 15,
            "frequency": 1
        },
        {
            "id": 1734,
            "word": "வெறியாட்டெழுந்திருப்பதைப்போல்",
            "length": 15,
            "frequency": 1
        },
        .
        .
        .
    ]






