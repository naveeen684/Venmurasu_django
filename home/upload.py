import os
from django.conf import settings
from home.models import Word


def upload():
    file_ = str(os.path.join(settings.BASE_DIR, 'sorted.txt'))

    with open(file_, "r", encoding="utf-8") as file:
        words = [line.rstrip('\n') for line in file]

    print(len(words))

    count = 0

    for i in words[:10000]:
        print(count)
        word, length, frequency = i.split("-")
        count += 1
        obj = Word(word=word, length=length, frequency=frequency)
        obj.save()

    print(words[count])
