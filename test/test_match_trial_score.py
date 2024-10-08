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

from opthub_api_client.models.match_trial_score import MatchTrialScore

class TestMatchTrialScore(unittest.TestCase):
    """MatchTrialScore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MatchTrialScore:
        """Test MatchTrialScore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchTrialScore`
        """
        model = MatchTrialScore()
        if include_optional:
            return MatchTrialScore(
                status = 'Success',
                error = '',
                value = 15.1617,
                started_at = '2024-08-29T10:56:02.933Z',
                finished_at = '2024-08-29T11:01:21.319Z'
            )
        else:
            return MatchTrialScore(
                status = 'Success',
                started_at = '2024-08-29T10:56:02.933Z',
                finished_at = '2024-08-29T11:01:21.319Z',
        )
        """

    def testMatchTrialScore(self):
        """Test MatchTrialScore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
