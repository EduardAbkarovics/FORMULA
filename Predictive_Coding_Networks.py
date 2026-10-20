from dataset import  dataset
ds = dataset()
weight = ds.Generate_Random_Weights()
inputs = ds.Generate_Random_Inputs()

class main:
    def __init__(self):
        pass

    def prediction(self, weight, inputs):
        prediction = weight * inputs
        return prediction

    def mistake(self, prediction, inputs):
        mistake = inputs - prediction
        return mistake


model = main()
learning_rate = 0.1

for i in range(500):
    pred = model.prediction(weight, inputs)
    err = model.mistake(pred, inputs)

    # Súly frissítése
    weight = weight + (learning_rate * err * inputs)

    print(f"{i+1}. lépés | Jóslat: {pred:.4f} | Hiba: {err:.4f} | Új súly: {weight:.4f}")         


