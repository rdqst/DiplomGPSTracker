import eel
import json
import numpy as np
from itertools import combinations

eel.init('UI')

points = []
sick = []
result = []



# Функция получения координат


def Lizzard(points, result):
    with open("geo.json", "r") as json_file:
        geo = json.load(json_file)

        # получаем количество активных работников
        numberOfWorkers = geo['active_workers']

        workersCount = 1
        # Получение массива координат
        while workersCount <= numberOfWorkers:

            workerArray = []
            for i in geo['id' + str(workersCount)]:

                pointArray = []

                pointArray.append(i['coordinateX'])
                pointArray.append(i['coordinateY'])
                workerArray.append(pointArray)


                sick.append(pointArray)

            workersCount += 1
            points.append(workerArray)

    # Временный вывод

    print(type(points))
    print(points)

    print(type(sick))
    print(sick[0])
    print(sick)
    # /Временный вывод

    g = 3
    n = len(sick)//g
    groups = [sick[i:i + n] for i in range(0, len(sick), n)]
    for x, y in combinations(groups, 2):
        numberOfContacts = sum(i==j for i,j in zip(x, y))
        result.append(int(numberOfContacts))
    print(result)

        # 1-2, 1-3, 2-3







    with open("txt.txt", "w") as file:
        print(points, file=file)

    return points, result

 #Функция




eel.call(Lizzard(points, result))


eel.start("index.html", mode='chrome', size=(1920, 1080))
