from logging import getLevelNamesMapping, log


LOG_LEVELS = getLevelNamesMapping()


def log_message(message="", level="INFO"):
    if message:
        log(LOG_LEVELS[level.upper()], message)


def log_except(e: Exception, message=""):
    message = message or "Unexpected exception occurred: "
    message += e.args[0] if e.args else e.msg
    log_message(message, level="ERROR")
