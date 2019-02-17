import time
import sched

# self.sched = sched.scheduler(time.time, sleep_func)
# self.sched.enter(delay_seconds, 0, action, args)

def execute_something(name):
    print "Executing something: {}".format(name)

def scheduled_method(sched_obj):
    sched_obj.enter(4, 1, execute_something, argument=("Ayush",))
    sched_obj.run()
    scheduled_method(sched_obj)

def main():
    sched_obj = sched.scheduler(time.time, time.sleep)
    scheduled_method(sched_obj)



if __name__=='__main__':
    main()

# import sched, time
# s = sched.scheduler(time.time, time.sleep)
#
# def print_time(a='default'):
#     print("From print_time", time.time(), a)
#
# def print_some_times():
#     # s.enter(10, 1, print_time)
#     s.enter(5, 2, print_time, argument=('positional',))
#     s.enter(5, 1, print_time, argument=('positional1',))
#     # s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
#     s.run()
#
#
# if __name__=="__main__":
#     print_some_times()