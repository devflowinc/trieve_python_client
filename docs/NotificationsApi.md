# trieve_python_client.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications**](NotificationsApi.md#get_notifications) | **GET** /api/notifications/{page} | get_notifications
[**mark_all_notifications_as_read**](NotificationsApi.md#mark_all_notifications_as_read) | **PUT** /api/notifications_readall | mark_all_read
[**mark_notification_as_read**](NotificationsApi.md#mark_notification_as_read) | **PUT** /api/notifications | mark_read


# **get_notifications**
> NotificationReturn get_notifications(page)

get_notifications

get_notifications  Get notifications for the auth'ed user. Currently, this is only for notifications belonging to the auth'ed user. Soon, we plan to associate notifications to datasets instead of users. Each page contains 10 notifications.

### Example


```python
import trieve_python_client
from trieve_python_client.models.notification_return import NotificationReturn
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.NotificationsApi(api_client)
    page = 56 # int | Page number of notifications to get

    try:
        # get_notifications
        api_response = api_instance.get_notifications(page)
        print("The response of NotificationsApi->get_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of notifications to get | 

### Return type

[**NotificationReturn**](NotificationReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notifications for the user |  -  |
**400** | Service error relating to getting notifications for the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_all_notifications_as_read**
> mark_all_notifications_as_read()

mark_all_read

mark_all_read  Mark all notifications as read. Currently, this is only for notifications belonging to the auth'ed user. Soon, we plan to associate notifications to datasets instead of users.

### Example


```python
import trieve_python_client
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.NotificationsApi(api_client)

    try:
        # mark_all_read
        api_instance.mark_all_notifications_as_read()
    except Exception as e:
        print("Exception when calling NotificationsApi->mark_all_notifications_as_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Confirmation that the all notification were marked read for the auth&#39;ed user |  -  |
**400** | Service error relating to finding the notifications for the auth&#39;ed user and marking them read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_notification_as_read**
> mark_notification_as_read(notification_id)

mark_read

mark_read  Mark a notification specified by id as read. Currently, this is only for notifications belonging to the auth'ed user. Soon, we plan to associate notifications to datasets instead of users.

### Example


```python
import trieve_python_client
from trieve_python_client.models.notification_id import NotificationId
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.NotificationsApi(api_client)
    notification_id = trieve_python_client.NotificationId() # NotificationId | JSON request payload with id of notification to mark read

    try:
        # mark_read
        api_instance.mark_notification_as_read(notification_id)
    except Exception as e:
        print("Exception when calling NotificationsApi->mark_notification_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | [**NotificationId**](NotificationId.md)| JSON request payload with id of notification to mark read | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Confirmation that the notification is marked read |  -  |
**400** | Service error relating to finding the notification and marking it read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

