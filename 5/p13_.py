class raises:
    def __init__(self, exception_type):
        self.exception_type = exception_type
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type is None:
            raise self.exception_type(
                f'Expected exception {self.exception_type.__name__}, bun no exception was raised')
        if not issubclass(exception_type, self.exception_type):
            return False
        self.exception = exception_value
        return True


class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


# with raises(MealyError) as e:
#     raise MealyError('Error happend')
# assert str(e.exception) == 'Error happend'
