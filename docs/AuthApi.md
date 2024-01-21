# arguflow.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callback**](AuthApi.md#callback) | **GET** /api/auth/callback | openid_callback
[**get_me**](AuthApi.md#get_me) | **GET** /api/auth/me | get_me
[**login**](AuthApi.md#login) | **GET** /api/auth | login
[**logout**](AuthApi.md#logout) | **DELETE** /api/auth | logout


# **callback**
> SlimUser callback()

openid_callback

openid_callback  This is the callback route for the OAuth provider, it should not be called directly. Redirects to browser with set-cookie header.

### Example


```python
import arguflow
from arguflow.models.slim_user import SlimUser
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.AuthApi(api_client)

    try:
        # openid_callback
        api_response = api_instance.callback()
        print("The response of AuthApi->callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->callback: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SlimUser**](SlimUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response that returns with set-cookie header |  -  |
**400** | Email or password empty or incorrect |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me**
> SlimUser get_me()

get_me

get_me  Get the user corresponding to your current auth credentials.

### Example


```python
import arguflow
from arguflow.models.slim_user import SlimUser
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.AuthApi(api_client)

    try:
        # get_me
        api_response = api_instance.get_me()
        print("The response of AuthApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SlimUser**](SlimUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user corresponding to your current auth credentials |  -  |
**400** | Error message indicitating you are not currently signed in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> login(inv_code=inv_code, organization_id=organization_id, redirect_uri=redirect_uri)

login

login  This will redirect you to the OAuth provider for authentication with email/pass, SSO, Google, Github, etc.

### Example


```python
import arguflow
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.AuthApi(api_client)
    inv_code = 'inv_code_example' # str | Code sent via email as a result of successful call to send_invitation (optional)
    organization_id = 'organization_id_example' # str | ID of organization to authenticate into (optional)
    redirect_uri = 'redirect_uri_example' # str | URL to redirect to after successful login (optional)

    try:
        # login
        api_instance.login(inv_code=inv_code, organization_id=organization_id, redirect_uri=redirect_uri)
    except Exception as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inv_code** | **str**| Code sent via email as a result of successful call to send_invitation | [optional] 
 **organization_id** | **str**| ID of organization to authenticate into | [optional] 
 **redirect_uri** | **str**| URL to redirect to after successful login | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**303** | Response that redirects to OAuth provider through a Location header to be handled by browser. |  -  |
**400** | OAuth error likely with OIDC provider. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

logout

logout  Invalidate your current auth credential stored typicall stored in a cookie. This does not invalidate your API key.

### Example


```python
import arguflow
from arguflow.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = arguflow.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with arguflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arguflow.AuthApi(api_client)

    try:
        # logout
        api_instance.logout()
    except Exception as e:
        print("Exception when calling AuthApi->logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Confirmation that your current auth token has been invalidated. This does not invalidate your API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

