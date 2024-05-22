class Perceptron:
    def __init__(self, weights, desired_number, learningrate = 0.0005):
        self.weights = weights
        self.learningrate = learningrate
        self.bias = 1
        self.desired_number = desired_number

    def activate(self, inputs):
        sum = 0
        for i ,number in enumerate(inputs):
            sum += number*self.weights[i-1]
        if sum > 0:
            return 1
        return 0
    def train(self, inputs, desired):
        inputs.append(self.bias);
        guess = self.activate(inputs);
        error = desired - guess;
        if error != 0:
            for i, number in enumerate(inputs):
                if number == 0:
                    number = -1
                self.weights[i-1] += self.learningrate * error * number;
        