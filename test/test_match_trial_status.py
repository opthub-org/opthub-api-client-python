# coding: utf-8

"""
    OptHub REST API

    OptHub Public REST API.

    The version of the OpenAPI document: 0.2.0
    Contact: dev@opthub.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opthub_api_client.models.match_trial_status import MatchTrialStatus

class TestMatchTrialStatus(unittest.TestCase):
    """MatchTrialStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MatchTrialStatus:
        """Test MatchTrialStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchTrialStatus`
        """
        model = MatchTrialStatus()
        if include_optional:
            return MatchTrialStatus(
                type = 'Success',
                evaluation = opthub_api_client.models.match_trial_evaluation.MatchTrialEvaluation(
                    objective = null, 
                    constraint = [1.234,-5.678,9.1011], 
                    feasible = True, 
                    extra_info = opthub_api_client.models.extra_info.extra_info(), 
                    started_at = '2024-08-29T10:12:58.123Z', 
                    finished_at = '2024-08-29T10:34:01.592Z', 
                    error = '', 
                    status = 'Success', ),
                score = opthub_api_client.models.match_trial_score.MatchTrialScore(
                    value = 15.1617, 
                    started_at = '2024-08-29T10:56:02.933Z', 
                    finished_at = '2024-08-29T11:01:21.319Z', 
                    error = '', 
                    status = 'Success', )
            )
        else:
            return MatchTrialStatus(
                type = 'Success',
        )
        """

    def testMatchTrialStatus(self):
        """Test MatchTrialStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
