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

from opthub_api_client.models.create_match_trial403_response import CreateMatchTrial403Response

class TestCreateMatchTrial403Response(unittest.TestCase):
    """CreateMatchTrial403Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateMatchTrial403Response:
        """Test CreateMatchTrial403Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateMatchTrial403Response`
        """
        model = CreateMatchTrial403Response()
        if include_optional:
            return CreateMatchTrial403Response(
                code = 'CompetitionNotStarted',
                message = 'Competition is not started.'
            )
        else:
            return CreateMatchTrial403Response(
        )
        """

    def testCreateMatchTrial403Response(self):
        """Test CreateMatchTrial403Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
