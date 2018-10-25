# dnac_api_client.NetworksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_topology_l2_vlan_id_get**](NetworksApi.md#api_v1_topology_l2_vlan_id_get) | **GET** /api/v1/topology/l2/{vlanID} | getL2Topology
[**api_v1_topology_l3_topology_type_get**](NetworksApi.md#api_v1_topology_l3_topology_type_get) | **GET** /api/v1/topology/l3/{topologyType} | getL3Topology
[**api_v1_topology_physical_topology_get**](NetworksApi.md#api_v1_topology_physical_topology_get) | **GET** /api/v1/topology/physical-topology | getPhysicalTopology
[**api_v1_topology_site_topology_get**](NetworksApi.md#api_v1_topology_site_topology_get) | **GET** /api/v1/topology/site-topology | getSiteTopology
[**api_v1_topology_vlan_vlan_names_get**](NetworksApi.md#api_v1_topology_vlan_vlan_names_get) | **GET** /api/v1/topology/vlan/vlan-names | getVlanNames


# **api_v1_topology_l2_vlan_id_get**
> TopologyResult api_v1_topology_l2_vlan_id_get(vlan_id)

getL2Topology

This method is used to obtain the Layer 2 topology by Vlan ID

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
api_instance = dnac_api_client.NetworksApi(dnac_api_client.ApiClient(configuration))
vlan_id = 'vlan_id_example' # str | Vlan Name for e.g Vlan1, Vlan23 etc

try:
    # getL2Topology
    api_response = api_instance.api_v1_topology_l2_vlan_id_get(vlan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->api_v1_topology_l2_vlan_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan_id** | **str**| Vlan Name for e.g Vlan1, Vlan23 etc | 

### Return type

[**TopologyResult**](TopologyResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_topology_l3_topology_type_get**
> TopologyResult api_v1_topology_l3_topology_type_get(topology_type)

getL3Topology

This method is used to obtain Layer 3 device topology by routing protocol type

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
api_instance = dnac_api_client.NetworksApi(dnac_api_client.ApiClient(configuration))
topology_type = 'topology_type_example' # str | Type of topology(OSPF,ISIS,etc)

try:
    # getL3Topology
    api_response = api_instance.api_v1_topology_l3_topology_type_get(topology_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->api_v1_topology_l3_topology_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_type** | **str**| Type of topology(OSPF,ISIS,etc) | 

### Return type

[**TopologyResult**](TopologyResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_topology_physical_topology_get**
> TopologyResult api_v1_topology_physical_topology_get(node_type=node_type)

getPhysicalTopology

This method is used to obtain the raw physical topology and filter based on nodeType

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
api_instance = dnac_api_client.NetworksApi(dnac_api_client.ApiClient(configuration))
node_type = 'node_type_example' # str | nodeType (optional)

try:
    # getPhysicalTopology
    api_response = api_instance.api_v1_topology_physical_topology_get(node_type=node_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->api_v1_topology_physical_topology_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_type** | **str**| nodeType | [optional] 

### Return type

[**TopologyResult**](TopologyResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_topology_site_topology_get**
> SiteResult api_v1_topology_site_topology_get()

getSiteTopology

This method is used to obtain the site topology

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
api_instance = dnac_api_client.NetworksApi(dnac_api_client.ApiClient(configuration))

try:
    # getSiteTopology
    api_response = api_instance.api_v1_topology_site_topology_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->api_v1_topology_site_topology_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SiteResult**](SiteResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_topology_vlan_vlan_names_get**
> VlanNamesResult api_v1_topology_vlan_vlan_names_get()

getVlanNames

This method is used to obtain the list of vlan names

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
api_instance = dnac_api_client.NetworksApi(dnac_api_client.ApiClient(configuration))

try:
    # getVlanNames
    api_response = api_instance.api_v1_topology_vlan_vlan_names_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->api_v1_topology_vlan_vlan_names_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VlanNamesResult**](VlanNamesResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

