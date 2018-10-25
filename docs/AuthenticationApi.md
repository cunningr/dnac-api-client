# dnac_api_client.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_system_v1_auth_token_post**](AuthenticationApi.md#api_system_v1_auth_token_post) | **POST** /api/system/v1/auth/token | Generate Token


# **api_system_v1_auth_token_post**
> GenerateTokenResponse api_system_v1_auth_token_post()

Generate Token

This method is used to generate token.

### Example

* Basic Authentication (basicAuth): 
```python
from __future__ import print_function
import time
import dnac_api_client
from dnac_api_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = dnac_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = dnac_api_client.AuthenticationApi(dnac_api_client.ApiClient(configuration))

try:
    # Generate Token
    api_response = api_instance.api_system_v1_auth_token_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->api_system_v1_auth_token_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GenerateTokenResponse**](GenerateTokenResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

