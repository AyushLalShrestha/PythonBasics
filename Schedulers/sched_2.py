import time
import sched

# self.sched = sched.scheduler(time.time, sleep_func)
# self.sched.enter(delay_seconds, 0, action, args)

def do_something(alert_name):
    print "Do something for alert: {}".format(alert_name)


def scheduled_method(sched_obj, alert, wait_time):
    do_something(alert)
    sched_obj.enter(wait_time, 0, scheduled_method, argument=(sched_obj, alert, wait_time ))


def main():
    sched_obj = sched.scheduler(time.time, time.sleep)
    sched_obj.run()

    print "waiting for 2 seconds"
    time.sleep(5)

    alerts = ['alert_1', 'alert_2', 'alert_3']
    for alert in alerts:
        scheduled_method(sched_obj, alert, 4)
    sched_obj.run()


if __name__=="__main__":
    main()
