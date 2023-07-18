import pickle
import pandas as pd

ride = {
    "trip_distance": 1.5,
    "total_amount": 10,
}
X = pd.DataFrame(ride, index=[0])

def load_model(model_path="./../../models/lin_reg.bin"):
    with open(model_path, "rb") as f_in:
        return pickle.load(f_in)

model = load_model()

if __name__=="__main__":

    # print(X)

    print(model.predict(X)[0][0])
