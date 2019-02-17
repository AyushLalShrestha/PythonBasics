import multiprocessing


def f1(**kwargs):
    print kwargs

kwargs = {"name": "Ayush", "l_name": "Shrestha"}

print("launching a new process")
new_p = multiprocessing.Process(target=f1, kwargs=kwargs)
new_p.start()
new_p.join()
print("launching a new process {}".format(new_p.pid))

