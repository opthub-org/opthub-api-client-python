# coding: utf-8

"""
    OptHub REST API

    OptHub Public REST API.

    The version of the OpenAPI document: 0.3.0
    Contact: dev@opthub.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RunnerStatus(str, Enum):
    """
    Status of the Trial
    """

    """
    allowed enum values
    """
    SUCCESS = 'Success'
    FAILED = 'Failed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RunnerStatus from a JSON string"""
        return cls(json.loads(json_str))


