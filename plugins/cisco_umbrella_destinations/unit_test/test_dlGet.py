import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dlGet import DlGet
from icon_cisco_umbrella_destinations.actions.dlGet.schema import Input
import json
import logging

from unit_test.mock import STUB_CONNECTION, mock_request_200, mocked_request, STUB_DESTINATION_LIST_ID


class TestDlGet(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DlGet()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.params = {"destination_list_id": STUB_DESTINATION_LIST_ID}

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_destination_list_get_success(self, mock_get):
        response = self.action.run({Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID})
        expected_response = {
            "success": {
                "status": {"code": 200, "text": "OK"},
                "data": {
                    "id": 15755711,
                    "organizationId": 2372338,
                    "access": "allow",
                    "isGlobal": False,
                    "name": "CreateListTest",
                    "thirdpartyCategoryId": None,
                    "createdAt": "2022-01-28T16:03:36+0000",
                    "modifiedAt": "2022-02-04T14:59:22+0000",
                    "isMspDefault": False,
                    "markedForDeletion": False,
                    "bundleTypeId": 1,
                    "meta": {"destinationCount": 3},
                },
            }
        }
        self.assertEqual(response, expected_response)
