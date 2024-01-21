# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from arguflow.models.add_chunk_to_collection_data import AddChunkToCollectionData

class TestAddChunkToCollectionData(unittest.TestCase):
    """AddChunkToCollectionData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddChunkToCollectionData:
        """Test AddChunkToCollectionData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddChunkToCollectionData`
        """
        model = AddChunkToCollectionData()
        if include_optional:
            return AddChunkToCollectionData(
                chunk_id = ''
            )
        else:
            return AddChunkToCollectionData(
                chunk_id = '',
        )
        """

    def testAddChunkToCollectionData(self):
        """Test AddChunkToCollectionData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
