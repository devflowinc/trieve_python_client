# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.search_chunk_data_time_range_inner import SearchChunkDataTimeRangeInner

class TestSearchChunkDataTimeRangeInner(unittest.TestCase):
    """SearchChunkDataTimeRangeInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchChunkDataTimeRangeInner:
        """Test SearchChunkDataTimeRangeInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchChunkDataTimeRangeInner`
        """
        model = SearchChunkDataTimeRangeInner()
        if include_optional:
            return SearchChunkDataTimeRangeInner(
            )
        else:
            return SearchChunkDataTimeRangeInner(
        )
        """

    def testSearchChunkDataTimeRangeInner(self):
        """Test SearchChunkDataTimeRangeInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
