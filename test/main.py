import lwforecast as lwf
import lwforecast as lwf

data = lwf.parse_csv("training.csv", 1)
model = lwf.train(data)

print(lwf.calc_acc(data, model))
print(lwf.predict([480, 420, 3866, 6, 8], model))