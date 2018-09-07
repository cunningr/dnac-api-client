# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dnac_api_client
from dnac_api_client.api.authentication_api import AuthenticationApi  # noqa: E501
from dnac_api_client.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = dnac_api_client.api.authentication_api.AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_system_v1_auth_token_post(self):
        """Test case for api_system_v1_auth_token_post

        Generate Token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
