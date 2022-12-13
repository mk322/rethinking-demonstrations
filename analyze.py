import pickle


path = "out/gpt-j"

file = "out/gpt-j/glue-sst5-test-direct-k=16-s=13.pkl"

with open(file, "rb") as f:
    output = pickle.load(f)
    print(output)