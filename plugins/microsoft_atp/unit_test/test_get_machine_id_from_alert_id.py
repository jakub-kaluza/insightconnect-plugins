import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_microsoft_atp.connection.connection import Connection
from komand_microsoft_atp.actions.get_machine_id_from_alert_id import GetMachineIdFromAlertId
import json
import logging


class TestGetMachineIdFromAlertId(TestCase):
    def test_integration_get_machine_id_from_alert_id(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetMachineIdFromAlertId()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/get_machine_id_from_alert_id.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = """
            Could not find or read sample tests from /tests directory
            
            An exception here likely means you didn't fill out your samples correctly in the /tests directory 
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        # TODO: The following assert should be updated to look for data from your action
        # For example: self.assertEquals({"success": True}, results)
        self.assertEquals({}, results)
