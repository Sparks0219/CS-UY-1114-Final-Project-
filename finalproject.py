#Joshua Lee
#CS-UY 1114
#May 9 2019
#Final project

import turtle


def create_table(file_name):
    list1 = []
    list2 = []
    list3 = []
    file_obj = open(file_name, "r")
    for line in file_obj:
        linelist = line.strip().split(',')
        list1 += [float(linelist[0])]
        list2 += [float(linelist[1])]
        list3 += [linelist[2]]
    return (list1,list2,list3)

def print_range_max_min(data):
    i = 1 
    for lst in data:
        temp_lst = lst[:]
        temp_lst.sort()
        maxnum = max(temp_lst)
        minnum = min(temp_lst)
        datarange = maxnum-minnum 
        print('Feature',i," - "+"min:", maxnum,"max:", minnum, "range:",datarange)
        i += 1

def find_mean(feature):
    acc = 0
    total = 0
    for num in feature:
        acc += num
        total += 1
    average = acc/total 
    return average 

def find_std_dev(feature, mean):
    acc = 0
    for i in range(0,len(feature)):
        acc += (feature[i]-mean)**2
    stdev = (acc/len(feature))**0.5
    return stdev 
        
def normalize_data(data):
    i = 1
    for i1 in range(0,2):
        mean = find_mean(data[i1])
        stdev = find_std_dev(data[i1],mean)
        for i2 in range(len(data[i1])):
            data[i1][i2] = (data[i1][i2]-mean)/stdev
        normmean =find_mean(data[i1])
        normstdev=find_std_dev(data[i1], normmean)
        print("Feature",i," - mean:",mean, "std dev:",stdev)
        print("Feature",i,"after normalization - mean:",normmean, "std dev:", normstdev)
        i += 1

def make_predictions(train_set, test_set):
    predictionlist = []
    for i1 in range(len(test_set[0])):
        holder = 100000
        for i2 in range(len(train_set[0])):
            dis = find_dist(test_set[0][i1],test_set[1][i1],train_set[0][i2],train_set[1][i2])
            if dis < holder:
                holder = dis
                predicttype = train_set[2][i2]
        predictionlist.append(predicttype)
    return predictionlist

def find_dist(x1, y1, x2, y2):
    deltax = x1-x2
    deltay = y1-y2
    dis = ((deltax)**2+(deltay)**2)**0.5
    return dis 

def find_error(test_data, pred_lst):
    error = 0 
    for i in range(len(test_data[2])):
        if  test_data[2][i] != pred_lst[i]:
            error += 1
    errorrate = error/len(test_data[2])*100
    return errorrate

def plot_data(train_data, test_data, pred_lst):
    turtle.up()
    turtle.goto(-500,0)
    turtle.down()
    turtle.goto(500,0)
    turtle.up()
    turtle.goto(0,-500)
    turtle.down()
    turtle.goto(0,500)
    turtle.up()
    turtle.goto(300,0)
    turtle.down()
    turtle.write("petal length", font= ("Arial",16,"normal"))
    turtle.up()
    turtle.goto(5,-350)
    turtle.down()
    turtle.write("petal width", font= ("Arial",16,"normal"))
    turtle.up()
    turtle.shape("circle")
    turtle.shapesize(0.5)
    for i in range(len(train_data[0])):
        turtle.goto(train_data[0][i]*175,train_data[1][i]*175)
        if train_data[2][i] == "Iris-setosa":
            turtle.color("blue")
        elif train_data[2][i] == "Iris-versicolor":
            turtle.color("green")
        else:
            turtle.color("orange")
        turtle.stamp()
    turtle.shape("square")
    for i in range(len(test_data[0])):
        turtle.goto(test_data[0][i]*175,test_data[1][i]*175)
        if test_data[2][i] == pred_lst[i]:
            if test_data[2][i] == "Iris-setosa":
                turtle.color("blue")
            elif test_data[2][i] == "Iris-versicolor":
                turtle.color("green")
            else:
                turtle.color("orange")
            turtle.stamp()
        else:
            turtle.color("red")
            turtle.stamp()
    draw_key()

def draw_key():
    turtle.up()
    legend_types = [["blue","Iris-setosa"],["green","Iris-versicolor"],["orange","Iris-virginica"]]
    legend_shapes = ["circle","square"]
    x1 = -300
    x2 = -285
    y1 = 350
    y2 = 343
    for shape in legend_shapes:
        turtle.shape(shape)
        if shape == "square":
                legend_types.append(["red","Incorrectly"])
        for lsts in legend_types:
            if shape == "square":
                lsts[1] = "predicted " + lsts[1]
            turtle.goto(x1,y1)
            turtle.color(lsts[0])
            turtle.stamp()
            turtle.goto(x2,y2)
            turtle.color("black")
            turtle.write(lsts[1],font= ("Arial",13,"normal"))
            y1 += -20
            y2 += -20
    turtle.color("red")
    turtle.goto(x1,y1+20)

def main():
    train_data = create_table("iris_train.csv")
    print_range_max_min(train_data[:2])
    print()
    normalize_data(train_data)
    test_data = create_table("iris_test.csv")
    print()
    normalize_data(test_data)
    pred_lst = make_predictions(train_data, test_data)
    error = find_error(test_data, pred_lst)
    print()
    print("The error percentage is: ", error)
    plot_data(train_data, test_data, pred_lst)
main()

