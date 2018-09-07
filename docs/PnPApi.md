# dnac_api_client.PnPApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_onboarding_pnp_device_claim_post**](PnPApi.md#api_v1_onboarding_pnp_device_claim_post) | **POST** /api/v1/onboarding/pnp-device/claim | Claim Device(s)
[**api_v1_onboarding_pnp_device_count_get**](PnPApi.md#api_v1_onboarding_pnp_device_count_get) | **GET** /api/v1/onboarding/pnp-device/count | Get Device Count
[**api_v1_onboarding_pnp_device_dashboard_count_get**](PnPApi.md#api_v1_onboarding_pnp_device_dashboard_count_get) | **GET** /api/v1/onboarding/pnp-device/dashboard/count | Get Categorized Device Count
[**api_v1_onboarding_pnp_device_get**](PnPApi.md#api_v1_onboarding_pnp_device_get) | **GET** /api/v1/onboarding/pnp-device | List devices
[**api_v1_onboarding_pnp_device_history_get**](PnPApi.md#api_v1_onboarding_pnp_device_history_get) | **GET** /api/v1/onboarding/pnp-device/history | Get Device History
[**api_v1_onboarding_pnp_device_id_delete**](PnPApi.md#api_v1_onboarding_pnp_device_id_delete) | **DELETE** /api/v1/onboarding/pnp-device/{id} | Delete Device
[**api_v1_onboarding_pnp_device_id_get**](PnPApi.md#api_v1_onboarding_pnp_device_id_get) | **GET** /api/v1/onboarding/pnp-device/{id} | Get Device by ID
[**api_v1_onboarding_pnp_device_id_put**](PnPApi.md#api_v1_onboarding_pnp_device_id_put) | **PUT** /api/v1/onboarding/pnp-device/{id} | Update Device
[**api_v1_onboarding_pnp_device_import_post**](PnPApi.md#api_v1_onboarding_pnp_device_import_post) | **POST** /api/v1/onboarding/pnp-device/import | Import Many Devices
[**api_v1_onboarding_pnp_device_post**](PnPApi.md#api_v1_onboarding_pnp_device_post) | **POST** /api/v1/onboarding/pnp-device | Create Device
[**api_v1_onboarding_pnp_device_provision_post**](PnPApi.md#api_v1_onboarding_pnp_device_provision_post) | **POST** /api/v1/onboarding/pnp-device/provision | Provision Device
[**api_v1_onboarding_pnp_device_reset_post**](PnPApi.md#api_v1_onboarding_pnp_device_reset_post) | **POST** /api/v1/onboarding/pnp-device/reset | Reset Device
[**api_v1_onboarding_pnp_device_sacct_domain_vacct_name_sync_result_get**](PnPApi.md#api_v1_onboarding_pnp_device_sacct_domain_vacct_name_sync_result_get) | **GET** /api/v1/onboarding/pnp-device/sacct/{domain}/vacct/{name}/sync-result | Get Sync Result for Virtual Account
[**api_v1_onboarding_pnp_device_unclaim_post**](PnPApi.md#api_v1_onboarding_pnp_device_unclaim_post) | **POST** /api/v1/onboarding/pnp-device/unclaim | Un-Claim Device
[**api_v1_onboarding_pnp_device_vacct_sync_post**](PnPApi.md#api_v1_onboarding_pnp_device_vacct_sync_post) | **POST** /api/v1/onboarding/pnp-device/vacct-sync | Sync Virtual Account Devices
[**api_v1_onboarding_pnp_settings_get**](PnPApi.md#api_v1_onboarding_pnp_settings_get) | **GET** /api/v1/onboarding/pnp-settings | View Settings
[**api_v1_onboarding_pnp_settings_put**](PnPApi.md#api_v1_onboarding_pnp_settings_put) | **PUT** /api/v1/onboarding/pnp-settings | Update Settings
[**api_v1_onboarding_pnp_settings_sacct_domain_vacct_get**](PnPApi.md#api_v1_onboarding_pnp_settings_sacct_domain_vacct_get) | **GET** /api/v1/onboarding/pnp-settings/sacct/{domain}/vacct | Get Virtual Account List
[**api_v1_onboarding_pnp_settings_sacct_get**](PnPApi.md#api_v1_onboarding_pnp_settings_sacct_get) | **GET** /api/v1/onboarding/pnp-settings/sacct | Get Smart Account List
[**api_v1_onboarding_pnp_settings_savacct_post**](PnPApi.md#api_v1_onboarding_pnp_settings_savacct_post) | **POST** /api/v1/onboarding/pnp-settings/savacct | Add Virtual Account
[**api_v1_onboarding_pnp_settings_savacct_put**](PnPApi.md#api_v1_onboarding_pnp_settings_savacct_put) | **PUT** /api/v1/onboarding/pnp-settings/savacct | Edit PnP Server Profile
[**api_v1_onboarding_pnp_settings_vacct_delete**](PnPApi.md#api_v1_onboarding_pnp_settings_vacct_delete) | **DELETE** /api/v1/onboarding/pnp-settings/vacct | Deregister Virtual Account
[**api_v1_onboarding_pnp_workflow_count_get**](PnPApi.md#api_v1_onboarding_pnp_workflow_count_get) | **GET** /api/v1/onboarding/pnp-workflow/count | Get Workflow Count
[**api_v1_onboarding_pnp_workflow_get**](PnPApi.md#api_v1_onboarding_pnp_workflow_get) | **GET** /api/v1/onboarding/pnp-workflow | List Workflows
[**api_v1_onboarding_pnp_workflow_id_delete**](PnPApi.md#api_v1_onboarding_pnp_workflow_id_delete) | **DELETE** /api/v1/onboarding/pnp-workflow/{id} | Delete Workflow
[**api_v1_onboarding_pnp_workflow_id_get**](PnPApi.md#api_v1_onboarding_pnp_workflow_id_get) | **GET** /api/v1/onboarding/pnp-workflow/{id} | Get Workflow
[**api_v1_onboarding_pnp_workflow_id_put**](PnPApi.md#api_v1_onboarding_pnp_workflow_id_put) | **PUT** /api/v1/onboarding/pnp-workflow/{id} | Update Workflow
[**api_v1_onboarding_pnp_workflow_post**](PnPApi.md#api_v1_onboarding_pnp_workflow_post) | **POST** /api/v1/onboarding/pnp-workflow | Create Workflow


# **api_v1_onboarding_pnp_device_claim_post**
> ClaimDevicesResponse api_v1_onboarding_pnp_device_claim_post(request)

Claim Device(s)

This API is used to assign a project & workflow (i.e. claim) one of more devices.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.ClaimDeviceRequest() # ClaimDeviceRequest | request

try:
    # Claim Device(s)
    api_response = api_instance.api_v1_onboarding_pnp_device_claim_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_claim_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClaimDeviceRequest**](ClaimDeviceRequest.md)| request | 

### Return type

[**ClaimDevicesResponse**](ClaimDevicesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_count_get**
> GetDeviceCountResponse api_v1_onboarding_pnp_device_count_get(serial_number=serial_number, state=state, onb_state=onb_state, cm_state=cm_state, name=name, pid=pid, source=source, project_id=project_id, workflow_id=workflow_id, project_name=project_name, workflow_name=workflow_name, smart_account_id=smart_account_id, virtual_account_id=virtual_account_id, last_contact=last_contact)

Get Device Count

This API is used to get the number of the devices matching provided filters. This is useful for pageination.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
serial_number = ['serial_number_example'] # list[str] | Device Serial Number (optional)
state = ['state_example'] # list[str] | Device State (optional)
onb_state = ['onb_state_example'] # list[str] | Device Onboarding State (optional)
cm_state = ['cm_state_example'] # list[str] | Device Connection Manager State (optional)
name = ['name_example'] # list[str] | Device Name (optional)
pid = ['pid_example'] # list[str] | Device ProductId (optional)
source = ['source_example'] # list[str] | Device Source (optional)
project_id = ['project_id_example'] # list[str] | Device Project Id (optional)
workflow_id = ['workflow_id_example'] # list[str] | Device Workflow Id (optional)
project_name = ['project_name_example'] # list[str] | Device Project Name (optional)
workflow_name = ['workflow_name_example'] # list[str] | Device Workflow Name (optional)
smart_account_id = ['smart_account_id_example'] # list[str] | Device Smart Account (optional)
virtual_account_id = ['virtual_account_id_example'] # list[str] | Device Virtual Account (optional)
last_contact = true # bool | Device Has Contacted lastContact > 0 (optional)

try:
    # Get Device Count
    api_response = api_instance.api_v1_onboarding_pnp_device_count_get(serial_number=serial_number, state=state, onb_state=onb_state, cm_state=cm_state, name=name, pid=pid, source=source, project_id=project_id, workflow_id=workflow_id, project_name=project_name, workflow_name=workflow_name, smart_account_id=smart_account_id, virtual_account_id=virtual_account_id, last_contact=last_contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | [**list[str]**](str.md)| Device Serial Number | [optional] 
 **state** | [**list[str]**](str.md)| Device State | [optional] 
 **onb_state** | [**list[str]**](str.md)| Device Onboarding State | [optional] 
 **cm_state** | [**list[str]**](str.md)| Device Connection Manager State | [optional] 
 **name** | [**list[str]**](str.md)| Device Name | [optional] 
 **pid** | [**list[str]**](str.md)| Device ProductId | [optional] 
 **source** | [**list[str]**](str.md)| Device Source | [optional] 
 **project_id** | [**list[str]**](str.md)| Device Project Id | [optional] 
 **workflow_id** | [**list[str]**](str.md)| Device Workflow Id | [optional] 
 **project_name** | [**list[str]**](str.md)| Device Project Name | [optional] 
 **workflow_name** | [**list[str]**](str.md)| Device Workflow Name | [optional] 
 **smart_account_id** | [**list[str]**](str.md)| Device Smart Account | [optional] 
 **virtual_account_id** | [**list[str]**](str.md)| Device Virtual Account | [optional] 
 **last_contact** | **bool**| Device Has Contacted lastContact &gt; 0 | [optional] 

### Return type

[**GetDeviceCountResponse**](GetDeviceCountResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_dashboard_count_get**
> GetCategorizedDeviceCountResponse api_v1_onboarding_pnp_device_dashboard_count_get(category)

Get Categorized Device Count

Get Categorized Device Count

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
category = 'category_example' # str | Valid Values: state, errorState, onbState or source

try:
    # Get Categorized Device Count
    api_response = api_instance.api_v1_onboarding_pnp_device_dashboard_count_get(category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_dashboard_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Valid Values: state, errorState, onbState or source | 

### Return type

[**GetCategorizedDeviceCountResponse**](GetCategorizedDeviceCountResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_get**
> ListDevicesResponse api_v1_onboarding_pnp_device_get(limit=limit, offset=offset, sort=sort, sort_order=sort_order, serial_number=serial_number, state=state, onb_state=onb_state, cm_state=cm_state, name=name, pid=pid, source=source, project_id=project_id, workflow_id=workflow_id, project_name=project_name, workflow_name=workflow_name, smart_account_id=smart_account_id, virtual_account_id=virtual_account_id, last_contact=last_contact)

List devices

This API is used to get the list of devices that match the provided filter. Pagination and sorting are also supported. If a limit is not specified, it will default to return 50 devices.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
limit = 56 # int | Limits number of results (optional)
offset = 56 # int | Index of first result (optional)
sort = ['sort_example'] # list[str] | Comma seperated list of fields to sort on (optional)
sort_order = 'sort_order_example' # str | Sort Order Ascending (asc) or Descending (des) (optional)
serial_number = ['serial_number_example'] # list[str] | Device Serial Number (optional)
state = ['state_example'] # list[str] | Device State (optional)
onb_state = ['onb_state_example'] # list[str] | Device Onboarding State (optional)
cm_state = ['cm_state_example'] # list[str] | Device Connection Manager State (optional)
name = ['name_example'] # list[str] | Device Name (optional)
pid = ['pid_example'] # list[str] | Device ProductId (optional)
source = ['source_example'] # list[str] | Device Source (optional)
project_id = ['project_id_example'] # list[str] | Device Project Id (optional)
workflow_id = ['workflow_id_example'] # list[str] | Device Workflow Id (optional)
project_name = ['project_name_example'] # list[str] | Device Project Name (optional)
workflow_name = ['workflow_name_example'] # list[str] | Device Workflow Name (optional)
smart_account_id = ['smart_account_id_example'] # list[str] | Device Smart Account (optional)
virtual_account_id = ['virtual_account_id_example'] # list[str] | Device Virtual Account (optional)
last_contact = true # bool | Device Has Contacted lastContact > 0 (optional)

try:
    # List devices
    api_response = api_instance.api_v1_onboarding_pnp_device_get(limit=limit, offset=offset, sort=sort, sort_order=sort_order, serial_number=serial_number, state=state, onb_state=onb_state, cm_state=cm_state, name=name, pid=pid, source=source, project_id=project_id, workflow_id=workflow_id, project_name=project_name, workflow_name=workflow_name, smart_account_id=smart_account_id, virtual_account_id=virtual_account_id, last_contact=last_contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits number of results | [optional] 
 **offset** | **int**| Index of first result | [optional] 
 **sort** | [**list[str]**](str.md)| Comma seperated list of fields to sort on | [optional] 
 **sort_order** | **str**| Sort Order Ascending (asc) or Descending (des) | [optional] 
 **serial_number** | [**list[str]**](str.md)| Device Serial Number | [optional] 
 **state** | [**list[str]**](str.md)| Device State | [optional] 
 **onb_state** | [**list[str]**](str.md)| Device Onboarding State | [optional] 
 **cm_state** | [**list[str]**](str.md)| Device Connection Manager State | [optional] 
 **name** | [**list[str]**](str.md)| Device Name | [optional] 
 **pid** | [**list[str]**](str.md)| Device ProductId | [optional] 
 **source** | [**list[str]**](str.md)| Device Source | [optional] 
 **project_id** | [**list[str]**](str.md)| Device Project Id | [optional] 
 **workflow_id** | [**list[str]**](str.md)| Device Workflow Id | [optional] 
 **project_name** | [**list[str]**](str.md)| Device Project Name | [optional] 
 **workflow_name** | [**list[str]**](str.md)| Device Workflow Name | [optional] 
 **smart_account_id** | [**list[str]**](str.md)| Device Smart Account | [optional] 
 **virtual_account_id** | [**list[str]**](str.md)| Device Virtual Account | [optional] 
 **last_contact** | **bool**| Device Has Contacted lastContact &gt; 0 | [optional] 

### Return type

[**ListDevicesResponse**](ListDevicesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_history_get**
> GetDeviceHistoryResponse api_v1_onboarding_pnp_device_history_get(serial_number, sort=sort, sort_order=sort_order)

Get Device History

Retrieves history for a specific device. Serial Number is a required parameter

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
serial_number = 'serial_number_example' # str | Device Serial Number
sort = ['sort_example'] # list[str] | Comma seperated list of fields to sort on (optional)
sort_order = 'sort_order_example' # str | Sort Order Ascending (asc) or Descending (des) (optional)

try:
    # Get Device History
    api_response = api_instance.api_v1_onboarding_pnp_device_history_get(serial_number, sort=sort, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| Device Serial Number | 
 **sort** | [**list[str]**](str.md)| Comma seperated list of fields to sort on | [optional] 
 **sort_order** | **str**| Sort Order Ascending (asc) or Descending (des) | [optional] 

### Return type

[**GetDeviceHistoryResponse**](GetDeviceHistoryResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_id_delete**
> DeleteDeviceResponse api_v1_onboarding_pnp_device_id_delete(id)

Delete Device

This API is used to delete the specified device from the database.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete Device
    api_response = api_instance.api_v1_onboarding_pnp_device_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**DeleteDeviceResponse**](DeleteDeviceResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_id_get**
> GetDeviceByIDResponse api_v1_onboarding_pnp_device_id_get(id)

Get Device by ID

Get device details of the device with input device id

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Get Device by ID
    api_response = api_instance.api_v1_onboarding_pnp_device_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**GetDeviceByIDResponse**](GetDeviceByIDResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_id_put**
> UpdateDeviceResponse api_v1_onboarding_pnp_device_id_put(request, id)

Update Device

This API is used to update device details of a device that exists in the PnP database.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.Device() # Device | request
id = 'id_example' # str | id

try:
    # Update Device
    api_response = api_instance.api_v1_onboarding_pnp_device_id_put(request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Device**](Device.md)| request | 
 **id** | **str**| id | 

### Return type

[**UpdateDeviceResponse**](UpdateDeviceResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_import_post**
> ImportManyDevicesResponse api_v1_onboarding_pnp_device_import_post(request)

Import Many Devices

This API is used to import a list of Planned devices to the PnP database. A Planned device is a device that the customer has bought and/or is planning to manage.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.Device() # Device | request

try:
    # Import Many Devices
    api_response = api_instance.api_v1_onboarding_pnp_device_import_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Device**](Device.md)| request | 

### Return type

[**ImportManyDevicesResponse**](ImportManyDevicesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_post**
> CreateDeviceResponse api_v1_onboarding_pnp_device_post(request)

Create Device

This API is used to add a Planned device to the PnP database. A Planned device is a device that the customer has bought and/or is planning to manage.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.Device() # Device | request

try:
    # Create Device
    api_response = api_instance.api_v1_onboarding_pnp_device_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Device**](Device.md)| request | 

### Return type

[**CreateDeviceResponse**](CreateDeviceResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_provision_post**
> ProvisionDeviceResponse api_v1_onboarding_pnp_device_provision_post(request)

Provision Device

This API is used push one or more devices to Provisoned state and add them to inventory.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.PushProvisionRequest() # PushProvisionRequest | request

try:
    # Provision Device
    api_response = api_instance.api_v1_onboarding_pnp_device_provision_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_provision_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PushProvisionRequest**](PushProvisionRequest.md)| request | 

### Return type

[**ProvisionDeviceResponse**](ProvisionDeviceResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_reset_post**
> ResetDeviceResponse api_v1_onboarding_pnp_device_reset_post(request)

Reset Device

This API is used to recover a device from a Workflow Execution Error state.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.ResetRequest() # ResetRequest | request

try:
    # Reset Device
    api_response = api_instance.api_v1_onboarding_pnp_device_reset_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ResetRequest**](ResetRequest.md)| request | 

### Return type

[**ResetDeviceResponse**](ResetDeviceResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_sacct_domain_vacct_name_sync_result_get**
> GetSyncResultForVirtualAccountResponse api_v1_onboarding_pnp_device_sacct_domain_vacct_name_sync_result_get(domain, name)

Get Sync Result for Virtual Account

This API is used to get the device sync info from the given smart account & virtual account with the PnP database. The SAVAMapping object which has the list of devices synced since the last sync is returned in the response.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
domain = 'domain_example' # str | Smart Account Domain
name = 'name_example' # str | Virtual Account Name

try:
    # Get Sync Result for Virtual Account
    api_response = api_instance.api_v1_onboarding_pnp_device_sacct_domain_vacct_name_sync_result_get(domain, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_sacct_domain_vacct_name_sync_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Smart Account Domain | 
 **name** | **str**| Virtual Account Name | 

### Return type

[**GetSyncResultForVirtualAccountResponse**](GetSyncResultForVirtualAccountResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_unclaim_post**
> UnClaimDeviceResponse api_v1_onboarding_pnp_device_unclaim_post(request)

Un-Claim Device

This API is used to unassign the project and workflow from one or more device.A device can only be unclaimed if it has not begun provisioning.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.UnclaimRequest() # UnclaimRequest | request

try:
    # Un-Claim Device
    api_response = api_instance.api_v1_onboarding_pnp_device_unclaim_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_unclaim_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UnclaimRequest**](UnclaimRequest.md)| request | 

### Return type

[**UnClaimDeviceResponse**](UnClaimDeviceResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_device_vacct_sync_post**
> SyncVirtualAccountDevicesResponse api_v1_onboarding_pnp_device_vacct_sync_post(request)

Sync Virtual Account Devices

This API is used to sync the device info from the given smart account & virtual account with the PnP database. The list of synced devices is returned in the response.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SAVAMapping() # SAVAMapping | request

try:
    # Sync Virtual Account Devices
    api_response = api_instance.api_v1_onboarding_pnp_device_vacct_sync_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_device_vacct_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SAVAMapping**](SAVAMapping.md)| request | 

### Return type

[**SyncVirtualAccountDevicesResponse**](SyncVirtualAccountDevicesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_settings_get**
> ViewSettingsResponse api_v1_onboarding_pnp_settings_get()

View Settings

Get this user's list of global PnP settings

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))

try:
    # View Settings
    api_response = api_instance.api_v1_onboarding_pnp_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ViewSettingsResponse**](ViewSettingsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_settings_put**
> UpdateSettingsResponse api_v1_onboarding_pnp_settings_put(request)

Update Settings

Change this user's list of global PnP settings

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.Settings() # Settings | request

try:
    # Update Settings
    api_response = api_instance.api_v1_onboarding_pnp_settings_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Settings**](Settings.md)| request | 

### Return type

[**UpdateSettingsResponse**](UpdateSettingsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_settings_sacct_domain_vacct_get**
> GetVirtualAccountListResponse api_v1_onboarding_pnp_settings_sacct_domain_vacct_get(domain)

Get Virtual Account List

This API is used to get list of Virtual Accounts associated with the specified Smart Account. The list of virtual account names is returned in the response.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
domain = 'domain_example' # str | Smart Account Domain

try:
    # Get Virtual Account List
    api_response = api_instance.api_v1_onboarding_pnp_settings_sacct_domain_vacct_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_settings_sacct_domain_vacct_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Smart Account Domain | 

### Return type

[**GetVirtualAccountListResponse**](GetVirtualAccountListResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_settings_sacct_get**
> GetSmartAccountListResponse api_v1_onboarding_pnp_settings_sacct_get()

Get Smart Account List

This API is used to get list of Smart Accounts. The list of smart account domains is returned in the response.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))

try:
    # Get Smart Account List
    api_response = api_instance.api_v1_onboarding_pnp_settings_sacct_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_settings_sacct_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSmartAccountListResponse**](GetSmartAccountListResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_settings_savacct_post**
> AddVirtualAccountResponse api_v1_onboarding_pnp_settings_savacct_post(request)

Add Virtual Account

This API is used to register a Smart Account, Virtual Account and the relevant server profile info with the PnP System & database. The devices present in the registered virtual account are synced with the PnP database as well. The new profile is returned in the response.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SAVAMapping() # SAVAMapping | request

try:
    # Add Virtual Account
    api_response = api_instance.api_v1_onboarding_pnp_settings_savacct_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_settings_savacct_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SAVAMapping**](SAVAMapping.md)| request | 

### Return type

[**AddVirtualAccountResponse**](AddVirtualAccountResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_settings_savacct_put**
> EditPnPServerProfileResponse api_v1_onboarding_pnp_settings_savacct_put(request)

Edit PnP Server Profile

This API is used to edit the PnP Server profile in a registered Virtual Account in the PnP database.The edited smart & virtual account info is returned in the response.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.SAVAMapping() # SAVAMapping | request

try:
    # Edit PnP Server Profile
    api_response = api_instance.api_v1_onboarding_pnp_settings_savacct_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_settings_savacct_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SAVAMapping**](SAVAMapping.md)| request | 

### Return type

[**EditPnPServerProfileResponse**](EditPnPServerProfileResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_settings_vacct_delete**
> DeregisterVirtualAccountResponse api_v1_onboarding_pnp_settings_vacct_delete(domain, name)

Deregister Virtual Account

This API is used to deregister the specified smart account & virtual account info and the associated device information from the PnP System & database. The devices associated with the deregistered virtual account are removed from the PnP database as well. The deregistered smart & virtual account info is returned in the response.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
domain = 'domain_example' # str | Smart Account Domain
name = 'name_example' # str | Virtual Account Name

try:
    # Deregister Virtual Account
    api_response = api_instance.api_v1_onboarding_pnp_settings_vacct_delete(domain, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_settings_vacct_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Smart Account Domain | 
 **name** | **str**| Virtual Account Name | 

### Return type

[**DeregisterVirtualAccountResponse**](DeregisterVirtualAccountResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_workflow_count_get**
> GetWorkflowCountResponse api_v1_onboarding_pnp_workflow_count_get(name=name)

Get Workflow Count

This API is used to get the number of the workflows.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
name = ['name_example'] # list[str] | Workflow Name (optional)

try:
    # Get Workflow Count
    api_response = api_instance.api_v1_onboarding_pnp_workflow_count_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_workflow_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**list[str]**](str.md)| Workflow Name | [optional] 

### Return type

[**GetWorkflowCountResponse**](GetWorkflowCountResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_workflow_get**
> ListWorkflowsResponse api_v1_onboarding_pnp_workflow_get(limit=limit, offset=offset, sort=sort, sort_order=sort_order, type=type, name=name)

List Workflows

This API is used to get the list of workflows that match the provided filter. Pagination and sorting are also supported. If a limit is not specified, it will default to return 50 workflows.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
limit = 56 # int | Limits number of results (optional)
offset = 56 # int | Index of first result (optional)
sort = ['sort_example'] # list[str] | Comma seperated lost of fields to sort on (optional)
sort_order = 'sort_order_example' # str | Sort Order Ascending (asc) or Descending (des) (optional)
type = ['type_example'] # list[str] | Workflow Type (optional)
name = ['name_example'] # list[str] | Workflow Name (optional)

try:
    # List Workflows
    api_response = api_instance.api_v1_onboarding_pnp_workflow_get(limit=limit, offset=offset, sort=sort, sort_order=sort_order, type=type, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_workflow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits number of results | [optional] 
 **offset** | **int**| Index of first result | [optional] 
 **sort** | [**list[str]**](str.md)| Comma seperated lost of fields to sort on | [optional] 
 **sort_order** | **str**| Sort Order Ascending (asc) or Descending (des) | [optional] 
 **type** | [**list[str]**](str.md)| Workflow Type | [optional] 
 **name** | [**list[str]**](str.md)| Workflow Name | [optional] 

### Return type

[**ListWorkflowsResponse**](ListWorkflowsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_workflow_id_delete**
> DeleteWorkflowResponse api_v1_onboarding_pnp_workflow_id_delete(id)

Delete Workflow

Delete a workflow given its id

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete Workflow
    api_response = api_instance.api_v1_onboarding_pnp_workflow_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_workflow_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**DeleteWorkflowResponse**](DeleteWorkflowResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_workflow_id_get**
> GetWorkflowResponse api_v1_onboarding_pnp_workflow_id_get(id)

Get Workflow

Get a workflow given its id

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Get Workflow
    api_response = api_instance.api_v1_onboarding_pnp_workflow_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_workflow_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**GetWorkflowResponse**](GetWorkflowResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_workflow_id_put**
> UpdateWorkflowResponse api_v1_onboarding_pnp_workflow_id_put(request, id)

Update Workflow

Update an existing workflow

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.Workflow() # Workflow | request
id = 'id_example' # str | id

try:
    # Update Workflow
    api_response = api_instance.api_v1_onboarding_pnp_workflow_id_put(request, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_workflow_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Workflow**](Workflow.md)| request | 
 **id** | **str**| id | 

### Return type

[**UpdateWorkflowResponse**](UpdateWorkflowResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_onboarding_pnp_workflow_post**
> CreateWorkflowResponse api_v1_onboarding_pnp_workflow_post(request)

Create Workflow

This API is used to add a PnP Workflow along with the relevant tasks in the workflow into the PnP database.

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
api_instance = dnac_api_client.PnPApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.Workflow() # Workflow | request

try:
    # Create Workflow
    api_response = api_instance.api_v1_onboarding_pnp_workflow_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnPApi->api_v1_onboarding_pnp_workflow_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Workflow**](Workflow.md)| request | 

### Return type

[**CreateWorkflowResponse**](CreateWorkflowResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

