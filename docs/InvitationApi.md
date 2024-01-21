# arguflow.InvitationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_invitation**](InvitationApi.md#post_invitation) | **POST** /api/invitation | send_invitation


# **post_invitation**
> post_invitation(invitation_data)

send_invitation

send_invitation  Invitations act as a way to invite users to join an organization. After a user is invited, they will automatically be added to the organization with the role specified in the invitation once they set their.

### Example


```python
import arguflow
from arguflow.models.invitation_data import InvitationData
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
    api_instance = arguflow.InvitationApi(api_client)
    invitation_data = arguflow.InvitationData() # InvitationData | JSON request payload to send an invitation

    try:
        # send_invitation
        api_instance.post_invitation(invitation_data)
    except Exception as e:
        print("Exception when calling InvitationApi->post_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_data** | [**InvitationData**](InvitationData.md)| JSON request payload to send an invitation | 

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
**204** | Ok response. Indicates that invitation email was sent correctly. |  -  |
**400** | Invalid email or some other error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

