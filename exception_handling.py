

def some_func(*args, **kwargs):
    print kwargs["marks"][-1]



def main():
    try:
        person = {'name': 'Ayush', marks:[]}
        some_func(**person)
    except KeyError as ke:
        print ke

    # print "No Finally!" #1
    finally: #2
        print "Finally!!"

    # Hence, finally block will run no matter if the actual exception is actually handled or not


if __name__=="__main__":
    main()