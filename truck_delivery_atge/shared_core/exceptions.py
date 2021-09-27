class CustomException(Exception):
    """class is grouping Timeout and connection error"""
    pass


class DataNotAvailableException(Exception):
    def __init__(self, msg, custom_param):
        self.custom_param = custom_param
        if self.custom_param == "something":
            self.message = f"{msg}- more specific"
        super(DataNotAvailableException, self).__init__(msg)

    def __reduce__(self):
        return (DataNotAvailableException,
                (self.message, self.custom_param))


class EnvNotAvailableException(Exception):
    def __init__(self, msg):
        self.message = msg
        super(EnvNotAvailableException, self).__init__(msg)

    def __reduce__(self):
        return (EnvNotAvailableException,
                self.message)


