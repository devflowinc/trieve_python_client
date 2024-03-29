# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.notification_id import NotificationId

class TestNotificationId(unittest.TestCase):
    """NotificationId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationId:
        """Test NotificationId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationId`
        """
        model = NotificationId()
        if include_optional:
            return NotificationId(
                notification_id = ''
            )
        else:
            return NotificationId(
                notification_id = '',
        )
        """

    def testNotificationId(self):
        """Test NotificationId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
