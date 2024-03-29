# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.get_direct_payment_link_data import GetDirectPaymentLinkData

class TestGetDirectPaymentLinkData(unittest.TestCase):
    """GetDirectPaymentLinkData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDirectPaymentLinkData:
        """Test GetDirectPaymentLinkData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDirectPaymentLinkData`
        """
        model = GetDirectPaymentLinkData()
        if include_optional:
            return GetDirectPaymentLinkData(
                organization_id = '',
                plan_id = ''
            )
        else:
            return GetDirectPaymentLinkData(
                organization_id = '',
                plan_id = '',
        )
        """

    def testGetDirectPaymentLinkData(self):
        """Test GetDirectPaymentLinkData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
