from logger import Logger


logger = Logger.get_instance()

logger.log_info("my my, what an info")
logger.log_warning("oh no, you've done it again!")
logger.log_error("RUN, PROGRAM, RUN!!!")

log_history = logger.get_log_history()

for message in log_history:
    print(message)
