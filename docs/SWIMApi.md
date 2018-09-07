# dnac_api_client.SWIMApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_image_activation_device_post**](SWIMApi.md#api_v1_image_activation_device_post) | **POST** /api/v1/image/activation/device | Trigger activation on a device
[**api_v1_image_distribution_post**](SWIMApi.md#api_v1_image_distribution_post) | **POST** /api/v1/image/distribution | Trigger distribution of an image
[**api_v1_image_importation_get**](SWIMApi.md#api_v1_image_importation_get) | **GET** /api/v1/image/importation | Get image details with filter
[**api_v1_image_importation_source_file_post**](SWIMApi.md#api_v1_image_importation_source_file_post) | **POST** /api/v1/image/importation/source/file | Import an image from local file system
[**api_v1_image_importation_source_url_post**](SWIMApi.md#api_v1_image_importation_source_url_post) | **POST** /api/v1/image/importation/source/url | Trigger now or schedule import of an image from a URL


# **api_v1_image_activation_device_post**
> TaskIdResult api_v1_image_activation_device_post(request, client_type=client_type, client_url=client_url, schedule_validate=schedule_validate)

Trigger activation on a device

Performs activation of an image on a given device.

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
api_instance = dnac_api_client.SWIMApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.ActivateDTO() # ActivateDTO | request
client_type = 'client_type_example' # str | Client-type (Optional) (optional)
client_url = 'client_url_example' # str | Client-url (Optional) (optional)
schedule_validate = true # bool | scheduleValidate, validates data before schedule (Optional) (optional)

try:
    # Trigger activation on a device
    api_response = api_instance.api_v1_image_activation_device_post(request, client_type=client_type, client_url=client_url, schedule_validate=schedule_validate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SWIMApi->api_v1_image_activation_device_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ActivateDTO**](ActivateDTO.md)| request | 
 **client_type** | **str**| Client-type (Optional) | [optional] 
 **client_url** | **str**| Client-url (Optional) | [optional] 
 **schedule_validate** | **bool**| scheduleValidate, validates data before schedule (Optional) | [optional] 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_image_distribution_post**
> TaskIdResult api_v1_image_distribution_post(request)

Trigger distribution of an image

Performs distribution of an image to a given device.

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
api_instance = dnac_api_client.SWIMApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.DistributeDTO() # DistributeDTO | request

try:
    # Trigger distribution of an image
    api_response = api_instance.api_v1_image_distribution_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SWIMApi->api_v1_image_distribution_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DistributeDTO**](DistributeDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_image_importation_get**
> ImageInfoListResponse api_v1_image_importation_get(image_uuid=image_uuid, name=name, family=family, application_type=application_type, image_integrity_status=image_integrity_status, version=version, image_series=image_series, image_name=image_name, is_tagged_golden=is_tagged_golden, is_cco_recommended=is_cco_recommended, is_cco_latest=is_cco_latest, created_time=created_time, image_size_greater_than=image_size_greater_than, image_size_lesser_than=image_size_lesser_than, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset)

Get image details with filter

Get image details based on filter criteria, use % for like operations. Example: filterByName = cat3k%

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
api_instance = dnac_api_client.SWIMApi(dnac_api_client.ApiClient(configuration))
image_uuid = 'image_uuid_example' # str | imageUuid (optional)
name = 'name_example' # str | name (optional)
family = 'family_example' # str | family (optional)
application_type = 'application_type_example' # str | applicationType (optional)
image_integrity_status = 'image_integrity_status_example' # str | imageIntegrityStatus - FAILURE, UNKNOWN, VERIFIED (optional)
version = 'version_example' # str | software Image Version (optional)
image_series = 'image_series_example' # str | image Series (optional)
image_name = 'image_name_example' # str | image Name (optional)
is_tagged_golden = true # bool | is Tagged Golden (optional)
is_cco_recommended = true # bool | is recommended from cisco.com (optional)
is_cco_latest = true # bool | is latest from cisco.com (optional)
created_time = 56 # int | time in milliseconds (epoch format) (optional)
image_size_greater_than = 56 # int | size in bytes (optional)
image_size_lesser_than = 56 # int | size in bytes (optional)
sort_by = 'sort_by_example' # str | sort results by this field (optional)
sort_order = 'sort_order_example' # str | sort order - 'asc' or 'des'. Default is asc (optional)
limit = 56 # int | limit (optional)
offset = 56 # int | offset (optional)

try:
    # Get image details with filter
    api_response = api_instance.api_v1_image_importation_get(image_uuid=image_uuid, name=name, family=family, application_type=application_type, image_integrity_status=image_integrity_status, version=version, image_series=image_series, image_name=image_name, is_tagged_golden=is_tagged_golden, is_cco_recommended=is_cco_recommended, is_cco_latest=is_cco_latest, created_time=created_time, image_size_greater_than=image_size_greater_than, image_size_lesser_than=image_size_lesser_than, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SWIMApi->api_v1_image_importation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_uuid** | **str**| imageUuid | [optional] 
 **name** | **str**| name | [optional] 
 **family** | **str**| family | [optional] 
 **application_type** | **str**| applicationType | [optional] 
 **image_integrity_status** | **str**| imageIntegrityStatus - FAILURE, UNKNOWN, VERIFIED | [optional] 
 **version** | **str**| software Image Version | [optional] 
 **image_series** | **str**| image Series | [optional] 
 **image_name** | **str**| image Name | [optional] 
 **is_tagged_golden** | **bool**| is Tagged Golden | [optional] 
 **is_cco_recommended** | **bool**| is recommended from cisco.com | [optional] 
 **is_cco_latest** | **bool**| is latest from cisco.com | [optional] 
 **created_time** | **int**| time in milliseconds (epoch format) | [optional] 
 **image_size_greater_than** | **int**| size in bytes | [optional] 
 **image_size_lesser_than** | **int**| size in bytes | [optional] 
 **sort_by** | **str**| sort results by this field | [optional] 
 **sort_order** | **str**| sort order - &#39;asc&#39; or &#39;des&#39;. Default is asc | [optional] 
 **limit** | **int**| limit | [optional] 
 **offset** | **int**| offset | [optional] 

### Return type

[**ImageInfoListResponse**](ImageInfoListResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_image_importation_source_file_post**
> TaskIdResult api_v1_image_importation_source_file_post(is_third_party=is_third_party, third_party_vendor=third_party_vendor, third_party_image_family=third_party_image_family, third_party_application_type=third_party_application_type)

Import an image from local file system

Imports an image to SWIM image repository from local file system. The image files with extensions bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2 are supported. Set siteUuid as -1 to tag as golden image.

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
api_instance = dnac_api_client.SWIMApi(dnac_api_client.ApiClient(configuration))
is_third_party = true # bool | Third party Image check (optional)
third_party_vendor = 'third_party_vendor_example' # str | Third Party Vendor (optional)
third_party_image_family = 'third_party_image_family_example' # str | Third Party image family (optional)
third_party_application_type = 'third_party_application_type_example' # str | Third Party Application Type (optional)

try:
    # Import an image from local file system
    api_response = api_instance.api_v1_image_importation_source_file_post(is_third_party=is_third_party, third_party_vendor=third_party_vendor, third_party_image_family=third_party_image_family, third_party_application_type=third_party_application_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SWIMApi->api_v1_image_importation_source_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_third_party** | **bool**| Third party Image check | [optional] 
 **third_party_vendor** | **str**| Third Party Vendor | [optional] 
 **third_party_image_family** | **str**| Third Party image family | [optional] 
 **third_party_application_type** | **str**| Third Party Application Type | [optional] 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_image_importation_source_url_post**
> TaskIdResult api_v1_image_importation_source_url_post(request, schedule_at=schedule_at, schedule_desc=schedule_desc, schedule_origin=schedule_origin)

Trigger now or schedule import of an image from a URL

Imports an image to SWIM image repository, source is any ftp or http URL. The image files with extensions bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2 are supported. Set siteUuid as -1 to tag as golden image.

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
api_instance = dnac_api_client.SWIMApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.ImageImportFromUrlDTO() # ImageImportFromUrlDTO | request
schedule_at = 'schedule_at_example' # str | Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the distribution should be scheduled (Optional)  (optional)
schedule_desc = 'schedule_desc_example' # str | Custom Description (Optional) (optional)
schedule_origin = 'schedule_origin_example' # str | Originator of this call (Optional) (optional)

try:
    # Trigger now or schedule import of an image from a URL
    api_response = api_instance.api_v1_image_importation_source_url_post(request, schedule_at=schedule_at, schedule_desc=schedule_desc, schedule_origin=schedule_origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SWIMApi->api_v1_image_importation_source_url_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ImageImportFromUrlDTO**](ImageImportFromUrlDTO.md)| request | 
 **schedule_at** | **str**| Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the distribution should be scheduled (Optional)  | [optional] 
 **schedule_desc** | **str**| Custom Description (Optional) | [optional] 
 **schedule_origin** | **str**| Originator of this call (Optional) | [optional] 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

