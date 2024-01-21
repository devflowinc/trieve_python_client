# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from arguflow.models.dataset_and_org_with_sub_and_plan import DatasetAndOrgWithSubAndPlan

class TestDatasetAndOrgWithSubAndPlan(unittest.TestCase):
    """DatasetAndOrgWithSubAndPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetAndOrgWithSubAndPlan:
        """Test DatasetAndOrgWithSubAndPlan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetAndOrgWithSubAndPlan`
        """
        model = DatasetAndOrgWithSubAndPlan()
        if include_optional:
            return DatasetAndOrgWithSubAndPlan(
                dataset = arguflow.models.dataset.Dataset(
                    client_configuration = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    name = '', 
                    organization_id = '', 
                    server_configuration = null, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                organization = arguflow.models.organization_with_sub_and_plan.OrganizationWithSubAndPlan(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    name = '', 
                    plan = null, 
                    registerable = True, 
                    subscription = null, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return DatasetAndOrgWithSubAndPlan(
                dataset = arguflow.models.dataset.Dataset(
                    client_configuration = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    name = '', 
                    organization_id = '', 
                    server_configuration = null, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                organization = arguflow.models.organization_with_sub_and_plan.OrganizationWithSubAndPlan(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    name = '', 
                    plan = null, 
                    registerable = True, 
                    subscription = null, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testDatasetAndOrgWithSubAndPlan(self):
        """Test DatasetAndOrgWithSubAndPlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
