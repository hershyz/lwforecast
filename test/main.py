import lwforecast as lwf
import lwforecast as lwf

data = lwf.parse_csv("water_potability.csv", 1)
model = lwf.train(data)

print(lwf.calc_acc(data, model))