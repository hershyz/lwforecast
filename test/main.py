import lwforecast as lwf
import lwforecast as lwf

data = lwf.parse_csv("training.csv", 0)
model = lwf.train(data)
print(lwf.calc_acc(data, model))