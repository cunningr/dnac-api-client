# dnac_api_client.IntentAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dna_intent_api_v1_client_detail_get**](IntentAPIApi.md#dna_intent_api_v1_client_detail_get) | **GET** /dna/intent/api/v1/client-detail | Client Detail
[**dna_intent_api_v1_client_health_get**](IntentAPIApi.md#dna_intent_api_v1_client_health_get) | **GET** /dna/intent/api/v1/client-health | Client Health
[**dna_intent_api_v1_network_device_detail_get**](IntentAPIApi.md#dna_intent_api_v1_network_device_detail_get) | **GET** /dna/intent/api/v1/network-device-detail | Network Device Detail
[**dna_intent_api_v1_network_health_get**](IntentAPIApi.md#dna_intent_api_v1_network_health_get) | **GET** /dna/intent/api/v1/network-health | Network Health
[**dna_intent_api_v1_site_hierarchy_get**](IntentAPIApi.md#dna_intent_api_v1_site_hierarchy_get) | **GET** /dna/intent/api/v1/site-hierarchy | Site Hierarchy


# **dna_intent_api_v1_client_detail_get**
> ClientDetailResponse dna_intent_api_v1_client_detail_get(timestamp, mac_address, runsync=runsync, timeout=timeout)

Client Detail

Get Client Details for a single client

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
api_instance = dnac_api_client.IntentAPIApi(dnac_api_client.ApiClient(configuration))
timestamp = 'timestamp_example' # str | timestamp
mac_address = 'mac_address_example' # str | MAC Address of the client
runsync = False # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to False)
timeout = 10.0 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10.0)

try:
    # Client Detail
    api_response = api_instance.dna_intent_api_v1_client_detail_get(timestamp, mac_address, runsync=runsync, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentAPIApi->dna_intent_api_v1_client_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| timestamp | 
 **mac_address** | **str**| MAC Address of the client | 
 **runsync** | **bool**| Enable this parameter to execute the API and return a response synchronously | [optional] [default to False]
 **timeout** | **float**| During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated | [optional] [default to 10.0]

### Return type

[**ClientDetailResponse**](ClientDetailResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dna_intent_api_v1_client_health_get**
> ClientHealthResponse dna_intent_api_v1_client_health_get(start_time, end_time, runsync=runsync, timeout=timeout)

Client Health

Get overall Client Health along with beak down on categories of wired and wireless

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
api_instance = dnac_api_client.IntentAPIApi(dnac_api_client.ApiClient(configuration))
start_time = 'start_time_example' # str | Start Time
end_time = 'end_time_example' # str | End Time
runsync = False # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to False)
timeout = 10.0 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10.0)

try:
    # Client Health
    api_response = api_instance.dna_intent_api_v1_client_health_get(start_time, end_time, runsync=runsync, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentAPIApi->dna_intent_api_v1_client_health_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| Start Time | 
 **end_time** | **str**| End Time | 
 **runsync** | **bool**| Enable this parameter to execute the API and return a response synchronously | [optional] [default to False]
 **timeout** | **float**| During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated | [optional] [default to 10.0]

### Return type

[**ClientHealthResponse**](ClientHealthResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dna_intent_api_v1_network_device_detail_get**
> NetworkDeviceDetailResponse dna_intent_api_v1_network_device_detail_get(runsync=runsync, timeout=timeout, timestamp=timestamp, search_by=search_by, identifier=identifier)

Network Device Detail

Get Network Device Detail

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
api_instance = dnac_api_client.IntentAPIApi(dnac_api_client.ApiClient(configuration))
runsync = False # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to False)
timeout = 10.0 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10.0)
timestamp = 'timestamp_example' # str | timestamp (optional)
search_by = 'search_by_example' # str | MAC Address or UUID or Name of the Device (optional)
identifier = 'identifier_example' # str | macAddress or uuid or nwDeviceName (optional)

try:
    # Network Device Detail
    api_response = api_instance.dna_intent_api_v1_network_device_detail_get(runsync=runsync, timeout=timeout, timestamp=timestamp, search_by=search_by, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentAPIApi->dna_intent_api_v1_network_device_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runsync** | **bool**| Enable this parameter to execute the API and return a response synchronously | [optional] [default to False]
 **timeout** | **float**| During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated | [optional] [default to 10.0]
 **timestamp** | **str**| timestamp | [optional] 
 **search_by** | **str**| MAC Address or UUID or Name of the Device | [optional] 
 **identifier** | **str**| macAddress or uuid or nwDeviceName | [optional] 

### Return type

[**NetworkDeviceDetailResponse**](NetworkDeviceDetailResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dna_intent_api_v1_network_health_get**
> dna_intent_api_v1_network_health_get(start_time, end_time, runsync=runsync, timeout=timeout)

Network Health

Network Devices and their health by category

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
api_instance = dnac_api_client.IntentAPIApi(dnac_api_client.ApiClient(configuration))
start_time = 'start_time_example' # str | Start Time
end_time = 'end_time_example' # str | End Time
runsync = False # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to False)
timeout = 10.0 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10.0)

try:
    # Network Health
    api_instance.dna_intent_api_v1_network_health_get(start_time, end_time, runsync=runsync, timeout=timeout)
except ApiException as e:
    print("Exception when calling IntentAPIApi->dna_intent_api_v1_network_health_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| Start Time | 
 **end_time** | **str**| End Time | 
 **runsync** | **bool**| Enable this parameter to execute the API and return a response synchronously | [optional] [default to False]
 **timeout** | **float**| During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated | [optional] [default to 10.0]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dna_intent_api_v1_site_hierarchy_get**
> SiteHierarchyResponse dna_intent_api_v1_site_hierarchy_get(timestamp, runsync=runsync, timeout=timeout)

Site Hierarchy

Site Hierarchy along with health Info

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
api_instance = dnac_api_client.IntentAPIApi(dnac_api_client.ApiClient(configuration))
timestamp = 'timestamp_example' # str | Timestamp 
runsync = False # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to False)
timeout = 10.0 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10.0)

try:
    # Site Hierarchy
    api_response = api_instance.dna_intent_api_v1_site_hierarchy_get(timestamp, runsync=runsync, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentAPIApi->dna_intent_api_v1_site_hierarchy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp  | 
 **runsync** | **bool**| Enable this parameter to execute the API and return a response synchronously | [optional] [default to False]
 **timeout** | **float**| During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated | [optional] [default to 10.0]

### Return type

[**SiteHierarchyResponse**](SiteHierarchyResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

