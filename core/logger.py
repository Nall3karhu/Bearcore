from core.event_logger import add_event



class Logger:


    def info(self, message):

        try:

            add_event(
                f"INFO: {message}"
            )

        except Exception:

            pass



    def error(self, message):

        try:

            add_event(
                f"ERROR: {message}"
            )

        except Exception:

            pass



    def warning(self, message):

        try:

            add_event(
                f"WARNING: {message}"
            )

        except Exception:

            pass



    def debug(self, message):

        try:

            add_event(
                f"DEBUG: {message}"
            )

        except Exception:

            pass



logger = Logger()



def log(message):

    logger.info(
        message
    )