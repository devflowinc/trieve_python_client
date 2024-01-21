# arguflow.StripeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_subscription**](StripeApi.md#cancel_subscription) | **DELETE** /api/stripe/subscription/{subscription_id} | 
[**direct_to_payment_link**](StripeApi.md#direct_to_payment_link) | **GET** /api/stripe/payment_link/{plan_id}/{organization_id} | 
[**get_all_plans**](StripeApi.md#get_all_plans) | **GET** /api/stripe/plans | 
[**update_subscription_plan**](StripeApi.md#update_subscription_plan) | **PATCH** /api/stripe/subscription_plan/{subscription_id}/{plan_id} | 


# **cancel_subscription**
> cancel_subscription(subscription_id)



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
    api_instance = arguflow.StripeApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of the subscription you want to cancel

    try:
        api_instance.cancel_subscription(subscription_id)
    except Exception as e:
        print("Exception when calling StripeApi->cancel_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id of the subscription you want to cancel | 

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
**200** | Confirmation that the subscription was cancelled |  -  |
**400** | Service error relating to creating a URL for a stripe checkout page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **direct_to_payment_link**
> direct_to_payment_link(plan_id, organization_id)



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
    api_instance = arguflow.StripeApi(api_client)
    plan_id = 'plan_id_example' # str | id of the plan you want to subscribe to
    organization_id = 'organization_id_example' # str | id of the organization you want to subscribe to the plan

    try:
        api_instance.direct_to_payment_link(plan_id, organization_id)
    except Exception as e:
        print("Exception when calling StripeApi->direct_to_payment_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| id of the plan you want to subscribe to | 
 **organization_id** | **str**| id of the organization you want to subscribe to the plan | 

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
**303** | SeeOther response redirecting user to stripe checkout page |  -  |
**400** | Service error relating to creating a URL for a stripe checkout page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plans**
> List[StripePlan] get_all_plans()



### Example


```python
import arguflow
from arguflow.models.stripe_plan import StripePlan
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
    api_instance = arguflow.StripeApi(api_client)

    try:
        api_response = api_instance.get_all_plans()
        print("The response of StripeApi->get_all_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->get_all_plans: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[StripePlan]**](StripePlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all plans |  -  |
**400** | Service error relating to getting all plans |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_plan**
> update_subscription_plan(subscription_id, plan_id)



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
    api_instance = arguflow.StripeApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of the subscription you want to update
    plan_id = 'plan_id_example' # str | id of the plan you want to subscribe to

    try:
        api_instance.update_subscription_plan(subscription_id, plan_id)
    except Exception as e:
        print("Exception when calling StripeApi->update_subscription_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id of the subscription you want to update | 
 **plan_id** | **str**| id of the plan you want to subscribe to | 

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
**200** | Confirmation that the subscription was updated to the new plan |  -  |
**400** | Service error relating to updating the subscription to the new plan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

