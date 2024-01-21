# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from arguflow.models.search_collections_data import SearchCollectionsData

class TestSearchCollectionsData(unittest.TestCase):
    """SearchCollectionsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchCollectionsData:
        """Test SearchCollectionsData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchCollectionsData`
        """
        model = SearchCollectionsData()
        if include_optional:
            return SearchCollectionsData(
                collection_id = '',
                date_bias = True,
                filters = None,
                link = [
                    ''
                    ],
                page = 0,
                query = '',
                search_type = '',
                tag_set = [
                    ''
                    ]
            )
        else:
            return SearchCollectionsData(
                collection_id = '',
                query = '',
                search_type = '',
        )
        """

    def testSearchCollectionsData(self):
        """Test SearchCollectionsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
