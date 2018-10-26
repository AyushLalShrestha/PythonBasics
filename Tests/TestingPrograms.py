# number = 3
# prime_count = 1
# prime_number = 0
# ex = 0
# while ex != 1:
#     print("For the number " + str(number))
#     count = 0
#     for i in range(2, int(number/2)+1):
#         if (number % i == 0):
#             count = 1
#             break
#     if count == 0:
#         prime_count = prime_count + 1
#         prime_number = number
#         print(str(prime_count) + "th prime number is -------------- " + str(prime_number))
#         if prime_count == 6:
#             print(prime_number)
#             ex = 1
#
#     number += 1
import gevent
import time

class Person():
    def __init__(self):
        self.number = 0
        self.count = 0

    def return_number_if_count_5(self):
        print "In method"
        time.sleep(5)
        return 1

def main():
    person = Person()
    response = gevent.with_timeout(3, person.return_number_if_count_5, timeout_value=3)
    if response>0:
        print "Some result came out"
    else:
        print "No results :("

    print "End of Main"


if __name__=="__main__":
    main()


