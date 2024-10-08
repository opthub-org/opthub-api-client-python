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

from opthub_api_client.models.get_match_score404_response import GetMatchScore404Response

class TestGetMatchScore404Response(unittest.TestCase):
    """GetMatchScore404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMatchScore404Response:
        """Test GetMatchScore404Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMatchScore404Response`
        """
        model = GetMatchScore404Response()
        if include_optional:
            return GetMatchScore404Response(
                code = 'MatchNotFound',
                message = 'Match is not found.'
            )
        else:
            return GetMatchScore404Response(
        )
        """

    def testGetMatchScore404Response(self):
        """Test GetMatchScore404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
