# coding: utf-8

"""
    OptHub REST API

    OptHubの公開REST APIです。

    The version of the OpenAPI document: 0.1.0
    Contact: dev@opthub.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opthub_api_client.models.solution import Solution

class TestSolution(unittest.TestCase):
    """Solution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Solution:
        """Test Solution
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Solution`
        """
        model = Solution()
        if include_optional:
            return Solution(
                match_id = '5d7fc778-3e59-4128-a797-2e423c0aa461',
                participant_type = 'User',
                participant_id = '912f548d-2bbe-48ab-90ce-e96dae38377d',
                trial_no = 4,
                variable = None,
                created_at = '2024-08-06T10:11:45.789Z',
                user_id = '1e892e70-47ba-4c8e-8563-6aea9019e334'
            )
        else:
            return Solution(
                match_id = '5d7fc778-3e59-4128-a797-2e423c0aa461',
                participant_type = 'User',
                participant_id = '912f548d-2bbe-48ab-90ce-e96dae38377d',
                trial_no = 4,
                variable = None,
                created_at = '2024-08-06T10:11:45.789Z',
        )
        """

    def testSolution(self):
        """Test Solution"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
