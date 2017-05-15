str_1 = "Ayush"

for method in dir(str_1):
    if method.startswith("__") & method.endswith("__"):
        continue
    print(method)




