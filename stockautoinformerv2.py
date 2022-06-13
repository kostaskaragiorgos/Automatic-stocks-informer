import pickle

try:
    file = open('kostas', 'rb')
    p = pickle.load(file)
    file.close()
except:
    print("There is no such file")
