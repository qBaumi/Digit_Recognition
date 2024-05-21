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

    train_perceptron(my_perceptron)

    #with open('weights.json', 'w') as f:
    #    json.dump(p1.weights, f)

    

def train_perceptron(p1):
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    for key in data:
        for i in range(10000):
            for image in data[key]:
                list_of_pixels = []
                for row in image:
                    list_of_pixels += row
                if str(p1.desired_number) == str(key):
                    p1.train(list_of_pixels, 1)
                else:
                    p1.train(list_of_pixels, 0)

            

main()
