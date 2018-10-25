# dnac_api_client.CommandRunnerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_network_device_poller_cli_legit_reads_get**](CommandRunnerApi.md#api_v1_network_device_poller_cli_legit_reads_get) | **GET** /api/v1/network-device-poller/cli/legit-reads | Get all keywords of CLIs accepted by command runner
[**api_v1_network_device_poller_cli_read_request_post**](CommandRunnerApi.md#api_v1_network_device_poller_cli_read_request_post) | **POST** /api/v1/network-device-poller/cli/read-request | Run read-only commands on devices to get their real-time configuration


# **api_v1_network_device_poller_cli_legit_reads_get**
> LegitCliKeyResult api_v1_network_device_poller_cli_legit_reads_get()

Get all keywords of CLIs accepted by command runner

Get valid keywords

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
api_instance = dnac_api_client.CommandRunnerApi(dnac_api_client.ApiClient(configuration))

try:
    # Get all keywords of CLIs accepted by command runner
    api_response = api_instance.api_v1_network_device_poller_cli_legit_reads_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandRunnerApi->api_v1_network_device_poller_cli_legit_reads_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LegitCliKeyResult**](LegitCliKeyResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_network_device_poller_cli_read_request_post**
> TaskIdResult api_v1_network_device_poller_cli_read_request_post(command_runner_dto)

Run read-only commands on devices to get their real-time configuration

Submit request for read-only CLIs

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
api_instance = dnac_api_client.CommandRunnerApi(dnac_api_client.ApiClient(configuration))
command_runner_dto = dnac_api_client.CommandRunnerDTO() # CommandRunnerDTO | request

try:
    # Run read-only commands on devices to get their real-time configuration
    api_response = api_instance.api_v1_network_device_poller_cli_read_request_post(command_runner_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandRunnerApi->api_v1_network_device_poller_cli_read_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_runner_dto** | [**CommandRunnerDTO**](CommandRunnerDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

