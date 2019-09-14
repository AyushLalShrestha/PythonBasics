
import logging as log
import time
from apscheduler.scheduler import Scheduler
from pylib.logger import setup_filelogger
ayush_logger = setup_filelogger("sched_test")

def iterative_function():
    ayush_logger.warning("Now running iteration")
    try:
        with open("/tmp/sched_test.txt", "a") as fh:
            fh.write("Written at: {}".format(time.time()))
    except Exception as ex:
        ayush_logger.warning(ex)


def add_cron_job(scheduler_obj, func, args, run_at):
    # scheduler_obj.add_cron_job(
    #     func,
    #     args=args,
    #     name="sched_test",
    #     start_date=None,
    #     coalesce=True,
    #     misfire_grace_time=60,
    #     max_instances=2,
    #     **run_at
    # )
    ayush_logger.warning("added the cron_job")


if __name__=='__main__':
    sched_obj = Scheduler()
    sched_obj.start()
    run_at ={"hour": "*", "minute": 56, "second": 0}
    args = []
    # add_cron_job(sched_obj, iterative_function, args, run_at)

    sched.add_cron_job(
        iterative_function,
        month='6-12',
        day_of_week='mon-fri',
        hour=5,
        minute=30)
    print("DONE")

