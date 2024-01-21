# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from arguflow.models.user_dto_with_chunks import UserDTOWithChunks

class TestUserDTOWithChunks(unittest.TestCase):
    """UserDTOWithChunks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserDTOWithChunks:
        """Test UserDTOWithChunks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserDTOWithChunks`
        """
        model = UserDTOWithChunks()
        if include_optional:
            return UserDTOWithChunks(
                chunks = [
                    arguflow.models.chunk_metadata_with_file_data.ChunkMetadataWithFileData(
                        author = null, 
                        chunk_html = '', 
                        content = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        file_id = '', 
                        file_name = '', 
                        id = '', 
                        link = '', 
                        metadata = null, 
                        qdrant_point_id = '', 
                        tag_set = '', 
                        time_stamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        tracking_id = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        weight = 1.337, )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email = '',
                id = '',
                total_chunks_created = 56,
                username = '',
                visible_email = True,
                website = ''
            )
        else:
            return UserDTOWithChunks(
                chunks = [
                    arguflow.models.chunk_metadata_with_file_data.ChunkMetadataWithFileData(
                        author = null, 
                        chunk_html = '', 
                        content = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        file_id = '', 
                        file_name = '', 
                        id = '', 
                        link = '', 
                        metadata = null, 
                        qdrant_point_id = '', 
                        tag_set = '', 
                        time_stamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        tracking_id = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        weight = 1.337, )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                total_chunks_created = 56,
                visible_email = True,
        )
        """

    def testUserDTOWithChunks(self):
        """Test UserDTOWithChunks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()