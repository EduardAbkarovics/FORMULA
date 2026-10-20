import random


From: float = -0.01
To: float = 0.01

def Generate_Random_Weights(From,To) -> float:
    from_to = random.uniform(From ,To)
    print(from_to) 

Generate_Random_Weights(From,To)



