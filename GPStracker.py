import eel
import json
from itertools import combinations

eel.init('UI')

points = []
sick = []
result = []
table = []

# Функция получения координат
def Lizzard(points, result, table):
    with open("geo.json", "r", encoding='utf-8') as json_file:
        geo = json.load(json_file)

        # Получаем количество активных работников
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
   
    # /Временный вывод

    g = 3
    n = len(sick)//g
    groups = [sick[i:i + n] for i in range(0, len(sick), n)]
    for x, y in combinations(groups, 2):
        numberOfContacts = sum(i==j for i,j in zip(x, y))
        result.append(int(numberOfContacts))
    print(result)

        # 1-2, 1-3, 2-3

    table = geo['workers']
    print(table)
    

    with open("txt.txt", "w") as file:
        print(points, file=file)

    return points, result, table


eel.call(Lizzard(points, result, table))

eel.start("index.html", mode='chrome', size=(1920, 1080))