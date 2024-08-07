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

from opthub_api_client.models.create_solution_response import CreateSolutionResponse

class TestCreateSolutionResponse(unittest.TestCase):
    """CreateSolutionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSolutionResponse:
        """Test CreateSolutionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSolutionResponse`
        """
        model = CreateSolutionResponse()
        if include_optional:
            return CreateSolutionResponse(
                match_id = '5d7fc778-3e59-4128-a797-2e423c0aa461',
                participant_type = 'User',
                participant_id = '912f548d-2bbe-48ab-90ce-e96dae38377d',
                trial_no = 4
            )
        else:
            return CreateSolutionResponse(
                match_id = '5d7fc778-3e59-4128-a797-2e423c0aa461',
                participant_type = 'User',
                participant_id = '912f548d-2bbe-48ab-90ce-e96dae38377d',
                trial_no = 4,
        )
        """

    def testCreateSolutionResponse(self):
        """Test CreateSolutionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
