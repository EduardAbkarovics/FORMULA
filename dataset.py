import random

class dataset:
    def __init__(self):
        # WEIGHTS

        self.From_Weights = -0.01
        self.To_Weights = 0.01
        # INPUTS
        self.From_Inputs = 0
        self.To_Inputs = 1

    def Generate_Random_Weights(self):
        from_to = random.uniform(self.From_Weights, self.To_Weights)
        print(from_to)
        return from_to

    def Generate_Random_Inputs(self):
        from_to = random.uniform(self.From_Inputs, self.To_Inputs)
        print(from_to)
        return from_to
