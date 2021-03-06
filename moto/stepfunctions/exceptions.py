from __future__ import unicode_literals
import json


class AWSError(Exception):
    TYPE = None
    STATUS = 400

    def __init__(self, message, type=None, status=None):
        self.message = message
        self.type = type if type is not None else self.TYPE
        self.status = status if status is not None else self.STATUS

    def response(self):
        return (
            json.dumps({"__type": self.type, "message": self.message}),
            dict(status=self.status),
        )


class ExecutionAlreadyExists(AWSError):
    TYPE = "ExecutionAlreadyExists"
    STATUS = 400


class ExecutionDoesNotExist(AWSError):
    TYPE = "ExecutionDoesNotExist"
    STATUS = 400


class InvalidArn(AWSError):
    TYPE = "InvalidArn"
    STATUS = 400


class InvalidName(AWSError):
    TYPE = "InvalidName"
    STATUS = 400


class InvalidExecutionInput(AWSError):
    TYPE = "InvalidExecutionInput"
    STATUS = 400


class StateMachineDoesNotExist(AWSError):
    TYPE = "StateMachineDoesNotExist"
    STATUS = 400


class InvalidToken(AWSError):
    TYPE = "InvalidToken"
    STATUS = 400

    def __init__(self, message="Invalid token"):
        super(InvalidToken, self).__init__("Invalid Token: {}".format(message))


class ResourceNotFound(AWSError):
    TYPE = "ResourceNotFound"
    STATUS = 400

    def __init__(self, arn):
        super(ResourceNotFound, self).__init__("Resource not found: '{}'".format(arn))
