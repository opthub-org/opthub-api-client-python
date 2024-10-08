# coding: utf-8

"""
    OptHub REST API

    OptHub Public REST API.

    The version of the OpenAPI document: 0.3.0
    Contact: dev@opthub.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opthub_api_client.models.match_trial_evaluation import MatchTrialEvaluation

class TestMatchTrialEvaluation(unittest.TestCase):
    """MatchTrialEvaluation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MatchTrialEvaluation:
        """Test MatchTrialEvaluation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchTrialEvaluation`
        """
        model = MatchTrialEvaluation()
        if include_optional:
            return MatchTrialEvaluation(
                status = 'Success',
                error = '',
                objective = {"vector":[1.234,-5.678,9.1011]},
                constraint = {"vector":[1.234,-5.678,9.1011]},
                info = None,
                feasible = True,
                started_at = '2024-08-29T10:12:58.123Z',
                finished_at = '2024-08-29T10:34:01.592Z'
            )
        else:
            return MatchTrialEvaluation(
                status = 'Success',
                started_at = '2024-08-29T10:12:58.123Z',
                finished_at = '2024-08-29T10:34:01.592Z',
        )
        """

    def testMatchTrialEvaluation(self):
        """Test MatchTrialEvaluation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
