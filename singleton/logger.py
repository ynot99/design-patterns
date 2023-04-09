import datetime


class Logger:
    __instance = None

    @staticmethod
    def get_instance() -> "Logger":
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def __init__(self) -> None:
        if Logger.__instance is not None:
            raise Exception(
                "Logger class is a singleton, use get_instance() to get the instance"
            )
        Logger.__instance = self
        self.__log_history: list[str] = []

    def log_info(self, message: str) -> None:
        self.__log("INFO", message)

    def log_warning(self, message: str) -> None:
        self.__log("WARNING", message)

    def log_error(self, message: str) -> None:
        self.__log("ERROR", message)

    def __log(self, log_level: str, message: str) -> None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = "{} [{}]: {}".format(timestamp, log_level, message)
        self.__log_history.append(log_entry)

    def get_log_history(self) -> list[str]:
        return self.__log_history
