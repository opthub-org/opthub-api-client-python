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
                variable = {"vector":[1.234,-5.678,9.1011]},
                created_at = '2024-08-29T10:08:03.345Z'
            )
        else:
            return Solution(
                created_at = '2024-08-29T10:08:03.345Z',
        )
        """

    def testSolution(self):
        """Test Solution"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
