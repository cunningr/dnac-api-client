# dnac_api_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_system_v1_maglev_backup_backup_id_delete**](DefaultApi.md#api_system_v1_maglev_backup_backup_id_delete) | **DELETE** /api/system/v1/maglev/backup/{BackupId} | Delete a restore point
[**api_system_v1_maglev_backup_get**](DefaultApi.md#api_system_v1_maglev_backup_get) | **GET** /api/system/v1/maglev/backup | Configured Backup Destination
[**api_system_v1_maglev_backup_history_get**](DefaultApi.md#api_system_v1_maglev_backup_history_get) | **GET** /api/system/v1/maglev/backup/history | Backup History
[**api_system_v1_maglev_backup_post**](DefaultApi.md#api_system_v1_maglev_backup_post) | **POST** /api/system/v1/maglev/backup | Creates a new Backup Point
[**api_system_v1_maglev_backup_progress_get**](DefaultApi.md#api_system_v1_maglev_backup_progress_get) | **GET** /api/system/v1/maglev/backup/progress | Backup Progress
[**api_system_v1_maglev_backup_remote_settings_get**](DefaultApi.md#api_system_v1_maglev_backup_remote_settings_get) | **GET** /api/system/v1/maglev/backup/remote/settings | Configured Backup Destination
[**api_system_v1_maglev_backup_remote_settings_put**](DefaultApi.md#api_system_v1_maglev_backup_remote_settings_put) | **PUT** /api/system/v1/maglev/backup/remote/settings | Updates Backup Server details
[**api_system_v1_maglev_restore_backup_id_post**](DefaultApi.md#api_system_v1_maglev_restore_backup_id_post) | **POST** /api/system/v1/maglev/restore/{BackupId} | Initiate Restore
[**api_v1_group_count_get**](DefaultApi.md#api_v1_group_count_get) | **GET** /api/v1/group/count | Returns the Site groups
[**api_v1_group_get**](DefaultApi.md#api_v1_group_get) | **GET** /api/v1/group | Returns the Site groups
[**api_v1_groupgroup_id_delete**](DefaultApi.md#api_v1_groupgroup_id_delete) | **DELETE** /api/v1/group{groupId} | Deletes a group from DNAC
[**api_v2_ippool_get**](DefaultApi.md#api_v2_ippool_get) | **GET** /api/v2/ippool | Fetches a list of configured IP Pools
[**api_v2_ippool_pool_id_delete**](DefaultApi.md#api_v2_ippool_pool_id_delete) | **DELETE** /api/v2/ippool/{poolId} | Deletes an IP pool to DNAC
[**api_v2_ippool_post**](DefaultApi.md#api_v2_ippool_post) | **POST** /api/v2/ippool | Adds an IP pool to DNAC


# **api_system_v1_maglev_backup_backup_id_delete**
> object api_system_v1_maglev_backup_backup_id_delete(backup_id)

Delete a restore point

Delete the restore point with given BackupId

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))
backup_id = 'backup_id_example' # str | UUID of Backup to restore

try:
    # Delete a restore point
    api_response = api_instance.api_system_v1_maglev_backup_backup_id_delete(backup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_system_v1_maglev_backup_backup_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_id** | **str**| UUID of Backup to restore | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_v1_maglev_backup_get**
> BackupDetailResponse api_system_v1_maglev_backup_get()

Configured Backup Destination

Fetches the configured backup destination

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))

try:
    # Configured Backup Destination
    api_response = api_instance.api_system_v1_maglev_backup_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_system_v1_maglev_backup_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupDetailResponse**](BackupDetailResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_v1_maglev_backup_history_get**
> object api_system_v1_maglev_backup_history_get()

Backup History

Fetches the backup history

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))

try:
    # Backup History
    api_response = api_instance.api_system_v1_maglev_backup_history_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_system_v1_maglev_backup_history_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_v1_maglev_backup_post**
> object api_system_v1_maglev_backup_post(backup)

Creates a new Backup Point

Initiates a new backup job

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))
backup = dnac_api_client.Backup() # Backup | Description of Backup point

try:
    # Creates a new Backup Point
    api_response = api_instance.api_system_v1_maglev_backup_post(backup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_system_v1_maglev_backup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | [**Backup**](Backup.md)| Description of Backup point | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_v1_maglev_backup_progress_get**
> object api_system_v1_maglev_backup_progress_get()

Backup Progress

Fetches the backup progress

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))

try:
    # Backup Progress
    api_response = api_instance.api_system_v1_maglev_backup_progress_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_system_v1_maglev_backup_progress_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_v1_maglev_backup_remote_settings_get**
> BackupRemote api_system_v1_maglev_backup_remote_settings_get()

Configured Backup Destination

Fetches the configured backup destination

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))

try:
    # Configured Backup Destination
    api_response = api_instance.api_system_v1_maglev_backup_remote_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_system_v1_maglev_backup_remote_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupRemote**](BackupRemote.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_v1_maglev_backup_remote_settings_put**
> object api_system_v1_maglev_backup_remote_settings_put(backup_remote)

Updates Backup Server details

Updates the remote backup server details

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))
backup_remote = dnac_api_client.BackupRemote() # BackupRemote | Bacup Remote Detais

try:
    # Updates Backup Server details
    api_response = api_instance.api_system_v1_maglev_backup_remote_settings_put(backup_remote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_system_v1_maglev_backup_remote_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_remote** | [**BackupRemote**](BackupRemote.md)| Bacup Remote Detais | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_v1_maglev_restore_backup_id_post**
> object api_system_v1_maglev_restore_backup_id_post(backup_id)

Initiate Restore

Initiate Restore of given BackupId

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))
backup_id = 'backup_id_example' # str | UUID of Backup to restore

