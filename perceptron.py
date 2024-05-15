class Perceptron:
    def __init__(self, weights, learningrate = 0.0005):
        self.weights = weights
        self.learningrate = learningrate
        self.bias = 1

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
                self.weights[i-1] += self.learningrate * error * number;
        