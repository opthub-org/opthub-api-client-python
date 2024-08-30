# coding: utf-8

"""
    OptHub REST API

    OptHub Public REST API.

    The version of the OpenAPI document: 0.2.0
    Contact: dev@opthub.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MatchTrialStatusType(str, Enum):
    """
    Types of trial status.
    """

    """
    allowed enum values
    """
    SUCCESS = 'Success'
    SCORING = 'Scoring'
    EVALUATING = 'Evaluating'
    SCORERFAILED = 'ScorerFailed'
    EVALUATORFAILED = 'EvaluatorFailed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MatchTrialStatusType from a JSON string"""
        return cls(json.loads(json_str))


