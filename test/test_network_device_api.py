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
from dnac_api_client.api.network_device_api import NetworkDeviceApi  # noqa: E501
from dnac_api_client.rest import ApiException


class TestNetworkDeviceApi(unittest.TestCase):
    """NetworkDeviceApi unit test stubs"""

    def setUp(self):
        self.api = dnac_api_client.api.network_device_api.NetworkDeviceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_interface_count_get(self):
        """Test case for api_v1_interface_count_get

        Retrieves interface count  # noqa: E501
        """
        pass

    def test_api_v1_interface_get(self):
        """Test case for api_v1_interface_get

        Retrieves all interfaces  # noqa: E501
        """
        pass

    def test_api_v1_interface_id_get(self):
        """Test case for api_v1_interface_id_get

        Retrieves interface by ID  # noqa: E501
        """
        pass

    def test_api_v1_interface_ip_address_ip_address_get(self):
        """Test case for api_v1_interface_ip_address_ip_address_get

        Retrieves interfaces by IP address  # noqa: E501
        """
        pass

    def test_api_v1_interface_isis_get(self):
        """Test case for api_v1_interface_isis_get

        Retrieves ISIS interfaces  # noqa: E501
        """
        pass

    def test_api_v1_interface_network_device_device_id_count_get(self):
        """Test case for api_v1_interface_network_device_device_id_count_get

        Retrieves device interface count  # noqa: E501
        """
        pass

    def test_api_v1_interface_network_device_device_id_get(self):
        """Test case for api_v1_interface_network_device_device_id_get

        Retrieves device interfaces  # noqa: E501
        """
        pass

    def test_api_v1_interface_network_device_device_id_interface_name_get(self):
        """Test case for api_v1_interface_network_device_device_id_interface_name_get

        Retrieves interface for the given device and interface name  # noqa: E501
        """
        pass

    def test_api_v1_interface_network_device_device_id_start_index_records_to_return_get(self):
        """Test case for api_v1_interface_network_device_device_id_start_index_records_to_return_get

        Retrieves device interfaces in the given range  # noqa: E501
        """
        pass

    def test_api_v1_interface_ospf_get(self):
        """Test case for api_v1_interface_ospf_get

        Retrieves OSPF interfaces  # noqa: E501
        """
        pass

    def test_api_v1_network_device_autocomplete_get(self):
        """Test case for api_v1_network_device_autocomplete_get

        Retrieves all network devices  # noqa: E501
        """
        pass

    def test_api_v1_network_device_brief_put(self):
        """Test case for api_v1_network_device_brief_put

        Updates network device role  # noqa: E501
        """
        pass

    def test_api_v1_network_device_collection_schedule_global_get(self):
        """Test case for api_v1_network_device_collection_schedule_global_get

        Retrieves the collection interval of all devices  # noqa: E501
        """
        pass

    def test_api_v1_network_device_config_count_get(self):
        """Test case for api_v1_network_device_config_count_get

        Retrieves config count  # noqa: E501
        """
        pass

    def test_api_v1_network_device_config_get(self):
        """Test case for api_v1_network_device_config_get

        Retrieves device config list  # noqa: E501
        """
        pass

    def test_api_v1_network_device_count_get(self):
        """Test case for api_v1_network_device_count_get

        Retrieves network device count  # noqa: E501
        """
        pass

    def test_api_v1_network_device_file_post(self):
        """Test case for api_v1_network_device_file_post

        Export network-device to file  # noqa: E501
        """
        pass

    def test_api_v1_network_device_functional_capability_autocomplete_get(self):
        """Test case for api_v1_network_device_functional_capability_autocomplete_get

        Retrieve the values of given fields  # noqa: E501
        """
        pass

    def test_api_v1_network_device_functional_capability_get(self):
        """Test case for api_v1_network_device_functional_capability_get

        Retrieves all functional-capability of devices  # noqa: E501
        """
        pass

    def test_api_v1_network_device_functional_capability_id_get(self):
        """Test case for api_v1_network_device_functional_capability_id_get

        Gets the functional capability by id  # noqa: E501
        """
        pass

    def test_api_v1_network_device_get(self):
        """Test case for api_v1_network_device_get

        Retrieves all network devices  # noqa: E501
        """
        pass

    def test_api_v1_network_device_id_brief_get(self):
        """Test case for api_v1_network_device_id_brief_get

        Retrieves network device brief by ID  # noqa: E501
        """
        pass

    def test_api_v1_network_device_id_collection_schedule_get(self):
        """Test case for api_v1_network_device_id_collection_schedule_get

        Retrieves the collection interval specified by device ID  # noqa: E501
        """
        pass

    def test_api_v1_network_device_id_delete(self):
        """Test case for api_v1_network_device_id_delete

        Delete network device by ID  # noqa: E501
        """
        pass

    def test_api_v1_network_device_id_get(self):
        """Test case for api_v1_network_device_id_get

        Retrieves network device by ID  # noqa: E501
        """
        pass

    def test_api_v1_network_device_id_meraki_organization_get(self):
        """Test case for api_v1_network_device_id_meraki_organization_get

        Get the organizations chosen while adding the meraki dashboard  # noqa: E501
        """
        pass

    def test_api_v1_network_device_id_vlan_get(self):
        """Test case for api_v1_network_device_id_vlan_get

        Retrieves list of VLAN data that are associated with interface for a device  # noqa: E501
        """
        pass

    def test_api_v1_network_device_id_wireless_info_get(self):
        """Test case for api_v1_network_device_id_wireless_info_get

        Retrieves wireless lan conrtoller info by Device ID  # noqa: E501
        """
        pass

    def test_api_v1_network_device_ip_address_ip_address_get(self):
        """Test case for api_v1_network_device_ip_address_ip_address_get

        Retrieves network device by IP address  # noqa: E501
        """
        pass

    def test_api_v1_network_device_module_count_get(self):
        """Test case for api_v1_network_device_module_count_get

        Gives total number of Modules  # noqa: E501
        """
        pass

    def test_api_v1_network_device_module_get(self):
        """Test case for api_v1_network_device_module_get

        Gives all the modules associated with given device id  # noqa: E501
        """
        pass

    def test_api_v1_network_device_module_id_get(self):
        """Test case for api_v1_network_device_module_id_get

        Gives Module info by its id  # noqa: E501
        """
        pass

    def test_api_v1_network_device_network_device_id_config_get(self):
        """Test case for api_v1_network_device_network_device_id_config_get

        Retrieves device config  # noqa: E501
        """
        pass

    def test_api_v1_network_device_post(self):
        """Test case for api_v1_network_device_post

        Network device POST api  # noqa: E501
        """
        pass

    def test_api_v1_network_device_put(self):
        """Test case for api_v1_network_device_put

        Network device sync api  # noqa: E501
        """
        pass

    def test_api_v1_network_device_serial_number_serial_number_get(self):
        """Test case for api_v1_network_device_serial_number_serial_number_get

        Retrieves network device by serial number  # noqa: E501
        """
        pass

    def test_api_v1_network_device_start_index_records_to_return_get(self):
        """Test case for api_v1_network_device_start_index_records_to_return_get

        Retrieves network device by range  # noqa: E501
        """
        pass

    def test_api_v1_network_device_sync_put(self):
        """Test case for api_v1_network_device_sync_put

        Network device sync api  # noqa: E501
        """
        pass

    def test_api_v1_network_device_tenantinfo_macaddress_get(self):
        """Test case for api_v1_network_device_tenantinfo_macaddress_get

        Updates certificate validation status and returns tenantId  # noqa: E501
        """
        pass

    def test_api_v1_snmp_property_get(self):
        """Test case for api_v1_snmp_property_get

        Retrieves SNMP properties  # noqa: E501
        """
        pass

    def test_api_v1_snmp_property_post(self):
        """Test case for api_v1_snmp_property_post

        Creates or updates SNMP properties  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
