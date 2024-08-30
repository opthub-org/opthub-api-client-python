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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from opthub_api_client.models.match_trial_evaluation import MatchTrialEvaluation
from opthub_api_client.models.match_trial_score import MatchTrialScore
from opthub_api_client.models.match_trial_status_type import MatchTrialStatusType
from typing import Optional, Set
from typing_extensions import Self

class MatchTrialStatus(BaseModel):
    """
    Match Trial status information
    """ # noqa: E501
    match_trial_status_type: Optional[MatchTrialStatusType] = None
    evaluation: Optional[MatchTrialEvaluation] = None
    score: Optional[MatchTrialScore] = None
    __properties: ClassVar[List[str]] = ["match_trial_status_type", "evaluation", "score"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MatchTrialStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of evaluation
        if self.evaluation:
            _dict['evaluation'] = self.evaluation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchTrialStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "match_trial_status_type": obj.get("match_trial_status_type"),
            "evaluation": MatchTrialEvaluation.from_dict(obj["evaluation"]) if obj.get("evaluation") is not None else None,
            "score": MatchTrialScore.from_dict(obj["score"]) if obj.get("score") is not None else None
        })
        return _obj


