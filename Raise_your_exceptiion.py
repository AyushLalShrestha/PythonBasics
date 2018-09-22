

class Ayusherror(Exception):

	def __init__(self, message, *args):
	    self.message = message
	    
	    super(Ayusherror, self).__init__(message, *args) 

def some_method():
    try:
        execute_method()

    except Ayusherror as ve:
    	print str(ve)

    
def execute_method():
    raise Ayusherror("Ayush Value Ayuh")
    print "After the error has been raised"

def main():
    some_method()

if __name__=='__main__':
    main()
