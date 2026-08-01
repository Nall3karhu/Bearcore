from core.event_logger import add_event


def log(message):

    try:

        add_event(
            message
        )

    except Exception:

        pass