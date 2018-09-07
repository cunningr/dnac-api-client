# dnac_api_client.IntentClientsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dna_intent_api_v1_client_detail_get**](IntentClientsApi.md#dna_intent_api_v1_client_detail_get) | **GET** /dna/intent/api/v1/client-detail | Client Detail
[**dna_intent_api_v1_client_health_get**](IntentClientsApi.md#dna_intent_api_v1_client_health_get) | **GET** /dna/intent/api/v1/client-health | Client Health


# **dna_intent_api_v1_client_detail_get**
> ClientDetailResponse dna_intent_api_v1_client_detail_get(timestamp, mac_address, runsync=runsync, timeout=timeout)

Client Detail

Get Client Details for a single client

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
api_instance = dnac_api_client.IntentClientsApi(dnac_api_client.ApiClient(configuration))
timestamp = '' # str | timestamp (default to )
mac_address = '' # str | MAC Address of the client (default to )
runsync = false # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to false)
timeout = 10 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10)

try:
    # Client Detail
    api_response = api_instance.dna_intent_api_v1_client_detail_get(timestamp, mac_address, runsync=runsync, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentClientsApi->dna_intent_api_v1_client_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| timestamp | [default to ]
 **mac_address** | **str**| MAC Address of the client | [default to ]
 **runsync** | **bool**| Enable this parameter to execute the API and return a response synchronously | [optional] [default to false]
 **timeout** | **float**| During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated | [optional] [default to 10]

### Return type

[**ClientDetailResponse**](ClientDetailResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dna_intent_api_v1_client_health_get**
> ClientHealthResponse dna_intent_api_v1_client_health_get(start_time, end_time, runsync=runsync, timeout=timeout)

Client Health

Get overall Client Health along with beak down on categories of wired and wireless

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
api_instance = dnac_api_client.IntentClientsApi(dnac_api_client.ApiClient(configuration))
start_time = '' # str | Start Time (default to )
end_time = '' # str | End Time (default to )
runsync = false # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to false)
timeout = 10 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10)

try:
    # Client Health
    api_response = api_instance.dna_intent_api_v1_client_health_get(start_time, end_time, runsync=runsync, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentClientsApi->dna_intent_api_v1_client_health_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| Start Time | [default to ]
 **end_time** | **str**| End Time | [default to ]
 **runsync** | **bool**| Enable this parameter to execute the API and return a response synchronously | [optional] [default to false]
 **timeout** | **float**| During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated | [optional] [default to 10]

### Return type

[**ClientHealthResponse**](ClientHealthResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

