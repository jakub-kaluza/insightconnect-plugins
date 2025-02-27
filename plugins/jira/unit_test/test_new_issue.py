import sys
import os
import timeout_decorator
from unittest import TestCase
from unittest.mock import patch
from komand_jira.triggers.new_issue import NewIssue
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test import util
from typing import Callable, Optional


sys.path.append(os.path.abspath("../"))


def timeout_pass(error_callback: Optional[Callable] = None):
    def func_timeout(func):
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except timeout_decorator.timeout_decorator.TimeoutError as e:
                if error_callback:
                    return error_callback()

                return None

        return func_wrapper

    return func_timeout


# Test class
class TestNewIssue(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = util.Util.default_connector(NewIssue())

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_new_issue(self, mock_send):
        action_params = {
            "get_attachments": False,
            "jql": "project=projectName",
            "poll_timeout": 60,
            "project": "projectName",
        }
        self.action.run(action_params)

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_new_issue_invalid_project(self, mock_send):
        action_params = {"get_attachments": False, "jql": "", "poll_timeout": 60, "project": "projectName2"}
        with self.assertRaises(PluginException) as e:
            self.action.run(action_params)
        self.assertEqual(
            e.exception.cause,
            "Project 'projectName2' does not exist or the user does not have permission to access the project.",
        )
        self.assertEqual(
            e.exception.assistance,
            "Please provide a valid project ID/name or make sure the project is accessible to the user.",
        )

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_new_issue_only_project(self, mock_send):
        action_params = {
            "get_attachments": False,
            "jql": "",
            "poll_timeout": 60,
            "project": "projectName",
        }
        self.action.run(action_params)

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_new_issue_only_jql(self, mock_send):
        action_params = {
            "get_attachments": False,
            "jql": "reporter='Bob Smith'",
            "poll_timeout": 60,
            "project": "",
        }
        self.action.run(action_params)

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_new_issue_without_jql_and_project(self, mock_send):
        action_params = {
            "get_attachments": False,
            "jql": "",
            "poll_timeout": 60,
            "project": "",
        }
        self.action.run(action_params)
