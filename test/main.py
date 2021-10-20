import lwforecast as lwf
import lwforecast as lwf

data = lwf.parse_csv("water_potability.csv", 1)
model = lwf.train(data)

for element in data:
    arr = []
    for i in range(0, len(element) - 1):
        arr.append(element[i])
    print(lwf.predict(arr, model))