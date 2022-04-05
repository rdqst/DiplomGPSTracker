import eel
import json

eel.init('UI')

points = []

#Функция получения координат
def Lizzard(points):
    with open("geo.json", "r") as json_file:
        geo = json.load(json_file)
        
        numberOfWorkers = geo['active_workers'] #получаем количество активных работников

        points = []

        workersCount = 1
        #Получение массива координат
        while workersCount <= numberOfWorkers: 
            for txt in geo['id' + str(workersCount)]: #создали цикл, который будет работать построчно
                points.append(txt['coordinateX'])
                points.append(txt['coordinateY'])
            #geo_str.append("-") #Добавление разделителя между координатами
            workersCount += 1

  
    #Временный вывод

    print(type(points))
    print(points)
    #/Временный вывод

    with open("txt.txt", "w") as file:
        print(points, file=file)

    return points

#Функция получения информации о работниках


   


    
        


       
        

eel.call(Lizzard(points))


eel.start("index.html", mode = 'chrome', size = (800, 960))