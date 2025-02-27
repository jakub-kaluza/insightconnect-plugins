import sys
import os
from unit_test.mockconnection import MockConnection
from unittest import TestCase

sys.path.append(os.path.abspath("../"))
from komand_rest.actions.patch import Patch


class TestPatch(TestCase):
    def test_integration_patch(self):
        """
        TODO: Implement assertions at the end of this test case

        This is an integration test that will connect to the services your plugin uses. It should be used
        as the basis for tests below that can run independent of a "live" connection.

        This test assumes a normal plugin structure with a /tests directory. In that /tests directory should
        be json samples that contain all the data needed to run this test. To generate samples run:

        icon-plugin generate samples



        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = Patch()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/patch.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message =
            Could not find or read sample tests from /tests directory

            An exception here likely means you didn't fill out your samples correctly in the /tests directory
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory

            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        # TODO: Remove this line
        self.fail("Unimplemented test case")

        # TODO: The following assert should be updated to look for data from your action
        # For example: self.assertEquals({"success": True}, results)
        self.assertEquals({}, results)
        """

    def test_patch_unit(self):
        test_conn = MockConnection()
        test_action = Patch()

        test_action.connection = test_conn
        action_params = {"route": "https://www.google.com", "headers": {}}
        results = test_action.run(action_params)

        # only new things to test is that it correctly routes output of results
        self.assertEqual(results["status"], 200)
        # more tests?
        self.assertEqual(results["body_object"], {"SampleSuccessBody": "SampleVal"})
        self.assertEqual(results["body_string"], "SAMPLETEXT for method PATCH")
        self.assertEqual(results["headers"], {"SampleHeader": "SampleVal"})
