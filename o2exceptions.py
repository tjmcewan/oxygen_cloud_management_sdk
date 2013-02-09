import os, sys, inspect
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"gen-py")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

from errors.ttypes import *

class O2ReasonCode:
    UNEXPECTED_ERROR = 1
    UPGRADE_REQUIRED = 2
    OPERATION_INVALID_BETWEEN_SPACES = 3
    INVALID_KEY = 4
    OBJECT_NOT_FOUND = 5
    PERMISSION_DENIED = 6
    SESSION_EXPIRED = 7
    SESSION_NOT_FOUND = 8
    LOCAL_FILE_NOT_FOUND = 9
    OPERATION_INVALID_ON_A_FILE_OBJECT = 10
    DEVICE_BLACKLISTED = 11
    DEVICE_NOT_REGISTERED = 12
    DEVICE_ID_REQUIRED = 13
    API_KEY_REQUIRED = 14
    MISSING_REQUIRED_ARGUMENT = 15
    INVALID_USAGE = 16
    UNABLE_TO_CONNECT_TO_API_GATEWAY = 17
    UNABLE_TO_CONNECT_TO_SERVER = 18
    STORAGE_LIMIT_EXCEEDED = 19
    OBJECT_DELETED = 20
    DUPLICATE_OBJECT = 21
    SUBSCRIPTION_VIOLATION = 22
    USER_ACCOUNT_LOCKED = 23
    INSUFFICIENT_STORAGE = 24
    USER_LIMIT_EXCEEDED = 25
    INVALID_CREDENTIALS = 26
    INVALID_FORMAT = 27
    USER_DISABLED = 28
    USER_DELETED = 29
    USER_NOT_ACTIVATED = 30
    USER_NOT_FOUND = 31
    INVALID_ACTIVATION_CODE = 32
    INVALID_AUTHENTICATION_TOKEN_ID = 33
    _reasoncodes_to_names = {1: 'UNEXPECTED_ERROR',
     2: 'UPGRADE_REQUIRED',
     3: 'OPERATION_INVALID_BETWEEN_SPACES',
     4: 'INVALID_KEY',
     5: 'OBJECT_NOT_FOUND',
     6: 'PERMISSION_DENIED',
     7: 'SESSION_EXPIRED',
     8: 'SESSION_NOT_FOUND',
     9: 'LOCAL_FILE_NOT_FOUND',
     10: 'OPERATION_INVALID_ON_A_FILE_OBJECT',
     11: 'DEVICE_BLACKLISTED',
     12: 'DEVICE_NOT_REGISTERED',
     13: 'DEVICE_ID_REQUIRED',
     14: 'API_KEY_REQUIRED',
     15: 'MISSING_REQUIRED_ARGUMENT',
     16: 'INVALID_USAGE',
     17: 'UNABLE_TO_CONNECT_TO_API_GATEWAY',
     18: 'UNABLE_TO_CONNECT_TO_SERVER',
     19: 'STORAGE_LIMIT_EXCEEDED',
     20: 'OBJECT_DELETED',
     21: 'DUPLICATE_OBJECT',
     22: 'SUBSCRIPTION_VIOLATION',
     23: 'USER_ACCOUNT_LOCKED',
     24: 'INSUFFICIENT_STORAGE',
     25: 'USER_LIMIT_EXCEEDED',
     26: 'INVALID_CREDENTIALS',
     27: 'INVALID_FORMAT',
     28: 'USER_DISABLED',
     29: 'USER_DELETED',
     30: 'USER_NOT_ACTIVATED',
     31: 'USER_NOT_FOUND',
     32: 'INVALID_ACTIVATION_CODE',
     33: 'INVALID_AUTHENTICATION_TOKEN_ID'}


class O2Exception(BaseException):
    pass


class O2InvalidInputError(O2Exception):

    def __init__(self, message, reason_code):
        self.message = message
        self.reason_code = reason_code


class O2RuleError(O2Exception):

    def __init__(self, message, reason_code):
        self.message = message
        self.reason_code = reason_code


class O2SystemError(O2Exception):

    def __init__(self, message, reason_code):
        self.message = message
        self.reason_code = reason_code


