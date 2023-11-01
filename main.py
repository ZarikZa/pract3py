import time
import json
import csv
import os
age = {"age1": "12 лет", "age2": "14 лет", "age3": "16 лет", "age4": "17 лет"}
vibormove = []
nameg = []
data = []
b = int()
a = int()
def zagruzka(save_name):
    try:
        with open(f"{save_name}.json", "r") as file:
            game_data = json.load(file)
            print(f"Сохранение '{save_name}' успешно загружено.")
    except FileNotFoundError:
        print(f"Сохранение '{save_name}' не найдено.")

def prosmotrjson():
    filename = input("Введите название json файла: ")
    try:
        with open(filename) as json_file:
            data2 = json.load(json_file)
            print(data2)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")

def delete():
    print("Название сохранения: ")
    save_name = input()
    try:
        os.remove(f"{save_name}.json")
        print(f"Сохранение '{save_name}' удалено.")
    except FileNotFoundError:
        print(f"Сохранение '{save_name}' не найдено.")
def zapistoscv(data):
    with open('novella.csv', 'w', newline='') as file:
        fieldname = ['Имя', 'Имя друга', 'Выбор 1', 'Выбор 2', 'Выбор 3', 'Выбор 4']
        writer = csv.DictWriter(file, fieldnames=fieldname, delimiter=';')
        writer.writeheader()
        for row in data:
            writer.writerow(row)
def readcsv():
    try:
        with open("novella.csv", 'r') as file:
            reader = csv.reader(file)
            for row1 in reader:
                data.append(row1)
    except FileNotFoundError:
        pass
    return data
def viborzz():
    l = bool(True)
    while (l != False):
        try:
            a = int(input())
            if a is not int and a > 12 or a < 0:
                 print("Введите число меньше или равному 12 или меньше или равному 1")
            else:
                l = False
        except ValueError:
            print("Не понятно, введите число меньше или равному 12 или меньше или равному 1!")

def name():
    b = bool
    while (b != True):
        myname = input()
        b = myname.isalpha()
        if b == False:
            print("Введите имя без цифр и пробелов!")
        elif b == True:
            c = myname.capitalize()
            nameg.append(c)
    return myname
def vibor(b):
    h = bool()
    while (h == False):
        if b is not int and b > 2 or b < 1:
            print("Введите число 1 или 2")
            try:
                b = int(input())
            except ValueError:
                print("Не понятно, введи число 1 или 2!")
        else:
            h = True
    return b

def nameMate ():
    print("Введите имя персонажа:")
    b = bool
    while (b != True):
        namema = input()
        b = namema.isalpha()
        if b == False:
            print("Введите имя без цифр и пробелов!")
        elif b == True:
            c = namema.capitalize()
            nameg.append(c)
    return namema
def coridor():
    print("Вы медленно заглянули в кабинет и были в шоке от увиденного")
    time.sleep(3)
    print("Mисс Мада что-то перебирала и уже собиралась отнест документы в сейф, но заметила вас ")
    time.sleep(1)
    print("Вы в ступоре смотрите на неё изумлёнными глазами")
    time.sleep(1)
    print("Она заставляет вас закрыть дверь")
    time.sleep(1)
    print("Отношение с мисс Мада несильно ухудшились")
    time.sleep(1)
    print("Вы закрытаете дверь и уходите")
def fraz():
    print("Вы напрвляетесь в столовую и встречаете своего друга")
    friend1 = nameMate()
    age1 = age["age4"]
    print(nameg[1] + " " + age1 + "- ваш друг, родился на пересечении двух знаков зодиака \"змееносец\" и \"телец\",\n который в тайне от всех обучает детей управлять своими способностями.")
    time.sleep(3)
    fraze1 = f"- Доброе утро, {nameg[0]}."
    print(fraze1)
    fraze2 = f"- Доброе утро, {nameg[1]}."
    time.sleep(1)
    print(fraze2 + " После завтрака встречаемся в нашем месте.")
    time.sleep(2)
    print("Вы идёте по дальше по коридору")
    time.sleep(1)
    print("Вы видите открытый кабинет")
    time.sleep(1)
    print("У вас непреодалимое желание заглянуть в него, но вы можете пересилить себя и пройти мимо")
    time.sleep(1)
    g = ["1.Заглянуть", "2.Пройти мимо"]
    print("Выбор:\n" + g[0] + "\n" + g[1])
    if vibor(b) == 1:
        vibormove.append(g[0])
        print("Вы выбрали: " + g[0])
        coridor()
    else:
        vibormove.append(g[1])
        print("Вы выбрали: " + g[1])
        print("Вы проходите мимо, но слышите странные звуки, исходящие из кабинета")
    print("Вы заходите в столовую и берёте тарелку с непонятной жижей")
    return (friend1)