try:
    # Initiate Restore
    api_response = api_instance.api_system_v1_maglev_restore_backup_id_post(backup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_system_v1_maglev_restore_backup_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_id** | **str**| UUID of Backup to restore | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_group_count_get**
> Response api_v1_group_count_get(group_type=group_type)

Returns the Site groups

Returns the Site groups.

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))
group_type = 'group_type_example' # str | groupName (Optional) (optional)

try:
    # Returns the Site groups
    api_response = api_instance.api_v1_group_count_get(group_type=group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_group_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_type** | **str**| groupName (Optional) | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_group_get**
> Response api_v1_group_get(group_name=group_name, group_type=group_type, field=field)

Returns the Site groups

Returns the Site groups.

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))
group_name = 'group_name_example' # str | groupName (Optional) (optional)
group_type = 'group_type_example' # str | groupType (Optional) (optional)
field = 'field_example' # str | field (Optional) (optional)

try:
    # Returns the Site groups
    api_response = api_instance.api_v1_group_get(group_name=group_name, group_type=group_type, field=field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| groupName (Optional) | [optional] 
 **group_type** | **str**| groupType (Optional) | [optional] 
 **field** | **str**| field (Optional) | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_groupgroup_id_delete**
> object api_v1_groupgroup_id_delete(group_id)

Deletes a group from DNAC

Deletes a group from DNAC

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))
group_id = 'group_id_example' # str | UID of group to delete

try:
    # Deletes a group from DNAC
    api_response = api_instance.api_v1_groupgroup_id_delete(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_groupgroup_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| UID of group to delete | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_ippool_get**
> object api_v2_ippool_get()

Fetches a list of configured IP Pools

Fetches all IP Pools.

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))

try:
    # Fetches a list of configured IP Pools
    api_response = api_instance.api_v2_ippool_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v2_ippool_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_ippool_pool_id_delete**
> object api_v2_ippool_pool_id_delete(pool_id)

Deletes an IP pool to DNAC

Deletes an IP Pool.

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | UID of IP Pool to delete

try:
    # Deletes an IP pool to DNAC
    api_response = api_instance.api_v2_ippool_pool_id_delete(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v2_ippool_pool_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| UID of IP Pool to delete | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_ippool_post**
> object api_v2_ippool_post(ippool)

Adds an IP pool to DNAC

Creates an IP Pool.

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
api_instance = dnac_api_client.DefaultApi(dnac_api_client.ApiClient(configuration))
ippool = dnac_api_client.Ippool() # Ippool | IP pool object

try:
    # Adds an IP pool to DNAC
    api_response = api_instance.api_v2_ippool_post(ippool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v2_ippool_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ippool** | [**Ippool**](Ippool.md)| IP pool object | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