class O2InvalidSessionError(O2RuleError):

    def __init__(self, message, reason_code):
        self.message = message
        self.reason_code = reason_code


class O2NetworkError(O2SystemError):

    def __init__(self, message, reason_code):
        self.message = message
        self.reason_code = reason_code


class O2UnexpectedError(O2Exception):

    def __init__(self, message):
        self.message = message
        self.reason_code = O2ReasonCode.UNEXPECTED_ERROR


def handle_exception(e):
    try:
        raise e
    except EOFError:
        raise O2SystemError('Could not connect to Oxygen API.', O2ReasonCode.UNABLE_TO_CONNECT_TO_API_GATEWAY)
    except ApiRuleException as arx:
        while switch(arx.errorCode):
            if case(ApiRuleErrorCode.ACCOUNT_EXTERNAL_AUTHENTICATION_DISABLED):
                raise O2RuleError('External authentication has been disabled for this account.', O2ReasonCode.PERMISSION_DENIED)
            if case(ApiRuleErrorCode.ACCOUNT_INTERNAL_AUTHENTICATION_DISABLED):
                raise O2RuleError('Internal authentication has been disabled for this account.', O2ReasonCode.PERMISSION_DENIED)
            if case(ApiRuleErrorCode.ACTIVATION_CODE_REACHED_MAXIMUM_NUMBER_OF_USES):
                raise O2RuleError('Cannot create additional users. Activation Code has expired.', O2ReasonCode.USER_LIMIT_EXCEEDED)
            if case(ApiRuleErrorCode.INVALID_API_KEY):
                raise O2RuleError('Invalid API Key.', O2ReasonCode.INVALID_KEY)
            if case(ApiRuleErrorCode.PERMISSION_DENIED):
                raise O2RuleError('Permission Denied. This action is not allowed.', O2ReasonCode.PERMISSION_DENIED)
            if case(ApiRuleErrorCode.POSSIBLE_SECURITY_ATTACK):
                raise O2RuleError('Permission Denied. This action is not allowed.', O2ReasonCode.PERMISSION_DENIED)
            if case(ApiRuleErrorCode.SUBSCRIPTION_VIOLATION):
                raise O2RuleError('Permission Denied. This action is not allowed for this user.', O2ReasonCode.PERMISSION_DENIED)
            if case(ApiRuleErrorCode.USER_ACCOUNT_LOCKED):
                raise O2RuleError('User account is locked.', O2ReasonCode.USER_ACCOUNT_LOCKED)
            if case(ApiRuleErrorCode.USER_CANNOT_LOGIN):
                raise O2RuleError('Cannot login due to an unexpected error.', O2ReasonCode.UNEXPECTED_ERROR)
            if case(ApiRuleErrorCode.USER_CREATION_FAILED_ON_INSUFFICIENT_STORAGE):
                raise O2RuleError('Cannot create user due to insufficient storage.', O2ReasonCode.INSUFFICIENT_STORAGE)
            if case(ApiRuleErrorCode.USER_DISABLED_FOR_AUTHENTICATED_EXTERNAL_LOGIN):
                raise O2RuleError('External authentication has been disabled for this user.', O2ReasonCode.PERMISSION_DENIED)
            if case(ApiRuleErrorCode.USER_LIMIT_EXCEEDED):
                raise O2RuleError('User limit exceeded. No more users can be created.', O2ReasonCode.USER_LIMIT_EXCEEDED)
            if case(ApiRuleErrorCode.USER_NOT_ACTIVATED_FOR_AUTHENTICATED_EXTERNAL_LOGIN):
                raise O2RuleError('Permission Denied. User not activated for external login.', O2ReasonCode.PERMISSION_DENIED)
            if case(ApiRuleErrorCode.USER_NOT_FOUND_FOR_AUTHENTICATED_EXTERNAL_LOGIN):
                raise O2RuleError('Permission Denied. User not found for external login.', O2ReasonCode.PERMISSION_DENIED)
            if case(ApiRuleErrorCode.DEVICE_BLACKLISTED):
                raise O2RuleError('Device has been blacklisted.', O2ReasonCode.DEVICE_BLACKLISTED)
            if case(ApiRuleErrorCode.DEVICE_NOT_REGISTERED):
                raise O2RuleError('Device has not been registered.', O2ReasonCode.DEVICE_NOT_REGISTERED)
            if case(ApiRuleErrorCode.LDAP_USER_NOT_MAPPED):
                raise O2RuleError('User has not been mapped.', O2ReasonCode.UNEXPECTED_ERROR)
            if case(ApiRuleErrorCode.API_KEY_AND_DEVICE_TYPE_MISMATCH):
                raise O2RuleError('Permission Denied. Your API key was not registered for this device. Please contact support.oxygencloud.com', O2ReasonCode.PERMISSION_DENIED)
            if case():
                raise O2UnexpectedError('Unknown ApiRuleException errorCode. Please update your Python SDK.')

    except ApiInvalidInputException as aiix:
        while switch(aiix.errorCode):
            if case(ApiInvalidInputErrorCode.ACCOUNT_ID_IS_REQUIRED):
                raise O2InvalidInputError('An account ID is required to perform this action.', O2ReasonCode.MISSING_REQUIRED_ARGUMENT)
            if case(ApiInvalidInputErrorCode.INVALID_ACCOUNT_ID):
                raise O2InvalidInputError('Please specify a valid account ID.', O2ReasonCode.OBJECT_NOT_FOUND)
            if case(ApiInvalidInputErrorCode.INVALID_ACCOUNT_ID_OR_EMAIL):
                raise O2InvalidInputError('Invalid account ID or email.', O2ReasonCode.OBJECT_NOT_FOUND)
            if case(ApiInvalidInputErrorCode.INVALID_ACCOUNT_ID_OR_LOGIN_ID):
                raise O2InvalidInputError('Invalid account ID or login Id.', O2ReasonCode.OBJECT_NOT_FOUND)
            if case(ApiInvalidInputErrorCode.INVALID_EMAIL):
                raise O2InvalidInputError('Invalid email.', O2ReasonCode.INVALID_FORMAT)
            if case(ApiInvalidInputErrorCode.INVALID_LOGIN_CREDENTIALS_INFORMATION):
                raise O2InvalidInputError('Invalid credentials.', O2ReasonCode.INVALID_CREDENTIALS)
            if case(ApiInvalidInputErrorCode.INVALID_LOGIN_ID):
                raise O2InvalidInputError('Invalid format or characters.', O2ReasonCode.INVALID_FORMAT)
            if case(ApiInvalidInputErrorCode.INVALID_LOGIN_ID_OR_PASSWORD):
                raise O2InvalidInputError('Invalid format or characters.', O2ReasonCode.INVALID_FORMAT)
            if case(ApiInvalidInputErrorCode.INVALID_NAME):
                raise O2InvalidInputError('Invalid format. Please specify a valid name.', O2ReasonCode.INVALID_FORMAT)
            if case(ApiInvalidInputErrorCode.INVALID_PASSWORD_FORMAT):
                raise O2InvalidInputError('Invalid format. Please specify a valid password.', O2ReasonCode.INVALID_FORMAT)
            if case(ApiInvalidInputErrorCode.LOGIN_ID_IS_ALREADY_TAKEN):
                raise O2InvalidInputError('Login ID is already taken.', O2ReasonCode.DUPLICATE_OBJECT)
            if case(ApiInvalidInputErrorCode.PRECONDITION_FAILED):
                raise O2InvalidInputError('Missing a required argument. Please see documentation.', O2ReasonCode.MISSING_REQUIRED_ARGUMENT)
            if case():
                raise O2UnexpectedError('Unknown ApiInvalidInputException errorCode. Please update your Python SDK.')

    except ApiSystemsException as asx:
        while switch(asx.errorCode):
            if case(ApiSystemsErrorCode.ACCOUNT_IS_DELETED):
                raise O2SystemError('Cannot perform action. Account is deleted.', O2ReasonCode.USER_DELETED)
            if case(ApiSystemsErrorCode.ACCOUNT_IS_DISABLED):
                raise O2SystemError('Cannot perform action. Account is disabled.', O2ReasonCode.USER_DISABLED)
            if case(ApiSystemsErrorCode.DUPLICATE_ENTRY):
                raise O2SystemError('This object already exists.', O2ReasonCode.DUPLICATE_OBJECT)
            if case(ApiSystemsErrorCode.OBJECT_ALREADY_DELETED):
                raise O2SystemError('This object is deleted.', O2ReasonCode.OBJECT_DELETED)
            if case(ApiSystemsErrorCode.OBJECT_NOT_FOUND):
                raise O2SystemError('This object could not be found.', O2ReasonCode.OBJECT_NOT_FOUND)
            if case(ApiSystemsErrorCode.STORAGE_LIMIT_EXCEEDED):
                raise O2SystemError('Insufficient Storage.', O2ReasonCode.INSUFFICIENT_STORAGE)
            if case(ApiSystemsErrorCode.USER_ALREADY_DELETED_OR_DISABLED):
                raise O2SystemError('User already deleted', O2ReasonCode.USER_DELETED)
            if case(ApiSystemsErrorCode.USER_ALREADY_EXISTS):
                raise O2SystemError('User already exists.', O2ReasonCode.DUPLICATE_OBJECT)
            if case(ApiSystemsErrorCode.USER_IS_DELETED):
                raise O2SystemError('User is deleted.', O2ReasonCode.USER_DELETED)
            if case(ApiSystemsErrorCode.USER_IS_DISABLED):
                raise O2SystemError('User is disabled.', O2ReasonCode.USER_DISABLED)
            if case(ApiSystemsErrorCode.USER_IS_NOT_ACTIVATED):
                raise O2SystemError('User is not activated.', O2ReasonCode.USER_NOT_ACTIVATED)
            if case(ApiSystemsErrorCode.USER_NOT_FOUND):
                raise O2SystemError('User not found.', O2ReasonCode.USER_NOT_FOUND)
            if case(ApiSystemsErrorCode.CONNECTION_EXCEPTION):
                raise O2SystemError('Could not connect to server.', O2ReasonCode.UNABLE_TO_CONNECT_TO_SERVER)
            if case(ApiSystemsErrorCode.INVALID_ACTIVATION_CODE):
                raise O2SystemError('Invalid activation code.', O2ReasonCode.INVALID_ACTIVATION_CODE)
            if case(ApiSystemsErrorCode.INVALID_AUTHENTICATION_TOKEN_ID):
                raise O2SystemError('Invalid authentication token.', O2ReasonCode.INVALID_AUTHENTICATION_TOKEN_ID)
            if case(ApiSystemsErrorCode.INVALID_LOGIN_URL):
                raise O2SystemError('Invalid login URL.', O2ReasonCode.OBJECT_NOT_FOUND)
            if case(ApiSystemsErrorCode.UPGRADE_REQUIRED):
                raise O2SystemError('New features have been released. Please update your Python SDK and implement new features.', O2ReasonCode.UPGRADE_REQUIRED)
            if case():
                raise O2UnexpectedError('Unknown ApiSystemsException errorCode. Please update your Python SDK.')

    except ApiSessionException as asx:
        while switch(asx.errorCode):
            if case(ApiSessionErrorCode.INVALID_USER_SESSION_ID):
                raise O2InvalidSessionError('Invalid session.', O2ReasonCode.SESSION_NOT_FOUND)
            if case(ApiSessionErrorCode.USER_SESSION_EXPIRED):
                raise O2InvalidSessionError('Session expired.', O2ReasonCode.SESSION_EXPIRED)
            if case(ApiSessionErrorCode.USER_SESSION_NOT_FOUND):
                raise O2InvalidSessionError('Invalid session.', O2ReasonCode.SESSION_NOT_FOUND)
            if case():
                raise O2UnexpectedError('Unknown ApiSessionException errorCode. Please update your Python SDK.')

    except ApiUnexpectedException as aue:
        raise O2UnexpectedError('An unexpected error occurred.')


class switch(object):
    value = None

    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == switch.value for arg in args))
