# dnac_api_client.NetworkDiscoveryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_discovery_count_get**](NetworkDiscoveryApi.md#api_v1_discovery_count_get) | **GET** /api/v1/discovery/count | Retrieves the number of discoveries
[**api_v1_discovery_delete**](NetworkDiscoveryApi.md#api_v1_discovery_delete) | **DELETE** /api/v1/discovery | Deletes all discovery
[**api_v1_discovery_id_auto_complete_get**](NetworkDiscoveryApi.md#api_v1_discovery_id_auto_complete_get) | **GET** /api/v1/discovery/{id}/autoComplete | Retrieve autoComplete values from a discovery based on id
[**api_v1_discovery_id_delete**](NetworkDiscoveryApi.md#api_v1_discovery_id_delete) | **DELETE** /api/v1/discovery/{id} | Deletes the discovery specified by id
[**api_v1_discovery_id_get**](NetworkDiscoveryApi.md#api_v1_discovery_id_get) | **GET** /api/v1/discovery/{id} | Retrieves the discovery specified by id
[**api_v1_discovery_id_job_get**](NetworkDiscoveryApi.md#api_v1_discovery_id_job_get) | **GET** /api/v1/discovery/{id}/job | Retrieves list of discovery jobs for the specified discovery id
[**api_v1_discovery_id_network_device_count_get**](NetworkDiscoveryApi.md#api_v1_discovery_id_network_device_count_get) | **GET** /api/v1/discovery/{id}/network-device/count | Retrieves the number of network devices discovered in the discovery specified by id
[**api_v1_discovery_id_network_device_get**](NetworkDiscoveryApi.md#api_v1_discovery_id_network_device_get) | **GET** /api/v1/discovery/{id}/network-device | Retrieves the network devices discovered in the discovery specified by id
[**api_v1_discovery_id_network_device_start_index_records_to_return_get**](NetworkDiscoveryApi.md#api_v1_discovery_id_network_device_start_index_records_to_return_get) | **GET** /api/v1/discovery/{id}/network-device/{startIndex}/{recordsToReturn} | Retrieves the range of network devices discovered for the given discovery
[**api_v1_discovery_id_summary_get**](NetworkDiscoveryApi.md#api_v1_discovery_id_summary_get) | **GET** /api/v1/discovery/{id}/summary | Retrieve network devices from a discovery on given filters
[**api_v1_discovery_job_get**](NetworkDiscoveryApi.md#api_v1_discovery_job_get) | **GET** /api/v1/discovery/job | Retrieves the list of discovery jobs for the given IP
[**api_v1_discovery_post**](NetworkDiscoveryApi.md#api_v1_discovery_post) | **POST** /api/v1/discovery | Starts a new discovery process and returns a task-id
[**api_v1_discovery_put**](NetworkDiscoveryApi.md#api_v1_discovery_put) | **PUT** /api/v1/discovery | Updates an existing discovery specified by id - only for starting/stopping the discovery
[**api_v1_discovery_start_index_records_to_delete_delete**](NetworkDiscoveryApi.md#api_v1_discovery_start_index_records_to_delete_delete) | **DELETE** /api/v1/discovery/{startIndex}/{recordsToDelete} | Deletes the discovery in the given range
[**api_v1_discovery_start_index_records_to_return_get**](NetworkDiscoveryApi.md#api_v1_discovery_start_index_records_to_return_get) | **GET** /api/v1/discovery/{startIndex}/{recordsToReturn} | Retrieves the discovery in the given range
[**api_v1_global_credential_cli_post**](NetworkDiscoveryApi.md#api_v1_global_credential_cli_post) | **POST** /api/v1/global-credential/cli | Creates global CLI credential
[**api_v1_global_credential_cli_put**](NetworkDiscoveryApi.md#api_v1_global_credential_cli_put) | **PUT** /api/v1/global-credential/cli | Updates global CLI credential
[**api_v1_global_credential_get**](NetworkDiscoveryApi.md#api_v1_global_credential_get) | **GET** /api/v1/global-credential | Retrieves global credential for the given credential sub type
[**api_v1_global_credential_global_credential_id_delete**](NetworkDiscoveryApi.md#api_v1_global_credential_global_credential_id_delete) | **DELETE** /api/v1/global-credential/{globalCredentialId} | Retrieves global credential by ID
[**api_v1_global_credential_global_credential_id_put**](NetworkDiscoveryApi.md#api_v1_global_credential_global_credential_id_put) | **PUT** /api/v1/global-credential/{globalCredentialId} | Update global credential for network devices in site(s)
[**api_v1_global_credential_http_read_post**](NetworkDiscoveryApi.md#api_v1_global_credential_http_read_post) | **POST** /api/v1/global-credential/http-read | Creates global HTTP read credentials
[**api_v1_global_credential_http_read_put**](NetworkDiscoveryApi.md#api_v1_global_credential_http_read_put) | **PUT** /api/v1/global-credential/http-read | Updates global HTTP Read credential
[**api_v1_global_credential_http_write_post**](NetworkDiscoveryApi.md#api_v1_global_credential_http_write_post) | **POST** /api/v1/global-credential/http-write | Creates global HTTP write credentials
[**api_v1_global_credential_http_write_put**](NetworkDiscoveryApi.md#api_v1_global_credential_http_write_put) | **PUT** /api/v1/global-credential/http-write | Updates global HTTP Write credential
[**api_v1_global_credential_id_get**](NetworkDiscoveryApi.md#api_v1_global_credential_id_get) | **GET** /api/v1/global-credential/{id} | Retrieves credential sub type for the given credential Id
[**api_v1_global_credential_netconf_post**](NetworkDiscoveryApi.md#api_v1_global_credential_netconf_post) | **POST** /api/v1/global-credential/netconf | Creates global netconf credential
[**api_v1_global_credential_netconf_put**](NetworkDiscoveryApi.md#api_v1_global_credential_netconf_put) | **PUT** /api/v1/global-credential/netconf | Updates global netconf credential
[**api_v1_global_credential_snmpv2_read_community_post**](NetworkDiscoveryApi.md#api_v1_global_credential_snmpv2_read_community_post) | **POST** /api/v1/global-credential/snmpv2-read-community | Creates global SNMP read community
[**api_v1_global_credential_snmpv2_read_community_put**](NetworkDiscoveryApi.md#api_v1_global_credential_snmpv2_read_community_put) | **PUT** /api/v1/global-credential/snmpv2-read-community | Updates global SNMP read community
[**api_v1_global_credential_snmpv2_write_community_post**](NetworkDiscoveryApi.md#api_v1_global_credential_snmpv2_write_community_post) | **POST** /api/v1/global-credential/snmpv2-write-community | Creates global SNMP write community
[**api_v1_global_credential_snmpv2_write_community_put**](NetworkDiscoveryApi.md#api_v1_global_credential_snmpv2_write_community_put) | **PUT** /api/v1/global-credential/snmpv2-write-community | Updates global SNMP write community
[**api_v1_global_credential_snmpv3_post**](NetworkDiscoveryApi.md#api_v1_global_credential_snmpv3_post) | **POST** /api/v1/global-credential/snmpv3 | Creates global SNMPv3 credential
[**api_v1_global_credential_snmpv3_put**](NetworkDiscoveryApi.md#api_v1_global_credential_snmpv3_put) | **PUT** /api/v1/global-credential/snmpv3 | Updates global SNMPv3 credential


# **api_v1_discovery_count_get**
> CountResult api_v1_discovery_count_get()

Retrieves the number of discoveries

Gets the count of all available discovery jobs

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))

try:
    # Retrieves the number of discoveries
    api_response = api_instance.api_v1_discovery_count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_delete**
> TaskIdResult api_v1_discovery_delete()

Deletes all discovery

Stops all the discoveries and removes them

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))

try:
    # Deletes all discovery
    api_response = api_instance.api_v1_discovery_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_id_auto_complete_get**
> SuccessResultList api_v1_discovery_id_auto_complete_get(id, task_id=task_id, ip_address=ip_address, ping_status=ping_status, snmp_status=snmp_status, cli_status=cli_status, netconf_status=netconf_status, http_status=http_status)

Retrieve autoComplete values from a discovery based on id

Gets the autoComplete values from a discovery job

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | id
task_id = 'task_id_example' # str | taskId (optional)
ip_address = 'ip_address_example' # str | ipAddress (optional)
ping_status = 'ping_status_example' # str | pingStatus (optional)
snmp_status = 'snmp_status_example' # str | snmpStatus (optional)
cli_status = 'cli_status_example' # str | cliStatus (optional)
netconf_status = 'netconf_status_example' # str | netconfStatus (optional)
http_status = 'http_status_example' # str | httpStatus (optional)

try:
    # Retrieve autoComplete values from a discovery based on id
    api_response = api_instance.api_v1_discovery_id_auto_complete_get(id, task_id=task_id, ip_address=ip_address, ping_status=ping_status, snmp_status=snmp_status, cli_status=cli_status, netconf_status=netconf_status, http_status=http_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_id_auto_complete_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **task_id** | **str**| taskId | [optional] 
 **ip_address** | **str**| ipAddress | [optional] 
 **ping_status** | **str**| pingStatus | [optional] 
 **snmp_status** | **str**| snmpStatus | [optional] 
 **cli_status** | **str**| cliStatus | [optional] 
 **netconf_status** | **str**| netconfStatus | [optional] 
 **http_status** | **str**| httpStatus | [optional] 

### Return type

[**SuccessResultList**](SuccessResultList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_id_delete**
> TaskIdResult api_v1_discovery_id_delete(id)

Deletes the discovery specified by id

Stops the discovery for the given ID and removes it

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Discovery ID

try:
    # Deletes the discovery specified by id
    api_response = api_instance.api_v1_discovery_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Discovery ID | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_id_get**
> DiscoveryNIOResult api_v1_discovery_id_get(id)

Retrieves the discovery specified by id

Gets discovery by ID

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Discovery ID

try:
    # Retrieves the discovery specified by id
    api_response = api_instance.api_v1_discovery_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Discovery ID | 

### Return type

[**DiscoveryNIOResult**](DiscoveryNIOResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_id_job_get**
> DiscoveryJobNIOListResult api_v1_discovery_id_job_get(id, offset=offset, limit=limit, ip_address=ip_address)

Retrieves list of discovery jobs for the specified discovery id

Gets the list of discovery jobs for the given id. The result can optionally be filtered based on IP

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Discovery ID
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
ip_address = 'ip_address_example' # str | ipAddress (optional)

try:
    # Retrieves list of discovery jobs for the specified discovery id
    api_response = api_instance.api_v1_discovery_id_job_get(id, offset=offset, limit=limit, ip_address=ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_id_job_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Discovery ID | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **ip_address** | **str**| ipAddress | [optional] 

### Return type

[**DiscoveryJobNIOListResult**](DiscoveryJobNIOListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_id_network_device_count_get**
> CountResult api_v1_discovery_id_network_device_count_get(id, task_id=task_id)

Retrieves the number of network devices discovered in the discovery specified by id

Gets the count of network devices discovered in the given discovery

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Discovery ID
task_id = 'task_id_example' # str | taskId (optional)

try:
    # Retrieves the number of network devices discovered in the discovery specified by id
    api_response = api_instance.api_v1_discovery_id_network_device_count_get(id, task_id=task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_id_network_device_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Discovery ID | 
 **task_id** | **str**| taskId | [optional] 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_id_network_device_get**
> NetworkDeviceNIOListResult api_v1_discovery_id_network_device_get(id, task_id=task_id)

Retrieves the network devices discovered in the discovery specified by id

Gets the network devices discovered for the given discovery

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | id
task_id = 'task_id_example' # str | taskId (optional)

try:
    # Retrieves the network devices discovered in the discovery specified by id
    api_response = api_instance.api_v1_discovery_id_network_device_get(id, task_id=task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_id_network_device_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **task_id** | **str**| taskId | [optional] 

### Return type

[**NetworkDeviceNIOListResult**](NetworkDeviceNIOListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_id_network_device_start_index_records_to_return_get**
> NetworkDeviceNIOListResult api_v1_discovery_id_network_device_start_index_records_to_return_get(id, start_index, records_to_return, task_id=task_id)

Retrieves the range of network devices discovered for the given discovery

Gets the network devices discovered for the given discovery and for the given range. The maximum number of records that could be retrieved is 500

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Discovery ID
start_index = 56 # int | Start index
records_to_return = 56 # int | Number of records to return
task_id = 'task_id_example' # str | taskId (optional)

try:
    # Retrieves the range of network devices discovered for the given discovery
    api_response = api_instance.api_v1_discovery_id_network_device_start_index_records_to_return_get(id, start_index, records_to_return, task_id=task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_id_network_device_start_index_records_to_return_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Discovery ID | 
 **start_index** | **int**| Start index | 
 **records_to_return** | **int**| Number of records to return | 
 **task_id** | **str**| taskId | [optional] 

### Return type

[**NetworkDeviceNIOListResult**](NetworkDeviceNIOListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_id_summary_get**
> CountResult api_v1_discovery_id_summary_get(id, task_id=task_id, sort_by=sort_by, sort_order=sort_order, ip_address=ip_address, ping_status=ping_status, snmp_status=snmp_status, cli_status=cli_status, netconf_status=netconf_status, http_status=http_status)

Retrieve network devices from a discovery on given filters

Gets the network devices from a discovery job based on given filters

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | id
task_id = 'task_id_example' # str | taskId (optional)
sort_by = 'sort_by_example' # str | sortBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)
ip_address = ['ip_address_example'] # list[str] | ipAddress (optional)
ping_status = ['ping_status_example'] # list[str] | pingStatus (optional)
snmp_status = ['snmp_status_example'] # list[str] | snmpStatus (optional)
cli_status = ['cli_status_example'] # list[str] | cliStatus (optional)
netconf_status = ['netconf_status_example'] # list[str] | netconfStatus (optional)
http_status = ['http_status_example'] # list[str] | httpStatus (optional)

try:
    # Retrieve network devices from a discovery on given filters
    api_response = api_instance.api_v1_discovery_id_summary_get(id, task_id=task_id, sort_by=sort_by, sort_order=sort_order, ip_address=ip_address, ping_status=ping_status, snmp_status=snmp_status, cli_status=cli_status, netconf_status=netconf_status, http_status=http_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_id_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **task_id** | **str**| taskId | [optional] 
 **sort_by** | **str**| sortBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 
 **ip_address** | [**list[str]**](str.md)| ipAddress | [optional] 
 **ping_status** | [**list[str]**](str.md)| pingStatus | [optional] 
 **snmp_status** | [**list[str]**](str.md)| snmpStatus | [optional] 
 **cli_status** | [**list[str]**](str.md)| cliStatus | [optional] 
 **netconf_status** | [**list[str]**](str.md)| netconfStatus | [optional] 
 **http_status** | [**list[str]**](str.md)| httpStatus | [optional] 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_job_get**
> DiscoveryJobNIOListResult api_v1_discovery_job_get(ip_address, offset=offset, limit=limit, name=name)

Retrieves the list of discovery jobs for the given IP

Gets the list of discovery jobs for the given IP

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
ip_address = 'ip_address_example' # str | ipAddress
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
name = 'name_example' # str | name (optional)

try:
    # Retrieves the list of discovery jobs for the given IP
    api_response = api_instance.api_v1_discovery_job_get(ip_address, offset=offset, limit=limit, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_job_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| ipAddress | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **name** | **str**| name | [optional] 

### Return type

[**DiscoveryJobNIOListResult**](DiscoveryJobNIOListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_post**
> TaskIdResult api_v1_discovery_post(request)

Starts a new discovery process and returns a task-id

Initiates discovery with the given parameters

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.InventoryRequest() # InventoryRequest | request

try:
    # Starts a new discovery process and returns a task-id
    api_response = api_instance.api_v1_discovery_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InventoryRequest**](InventoryRequest.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_put**
> TaskIdResult api_v1_discovery_put(request)

Updates an existing discovery specified by id - only for starting/stopping the discovery

Stops or starts an existing discovery

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.DiscoveryNIO() # DiscoveryNIO | request

try:
    # Updates an existing discovery specified by id - only for starting/stopping the discovery
    api_response = api_instance.api_v1_discovery_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DiscoveryNIO**](DiscoveryNIO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_start_index_records_to_delete_delete**
> TaskIdResult api_v1_discovery_start_index_records_to_delete_delete(start_index, records_to_delete)

Deletes the discovery in the given range

Stops discovery for the given range and removes them

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
start_index = 56 # int | Start index
records_to_delete = 56 # int | Number of records to delete

try:
    # Deletes the discovery in the given range
    api_response = api_instance.api_v1_discovery_start_index_records_to_delete_delete(start_index, records_to_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_start_index_records_to_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Start index | 
 **records_to_delete** | **int**| Number of records to delete | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_discovery_start_index_records_to_return_get**
> DiscoveryNIOListResult api_v1_discovery_start_index_records_to_return_get(start_index, records_to_return)

Retrieves the discovery in the given range

Gets the discovery for the range specified

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
start_index = 56 # int | Start index
records_to_return = 56 # int | Number of records to return

try:
    # Retrieves the discovery in the given range
    api_response = api_instance.api_v1_discovery_start_index_records_to_return_get(start_index, records_to_return)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_discovery_start_index_records_to_return_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Start index | 
 **records_to_return** | **int**| Number of records to return | 

### Return type

[**DiscoveryNIOListResult**](DiscoveryNIOListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_cli_post**
> TaskIdResult api_v1_global_credential_cli_post(request)

Creates global CLI credential

This method is used to add global CLI credential

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.CLICredentialDTO() # CLICredentialDTO | request

try:
    # Creates global CLI credential
    api_response = api_instance.api_v1_global_credential_cli_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_cli_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CLICredentialDTO**](CLICredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_cli_put**
> TaskIdResult api_v1_global_credential_cli_put(request)

Updates global CLI credential

This method is used to update global CLI credential

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.CLICredentialDTO() # CLICredentialDTO | request

try:
    # Updates global CLI credential
    api_response = api_instance.api_v1_global_credential_cli_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_cli_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CLICredentialDTO**](CLICredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_get**
> GlobalCredentialListResult api_v1_global_credential_get(credential_sub_type=credential_sub_type, sort_by=sort_by, order=order)

Retrieves global credential for the given credential sub type

This method is used to get global credential for the given credential sub type

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
credential_sub_type = 'credential_sub_type_example' # str | Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF (optional)
sort_by = 'sort_by_example' # str | sortBy (optional)
order = 'order_example' # str | order (optional)

try:
    # Retrieves global credential for the given credential sub type
    api_response = api_instance.api_v1_global_credential_get(credential_sub_type=credential_sub_type, sort_by=sort_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_sub_type** | **str**| Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF | [optional] 
 **sort_by** | **str**| sortBy | [optional] 
 **order** | **str**| order | [optional] 

### Return type

[**GlobalCredentialListResult**](GlobalCredentialListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_global_credential_id_delete**
> TaskIdResult api_v1_global_credential_global_credential_id_delete(global_credential_id)

Retrieves global credential by ID

This method is used to delete global credential for the given ID

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
global_credential_id = 'global_credential_id_example' # str | ID of global-credential

try:
    # Retrieves global credential by ID
    api_response = api_instance.api_v1_global_credential_global_credential_id_delete(global_credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_global_credential_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_credential_id** | **str**| ID of global-credential | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_global_credential_id_put**
> TaskIdResult api_v1_global_credential_global_credential_id_put(request, global_credential_id)

Update global credential for network devices in site(s)

Update global credential for network devices in site(s)

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SitesInfoDTO() # SitesInfoDTO | request
global_credential_id = 'global_credential_id_example' # str | Global credential Uuid

try:
    # Update global credential for network devices in site(s)
    api_response = api_instance.api_v1_global_credential_global_credential_id_put(request, global_credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_global_credential_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SitesInfoDTO**](SitesInfoDTO.md)| request | 
 **global_credential_id** | **str**| Global credential Uuid | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_http_read_post**
> TaskIdResult api_v1_global_credential_http_read_post(request)

Creates global HTTP read credentials

This method is used to add HTTP read credentials

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.HTTPReadCredentialDTO() # HTTPReadCredentialDTO | request

try:
    # Creates global HTTP read credentials
    api_response = api_instance.api_v1_global_credential_http_read_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_http_read_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**HTTPReadCredentialDTO**](HTTPReadCredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_http_read_put**
> TaskIdResult api_v1_global_credential_http_read_put(request)

Updates global HTTP Read credential

This method is used to update global HTTP Read credential

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.HTTPReadCredentialDTO() # HTTPReadCredentialDTO | request

try:
    # Updates global HTTP Read credential
    api_response = api_instance.api_v1_global_credential_http_read_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_http_read_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**HTTPReadCredentialDTO**](HTTPReadCredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_http_write_post**
> TaskIdResult api_v1_global_credential_http_write_post(request)

Creates global HTTP write credentials

This method is used to add global HTTP write credentials

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.HTTPWriteCredentialDTO() # HTTPWriteCredentialDTO | request

try:
    # Creates global HTTP write credentials
    api_response = api_instance.api_v1_global_credential_http_write_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_http_write_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**HTTPWriteCredentialDTO**](HTTPWriteCredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_http_write_put**
> TaskIdResult api_v1_global_credential_http_write_put(request)

Updates global HTTP Write credential

This method is used to update global HTTP Write credential

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.HTTPWriteCredentialDTO() # HTTPWriteCredentialDTO | request

try:
    # Updates global HTTP Write credential
    api_response = api_instance.api_v1_global_credential_http_write_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_http_write_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**HTTPWriteCredentialDTO**](HTTPWriteCredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_id_get**
> GlobalCredentialSubTypeResult api_v1_global_credential_id_get(id)

Retrieves credential sub type for the given credential Id

This method is used to get credential sub type for the given Id

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | Global Credential ID

try:
    # Retrieves credential sub type for the given credential Id
    api_response = api_instance.api_v1_global_credential_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Global Credential ID | 

### Return type

[**GlobalCredentialSubTypeResult**](GlobalCredentialSubTypeResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_netconf_post**
> TaskIdResult api_v1_global_credential_netconf_post(request)

Creates global netconf credential

This method is used to add global netconf credential

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.NetconfCredentialDTO() # NetconfCredentialDTO | request

try:
    # Creates global netconf credential
    api_response = api_instance.api_v1_global_credential_netconf_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_netconf_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**NetconfCredentialDTO**](NetconfCredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_netconf_put**
> TaskIdResult api_v1_global_credential_netconf_put(request)

Updates global netconf credential

This method is used to update global netconf credential

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.NetconfCredentialDTO() # NetconfCredentialDTO | request

try:
    # Updates global netconf credential
    api_response = api_instance.api_v1_global_credential_netconf_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_netconf_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**NetconfCredentialDTO**](NetconfCredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_snmpv2_read_community_post**
> TaskIdResult api_v1_global_credential_snmpv2_read_community_post(request)

Creates global SNMP read community

This method is used to add global SNMP read community

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SNMPvReadCommunityDTO() # SNMPvReadCommunityDTO | request

try:
    # Creates global SNMP read community
    api_response = api_instance.api_v1_global_credential_snmpv2_read_community_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_snmpv2_read_community_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SNMPvReadCommunityDTO**](SNMPvReadCommunityDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_snmpv2_read_community_put**
> TaskIdResult api_v1_global_credential_snmpv2_read_community_put(request)

Updates global SNMP read community

This method is used to update global SNMP read community

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SNMPvReadCommunityDTO() # SNMPvReadCommunityDTO | request

try:
    # Updates global SNMP read community
    api_response = api_instance.api_v1_global_credential_snmpv2_read_community_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_snmpv2_read_community_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SNMPvReadCommunityDTO**](SNMPvReadCommunityDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_snmpv2_write_community_post**
> TaskIdResult api_v1_global_credential_snmpv2_write_community_post(request)

Creates global SNMP write community

This method is used to add global SNMP write community

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SNMPvWriteCommunityDTO() # SNMPvWriteCommunityDTO | request

try:
    # Creates global SNMP write community
    api_response = api_instance.api_v1_global_credential_snmpv2_write_community_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_snmpv2_write_community_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SNMPvWriteCommunityDTO**](SNMPvWriteCommunityDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_snmpv2_write_community_put**
> TaskIdResult api_v1_global_credential_snmpv2_write_community_put(request)

Updates global SNMP write community

This method is used to update global SNMP write community

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SNMPvWriteCommunityDTO() # SNMPvWriteCommunityDTO | request

try:
    # Updates global SNMP write community
    api_response = api_instance.api_v1_global_credential_snmpv2_write_community_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_snmpv2_write_community_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SNMPvWriteCommunityDTO**](SNMPvWriteCommunityDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_snmpv3_post**
> TaskIdResult api_v1_global_credential_snmpv3_post(request)

Creates global SNMPv3 credential

This method is used to add global SNMPv3 credential

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SNMPvCredentialDTO() # SNMPvCredentialDTO | request

try:
    # Creates global SNMPv3 credential
    api_response = api_instance.api_v1_global_credential_snmpv3_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_snmpv3_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SNMPvCredentialDTO**](SNMPvCredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_global_credential_snmpv3_put**
> TaskIdResult api_v1_global_credential_snmpv3_put(request)

Updates global SNMPv3 credential

This method is used to update global SNMPv3 credential

### Example
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
api_instance = dnac_api_client.NetworkDiscoveryApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SNMPvCredentialDTO() # SNMPvCredentialDTO | request

try:
    # Updates global SNMPv3 credential
    api_response = api_instance.api_v1_global_credential_snmpv3_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiscoveryApi->api_v1_global_credential_snmpv3_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SNMPvCredentialDTO**](SNMPvCredentialDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

