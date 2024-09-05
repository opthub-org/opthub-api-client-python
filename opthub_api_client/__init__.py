# coding: utf-8

# flake8: noqa

"""
    OptHub REST API

    OptHub Public REST API.

    The version of the OpenAPI document: 0.3.0
    Contact: dev@opthub.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from opthub_api_client.api.match_trials_api import MatchTrialsApi

# import ApiClient
from opthub_api_client.api_response import ApiResponse
from opthub_api_client.api_client import ApiClient
from opthub_api_client.configuration import Configuration
from opthub_api_client.exceptions import OpenApiException
from opthub_api_client.exceptions import ApiTypeError
from opthub_api_client.exceptions import ApiValueError
from opthub_api_client.exceptions import ApiKeyError
from opthub_api_client.exceptions import ApiAttributeError
from opthub_api_client.exceptions import ApiException

# import models into sdk package
from opthub_api_client.models.auth_error_code import AuthErrorCode
from opthub_api_client.models.auth_error_response import AuthErrorResponse
from opthub_api_client.models.create_match_trial400_response import CreateMatchTrial400Response
from opthub_api_client.models.create_match_trial403_response import CreateMatchTrial403Response
from opthub_api_client.models.create_match_trial404_response import CreateMatchTrial404Response
from opthub_api_client.models.create_match_trial_request import CreateMatchTrialRequest
from opthub_api_client.models.get_match_evaluation404_response import GetMatchEvaluation404Response
from opthub_api_client.models.get_match_score404_response import GetMatchScore404Response
from opthub_api_client.models.get_match_trial403_response import GetMatchTrial403Response
from opthub_api_client.models.get_match_trial404_response import GetMatchTrial404Response
from opthub_api_client.models.get_solution404_response import GetSolution404Response
from opthub_api_client.models.match_trial_evaluation import MatchTrialEvaluation
from opthub_api_client.models.match_trial_response import MatchTrialResponse
from opthub_api_client.models.match_trial_score import MatchTrialScore
from opthub_api_client.models.match_trial_status import MatchTrialStatus
from opthub_api_client.models.runner_status import RunnerStatus
from opthub_api_client.models.scalar_or_vector import ScalarOrVector
from opthub_api_client.models.server_error_code import ServerErrorCode
from opthub_api_client.models.server_error_response import ServerErrorResponse
from opthub_api_client.models.solution import Solution
