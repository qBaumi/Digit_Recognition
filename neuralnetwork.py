import json
import random
import threading
from perceptron import Perceptron

class neuralnetwork():
    def __init__(self):
        self.perceptrons = []
        for i in range(10):
            new_perceptron = Perceptron(self.get_weights(i), str(i))
            self.perceptrons.append(new_perceptron)

    def guess_number(self, pixel_array):
        my_str = f""
        for perceptron in self.perceptrons:
            my_str += f"{perceptron.desired_number} : {perceptron.activate(pixel_array)} | "
        print(my_str)

    def train_and_save(self):
        with open('weights.json', 'r') as f:
            saved_weights = json.load(f)

        thread_list = []
        for perceptron in self.perceptrons:
            th = threading.Thread(target=train_perceptron, args=(perceptron,))
            thread_list.append(th)
            th.start()
        for th in thread_list:
            th.join()
        for perceptron in self.perceptrons:
            saved_weights[str(perceptron.desired_number)] = perceptron.weights
        with open('weights.json', 'w') as f:
            json.dump(saved_weights, f)

    def get_random_weights(self):
        randomweights = []
        for i in range(784):
            randomweights.append(random.random()*2-1)
        return randomweights

    def get_weights(self, number):
        number = str(number)
        with open('weights.json', 'r') as f:
            saved_weights = json.load(f)
        if saved_weights[number] == []:
            return self.get_random_weights()
        return saved_weights[number]
    
def train_perceptron(perceptron):
    with open('data.json', 'r') as f:
        data = json.load(f)
    thread_list = []

    def train_number_perceptron(number_to_train):
        for i in range(3000):
            print(i)
            for image in data[number_to_train]:
                list_of_pixels = []
                for row in image:
                    list_of_pixels += row
                if str(perceptron.desired_number) == str(number_to_train):
                    perceptron.train(list_of_pixels, 1)
                else:
                    perceptron.train(list_of_pixels, 0)

    for key in data:
        th = threading.Thread(target=train_number_perceptron, args=(key,))
        thread_list.append(th)
        th.start()
    for th in thread_list:
        th.join()