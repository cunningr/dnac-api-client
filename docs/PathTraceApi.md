# dnac_api_client.PathTraceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_flow_analysis_flow_analysis_id_delete**](PathTraceApi.md#api_v1_flow_analysis_flow_analysis_id_delete) | **DELETE** /api/v1/flow-analysis/{flowAnalysisId} | Deletes a flow analysis request
[**api_v1_flow_analysis_flow_analysis_id_get**](PathTraceApi.md#api_v1_flow_analysis_flow_analysis_id_get) | **GET** /api/v1/flow-analysis/{flowAnalysisId} | Retrieves result of a previously requested flow analysis
[**api_v1_flow_analysis_get**](PathTraceApi.md#api_v1_flow_analysis_get) | **GET** /api/v1/flow-analysis | Retrieves a summary of all flow analyses stored
[**api_v1_flow_analysis_post**](PathTraceApi.md#api_v1_flow_analysis_post) | **POST** /api/v1/flow-analysis | Initiates a new flow analysis


# **api_v1_flow_analysis_flow_analysis_id_delete**
> TaskIdResult api_v1_flow_analysis_flow_analysis_id_delete(flow_analysis_id)

Deletes a flow analysis request

Deletes a flow analysis request by its id

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
api_instance = dnac_api_client.PathTraceApi(dnac_api_client.ApiClient(configuration))
flow_analysis_id = 'flow_analysis_id_example' # str | Flow analysis request id

try:
    # Deletes a flow analysis request
    api_response = api_instance.api_v1_flow_analysis_flow_analysis_id_delete(flow_analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathTraceApi->api_v1_flow_analysis_flow_analysis_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_analysis_id** | **str**| Flow analysis request id | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_flow_analysis_flow_analysis_id_get**
> PathResponseResult api_v1_flow_analysis_flow_analysis_id_get(flow_analysis_id)

Retrieves result of a previously requested flow analysis

Retrieves result of a previously requested flow analysis by its Flow Analysis id

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
api_instance = dnac_api_client.PathTraceApi(dnac_api_client.ApiClient(configuration))
flow_analysis_id = 'flow_analysis_id_example' # str | Flow analysis request id

try:
    # Retrieves result of a previously requested flow analysis
    api_response = api_instance.api_v1_flow_analysis_flow_analysis_id_get(flow_analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathTraceApi->api_v1_flow_analysis_flow_analysis_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_analysis_id** | **str**| Flow analysis request id | 

### Return type

[**PathResponseResult**](PathResponseResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_flow_analysis_get**
> FlowAnalysisListOutput api_v1_flow_analysis_get(periodic_refresh=periodic_refresh, source_ip=source_ip, dest_ip=dest_ip, source_port=source_port, dest_port=dest_port, gt_create_time=gt_create_time, lt_create_time=lt_create_time, protocol=protocol, status=status, task_id=task_id, last_update_time=last_update_time, limit=limit, offset=offset, order=order, sort_by=sort_by)

Retrieves a summary of all flow analyses stored

Retrieves a summary of all flow analyses stored. Filters the results by given parameters.

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
api_instance = dnac_api_client.PathTraceApi(dnac_api_client.ApiClient(configuration))
periodic_refresh = true # bool | Is analysis periodically refreshed? (optional)
source_ip = 'source_ip_example' # str | Source IP address (optional)
dest_ip = 'dest_ip_example' # str | Destination IP adress (optional)
source_port = 'source_port_example' # str | Source port (optional)
dest_port = 'dest_port_example' # str | Destination port (optional)
gt_create_time = 'gt_create_time_example' # str | Analyses requested after this time (optional)
lt_create_time = 'lt_create_time_example' # str | Analyses requested before this time (optional)
protocol = 'protocol_example' # str | Protocol (optional)
status = 'status_example' # str | Status (optional)
task_id = 'task_id_example' # str | Task ID (optional)
last_update_time = 'last_update_time_example' # str | Last update time (optional)
limit = 'limit_example' # str | Number of resources returned (optional)
offset = 'offset_example' # str | Start index of resources returned (1-based) (optional)
order = 'order_example' # str | Order by this field (optional)
sort_by = 'sort_by_example' # str | Sort by this field (optional)

try:
    # Retrieves a summary of all flow analyses stored
    api_response = api_instance.api_v1_flow_analysis_get(periodic_refresh=periodic_refresh, source_ip=source_ip, dest_ip=dest_ip, source_port=source_port, dest_port=dest_port, gt_create_time=gt_create_time, lt_create_time=lt_create_time, protocol=protocol, status=status, task_id=task_id, last_update_time=last_update_time, limit=limit, offset=offset, order=order, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathTraceApi->api_v1_flow_analysis_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **periodic_refresh** | **bool**| Is analysis periodically refreshed? | [optional] 
 **source_ip** | **str**| Source IP address | [optional] 
 **dest_ip** | **str**| Destination IP adress | [optional] 
 **source_port** | **str**| Source port | [optional] 
 **dest_port** | **str**| Destination port | [optional] 
 **gt_create_time** | **str**| Analyses requested after this time | [optional] 
 **lt_create_time** | **str**| Analyses requested before this time | [optional] 
 **protocol** | **str**| Protocol | [optional] 
 **status** | **str**| Status | [optional] 
 **task_id** | **str**| Task ID | [optional] 
 **last_update_time** | **str**| Last update time | [optional] 
 **limit** | **str**| Number of resources returned | [optional] 
 **offset** | **str**| Start index of resources returned (1-based) | [optional] 
 **order** | **str**| Order by this field | [optional] 
 **sort_by** | **str**| Sort by this field | [optional] 

### Return type

[**FlowAnalysisListOutput**](FlowAnalysisListOutput.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_flow_analysis_post**
> FlowAnalysisRequestResultOutput api_v1_flow_analysis_post(request)

Initiates a new flow analysis

Initiates a new flow analysis with periodic refresh and stat collection options. Returns a request id and a task id to get results and follow progress.

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
api_instance = dnac_api_client.PathTraceApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.FlowAnalysisRequest() # FlowAnalysisRequest | request

try:
    # Initiates a new flow analysis
    api_response = api_instance.api_v1_flow_analysis_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathTraceApi->api_v1_flow_analysis_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**FlowAnalysisRequest**](FlowAnalysisRequest.md)| request | 

### Return type

[**FlowAnalysisRequestResultOutput**](FlowAnalysisRequestResultOutput.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

