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

from opthub_api_client.models.get_match_trial404_response import GetMatchTrial404Response

class TestGetMatchTrial404Response(unittest.TestCase):
    """GetMatchTrial404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMatchTrial404Response:
        """Test GetMatchTrial404Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMatchTrial404Response`
        """
        model = GetMatchTrial404Response()
        if include_optional:
            return GetMatchTrial404Response(
                code = 'MatchNotFound',
                message = 'Match is not found.'
            )
        else:
            return GetMatchTrial404Response(
        )
        """

    def testGetMatchTrial404Response(self):
        """Test GetMatchTrial404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
