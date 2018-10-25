# dnac_api_client.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_file_file_id_get**](SystemApi.md#api_v1_file_file_id_get) | **GET** /api/v1/file/{fileId} | Downloads a file referred by the fileId
[**api_v1_file_namespace_get**](SystemApi.md#api_v1_file_namespace_get) | **GET** /api/v1/file/namespace | Returns list of available namespaces
[**api_v1_file_namespace_name_space_get**](SystemApi.md#api_v1_file_namespace_name_space_get) | **GET** /api/v1/file/namespace/{nameSpace} | Returns list of files under a specific namespace


# **api_v1_file_file_id_get**
> DownloadsAFileReferredByTheFileIdResponse api_v1_file_file_id_get(file_id)

Downloads a file referred by the fileId

This method is used to download a file referred by the fileId

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
api_instance = dnac_api_client.SystemApi(dnac_api_client.ApiClient(configuration))
file_id = 'file_id_example' # str | File Identification number

try:
    # Downloads a file referred by the fileId
    api_response = api_instance.api_v1_file_file_id_get(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_v1_file_file_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| File Identification number | 

### Return type

[**DownloadsAFileReferredByTheFileIdResponse**](DownloadsAFileReferredByTheFileIdResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_file_namespace_get**
> NameSpaceListResult api_v1_file_namespace_get()

Returns list of available namespaces

This method is used to obtain a list of available namespaces

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
api_instance = dnac_api_client.SystemApi(dnac_api_client.ApiClient(configuration))

try:
    # Returns list of available namespaces
    api_response = api_instance.api_v1_file_namespace_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_v1_file_namespace_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NameSpaceListResult**](NameSpaceListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_file_namespace_name_space_get**
> FileObjectListResult api_v1_file_namespace_name_space_get(name_space)

Returns list of files under a specific namespace

This method is used to obtain a list of files under a specific namespace

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
api_instance = dnac_api_client.SystemApi(dnac_api_client.ApiClient(configuration))
name_space = 'name_space_example' # str | A listing of fileId's

try:
    # Returns list of files under a specific namespace
    api_response = api_instance.api_v1_file_namespace_name_space_get(name_space)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_v1_file_namespace_name_space_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_space** | **str**| A listing of fileId&#39;s | 

### Return type

[**FileObjectListResult**](FileObjectListResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

