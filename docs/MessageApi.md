# arguflow.MessageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message_completion_handler**](MessageApi.md#create_message_completion_handler) | **POST** /api/message | create_message
[**edit_message_handler**](MessageApi.md#edit_message_handler) | **PUT** /api/message | edit_message
[**get_all_topic_messages**](MessageApi.md#get_all_topic_messages) | **GET** /api/messages/{messages_topic_id} | get_all_messages
[**regenerate_message_handler**](MessageApi.md#regenerate_message_handler) | **DELETE** /api/message | regenerate_message


# **create_message_completion_handler**
> create_message_completion_handler(create_message_data)

create_message

create_message  Create a message. Messages are attached to topics in order to coordinate memory of gen-AI chat sessions. We are considering refactoring this resource of the API soon. Currently, you can only send user messages. If the topic is a RAG topic then the response will include Chunks first on the stream. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more information.

### Example


```python
import arguflow
from arguflow.models.create_message_data import CreateMessageData
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
    api_instance = arguflow.MessageApi(api_client)
    create_message_data = arguflow.CreateMessageData() # CreateMessageData | JSON request payload to create a message completion

    try:
        # create_message
        api_instance.create_message_completion_handler(create_message_data)
    except Exception as e:
        print("Exception when calling MessageApi->create_message_completion_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_message_data** | [**CreateMessageData**](CreateMessageData.md)| JSON request payload to create a message completion | 

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
**200** | This will be a HTTP stream, check the chat or search UI for an example how to process this |  -  |
**400** | Service error relating to getting a chat completion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_message_handler**
> edit_message_handler(edit_message_data)

edit_message

edit_message  Edit a message which exists within the topic's chat history. This will delete the message and replace it with a new message. The new message will be generated by the AI based on the new content provided in the request body. The response will include Chunks first on the stream if the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more information.

### Example


```python
import arguflow
from arguflow.models.edit_message_data import EditMessageData
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
    api_instance = arguflow.MessageApi(api_client)
    edit_message_data = arguflow.EditMessageData() # EditMessageData | JSON request payload to edit a message and get a new stream

    try:
        # edit_message
        api_instance.edit_message_handler(edit_message_data)
    except Exception as e:
        print("Exception when calling MessageApi->edit_message_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_message_data** | [**EditMessageData**](EditMessageData.md)| JSON request payload to edit a message and get a new stream | 

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
**200** | This will be a HTTP stream, check the chat or search UI for an example how to process this |  -  |
**400** | Service error relating to getting a chat completion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_topic_messages**
> List[Message] get_all_topic_messages(messages_topic_id)

get_all_messages

get_all_messages  Get all messages for a given topic. If the topic is a RAG topic then the response will include Chunks first on each message. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more information.

### Example


```python
import arguflow
from arguflow.models.message import Message
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
    api_instance = arguflow.MessageApi(api_client)
    messages_topic_id = 'messages_topic_id_example' # str | The ID of the topic to get messages for.

    try:
        # get_all_messages
        api_response = api_instance.get_all_topic_messages(messages_topic_id)
        print("The response of MessageApi->get_all_topic_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageApi->get_all_topic_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **messages_topic_id** | **str**| The ID of the topic to get messages for. | 

### Return type

[**List[Message]**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All messages relating to the topic with the given ID |  -  |
**400** | Service error relating to getting the messages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_message_handler**
> regenerate_message_handler(regenerate_message_data)

regenerate_message

regenerate_message  Regenerate the assistant response to the last user message of a topic. This will delete the last message and replace it with a new message. The response will include Chunks first on the stream if the topic is using RAG. The structure will look like `[chunks]||mesage`. See docs.trieve.ai for more information.

### Example


```python
import arguflow
from arguflow.models.regenerate_message_data import RegenerateMessageData
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
    api_instance = arguflow.MessageApi(api_client)
    regenerate_message_data = arguflow.RegenerateMessageData() # RegenerateMessageData | JSON request payload to delete an agent message then regenerate it in a strem

    try:
        # regenerate_message
        api_instance.regenerate_message_handler(regenerate_message_data)
    except Exception as e:
        print("Exception when calling MessageApi->regenerate_message_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regenerate_message_data** | [**RegenerateMessageData**](RegenerateMessageData.md)| JSON request payload to delete an agent message then regenerate it in a strem | 

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
**200** | This will be a HTTP stream, check the chat or search UI for an example how to process this |  -  |
**400** | Service error relating to getting a chat completion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
