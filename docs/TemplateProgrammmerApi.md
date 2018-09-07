# dnac_api_client.TemplateProgrammmerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_template_programmer_project_get**](TemplateProgrammmerApi.md#api_v1_template_programmer_project_get) | **GET** /api/v1/template-programmer/project | Gets a list of projects
[**api_v1_template_programmer_project_post**](TemplateProgrammmerApi.md#api_v1_template_programmer_project_post) | **POST** /api/v1/template-programmer/project | Create Project
[**api_v1_template_programmer_project_project_id_delete**](TemplateProgrammmerApi.md#api_v1_template_programmer_project_project_id_delete) | **DELETE** /api/v1/template-programmer/project/{projectId} | Deletes the project
[**api_v1_template_programmer_project_project_id_template_post**](TemplateProgrammmerApi.md#api_v1_template_programmer_project_project_id_template_post) | **POST** /api/v1/template-programmer/project/{projectId}/template | Create Template
[**api_v1_template_programmer_project_put**](TemplateProgrammmerApi.md#api_v1_template_programmer_project_put) | **PUT** /api/v1/template-programmer/project | Update Project
[**api_v1_template_programmer_template_deploy_post**](TemplateProgrammmerApi.md#api_v1_template_programmer_template_deploy_post) | **POST** /api/v1/template-programmer/template/deploy | Deploy Template
[**api_v1_template_programmer_template_deploy_status_deployment_id_get**](TemplateProgrammmerApi.md#api_v1_template_programmer_template_deploy_status_deployment_id_get) | **GET** /api/v1/template-programmer/template/deploy/status/{deploymentId} | Status of template deployment
[**api_v1_template_programmer_template_get**](TemplateProgrammmerApi.md#api_v1_template_programmer_template_get) | **GET** /api/v1/template-programmer/template | Gets the templates available depending on the criteria
[**api_v1_template_programmer_template_preview_put**](TemplateProgrammmerApi.md#api_v1_template_programmer_template_preview_put) | **PUT** /api/v1/template-programmer/template/preview | Preview Template
[**api_v1_template_programmer_template_put**](TemplateProgrammmerApi.md#api_v1_template_programmer_template_put) | **PUT** /api/v1/template-programmer/template | Update Template
[**api_v1_template_programmer_template_template_id_delete**](TemplateProgrammmerApi.md#api_v1_template_programmer_template_template_id_delete) | **DELETE** /api/v1/template-programmer/template/{templateId} | Deletes the template
[**api_v1_template_programmer_template_template_id_get**](TemplateProgrammmerApi.md#api_v1_template_programmer_template_template_id_get) | **GET** /api/v1/template-programmer/template/{templateId} | Gets details of a given template
[**api_v1_template_programmer_template_version_post**](TemplateProgrammmerApi.md#api_v1_template_programmer_template_version_post) | **POST** /api/v1/template-programmer/template/version | Version Template
[**api_v1_template_programmer_template_version_template_id_get**](TemplateProgrammmerApi.md#api_v1_template_programmer_template_version_template_id_get) | **GET** /api/v1/template-programmer/template/version/{templateId} | Gets all the versions of a given template


# **api_v1_template_programmer_project_get**
> CollectionProjectDTO api_v1_template_programmer_project_get(name=name)

Gets a list of projects

List the projects

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
name = 'name_example' # str | Name of project to be searched (optional)

try:
    # Gets a list of projects
    api_response = api_instance.api_v1_template_programmer_project_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_project_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of project to be searched | [optional] 

### Return type

[**CollectionProjectDTO**](CollectionProjectDTO.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_project_post**
> TaskIdResult api_v1_template_programmer_project_post(request)

Create Project

This API is used to create a new project.

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.ProjectDTO() # ProjectDTO | request

try:
    # Create Project
    api_response = api_instance.api_v1_template_programmer_project_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_project_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ProjectDTO**](ProjectDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_project_project_id_delete**
> TaskIdResult api_v1_template_programmer_project_project_id_delete(project_id)

Deletes the project

Deletes the project

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
project_id = 'project_id_example' # str | projectId

try:
    # Deletes the project
    api_response = api_instance.api_v1_template_programmer_project_project_id_delete(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_project_project_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| projectId | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_project_project_id_template_post**
> TaskIdResult api_v1_template_programmer_project_project_id_template_post(request, project_id)

Create Template

API to create a template.

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.TemplateDTO() # TemplateDTO | request
project_id = 'project_id_example' # str | projectId

try:
    # Create Template
    api_response = api_instance.api_v1_template_programmer_project_project_id_template_post(request, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_project_project_id_template_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TemplateDTO**](TemplateDTO.md)| request | 
 **project_id** | **str**| projectId | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_project_put**
> TaskIdResult api_v1_template_programmer_project_put(request)

Update Project

This API is used to update an existing project.

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.ProjectDTO() # ProjectDTO | request

try:
    # Update Project
    api_response = api_instance.api_v1_template_programmer_project_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_project_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ProjectDTO**](ProjectDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_template_deploy_post**
> TemplateDeploymentStatusDTO api_v1_template_programmer_template_deploy_post(request)

Deploy Template

API to deploy a template.

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.TemplateDeploymentInfo() # TemplateDeploymentInfo | request

try:
    # Deploy Template
    api_response = api_instance.api_v1_template_programmer_template_deploy_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_template_deploy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TemplateDeploymentInfo**](TemplateDeploymentInfo.md)| request | 

### Return type

[**TemplateDeploymentStatusDTO**](TemplateDeploymentStatusDTO.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_template_deploy_status_deployment_id_get**
> TemplateDeploymentStatusDTO api_v1_template_programmer_template_deploy_status_deployment_id_get(deployment_id)

Status of template deployment

API to retrieve the status of template deployment.

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
deployment_id = 'deployment_id_example' # str | deploymentId

try:
    # Status of template deployment
    api_response = api_instance.api_v1_template_programmer_template_deploy_status_deployment_id_get(deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_template_deploy_status_deployment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| deploymentId | 

### Return type

[**TemplateDeploymentStatusDTO**](TemplateDeploymentStatusDTO.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_template_get**
> CollectionTemplateInfo api_v1_template_programmer_template_get(project_id=project_id, software_type=software_type, software_version=software_version, product_family=product_family, product_series=product_series, product_type=product_type, include_head=include_head, filter_conflicting_templates=filter_conflicting_templates)

Gets the templates available depending on the criteria

Gets the templates available depending on the criteria

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
project_id = 'project_id_example' # str | projectId (optional)
software_type = 'software_type_example' # str | softwareType (optional)
software_version = 'software_version_example' # str | softwareVersion (optional)
product_family = 'product_family_example' # str | productFamily (optional)
product_series = 'product_series_example' # str | productSeries (optional)
product_type = 'product_type_example' # str | productType (optional)
include_head = true # bool | includeHead (optional)
filter_conflicting_templates = true # bool | filterConflictingTemplates (optional)

try:
    # Gets the templates available depending on the criteria
    api_response = api_instance.api_v1_template_programmer_template_get(project_id=project_id, software_type=software_type, software_version=software_version, product_family=product_family, product_series=product_series, product_type=product_type, include_head=include_head, filter_conflicting_templates=filter_conflicting_templates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| projectId | [optional] 
 **software_type** | **str**| softwareType | [optional] 
 **software_version** | **str**| softwareVersion | [optional] 
 **product_family** | **str**| productFamily | [optional] 
 **product_series** | **str**| productSeries | [optional] 
 **product_type** | **str**| productType | [optional] 
 **include_head** | **bool**| includeHead | [optional] 
 **filter_conflicting_templates** | **bool**| filterConflictingTemplates | [optional] 

### Return type

[**CollectionTemplateInfo**](CollectionTemplateInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_template_preview_put**
> TemplatePreviewResponseDTO api_v1_template_programmer_template_preview_put(request)

Preview Template

API to preview a template.

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.TemplatePreviewRequestDTO() # TemplatePreviewRequestDTO | request

try:
    # Preview Template
    api_response = api_instance.api_v1_template_programmer_template_preview_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_template_preview_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TemplatePreviewRequestDTO**](TemplatePreviewRequestDTO.md)| request | 

### Return type

[**TemplatePreviewResponseDTO**](TemplatePreviewResponseDTO.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_template_put**
> TaskIdResult api_v1_template_programmer_template_put(request)

Update Template

API to update a template.

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.TemplateDTO() # TemplateDTO | request

try:
    # Update Template
    api_response = api_instance.api_v1_template_programmer_template_put(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_template_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TemplateDTO**](TemplateDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_template_template_id_delete**
> TaskIdResult api_v1_template_programmer_template_template_id_delete(template_id)

Deletes the template

Deletes the template

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
template_id = 'template_id_example' # str | templateId

try:
    # Deletes the template
    api_response = api_instance.api_v1_template_programmer_template_template_id_delete(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_template_template_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| templateId | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_template_template_id_get**
> TemplateDTO api_v1_template_programmer_template_template_id_get(template_id)

Gets details of a given template

Details of the template

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
template_id = 'template_id_example' # str | templateId

try:
    # Gets details of a given template
    api_response = api_instance.api_v1_template_programmer_template_template_id_get(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_template_template_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| templateId | 

### Return type

[**TemplateDTO**](TemplateDTO.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_template_version_post**
> TaskIdResult api_v1_template_programmer_template_version_post(request)

Version Template

API to version the current contents of the template.

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
request = dnac_api_client.TemplateVersionRequestDTO() # TemplateVersionRequestDTO | request

try:
    # Version Template
    api_response = api_instance.api_v1_template_programmer_template_version_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_template_version_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TemplateVersionRequestDTO**](TemplateVersionRequestDTO.md)| request | 

### Return type

[**TaskIdResult**](TaskIdResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_template_programmer_template_version_template_id_get**
> CollectionTemplateInfo api_v1_template_programmer_template_version_template_id_get(template_id)

Gets all the versions of a given template

Get all the versions of template

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
api_instance = dnac_api_client.TemplateProgrammmerApi(dnac_api_client.ApiClient(configuration))
template_id = 'template_id_example' # str | templateId

try:
    # Gets all the versions of a given template
    api_response = api_instance.api_v1_template_programmer_template_version_template_id_get(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateProgrammmerApi->api_v1_template_programmer_template_version_template_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| templateId | 

### Return type

[**CollectionTemplateInfo**](CollectionTemplateInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

