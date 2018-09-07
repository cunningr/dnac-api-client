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
from dnac_api_client.api.intent_api_api import IntentAPIApi  # noqa: E501
from dnac_api_client.rest import ApiException


class TestIntentAPIApi(unittest.TestCase):
    """IntentAPIApi unit test stubs"""

    def setUp(self):
        self.api = dnac_api_client.api.intent_api_api.IntentAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dna_intent_api_v1_client_detail_get(self):
        """Test case for dna_intent_api_v1_client_detail_get

        Client Detail  # noqa: E501
        """
        pass

    def test_dna_intent_api_v1_client_health_get(self):
        """Test case for dna_intent_api_v1_client_health_get

        Client Health  # noqa: E501
        """
        pass

    def test_dna_intent_api_v1_network_device_detail_get(self):
        """Test case for dna_intent_api_v1_network_device_detail_get

        Network Device Detail  # noqa: E501
        """
        pass

    def test_dna_intent_api_v1_network_health_get(self):
        """Test case for dna_intent_api_v1_network_health_get

        Network Health  # noqa: E501
        """
        pass

    def test_dna_intent_api_v1_site_hierarchy_get(self):
        """Test case for dna_intent_api_v1_site_hierarchy_get

        Site Hierarchy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
