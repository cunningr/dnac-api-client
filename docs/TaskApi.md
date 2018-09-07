# dnac_api_client.TaskApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_task_count_get**](TaskApi.md#api_v1_task_count_get) | **GET** /api/v1/task/count | Get task count
[**api_v1_task_get**](TaskApi.md#api_v1_task_get) | **GET** /api/v1/task | Get filtered tasks
[**api_v1_task_operation_operation_id_offset_limit_get**](TaskApi.md#api_v1_task_operation_operation_id_offset_limit_get) | **GET** /api/v1/task/operation/{operationId}/{offset}/{limit} | getTaskByOperationId
[**api_v1_task_task_id_get**](TaskApi.md#api_v1_task_task_id_get) | **GET** /api/v1/task/{taskId} | getTruststoreFileCount
[**api_v1_task_task_id_tree_get**](TaskApi.md#api_v1_task_task_id_tree_get) | **GET** /api/v1/task/{taskId}/tree | Get Task Tree


# **api_v1_task_count_get**
> CountResult api_v1_task_count_get(start_time=start_time, end_time=end_time, data=data, error_code=error_code, service_type=service_type, username=username, progress=progress, is_error=is_error, failure_reason=failure_reason, parent_id=parent_id)

Get task count

This method is used to retrieve task count

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
api_instance = dnac_api_client.TaskApi(dnac_api_client.ApiClient(configuration))
start_time = 'start_time_example' # str | This is the epoch start time from which tasks need to be fetched (optional)
end_time = 'end_time_example' # str | This is the epoch end time upto which audit records need to be fetched (optional)
data = 'data_example' # str | Fetch tasks that contains this data (optional)
error_code = 'error_code_example' # str | Fetch tasks that have this error code (optional)
service_type = 'service_type_example' # str | Fetch tasks with this service type (optional)
username = 'username_example' # str | Fetch tasks with this username (optional)
progress = 'progress_example' # str | Fetch tasks that contains this progress (optional)
is_error = 'is_error_example' # str | Fetch tasks ended as success or failure. Valid values: true, false (optional)
failure_reason = 'failure_reason_example' # str | Fetch tasks that contains this failure reason (optional)
parent_id = 'parent_id_example' # str | Fetch tasks that have this parent Id (optional)

try:
    # Get task count
    api_response = api_instance.api_v1_task_count_get(start_time=start_time, end_time=end_time, data=data, error_code=error_code, service_type=service_type, username=username, progress=progress, is_error=is_error, failure_reason=failure_reason, parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_v1_task_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| This is the epoch start time from which tasks need to be fetched | [optional] 
 **end_time** | **str**| This is the epoch end time upto which audit records need to be fetched | [optional] 
 **data** | **str**| Fetch tasks that contains this data | [optional] 
 **error_code** | **str**| Fetch tasks that have this error code | [optional] 
 **service_type** | **str**| Fetch tasks with this service type | [optional] 
 **username** | **str**| Fetch tasks with this username | [optional] 
 **progress** | **str**| Fetch tasks that contains this progress | [optional] 
 **is_error** | **str**| Fetch tasks ended as success or failure. Valid values: true, false | [optional] 
 **failure_reason** | **str**| Fetch tasks that contains this failure reason | [optional] 
 **parent_id** | **str**| Fetch tasks that have this parent Id | [optional] 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_task_get**
> TaskDTOListResponse api_v1_task_get(start_time=start_time, end_time=end_time, data=data, error_code=error_code, service_type=service_type, username=username, progress=progress, is_error=is_error, failure_reason=failure_reason, parent_id=parent_id, offset=offset, limit=limit, sort_by=sort_by, order=order)

Get filtered tasks

This method is used to retrieve task(s) based on various filters

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
api_instance = dnac_api_client.TaskApi(dnac_api_client.ApiClient(configuration))
start_time = 'start_time_example' # str | This is the epoch start time from which tasks need to be fetched (optional)
end_time = 'end_time_example' # str | This is the epoch end time upto which audit records need to be fetched (optional)
data = 'data_example' # str | Fetch tasks that contains this data (optional)
error_code = 'error_code_example' # str | Fetch tasks that have this error code (optional)
service_type = 'service_type_example' # str | Fetch tasks with this service type (optional)
username = 'username_example' # str | Fetch tasks with this username (optional)
progress = 'progress_example' # str | Fetch tasks that contains this progress (optional)
is_error = 'is_error_example' # str | Fetch tasks ended as success or failure. Valid values: true, false (optional)
failure_reason = 'failure_reason_example' # str | Fetch tasks that contains this failure reason (optional)
parent_id = 'parent_id_example' # str | Fetch tasks that have this parent Id (optional)
offset = 'offset_example' # str | offset (optional)
limit = 'limit_example' # str | limit (optional)
sort_by = 'sort_by_example' # str | Sort results by this field (optional)
order = 'order_example' # str | Sort order - asc or dsc (optional)

try:
    # Get filtered tasks
    api_response = api_instance.api_v1_task_get(start_time=start_time, end_time=end_time, data=data, error_code=error_code, service_type=service_type, username=username, progress=progress, is_error=is_error, failure_reason=failure_reason, parent_id=parent_id, offset=offset, limit=limit, sort_by=sort_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_v1_task_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| This is the epoch start time from which tasks need to be fetched | [optional] 
 **end_time** | **str**| This is the epoch end time upto which audit records need to be fetched | [optional] 
 **data** | **str**| Fetch tasks that contains this data | [optional] 
 **error_code** | **str**| Fetch tasks that have this error code | [optional] 
 **service_type** | **str**| Fetch tasks with this service type | [optional] 
 **username** | **str**| Fetch tasks with this username | [optional] 
 **progress** | **str**| Fetch tasks that contains this progress | [optional] 
 **is_error** | **str**| Fetch tasks ended as success or failure. Valid values: true, false | [optional] 
 **failure_reason** | **str**| Fetch tasks that contains this failure reason | [optional] 
 **parent_id** | **str**| Fetch tasks that have this parent Id | [optional] 
 **offset** | **str**| offset | [optional] 
 **limit** | **str**| limit | [optional] 
 **sort_by** | **str**| Sort results by this field | [optional] 
 **order** | **str**| Sort order - asc or dsc | [optional] 

### Return type

[**TaskDTOListResponse**](TaskDTOListResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_task_operation_operation_id_offset_limit_get**
> TaskDTOListResponse api_v1_task_operation_operation_id_offset_limit_get(operation_id, offset, limit)

getTaskByOperationId

This method is used to find root tasks assoicated to an operationid 

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
api_instance = dnac_api_client.TaskApi(dnac_api_client.ApiClient(configuration))
operation_id = 'operation_id_example' # str | operationId
offset = 56 # int | Index, minimum value is 0
limit = 56 # int | The maximum value of {limit} supported is 500. <br/> Base 1 indexing for {limit}, minimum value is 1

try:
    # getTaskByOperationId
    api_response = api_instance.api_v1_task_operation_operation_id_offset_limit_get(operation_id, offset, limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_v1_task_operation_operation_id_offset_limit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**| operationId | 
 **offset** | **int**| Index, minimum value is 0 | 
 **limit** | **int**| The maximum value of {limit} supported is 500. &lt;br/&gt; Base 1 indexing for {limit}, minimum value is 1 | 

### Return type

[**TaskDTOListResponse**](TaskDTOListResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_task_task_id_get**
> TaskDTOResponse api_v1_task_task_id_get(task_id)

getTruststoreFileCount

This method is used to retrieve a task based on their id

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
api_instance = dnac_api_client.TaskApi(dnac_api_client.ApiClient(configuration))
task_id = 'task_id_example' # str | UUID of the Task

try:
    # getTruststoreFileCount
    api_response = api_instance.api_v1_task_task_id_get(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_v1_task_task_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| UUID of the Task | 

### Return type

[**TaskDTOResponse**](TaskDTOResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_task_task_id_tree_get**
> TaskDTOListResponse api_v1_task_task_id_tree_get(task_id)

Get Task Tree

This method is used to retrieve a task with its children tasks based on their id

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
api_instance = dnac_api_client.TaskApi(dnac_api_client.ApiClient(configuration))
task_id = 'task_id_example' # str | UUID of the Task

try:
    # Get Task Tree
    api_response = api_instance.api_v1_task_task_id_tree_get(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->api_v1_task_task_id_tree_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| UUID of the Task | 

### Return type

[**TaskDTOListResponse**](TaskDTOListResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

