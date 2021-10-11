def xy_regression(points):
    xy_data = []
    x = []
    y = []
    xy = []
    x2 = []

    x_sum = 0
    y_sum = 0
    xy_sum = 0
    x2_sum = 0

    for point in points:
        xy_data.append(point)

    for point in xy_data:
        xy.append(point[0] * point[1])
        x2.append(point[0] * point[0])
        x.append(point[0])
        y.append(point[1])

    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = sum(xy)
    x2_sum = sum(x2)

    a = (y_sum * x2_sum) - (x_sum * xy_sum)
    a /= (len(xy_data) * x2_sum) - (x_sum * x_sum)

    b = (len(xy_data) * xy_sum) - (x_sum * y_sum)
    b /= (len(xy_data) * x2_sum) - (x_sum * x_sum)

    return [a, b]


def parse_csv(csv, start_index):

    data = []

    with open(csv) as f:

        lines = f.readlines()
        for i in range(0, len(lines)):
            lines[i] = str.replace(lines[i], "\n", "")
        
        for i in range(start_index, len(lines)):
            raw = lines[i].split(",")
            data_row = []
            for element in raw:
                data_row.append(float(element))
            data.append(data_row)
        
    return data


def train(data):

    model = []

    for i in range(0, len(data[0]) - 1):

        xy_list = []
        for j in range(0, len(data)):
            xy_list.append([data[j][i], data[j][len(data[0]) - 1]])
        
        model.append(xy_regression(xy_list))
    
    return model


def predict(point, model):

    prediction = 0
    for i in range(0, len(point)):
        line = model[i]
        prediction += (point[i] * line[1]) + line[0]
    
    prediction /= len(point)
    return prediction