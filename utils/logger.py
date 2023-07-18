import logging

logging.basicConfig(filename="geckodriver.log", level=logging.DEBUG)


def log_message(message="", level="info"):
    if message:
        eval(f"logging.{level.lower()}(message)")
        log_blue(message)


def log_except(e: Exception, message=""):
    message = message or "Unexpected exception occurred: "
    message += e.args[0] if e.args else e.msg
    log_message(message, level="ERROR")
    log_red(message)


def log_blue(text):
    print(f'\033[94m\n\n{text} \n\n\033[0m')


def log_red(text):
    print(f'\033[91m\n\n{text} \n\n\033[0m')
