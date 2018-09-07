# dnac_api_client.IntentConnectivityApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dna_intent_api_v1_create_ssid_post**](IntentConnectivityApi.md#dna_intent_api_v1_create_ssid_post) | **POST** /dna/intent/api/v1/create-ssid | Create SSID
[**dna_intent_api_v1_delete_ssid_device_name_wireless_network_profile_name_ssid_name_interface_name_delete**](IntentConnectivityApi.md#dna_intent_api_v1_delete_ssid_device_name_wireless_network_profile_name_ssid_name_interface_name_delete) | **DELETE** /dna/intent/api/v1/delete-ssid/{deviceName}/{wirelessNetworkProfileName}/{ssidName}/{interfaceName} | Delete SSID


# **dna_intent_api_v1_create_ssid_post**
> CreateSSIDResponse dna_intent_api_v1_create_ssid_post(request, runsync=runsync, timeout=timeout)

Create SSID

Creates non fabric enterprise SSID, dynamic interface, Wireless Network Profile and provisions WLC and AP

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
api_instance = dnac_api_client.IntentConnectivityApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.CreateSSIDRequest() # CreateSSIDRequest | request
runsync = false # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to false)
timeout = 10 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10)

try:
    # Create SSID
    api_response = api_instance.dna_intent_api_v1_create_ssid_post(request, runsync=runsync, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentConnectivityApi->dna_intent_api_v1_create_ssid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateSSIDRequest**](CreateSSIDRequest.md)| request | 
 **runsync** | **bool**| Enable this parameter to execute the API and return a response synchronously | [optional] [default to false]
 **timeout** | **float**| During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated | [optional] [default to 10]

### Return type

[**CreateSSIDResponse**](CreateSSIDResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dna_intent_api_v1_delete_ssid_device_name_wireless_network_profile_name_ssid_name_interface_name_delete**
> DeleteSSIDResponse dna_intent_api_v1_delete_ssid_device_name_wireless_network_profile_name_ssid_name_interface_name_delete(device_name, wireless_network_profile_name, ssid_name, interface_name, runsync=runsync, timeout=timeout)

Delete SSID

De-provision WLC, also removes wireless network profile, SSID and dynamic interface

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
api_instance = dnac_api_client.IntentConnectivityApi(dnac_api_client.ApiClient(configuration))
device_name = 'device_name_example' # str | 
wireless_network_profile_name = 'wireless_network_profile_name_example' # str | 
ssid_name = 'ssid_name_example' # str | 
interface_name = 'interface_name_example' # str | 
runsync = false # bool | Enable this parameter to execute the API and return a response synchronously (optional) (default to false)
timeout = 10 # float | During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated (optional) (default to 10)

try:
    # Delete SSID
    api_response = api_instance.dna_intent_api_v1_delete_ssid_device_name_wireless_network_profile_name_ssid_name_interface_name_delete(device_name, wireless_network_profile_name, ssid_name, interface_name, runsync=runsync, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentConnectivityApi->dna_intent_api_v1_delete_ssid_device_name_wireless_network_profile_name_ssid_name_interface_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**|  | 
 **wireless_network_profile_name** | **str**|  | 
 **ssid_name** | **str**|  | 
 **interface_name** | **str**|  | 
 **runsync** | **bool**| Enable this parameter to execute the API and return a response synchronously | [optional] [default to false]
 **timeout** | **float**| During synchronous execution, this defines the maximum time to wait for a response, before the API execution is terminated | [optional] [default to 10]

### Return type

[**DeleteSSIDResponse**](DeleteSSIDResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

