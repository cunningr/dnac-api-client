# dnac_api_client.IntentSitesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dna_intent_api_v1_site_hierarchy_get**](IntentSitesApi.md#dna_intent_api_v1_site_hierarchy_get) | **GET** /dna/intent/api/v1/site-hierarchy | Site Hierarchy


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
api_instance = dnac_api_client.IntentSitesApi(dnac_api_client.ApiClient(configuration))
timestamp = 'timestamp_example' # str | Timestamp 
runsync = False # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to False)
timeout = 10.0 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10.0)

try:
    # Site Hierarchy
    api_response = api_instance.dna_intent_api_v1_site_hierarchy_get(timestamp, runsync=runsync, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentSitesApi->dna_intent_api_v1_site_hierarchy_get: %s\n" % e)
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

