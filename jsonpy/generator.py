import collections
import re

from .exceptions import JsonSchemaException


class CodeGenerator:
    """
    This class generates code of validation function from JSON schema object as string.
    """

    INDENT = 4
    JSON_TYPE_TO_PYTHON_TYPE = {
        'null': 'NoneType',
        "boolean": 'bool',
        'number': 'int',
        'integer': 'int',
        'string': 'str',
        'array': 'list',
        'object': 'dict'
    }
