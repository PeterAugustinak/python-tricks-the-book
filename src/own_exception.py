"""4.3 Defining your own exception classes"""

# user defined BASE exception class
class BaseValidationError(ValueError):
    pass

# user defined Validation errors inherited from common base Validation
# Error class
class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass


def validate(name):
    if len(name) < 3:
        raise NameTooShortError(name)
    elif len(name) > 8:
        raise NameTooLongError(name)


try:
    validate("Pe")
except NameTooShortError as err:
    print(f'Name too short: {err}!')

try:
    validate("PeterPeter")
except NameTooLongError as err:
    print(f'Name too long: {err}!')
