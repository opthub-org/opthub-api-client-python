# coding: utf-8

"""
    OptHub REST API

    OptHub Public REST API.

    The version of the OpenAPI document: 0.1.0
    Contact: dev@opthub.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opthub_api_client.api.competition_api import CompetitionApi


class TestCompetitionApi(unittest.TestCase):
    """CompetitionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CompetitionApi()

    def tearDown(self) -> None:
        pass

    def test_resolve_competition_alias_by_id(self) -> None:
        """Test case for resolve_competition_alias_by_id

        Retrieve the competition alias from the competition ID
        """
        pass

    def test_resolve_competition_id_by_alias(self) -> None:
        """Test case for resolve_competition_id_by_alias

        Retrieve the competition ID from the competition alias
        """
        pass


if __name__ == '__main__':
    unittest.main()