def ssora():
    print("Вы начинаете обвинять персонал в их некомпитентности")
    time.sleep(1)
    print("Мисс Мада грозно смотрит на вас, но Вы не замечаете и продолжаете инкриминировать поварской состав")
    time.sleep(1)
    print("- Как вы можете такое подавать детям, мне " + f + " у меня молодой растущий орга...")
    time.sleep(0.4)
    print("Мисс Мада вмешивается в ваш конфликт и принуждает вас замолчать")
    time.sleep(0.5)
    print("Отношения с мисс Мада ухудшились")
    time.sleep(0.5)
    print("- Быстро вышел отсюда!")
    time.sleep(0.5)
    print("Вы смотрите на разъярённую мисс Мада и уходите, устремив свой взгляд в пол")
def run():
    print("Вы идёте по коридору, оглядываетесь и сворачиваете в стену, ппроникая в потойную комнату")
    time.sleep(0.5)
    print("Примечание: способность знака зодиака \"телец\" - создавать потайные проходы")
    h = f"Вы заходите и встречаете {nameg[1]}"
    print(h)
    time.sleep(1)
    print("- Сегодня, как планировали сбегаем из этой шаражки")
    v = f"- Хорошо, {nameg[1]}, надеюсь всё пройдёт по плану"
    print(v)
    time.sleep(1)
    print("Вы выходите из комнаты и идёте на улицу, потому что настало время прогулки")
    j = f"{nameg[1]} направляется к посту охраны, Вы идёте за ним, но держитесь на небольшой дистанции"
    print(j)
    time.sleep(1)
    print("В вашу голову попадает мысль одуматься или пойти дальше")
def otrvibor():
    print("Вы не можете сделать такое действие, у Вас недостаточный уровень отношений с мисс Мада")
    a = int(input())
    while a < 2:
        print("Вы не можете сделать такое действие, у Вас недостаточный уровень отношений с мисс Мада")
        time.sleep(1)
        a = int(input())
    return(a)
def end():
    print("Вы заходите на пост охраны, но они ожидали вашего прибытия, так как мисс Мада следила за вами и сообщила, куда вы направляетесь.")
    time.sleep(1)
    print("Вас принуждают следовать за мисс Мада, которая ведёт вас в кабинет ликвадации метежников")
    time.sleep(2)
    print("КОНЕЦ.\nКонцовка неудачная.")

