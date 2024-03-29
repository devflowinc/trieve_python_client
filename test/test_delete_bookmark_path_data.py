# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.delete_bookmark_path_data import DeleteBookmarkPathData

class TestDeleteBookmarkPathData(unittest.TestCase):
    """DeleteBookmarkPathData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteBookmarkPathData:
        """Test DeleteBookmarkPathData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteBookmarkPathData`
        """
        model = DeleteBookmarkPathData()
        if include_optional:
            return DeleteBookmarkPathData(
                bookmark_id = '',
                collection_id = ''
            )
        else:
            return DeleteBookmarkPathData(
                bookmark_id = '',
                collection_id = '',
        )
        """

    def testDeleteBookmarkPathData(self):
        """Test DeleteBookmarkPathData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
