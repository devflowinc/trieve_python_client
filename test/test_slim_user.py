# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.slim_user import SlimUser

class TestSlimUser(unittest.TestCase):
    """SlimUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlimUser:
        """Test SlimUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlimUser`
        """
        model = SlimUser()
        if include_optional:
            return SlimUser(
                email = '',
                id = '',
                name = '',
                orgs = [
                    trieve_python_client.models.organization.Organization(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        name = '', 
                        registerable = True, 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                user_orgs = [
                    trieve_python_client.models.user_organization.UserOrganization(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        organization_id = '', 
                        role = 56, 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user_id = '', )
                    ],
                username = '',
                visible_email = True,
                website = ''
            )
        else:
            return SlimUser(
                email = '',
                id = '',
                orgs = [
                    trieve_python_client.models.organization.Organization(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        name = '', 
                        registerable = True, 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                user_orgs = [
                    trieve_python_client.models.user_organization.UserOrganization(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        organization_id = '', 
                        role = 56, 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user_id = '', )
                    ],
                visible_email = True,
        )
        """

    def testSlimUser(self):
        """Test SlimUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
