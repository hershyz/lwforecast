import lwforecast as lwf

data = lwf.parse_csv("training.csv", 1)
model = lwf.train(data)

print(lwf.predict([69, 150], model))