print("Добро пожаловать в текстовую новеллу \"Знаки зодиака\"")
print("------------------------")
print("Выберете действие:\n1.Начать игру\n2.Работа с сохранениями")
if vibor(b) == 1:
    print("Вы живете в мире, где ваша магия зависит от вашего знака зодиака.")
    time.sleep(1)
    print("Если Вы стрелец, то у вас могут появляться лук и стрелы.")
    time.sleep(1)
    print("Будучи близнецами, Вы можете создавать клона, которым можете управлять.")
    time.sleep(1)
    print("Выберите свой знак зодиака:\n1.Овен\t2.Телец\t3.Близнецы\n4.Рак\t5.Лев\t6.Дева\n7.Весы\t8.Скорпион\t9.Стрелец\n10.Козерог\t11.Водолей\t12.Рыбы")
    f = age["age2"]
    viborzz()
    print("Ошибка...")
    time.sleep(1)
    print("Ошибка...")
    time.sleep(1)
    print("Сбой системы...")
    time.sleep(1)
    print("Ваш знак зодиака \"Змееносец\"\nВаша способность - Вы можете призвать змею с смертельным ядом,\nкоторая полностью подвластна вам.")
    time.sleep(1)
    print("Введите имя:")
    name()
    print("Вам " + f)
    begining = f"Доброе утро, {nameg[0]}, пара вствать."
    print("Вы открывает глаза и видите как вас забирают от матери и увозят в лагерь для таких же как Вы.")
    time.sleep(1)
    print("Шли годы Вы повзрослели и начали полностью осознавать свои действия.")
    time.sleep(1)
    print("Вас будит ваша воспитательница, у которой знак зодиака «скорпион».\n-" + begining)
    g = ["1.Проснуться", "2.Продолжить спать"]
    print("Выбор:\n" + g[0] + "\n" + g[1])
    if vibor(b) == 1:
        vibormove.append(g[0])
        print("Вы выбрали:" + g[0])
        print("- Доброе утро, мисс Мада")
        time.sleep(1)
        print("- Давай одевайся и иди в столовую\nмисс Мада уходит")
        time.sleep(1)
        fraz()
        print("Вы ловите на себе приятный взгляд мисс Мада")
        time.sleep(2)
        h = ["1.Подойти к мисс Мада", "2.Начать возмущаться на месте"]
        print("Выбор:\n" + h[0] + "\n" + h[1])
        if vibor(b) == 1:
            vibormove.append(h[0])
            print("Вы выбрали: " + h[0])
            fraz2 = f"Прости, {nameg[0]}, ничем не могу тебе помочь, сама в шоке"
            print("Вы подходите к мисс Мада и высказываете ей своё недовольство\nМисс Мада пожимает плечами")
            time.sleep(1)
            print("- " + fraz2)
            time.sleep(1)
            print("Вы решаете сегодня не кушать и уходите из столовой")
            time.sleep(1)
            run()
            time.sleep(1)
            h = ["1.Одуматься и пойти к мисс Мада", "2.Пойти дальше"]
            print("Выбор:\n" + h[0] + "\n" + h[1])
            if vibor(b) == 1:
                vibormove.append(h[0])
                print("Вы выбрали: " + h[0])
                print("Вы разворачиваетесь и направляетесь к мисс Мада")
                time.sleep(1)
                h = f"- Привет {nameg[0]}, что случилось?"
                print(h)
                time.sleep(1)
                n = f"- Мисс Мада я должен вам признаться я и {nameg[1]} хотли сегодня сбежать, он сейчас идёт к посту охраны"
                print(n)
                time.sleep(1)
                print("Мисс Мада приходит в ярость и напрявляется к посту охраны, принуждая вас стоять на месте")
                time.sleep(1)
                print("Вы стоите в ожидании возвращения мисс Мада 20 минут, и когда она попадает в ваше поле зрения, Вы видите, как вашего друга ведут охранники.")
                time.sleep(1)
                print("Мисс Мада принуждает вас забыть об этом человке")
                time.sleep(1)
                print("КОНЕЦ.\nКонцовка неудачная.")
            else:
                vibormove.append(h[1])
                print("Вы выбрали: " + h[1])
                print("Вы заходите в пост и нападаете на охранников.")
                time.sleep(1)
                j = f"Вы и {nameg[1]} призываете змей и направляете их на охранников"
                print(j)
                time.sleep(1)
                print("Так как ваше поялвение было неожиданно, охранники не успели применить свои способности\nВы сбежали")
                time.sleep(1)
                print("КОНЕЦ.\nУдачная концовка.")
        else:
            vibormove.append(h[1])
            print("Вы выбрали: " + h[1])
            time.sleep(1)
            ssora()
            run()
    else:
        vibormove.append(g[1])
        print("Вы выбрали:" + g[1])
        time.sleep(1)
        print("Мисс Мада начинает злиться и применяет способность своего знака зодиака «принуждение» и заставляет тебя пронуться")
        time.sleep(2)
        print("Вы просыпаетесь и держитесь за голову\n- \"Давай вставай и иди в столовую\"\n мисс Мада уходит\nВаши отношения с мисс Мада ухудшились")
        time.sleep(2)
        fraz()
        print("Вы ловите на себе презрительный взгляд мисс Мада")
        h = ["1.Подойти к мисс Мада", "2.Начать возмущаться на месте"]
        print("Выбор:\n" + h[0] + "\n" + h[1])
        if vibor(b) == 2:
            vibormove.append(h[1])
            print("Вы выбрали:" + h[1])
            ssora()
            run()
        else:
            vibormove.append(h[0])
            otrvibor()
            ssora()
            run()
        h = ["1.Одуматься и пойти к мисс Мада", "2.Пойти дальше"]
        print("Выбор:\n" + h[0] + "\n" + h[1])
        if vibor(b) == 2:
            vibormove.append(h[1])
            end()
        else:
            vibormove.append(h[0])
            otrvibor()
            end()
else:
    while(True):
        print("1 - Загрузить сохранение\n2 - Удалить сохранение\n3 - Просмотр сохранения\n4 - Выйти из программы")
        vib = input()
        if vib == "1":
            print("Введите название сохранения")
            save_name = input("Введите название сохранения: ")
            zagruzka(save_name)
        elif vib == "2":
            delete()

        elif vib == "3":
            prosmotrjson()
        elif vib == "4":
            exit()
        else:
            print("Неверный выбор")
print("Название сохранения:")
nammeofsave = input()
data1 = {
        "Имя": nameg[0],
        "Имя друга": nameg[1],
        "Выбор 1": vibormove[0],
        "Выбор 2": vibormove[1],
        "Выбор 3": vibormove[2],
        "Выбор 4": vibormove[3]
}
data.append(data1)
with open(f'{nammeofsave}.json', 'w') as file:
    json.dump(data, file, indent=4)
datar = readcsv()
zapistoscv(datar)



exit()