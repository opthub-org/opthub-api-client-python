# coding: utf-8

"""
    OptHub REST API

    OptHub Public REST API.

    The version of the OpenAPI document: 0.1.1
    Contact: dev@opthub.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opthub_api_client.api.participant_api import ParticipantApi


class TestParticipantApi(unittest.TestCase):
    """ParticipantApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ParticipantApi()

    def tearDown(self) -> None:
        pass

    def test_get_participant(self) -> None:
        """Test case for get_participant

        Retrieve the participant information
        """
        pass


if __name__ == '__main__':
    unittest.main()
