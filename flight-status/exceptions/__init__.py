class CustomErrors(Exception):
    status_code = 500

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message

        if status_code:
            self.status_code = status_code
