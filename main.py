from analyze import analyzecode

file_path = "test.py"

def loadcode():
    with open("test.py", "r") as f:
        return f.read()

loadedcode = loadcode()
length = analyzecode(loadedcode)
print (length)





