# dnac_api_client.NetworkDeviceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_interface_count_get**](NetworkDeviceApi.md#api_v1_interface_count_get) | **GET** /api/v1/interface/count | Retrieves interface count
[**api_v1_interface_get**](NetworkDeviceApi.md#api_v1_interface_get) | **GET** /api/v1/interface | Retrieves all interfaces
[**api_v1_interface_id_get**](NetworkDeviceApi.md#api_v1_interface_id_get) | **GET** /api/v1/interface/{id} | Retrieves interface by ID
[**api_v1_interface_ip_address_ip_address_get**](NetworkDeviceApi.md#api_v1_interface_ip_address_ip_address_get) | **GET** /api/v1/interface/ip-address/{ipAddress} | Retrieves interfaces by IP address
[**api_v1_interface_isis_get**](NetworkDeviceApi.md#api_v1_interface_isis_get) | **GET** /api/v1/interface/isis | Retrieves ISIS interfaces
[**api_v1_interface_network_device_device_id_count_get**](NetworkDeviceApi.md#api_v1_interface_network_device_device_id_count_get) | **GET** /api/v1/interface/network-device/{deviceId}/count | Retrieves device interface count
[**api_v1_interface_network_device_device_id_get**](NetworkDeviceApi.md#api_v1_interface_network_device_device_id_get) | **GET** /api/v1/interface/network-device/{deviceId} | Retrieves device interfaces
[**api_v1_interface_network_device_device_id_interface_name_get**](NetworkDeviceApi.md#api_v1_interface_network_device_device_id_interface_name_get) | **GET** /api/v1/interface/network-device/{deviceId}/interface-name | Retrieves interface for the given device and interface name
[**api_v1_interface_network_device_device_id_start_index_records_to_return_get**](NetworkDeviceApi.md#api_v1_interface_network_device_device_id_start_index_records_to_return_get) | **GET** /api/v1/interface/network-device/{deviceId}/{startIndex}/{recordsToReturn} | Retrieves device interfaces in the given range
[**api_v1_interface_ospf_get**](NetworkDeviceApi.md#api_v1_interface_ospf_get) | **GET** /api/v1/interface/ospf | Retrieves OSPF interfaces
[**api_v1_network_device_autocomplete_get**](NetworkDeviceApi.md#api_v1_network_device_autocomplete_get) | **GET** /api/v1/network-device/autocomplete | Retrieves all network devices
[**api_v1_network_device_brief_put**](NetworkDeviceApi.md#api_v1_network_device_brief_put) | **PUT** /api/v1/network-device/brief | Updates network device role
[**api_v1_network_device_collection_schedule_global_get**](NetworkDeviceApi.md#api_v1_network_device_collection_schedule_global_get) | **GET** /api/v1/network-device/collection-schedule/global | Retrieves the collection interval of all devices
[**api_v1_network_device_config_count_get**](NetworkDeviceApi.md#api_v1_network_device_config_count_get) | **GET** /api/v1/network-device/config/count | Retrieves config count
[**api_v1_network_device_config_get**](NetworkDeviceApi.md#api_v1_network_device_config_get) | **GET** /api/v1/network-device/config | Retrieves device config list
[**api_v1_network_device_count_get**](NetworkDeviceApi.md#api_v1_network_device_count_get) | **GET** /api/v1/network-device/count | Retrieves network device count
[**api_v1_network_device_file_post**](NetworkDeviceApi.md#api_v1_network_device_file_post) | **POST** /api/v1/network-device/file | Export network-device to file
[**api_v1_network_device_functional_capability_autocomplete_get**](NetworkDeviceApi.md#api_v1_network_device_functional_capability_autocomplete_get) | **GET** /api/v1/network-device/functional-capability/autocomplete | Retrieve the values of given fields
[**api_v1_network_device_functional_capability_get**](NetworkDeviceApi.md#api_v1_network_device_functional_capability_get) | **GET** /api/v1/network-device/functional-capability | Retrieves all functional-capability of devices
[**api_v1_network_device_functional_capability_id_get**](NetworkDeviceApi.md#api_v1_network_device_functional_capability_id_get) | **GET** /api/v1/network-device/functional-capability/{id} | Gets the functional capability by id
[**api_v1_network_device_get**](NetworkDeviceApi.md#api_v1_network_device_get) | **GET** /api/v1/network-device | Retrieves all network devices
[**api_v1_network_device_id_brief_get**](NetworkDeviceApi.md#api_v1_network_device_id_brief_get) | **GET** /api/v1/network-device/{id}/brief | Retrieves network device brief by ID
[**api_v1_network_device_id_collection_schedule_get**](NetworkDeviceApi.md#api_v1_network_device_id_collection_schedule_get) | **GET** /api/v1/network-device/{id}/collection-schedule | Retrieves the collection interval specified by device ID
[**api_v1_network_device_id_delete**](NetworkDeviceApi.md#api_v1_network_device_id_delete) | **DELETE** /api/v1/network-device/{id} | Delete network device by ID
[**api_v1_network_device_id_get**](NetworkDeviceApi.md#api_v1_network_device_id_get) | **GET** /api/v1/network-device/{id} | Retrieves network device by ID
[**api_v1_network_device_id_meraki_organization_get**](NetworkDeviceApi.md#api_v1_network_device_id_meraki_organization_get) | **GET** /api/v1/network-device/{id}/meraki-organization | Get the organizations chosen while adding the meraki dashboard
[**api_v1_network_device_id_vlan_get**](NetworkDeviceApi.md#api_v1_network_device_id_vlan_get) | **GET** /api/v1/network-device/{id}/vlan | Retrieves list of VLAN data that are associated with interface for a device
[**api_v1_network_device_id_wireless_info_get**](NetworkDeviceApi.md#api_v1_network_device_id_wireless_info_get) | **GET** /api/v1/network-device/{id}/wireless-info | Retrieves wireless lan conrtoller info by Device ID
[**api_v1_network_device_ip_address_ip_address_get**](NetworkDeviceApi.md#api_v1_network_device_ip_address_ip_address_get) | **GET** /api/v1/network-device/ip-address/{ipAddress} | Retrieves network device by IP address
[**api_v1_network_device_module_count_get**](NetworkDeviceApi.md#api_v1_network_device_module_count_get) | **GET** /api/v1/network-device/module/count | Gives total number of Modules
[**api_v1_network_device_module_get**](NetworkDeviceApi.md#api_v1_network_device_module_get) | **GET** /api/v1/network-device/module | Gives all the modules associated with given device id
[**api_v1_network_device_module_id_get**](NetworkDeviceApi.md#api_v1_network_device_module_id_get) | **GET** /api/v1/network-device/module/{id} | Gives Module info by its id
[**api_v1_network_device_network_device_id_config_get**](NetworkDeviceApi.md#api_v1_network_device_network_device_id_config_get) | **GET** /api/v1/network-device/{networkDeviceId}/config | Retrieves device config
[**api_v1_network_device_post**](NetworkDeviceApi.md#api_v1_network_device_post) | **POST** /api/v1/network-device | Network device POST api
[**api_v1_network_device_put**](NetworkDeviceApi.md#api_v1_network_device_put) | **PUT** /api/v1/network-device | Network device sync api
[**api_v1_network_device_serial_number_serial_number_get**](NetworkDeviceApi.md#api_v1_network_device_serial_number_serial_number_get) | **GET** /api/v1/network-device/serial-number/{serialNumber} | Retrieves network device by serial number
[**api_v1_network_device_start_index_records_to_return_get**](NetworkDeviceApi.md#api_v1_network_device_start_index_records_to_return_get) | **GET** /api/v1/network-device/{startIndex}/{recordsToReturn} | Retrieves network device by range
[**api_v1_network_device_sync_put**](NetworkDeviceApi.md#api_v1_network_device_sync_put) | **PUT** /api/v1/network-device/sync | Network device sync api
[**api_v1_network_device_tenantinfo_macaddress_get**](NetworkDeviceApi.md#api_v1_network_device_tenantinfo_macaddress_get) | **GET** /api/v1/network-device/tenantinfo/macaddress | Updates certificate validation status and returns tenantId
[**api_v1_snmp_property_get**](NetworkDeviceApi.md#api_v1_snmp_property_get) | **GET** /api/v1/snmp-property | Retrieves SNMP properties
[**api_v1_snmp_property_post**](NetworkDeviceApi.md#api_v1_snmp_property_post) | **POST** /api/v1/snmp-property | Creates or updates SNMP properties


# **api_v1_interface_count_get**
> CountResult api_v1_interface_count_get()

Retrieves interface count

Gets the count of interfaces for all devices

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves interface count
    api_response = api_instance.api_v1_interface_count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interface_get**
> DeviceIfListResult api_v1_interface_get()

Retrieves all interfaces

Gets all available interfaces with a maximum limit of 500

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves all interfaces
    api_response = api_instance.api_v1_interface_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceIfListResult**](DeviceIfListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interface_id_get**
> DeviceIfResult api_v1_interface_id_get(id)

Retrieves interface by ID

Gets the interface for the given interface ID

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Interface ID

try:
    # Retrieves interface by ID
    api_response = api_instance.api_v1_interface_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Interface ID | 

### Return type

[**DeviceIfResult**](DeviceIfResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interface_ip_address_ip_address_get**
> DeviceIfListResult api_v1_interface_ip_address_ip_address_get(ip_address)

Retrieves interfaces by IP address

Gets list of interfaces with the given IP address

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
ip_address = 'ip_address_example' # str | IP address of the interface

try:
    # Retrieves interfaces by IP address
    api_response = api_instance.api_v1_interface_ip_address_ip_address_get(ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_ip_address_ip_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| IP address of the interface | 

### Return type

[**DeviceIfListResult**](DeviceIfListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interface_isis_get**
> DeviceIfListResult api_v1_interface_isis_get()

Retrieves ISIS interfaces

Gets the interfaces that has ISIS enabled

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves ISIS interfaces
    api_response = api_instance.api_v1_interface_isis_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_isis_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceIfListResult**](DeviceIfListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interface_network_device_device_id_count_get**
> CountResult api_v1_interface_network_device_device_id_count_get(device_id)

Retrieves device interface count

Gets the interface count for the given device

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Device ID

try:
    # Retrieves device interface count
    api_response = api_instance.api_v1_interface_network_device_device_id_count_get(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_network_device_device_id_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interface_network_device_device_id_get**
> DeviceIfListResult api_v1_interface_network_device_device_id_get(device_id)

Retrieves device interfaces

Gets list of interfaces for the given device

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Device ID

try:
    # Retrieves device interfaces
    api_response = api_instance.api_v1_interface_network_device_device_id_get(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_network_device_device_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID | 

### Return type

[**DeviceIfListResult**](DeviceIfListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interface_network_device_device_id_interface_name_get**
> DeviceIfResult api_v1_interface_network_device_device_id_interface_name_get(device_id, name)

Retrieves interface for the given device and interface name

Gets the interface for the given device ID and for the given interface name

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Device ID
name = 'name_example' # str | Interface name

try:
    # Retrieves interface for the given device and interface name
    api_response = api_instance.api_v1_interface_network_device_device_id_interface_name_get(device_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_network_device_device_id_interface_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID | 
 **name** | **str**| Interface name | 

### Return type

[**DeviceIfResult**](DeviceIfResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interface_network_device_device_id_start_index_records_to_return_get**
> DeviceIfListResult api_v1_interface_network_device_device_id_start_index_records_to_return_get(device_id, start_index, records_to_return)

Retrieves device interfaces in the given range

Gets the list of interfaces for the device for the specified range

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Device ID
start_index = 56 # int | Start index
records_to_return = 56 # int | Number of records to return

try:
    # Retrieves device interfaces in the given range
    api_response = api_instance.api_v1_interface_network_device_device_id_start_index_records_to_return_get(device_id, start_index, records_to_return)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_network_device_device_id_start_index_records_to_return_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID | 
 **start_index** | **int**| Start index | 
 **records_to_return** | **int**| Number of records to return | 

### Return type

[**DeviceIfListResult**](DeviceIfListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interface_ospf_get**
> DeviceIfListResult api_v1_interface_ospf_get()

Retrieves OSPF interfaces

Gets the interfaces that has OSPF enabled

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves OSPF interfaces
    api_response = api_instance.api_v1_interface_ospf_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_interface_ospf_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceIfListResult**](DeviceIfListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_autocomplete_get**
> RetrievesAllNetworkDevicesResponse api_v1_network_device_autocomplete_get(vrf_name=vrf_name, management_ip_address=management_ip_address, hostname=hostname, mac_address=mac_address, family=family, collection_status=collection_status, collection_interval=collection_interval, software_version=software_version, software_type=software_type, reachability_status=reachability_status, reachability_failure_reason=reachability_failure_reason, error_code=error_code, platform_id=platform_id, series=series, type=type, serial_number=serial_number, up_time=up_time, role=role, role_source=role_source, associated_wlc_ip=associated_wlc_ip, offset=offset, limit=limit)

Retrieves all network devices

Gets the list of first 500 network devices sorted lexicographically based on host name. It can be filtered using management IP address, mac address, hostname and location name. If id param is provided, it will be returning the list of network-devices for the given id's and other request params will be ignored. In case of autocomplete request, returns the list of specified attributes.

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
vrf_name = 'vrf_name_example' # str | vrfName (optional)
management_ip_address = 'management_ip_address_example' # str | managementIpAddress (optional)
hostname = 'hostname_example' # str | hostname (optional)
mac_address = 'mac_address_example' # str | macAddress (optional)
family = 'family_example' # str | family (optional)
collection_status = 'collection_status_example' # str | collectionStatus (optional)
collection_interval = 'collection_interval_example' # str | collectionInterval (optional)
software_version = 'software_version_example' # str | softwareVersion (optional)
software_type = 'software_type_example' # str | softwareType (optional)
reachability_status = 'reachability_status_example' # str | reachabilityStatus (optional)
reachability_failure_reason = 'reachability_failure_reason_example' # str | reachabilityFailureReason (optional)
error_code = 'error_code_example' # str | errorCode (optional)
platform_id = 'platform_id_example' # str | platformId (optional)
series = 'series_example' # str | series (optional)
type = 'type_example' # str | type (optional)
serial_number = 'serial_number_example' # str | serialNumber (optional)
up_time = 'up_time_example' # str | upTime (optional)
role = 'role_example' # str | role (optional)
role_source = 'role_source_example' # str | roleSource (optional)
associated_wlc_ip = 'associated_wlc_ip_example' # str | associatedWlcIp (optional)
offset = 'offset_example' # str | offset (optional)
limit = 'limit_example' # str | limit (optional)

try:
    # Retrieves all network devices
    api_response = api_instance.api_v1_network_device_autocomplete_get(vrf_name=vrf_name, management_ip_address=management_ip_address, hostname=hostname, mac_address=mac_address, family=family, collection_status=collection_status, collection_interval=collection_interval, software_version=software_version, software_type=software_type, reachability_status=reachability_status, reachability_failure_reason=reachability_failure_reason, error_code=error_code, platform_id=platform_id, series=series, type=type, serial_number=serial_number, up_time=up_time, role=role, role_source=role_source, associated_wlc_ip=associated_wlc_ip, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_autocomplete_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vrf_name** | **str**| vrfName | [optional] 
 **management_ip_address** | **str**| managementIpAddress | [optional] 
 **hostname** | **str**| hostname | [optional] 
 **mac_address** | **str**| macAddress | [optional] 
 **family** | **str**| family | [optional] 
 **collection_status** | **str**| collectionStatus | [optional] 
 **collection_interval** | **str**| collectionInterval | [optional] 
 **software_version** | **str**| softwareVersion | [optional] 
 **software_type** | **str**| softwareType | [optional] 
 **reachability_status** | **str**| reachabilityStatus | [optional] 
 **reachability_failure_reason** | **str**| reachabilityFailureReason | [optional] 
 **error_code** | **str**| errorCode | [optional] 
 **platform_id** | **str**| platformId | [optional] 
 **series** | **str**| series | [optional] 
 **type** | **str**| type | [optional] 
 **serial_number** | **str**| serialNumber | [optional] 
 **up_time** | **str**| upTime | [optional] 
 **role** | **str**| role | [optional] 
 **role_source** | **str**| roleSource | [optional] 
 **associated_wlc_ip** | **str**| associatedWlcIp | [optional] 
 **offset** | **str**| offset | [optional] 
 **limit** | **str**| limit | [optional] 

### Return type

[**RetrievesAllNetworkDevicesResponse**](RetrievesAllNetworkDevicesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_brief_put**
> TaskIdResult api_v1_network_device_brief_put(network_device_brief_nio)

Updates network device role

Updates the role of the device as access, core, distribution, border router

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
network_device_brief_nio = dnac_api_client.NetworkDeviceBriefNIO() # NetworkDeviceBriefNIO | request

try:
    # Updates network device role
    api_response = api_instance.api_v1_network_device_brief_put(network_device_brief_nio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_brief_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_device_brief_nio** | [**NetworkDeviceBriefNIO**](NetworkDeviceBriefNIO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_collection_schedule_global_get**
> CountResult api_v1_network_device_collection_schedule_global_get()

Retrieves the collection interval of all devices

Retrieves collection interval of all devices

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves the collection interval of all devices
    api_response = api_instance.api_v1_network_device_collection_schedule_global_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_collection_schedule_global_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_config_count_get**
> CountResult api_v1_network_device_config_count_get()

Retrieves config count

Gets the count of device configs

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves config count
    api_response = api_instance.api_v1_network_device_config_count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_config_count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_config_get**
> RawCliInfoNIOListResult api_v1_network_device_config_get()

Retrieves device config list

Gets the config for all devices

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves device config list
    api_response = api_instance.api_v1_network_device_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RawCliInfoNIOListResult**](RawCliInfoNIOListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_count_get**
> CountResult api_v1_network_device_count_get()

Retrieves network device count

Gets the count of network devices filtered by management IP address, mac address, hostname and location name

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves network device count
    api_response = api_instance.api_v1_network_device_count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_file_post**
> TaskIdResult api_v1_network_device_file_post(export_device_dto)

Export network-device to file

Export the selected network-device to a file

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
export_device_dto = dnac_api_client.ExportDeviceDTO() # ExportDeviceDTO | request

try:
    # Export network-device to file
    api_response = api_instance.api_v1_network_device_file_post(export_device_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_device_dto** | [**ExportDeviceDTO**](ExportDeviceDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_functional_capability_autocomplete_get**
> SuccessResultList api_v1_network_device_functional_capability_autocomplete_get(function_name=function_name)

Retrieve the values of given fields

Gets the field values based on given filter

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
function_name = ['function_name_example'] # list[str] | functionName (optional)

try:
    # Retrieve the values of given fields
    api_response = api_instance.api_v1_network_device_functional_capability_autocomplete_get(function_name=function_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_functional_capability_autocomplete_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_name** | [**list[str]**](str.md)| functionName | [optional] 

### Return type

[**SuccessResultList**](SuccessResultList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_functional_capability_get**
> FunctionalCapabilityListResult api_v1_network_device_functional_capability_get(device_id=device_id, function_name=function_name)

Retrieves all functional-capability of devices

Gets the functional-capability for given devices

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Accepts comma separated deviceid's and return list of functional-capabilities for the given id's. If invalid or not-found id's are provided, null entry will be returned in the list. (optional)
function_name = ['function_name_example'] # list[str] | functionName (optional)

try:
    # Retrieves all functional-capability of devices
    api_response = api_instance.api_v1_network_device_functional_capability_get(device_id=device_id, function_name=function_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_functional_capability_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Accepts comma separated deviceid&#39;s and return list of functional-capabilities for the given id&#39;s. If invalid or not-found id&#39;s are provided, null entry will be returned in the list. | [optional] 
 **function_name** | [**list[str]**](str.md)| functionName | [optional] 

### Return type

[**FunctionalCapabilityListResult**](FunctionalCapabilityListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_functional_capability_id_get**
> FunctionalCapabilityResult api_v1_network_device_functional_capability_id_get(id)

Gets the functional capability by id

Retrieve functional capability with given id

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Device ID

try:
    # Gets the functional capability by id
    api_response = api_instance.api_v1_network_device_functional_capability_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_functional_capability_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device ID | 

### Return type

[**FunctionalCapabilityResult**](FunctionalCapabilityResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_get**
> NetworkDeviceListResult api_v1_network_device_get(hostname=hostname, management_ip_address=management_ip_address, mac_address=mac_address, location_name=location_name, serial_number=serial_number, location=location, family=family, type=type, series=series, collection_status=collection_status, collection_interval=collection_interval, not_synced_for_minutes=not_synced_for_minutes, error_code=error_code, error_description=error_description, software_version=software_version, software_type=software_type, platform_id=platform_id, role=role, reachability_status=reachability_status, up_time=up_time, associated_wlc_ip=associated_wlc_ip, license_name=license_name, license_type=license_type, license_status=license_status, modulename=modulename, moduleequpimenttype=moduleequpimenttype, moduleservicestate=moduleservicestate, modulevendorequipmenttype=modulevendorequipmenttype, modulepartnumber=modulepartnumber, moduleoperationstatecode=moduleoperationstatecode, id=id)

Retrieves all network devices

Gets the list of first 500 network devices sorted lexicographically based on host name. It can be filtered using management IP address, mac address, hostname and location name. If id param is provided, it will be returning the list of network-devices for the given id's and other request params will be ignored. In case of autocomplete request, returns the list of specified attributes.

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
hostname = ['hostname_example'] # list[str] | hostname (optional)
management_ip_address = ['management_ip_address_example'] # list[str] | managementIpAddress (optional)
mac_address = ['mac_address_example'] # list[str] | macAddress (optional)
location_name = ['location_name_example'] # list[str] | locationName (optional)
serial_number = ['serial_number_example'] # list[str] | serialNumber (optional)
location = ['location_example'] # list[str] | location (optional)
family = ['family_example'] # list[str] | family (optional)
type = ['type_example'] # list[str] | type (optional)
series = ['series_example'] # list[str] | series (optional)
collection_status = ['collection_status_example'] # list[str] | collectionStatus (optional)
collection_interval = ['collection_interval_example'] # list[str] | collectionInterval (optional)
not_synced_for_minutes = ['not_synced_for_minutes_example'] # list[str] | notSyncedForMinutes (optional)
error_code = ['error_code_example'] # list[str] | errorCode (optional)
error_description = ['error_description_example'] # list[str] | errorDescription (optional)
software_version = ['software_version_example'] # list[str] | softwareVersion (optional)
software_type = ['software_type_example'] # list[str] | softwareType (optional)
platform_id = ['platform_id_example'] # list[str] | platformId (optional)
role = ['role_example'] # list[str] | role (optional)
reachability_status = ['reachability_status_example'] # list[str] | reachabilityStatus (optional)
up_time = ['up_time_example'] # list[str] | upTime (optional)
associated_wlc_ip = ['associated_wlc_ip_example'] # list[str] | associatedWlcIp (optional)
license_name = ['license_name_example'] # list[str] | licenseName (optional)
license_type = ['license_type_example'] # list[str] | licenseType (optional)
license_status = ['license_status_example'] # list[str] | licenseStatus (optional)
modulename = ['modulename_example'] # list[str] | moduleName (optional)
moduleequpimenttype = ['moduleequpimenttype_example'] # list[str] | moduleEqupimentType (optional)
moduleservicestate = ['moduleservicestate_example'] # list[str] | moduleServiceState (optional)
modulevendorequipmenttype = ['modulevendorequipmenttype_example'] # list[str] | moduleVendorEquipmentType (optional)
modulepartnumber = ['modulepartnumber_example'] # list[str] | modulePartNumber (optional)
moduleoperationstatecode = ['moduleoperationstatecode_example'] # list[str] | moduleOperationStateCode (optional)
id = 'id_example' # str | Accepts comma separated id's and return list of network-devices for the given id's. If invalid or not-found id's are provided, null entry will be returned in the list. (optional)

try:
    # Retrieves all network devices
    api_response = api_instance.api_v1_network_device_get(hostname=hostname, management_ip_address=management_ip_address, mac_address=mac_address, location_name=location_name, serial_number=serial_number, location=location, family=family, type=type, series=series, collection_status=collection_status, collection_interval=collection_interval, not_synced_for_minutes=not_synced_for_minutes, error_code=error_code, error_description=error_description, software_version=software_version, software_type=software_type, platform_id=platform_id, role=role, reachability_status=reachability_status, up_time=up_time, associated_wlc_ip=associated_wlc_ip, license_name=license_name, license_type=license_type, license_status=license_status, modulename=modulename, moduleequpimenttype=moduleequpimenttype, moduleservicestate=moduleservicestate, modulevendorequipmenttype=modulevendorequipmenttype, modulepartnumber=modulepartnumber, moduleoperationstatecode=moduleoperationstatecode, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | [**list[str]**](str.md)| hostname | [optional] 
 **management_ip_address** | [**list[str]**](str.md)| managementIpAddress | [optional] 
 **mac_address** | [**list[str]**](str.md)| macAddress | [optional] 
 **location_name** | [**list[str]**](str.md)| locationName | [optional] 
 **serial_number** | [**list[str]**](str.md)| serialNumber | [optional] 
 **location** | [**list[str]**](str.md)| location | [optional] 
 **family** | [**list[str]**](str.md)| family | [optional] 
 **type** | [**list[str]**](str.md)| type | [optional] 
 **series** | [**list[str]**](str.md)| series | [optional] 
 **collection_status** | [**list[str]**](str.md)| collectionStatus | [optional] 
 **collection_interval** | [**list[str]**](str.md)| collectionInterval | [optional] 
 **not_synced_for_minutes** | [**list[str]**](str.md)| notSyncedForMinutes | [optional] 
 **error_code** | [**list[str]**](str.md)| errorCode | [optional] 
 **error_description** | [**list[str]**](str.md)| errorDescription | [optional] 
 **software_version** | [**list[str]**](str.md)| softwareVersion | [optional] 
 **software_type** | [**list[str]**](str.md)| softwareType | [optional] 
 **platform_id** | [**list[str]**](str.md)| platformId | [optional] 
 **role** | [**list[str]**](str.md)| role | [optional] 
 **reachability_status** | [**list[str]**](str.md)| reachabilityStatus | [optional] 
 **up_time** | [**list[str]**](str.md)| upTime | [optional] 
 **associated_wlc_ip** | [**list[str]**](str.md)| associatedWlcIp | [optional] 
 **license_name** | [**list[str]**](str.md)| licenseName | [optional] 
 **license_type** | [**list[str]**](str.md)| licenseType | [optional] 
 **license_status** | [**list[str]**](str.md)| licenseStatus | [optional] 
 **modulename** | [**list[str]**](str.md)| moduleName | [optional] 
 **moduleequpimenttype** | [**list[str]**](str.md)| moduleEqupimentType | [optional] 
 **moduleservicestate** | [**list[str]**](str.md)| moduleServiceState | [optional] 
 **modulevendorequipmenttype** | [**list[str]**](str.md)| moduleVendorEquipmentType | [optional] 
 **modulepartnumber** | [**list[str]**](str.md)| modulePartNumber | [optional] 
 **moduleoperationstatecode** | [**list[str]**](str.md)| moduleOperationStateCode | [optional] 
 **id** | **str**| Accepts comma separated id&#39;s and return list of network-devices for the given id&#39;s. If invalid or not-found id&#39;s are provided, null entry will be returned in the list. | [optional] 

### Return type

[**NetworkDeviceListResult**](NetworkDeviceListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_id_brief_get**
> NetworkDeviceBriefNIOResult api_v1_network_device_id_brief_get(id)

Retrieves network device brief by ID

Gets brief network device info such as hostname, management IP address for the given device ID

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Device ID

try:
    # Retrieves network device brief by ID
    api_response = api_instance.api_v1_network_device_id_brief_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_id_brief_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device ID | 

### Return type

[**NetworkDeviceBriefNIOResult**](NetworkDeviceBriefNIOResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_id_collection_schedule_get**
> CountResult api_v1_network_device_id_collection_schedule_get(id)

Retrieves the collection interval specified by device ID

Retrieves collection interval by device id

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Device ID

try:
    # Retrieves the collection interval specified by device ID
    api_response = api_instance.api_v1_network_device_id_collection_schedule_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_id_collection_schedule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device ID | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_id_delete**
> TaskIdResult api_v1_network_device_id_delete(id, is_force_delete=is_force_delete)

Delete network device by ID

Removes the network device for the given ID

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Device ID
is_force_delete = True # bool | isForceDelete (optional)

try:
    # Delete network device by ID
    api_response = api_instance.api_v1_network_device_id_delete(id, is_force_delete=is_force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device ID | 
 **is_force_delete** | **bool**| isForceDelete | [optional] 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_id_get**
> NetworkDeviceResult api_v1_network_device_id_get(id)

Retrieves network device by ID

Gets the network device for the given device ID

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Device ID

try:
    # Retrieves network device by ID
    api_response = api_instance.api_v1_network_device_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device ID | 

### Return type

[**NetworkDeviceResult**](NetworkDeviceResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_id_meraki_organization_get**
> SuccessResultList api_v1_network_device_id_meraki_organization_get(id)

Get the organizations chosen while adding the meraki dashboard

This method is used to get the selected organizations for the meraki dashboard

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Get the organizations chosen while adding the meraki dashboard
    api_response = api_instance.api_v1_network_device_id_meraki_organization_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_id_meraki_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**SuccessResultList**](SuccessResultList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_id_vlan_get**
> VlanListResult api_v1_network_device_id_vlan_get(id, interface_type=interface_type)

Retrieves list of VLAN data that are associated with interface for a device

getDeviceVLANData

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | deviceUUID
interface_type = 'interface_type_example' # str | Vlan assocaited with sub-interface (optional)

try:
    # Retrieves list of VLAN data that are associated with interface for a device
    api_response = api_instance.api_v1_network_device_id_vlan_get(id, interface_type=interface_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_id_vlan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| deviceUUID | 
 **interface_type** | **str**| Vlan assocaited with sub-interface | [optional] 

### Return type

[**VlanListResult**](VlanListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_id_wireless_info_get**
> WirelessInfoResult api_v1_network_device_id_wireless_info_get(id)

Retrieves wireless lan conrtoller info by Device ID

Gets the wireless lan controller info using the given device ID

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Device ID

try:
    # Retrieves wireless lan conrtoller info by Device ID
    api_response = api_instance.api_v1_network_device_id_wireless_info_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_id_wireless_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device ID | 

### Return type

[**WirelessInfoResult**](WirelessInfoResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_ip_address_ip_address_get**
> NetworkDeviceResult api_v1_network_device_ip_address_ip_address_get(ip_address)

Retrieves network device by IP address

Gets the network device with the given IP address

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
ip_address = 'ip_address_example' # str | Device IP address

try:
    # Retrieves network device by IP address
    api_response = api_instance.api_v1_network_device_ip_address_ip_address_get(ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_ip_address_ip_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| Device IP address | 

### Return type

[**NetworkDeviceResult**](NetworkDeviceResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_module_count_get**
> CountResult api_v1_network_device_module_count_get(device_id, name_list=name_list, vendor_equipment_type_list=vendor_equipment_type_list, part_number_list=part_number_list, operational_state_code_list=operational_state_code_list)

Gives total number of Modules

Get Module Count

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
device_id = 'device_id_example' # str | deviceId
name_list = ['name_list_example'] # list[str] | nameList (optional)
vendor_equipment_type_list = ['vendor_equipment_type_list_example'] # list[str] | vendorEquipmentTypeList (optional)
part_number_list = ['part_number_list_example'] # list[str] | partNumberList (optional)
operational_state_code_list = ['operational_state_code_list_example'] # list[str] | operationalStateCodeList (optional)

try:
    # Gives total number of Modules
    api_response = api_instance.api_v1_network_device_module_count_get(device_id, name_list=name_list, vendor_equipment_type_list=vendor_equipment_type_list, part_number_list=part_number_list, operational_state_code_list=operational_state_code_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_module_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 
 **name_list** | [**list[str]**](str.md)| nameList | [optional] 
 **vendor_equipment_type_list** | [**list[str]**](str.md)| vendorEquipmentTypeList | [optional] 
 **part_number_list** | [**list[str]**](str.md)| partNumberList | [optional] 
 **operational_state_code_list** | [**list[str]**](str.md)| operationalStateCodeList | [optional] 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_module_get**
> ModuleListResult api_v1_network_device_module_get(device_id, limit=limit, offset=offset, name_list=name_list, vendor_equipment_type_list=vendor_equipment_type_list, part_number_list=part_number_list, operational_state_code_list=operational_state_code_list)

Gives all the modules associated with given device id

Get modules of the given device id

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
device_id = 'device_id_example' # str | deviceId
limit = 'limit_example' # str | limit (optional)
offset = 'offset_example' # str | offset (optional)
name_list = ['name_list_example'] # list[str] | nameList (optional)
vendor_equipment_type_list = ['vendor_equipment_type_list_example'] # list[str] | vendorEquipmentTypeList (optional)
part_number_list = ['part_number_list_example'] # list[str] | partNumberList (optional)
operational_state_code_list = ['operational_state_code_list_example'] # list[str] | operationalStateCodeList (optional)

try:
    # Gives all the modules associated with given device id
    api_response = api_instance.api_v1_network_device_module_get(device_id, limit=limit, offset=offset, name_list=name_list, vendor_equipment_type_list=vendor_equipment_type_list, part_number_list=part_number_list, operational_state_code_list=operational_state_code_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_module_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 
 **limit** | **str**| limit | [optional] 
 **offset** | **str**| offset | [optional] 
 **name_list** | [**list[str]**](str.md)| nameList | [optional] 
 **vendor_equipment_type_list** | [**list[str]**](str.md)| vendorEquipmentTypeList | [optional] 
 **part_number_list** | [**list[str]**](str.md)| partNumberList | [optional] 
 **operational_state_code_list** | [**list[str]**](str.md)| operationalStateCodeList | [optional] 

### Return type

[**ModuleListResult**](ModuleListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_module_id_get**
> ModuleResult api_v1_network_device_module_id_get(id)

Gives Module info by its id

Get module by id

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Gives Module info by its id
    api_response = api_instance.api_v1_network_device_module_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_module_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**ModuleResult**](ModuleResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_network_device_id_config_get**
> SuccessResult api_v1_network_device_network_device_id_config_get(network_device_id)

Retrieves device config

Gets the device config by device ID

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
network_device_id = 'network_device_id_example' # str | networkDeviceId

try:
    # Retrieves device config
    api_response = api_instance.api_v1_network_device_network_device_id_config_get(network_device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_network_device_id_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_device_id** | **str**| networkDeviceId | 

### Return type

[**SuccessResult**](SuccessResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_post**
> TaskIdResult api_v1_network_device_post(inventory_device_info)

Network device POST api

Adds the device with given credential

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
inventory_device_info = dnac_api_client.InventoryDeviceInfo() # InventoryDeviceInfo | request

try:
    # Network device POST api
    api_response = api_instance.api_v1_network_device_post(inventory_device_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_device_info** | [**InventoryDeviceInfo**](InventoryDeviceInfo.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_put**
> TaskIdResult api_v1_network_device_put(inventory_device_info)

Network device sync api

Sync the devices provided as input

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
inventory_device_info = dnac_api_client.InventoryDeviceInfo() # InventoryDeviceInfo | request

try:
    # Network device sync api
    api_response = api_instance.api_v1_network_device_put(inventory_device_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_device_info** | [**InventoryDeviceInfo**](InventoryDeviceInfo.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_serial_number_serial_number_get**
> NetworkDeviceResult api_v1_network_device_serial_number_serial_number_get(serial_number)

Retrieves network device by serial number

Gets the network device with the given serial number

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
serial_number = 'serial_number_example' # str | Device serial number

try:
    # Retrieves network device by serial number
    api_response = api_instance.api_v1_network_device_serial_number_serial_number_get(serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_serial_number_serial_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| Device serial number | 

### Return type

[**NetworkDeviceResult**](NetworkDeviceResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_start_index_records_to_return_get**
> NetworkDeviceListResult api_v1_network_device_start_index_records_to_return_get(start_index, records_to_return)

Retrieves network device by range

Gets the list of network devices for the given range

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
start_index = 56 # int | Start index
records_to_return = 56 # int | Number of records to return

try:
    # Retrieves network device by range
    api_response = api_instance.api_v1_network_device_start_index_records_to_return_get(start_index, records_to_return)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_start_index_records_to_return_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Start index | 
 **records_to_return** | **int**| Number of records to return | 

### Return type

[**NetworkDeviceListResult**](NetworkDeviceListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_sync_put**
> TaskIdResult api_v1_network_device_sync_put(request_body, force_sync=force_sync)

Network device sync api

Sync's the devices. If forceSync param is false (default) then the sync would run in normal priority thread. If forceSync param is true then the sync would run in high priority thread if avaiable, else the sync will fail. Result can be seen in the child task of each device

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
request_body = NULL # list[object] | request
force_sync = True # bool | forceSync (optional)

try:
    # Network device sync api
    api_response = api_instance.api_v1_network_device_sync_put(request_body, force_sync=force_sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_sync_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[object]**](list.md)| request | 
 **force_sync** | **bool**| forceSync | [optional] 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_tenantinfo_macaddress_get**
> RegisterNetworkDeviceResult api_v1_network_device_tenantinfo_macaddress_get(serial_number=serial_number, macaddress=macaddress)

Updates certificate validation status and returns tenantId

Registers a device for WSA notification

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
serial_number = 'serial_number_example' # str | Serial number of the device (optional)
macaddress = 'macaddress_example' # str | Mac addres of the device (optional)

try:
    # Updates certificate validation status and returns tenantId
    api_response = api_instance.api_v1_network_device_tenantinfo_macaddress_get(serial_number=serial_number, macaddress=macaddress)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_network_device_tenantinfo_macaddress_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| Serial number of the device | [optional] 
 **macaddress** | **str**| Mac addres of the device | [optional] 

### Return type

[**RegisterNetworkDeviceResult**](RegisterNetworkDeviceResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_snmp_property_get**
> SystemPropertyListResult api_v1_snmp_property_get()

Retrieves SNMP properties

This method is used to get SNMP properties

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves SNMP properties
    api_response = api_instance.api_v1_snmp_property_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_snmp_property_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemPropertyListResult**](SystemPropertyListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_snmp_property_post**
> TaskIdResult api_v1_snmp_property_post(request_body)

Creates or updates SNMP properties

This method is used to add SNMP properties

### Example

* Api Key Authentication (APIKeyHeader): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = dnac_api_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = dnac_api_client.NetworkDeviceApi(dnac_api_client.ApiClient(configuration))
request_body = NULL # list[object] | request

try:
    # Creates or updates SNMP properties
    api_response = api_instance.api_v1_snmp_property_post(request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDeviceApi->api_v1_snmp_property_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[object]**](list.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

