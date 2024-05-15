import __main__
import json
import random
import perceptron

def main():
    randomweights = []
    for i in range(784):
        randomweights.append(random.random()*2-1)

    with open('weights.json', 'r') as f:
        saved_weights = json.load(f)
    
    my_perceptron = perceptron.Perceptron(saved_weights)


    #with open('weights.json', 'w') as f:
    #    json.dump(p1.weights, f)
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    list_of_zeros = data["0"]
    list_of_ones = data["1"]
    list_of_pixels = []
    for row in list_of_ones[0]:
        list_of_pixels += row
    print(my_perceptron.activate(list_of_pixels))
main()

def train_perceptron(p1):
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    list_of_zeros = data["0"]
    list_of_ones = data["1"]
    for i in range(10000):
        for image in list_of_zeros:
            list_of_pixels = []
            for row in image:
                list_of_pixels += row
            #print(len(list_of_pixels))
            #print(len(p1.weights))
            p1.train(list_of_pixels, 0)
        
        for image in list_of_ones:
            list_of_pixels = []
            for row in image:
                list_of_pixels += row
            p1.train(list_of_pixels, 1)
