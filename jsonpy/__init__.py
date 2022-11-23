"""
this small project follows and implements `JSON schema <http://json-schema.org>`_.

Supports only for Python 3.3 and higher
"""

from .exceptions import JsonSchemaException
from .generator import CodeGenerator

__all__ = ('JsonSchemaException', 'compile_func')


def compile_func(definition):
    """
    Generates a validation function for validating the JSON schema bu definition
    """

    code_generator = CodeGenerator(definition)
    local_state = {}
    exec(code_generator.func_code, code_generator.global_state, local_state)
    return local_state['func']
