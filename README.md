# trieve-python-client
Trieve REST API OpenAPI Documentation

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import trieve_python_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import trieve_python_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = trieve_python_client.AuthApi(api_client)

    try:
        # openid_callback
        api_response = api_instance.callback()
        print("The response of AuthApi->callback:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->callback: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**callback**](docs/AuthApi.md#callback) | **GET** /api/auth/callback | openid_callback
*AuthApi* | [**get_me**](docs/AuthApi.md#get_me) | **GET** /api/auth/me | get_me
*AuthApi* | [**login**](docs/AuthApi.md#login) | **GET** /api/auth | login
*AuthApi* | [**logout**](docs/AuthApi.md#logout) | **DELETE** /api/auth | logout
*ChunkApi* | [**create_chunk**](docs/ChunkApi.md#create_chunk) | **POST** /api/chunk | create_chunk
*ChunkApi* | [**create_suggested_queries_handler**](docs/ChunkApi.md#create_suggested_queries_handler) | **POST** /api/chunk/gen_suggestions | get_suggested_queries
*ChunkApi* | [**delete_chunk**](docs/ChunkApi.md#delete_chunk) | **DELETE** /api/chunk/{chunk_id} | delete_chunk
*ChunkApi* | [**delete_chunk_by_tracking_id**](docs/ChunkApi.md#delete_chunk_by_tracking_id) | **DELETE** /api/chunk/tracking_id/{tracking_id} | delete_chunk_by_tracking_id
*ChunkApi* | [**generate_off_chunks**](docs/ChunkApi.md#generate_off_chunks) | **POST** /api/chunk/generate | generate_off_chunks
*ChunkApi* | [**get_chunk_by_id**](docs/ChunkApi.md#get_chunk_by_id) | **GET** /api/chunk/{chunk_id} | get_chunk
*ChunkApi* | [**get_chunk_by_tracking_id**](docs/ChunkApi.md#get_chunk_by_tracking_id) | **GET** /api/chunk/tracking_id/{tracking_id} | get_chunk_by_tracking_id
*ChunkApi* | [**get_recommended_chunks**](docs/ChunkApi.md#get_recommended_chunks) | **POST** /api/chunk/recommend | get_recommended_chunks
*ChunkApi* | [**search_chunk**](docs/ChunkApi.md#search_chunk) | **POST** /api/chunk/search | search
*ChunkApi* | [**update_chunk**](docs/ChunkApi.md#update_chunk) | **PUT** /api/chunk/update | update_chunk
*ChunkApi* | [**update_chunk_by_tracking_id**](docs/ChunkApi.md#update_chunk_by_tracking_id) | **PUT** /api/chunk/tracking_id/update | update_chunk_by_tracking_id
*ChunkCollectionApi* | [**add_bookmark**](docs/ChunkCollectionApi.md#add_bookmark) | **POST** /api/chunk_collection/{collection_id} | add_bookmark
*ChunkCollectionApi* | [**create_chunk_collection**](docs/ChunkCollectionApi.md#create_chunk_collection) | **POST** /api/chunk_collection | create_chunk_collection
*ChunkCollectionApi* | [**delete_bookmark**](docs/ChunkCollectionApi.md#delete_bookmark) | **DELETE** /api/bookmark/{collection_id}/{bookmark_id} | delete_bookmark
*ChunkCollectionApi* | [**delete_chunk_collection**](docs/ChunkCollectionApi.md#delete_chunk_collection) | **DELETE** /api/chunk_collection/{collection_id} | delete_chunk_collection
*ChunkCollectionApi* | [**get_all_bookmarks**](docs/ChunkCollectionApi.md#get_all_bookmarks) | **GET** /api/chunk_collection/{collection_id}/{page} | get_all_bookmarks
*ChunkCollectionApi* | [**get_collections_chunk_is_in**](docs/ChunkCollectionApi.md#get_collections_chunk_is_in) | **POST** /api/chunk_collection/bookmark | 
*ChunkCollectionApi* | [**get_logged_in_user_chunk_collections**](docs/ChunkCollectionApi.md#get_logged_in_user_chunk_collections) | **GET** /api/chunk_collection/{page} | get_current_user_collections
*ChunkCollectionApi* | [**get_specific_user_chunk_collections**](docs/ChunkCollectionApi.md#get_specific_user_chunk_collections) | **GET** /api/user/collections/{user_id}/{page} | get_user_collections
*ChunkCollectionApi* | [**search_collections**](docs/ChunkCollectionApi.md#search_collections) | **POST** /api/chunk_collection/search | collection_search
*ChunkCollectionApi* | [**update_chunk_collection**](docs/ChunkCollectionApi.md#update_chunk_collection) | **PUT** /api/chunk_collection | update_chunk_collection
*DatasetApi* | [**create_dataset**](docs/DatasetApi.md#create_dataset) | **POST** /api/dataset | create_dataset
*DatasetApi* | [**delete_dataset**](docs/DatasetApi.md#delete_dataset) | **DELETE** /api/dataset | delete_dataset
*DatasetApi* | [**get_client_dataset_config**](docs/DatasetApi.md#get_client_dataset_config) | **GET** /api/dataset/envs | get_client_dataset_config
*DatasetApi* | [**get_dataset**](docs/DatasetApi.md#get_dataset) | **GET** /api/dataset/{dataset_id} | get_dataset
*DatasetApi* | [**get_datasets_from_organization**](docs/DatasetApi.md#get_datasets_from_organization) | **GET** /api/dataset/organization/{organization_id} | get_organization_datasets
*DatasetApi* | [**update_dataset**](docs/DatasetApi.md#update_dataset) | **PUT** /api/dataset | update_dataset
*FileApi* | [**delete_file_handler**](docs/FileApi.md#delete_file_handler) | **DELETE** /api/file/{file_id} | delete_file
*FileApi* | [**get_file_handler**](docs/FileApi.md#get_file_handler) | **GET** /api/file/{file_id} | get_file
*FileApi* | [**get_image_file**](docs/FileApi.md#get_image_file) | **GET** /api/image/{file_name} | get_image_file
*FileApi* | [**upload_file_handler**](docs/FileApi.md#upload_file_handler) | **POST** /api/file | upload_file
*HealthApi* | [**health_check**](docs/HealthApi.md#health_check) | **GET** /api/health | 
*InvitationApi* | [**post_invitation**](docs/InvitationApi.md#post_invitation) | **POST** /api/invitation | send_invitation
*MessageApi* | [**create_message_completion_handler**](docs/MessageApi.md#create_message_completion_handler) | **POST** /api/message | create_message
*MessageApi* | [**edit_message_handler**](docs/MessageApi.md#edit_message_handler) | **PUT** /api/message | edit_message
*MessageApi* | [**get_all_topic_messages**](docs/MessageApi.md#get_all_topic_messages) | **GET** /api/messages/{messages_topic_id} | get_all_messages
*MessageApi* | [**regenerate_message_handler**](docs/MessageApi.md#regenerate_message_handler) | **DELETE** /api/message | regenerate_message
*NotificationsApi* | [**get_notifications**](docs/NotificationsApi.md#get_notifications) | **GET** /api/notifications/{page} | get_notifications
*NotificationsApi* | [**mark_all_notifications_as_read**](docs/NotificationsApi.md#mark_all_notifications_as_read) | **PUT** /api/notifications_readall | mark_all_read
*NotificationsApi* | [**mark_notification_as_read**](docs/NotificationsApi.md#mark_notification_as_read) | **PUT** /api/notifications | mark_read
*OrganizationApi* | [**create_organization**](docs/OrganizationApi.md#create_organization) | **POST** /api/organization | create_organization
*OrganizationApi* | [**get_organization_by_id**](docs/OrganizationApi.md#get_organization_by_id) | **GET** /api/organization/{organization_id} | get_organization
*OrganizationApi* | [**get_organization_usage**](docs/OrganizationApi.md#get_organization_usage) | **GET** /api/organization/usage/{organization_id} | get_organization_usage
*OrganizationApi* | [**get_organization_users**](docs/OrganizationApi.md#get_organization_users) | **GET** /api/organization/users/{organization_id} | get_organization_users
*OrganizationApi* | [**update_organization**](docs/OrganizationApi.md#update_organization) | **PUT** /api/organization | update_organization
*StripeApi* | [**cancel_subscription**](docs/StripeApi.md#cancel_subscription) | **DELETE** /api/stripe/subscription/{subscription_id} | 
*StripeApi* | [**direct_to_payment_link**](docs/StripeApi.md#direct_to_payment_link) | **GET** /api/stripe/payment_link/{plan_id}/{organization_id} | 
*StripeApi* | [**get_all_plans**](docs/StripeApi.md#get_all_plans) | **GET** /api/stripe/plans | 
*StripeApi* | [**update_subscription_plan**](docs/StripeApi.md#update_subscription_plan) | **PATCH** /api/stripe/subscription_plan/{subscription_id}/{plan_id} | 
*TopicApi* | [**create_topic**](docs/TopicApi.md#create_topic) | **POST** /api/topic | create_topic
*TopicApi* | [**delete_topic**](docs/TopicApi.md#delete_topic) | **DELETE** /api/topic | delete_topic
*TopicApi* | [**get_all_topics**](docs/TopicApi.md#get_all_topics) | **GET** /api/topic | get_all_topics
*TopicApi* | [**update_topic**](docs/TopicApi.md#update_topic) | **PUT** /api/topic | update_topic
*UserApi* | [**delete_user_api_key**](docs/UserApi.md#delete_user_api_key) | **DELETE** /api/user/delete_api_key | delete_user_api_key
*UserApi* | [**get_user_files_handler**](docs/UserApi.md#get_user_files_handler) | **GET** /api/user/files/{user_id} | get_user_files
*UserApi* | [**get_user_with_chunks_by_id**](docs/UserApi.md#get_user_with_chunks_by_id) | **GET** /api/user/{user_id}/{page} | get_user_chunks
*UserApi* | [**set_user_api_key**](docs/UserApi.md#set_user_api_key) | **POST** /api/user/set_api_key | set_user_api_key
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /api/user | update_user


## Documentation For Models

 - [AddChunkToCollectionData](docs/AddChunkToCollectionData.md)
 - [ApiKeyDTO](docs/ApiKeyDTO.md)
 - [AuthData](docs/AuthData.md)
 - [BookmarkChunks](docs/BookmarkChunks.md)
 - [BookmarkCollectionResult](docs/BookmarkCollectionResult.md)
 - [BookmarkData](docs/BookmarkData.md)
 - [ChatMessageProxy](docs/ChatMessageProxy.md)
 - [ChunkCollection](docs/ChunkCollection.md)
 - [ChunkCollectionAndFile](docs/ChunkCollectionAndFile.md)
 - [ChunkMetadata](docs/ChunkMetadata.md)
 - [ChunkMetadataWithFileData](docs/ChunkMetadataWithFileData.md)
 - [ClientDatasetConfiguration](docs/ClientDatasetConfiguration.md)
 - [CollectionData](docs/CollectionData.md)
 - [CreateChunkCollectionData](docs/CreateChunkCollectionData.md)
 - [CreateChunkData](docs/CreateChunkData.md)
 - [CreateDatasetRequest](docs/CreateDatasetRequest.md)
 - [CreateMessageData](docs/CreateMessageData.md)
 - [CreateOrganizationData](docs/CreateOrganizationData.md)
 - [CreateTopicData](docs/CreateTopicData.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetAndOrgWithSubAndPlan](docs/DatasetAndOrgWithSubAndPlan.md)
 - [DatasetAndUsage](docs/DatasetAndUsage.md)
 - [DatasetDTO](docs/DatasetDTO.md)
 - [DatasetUsageCount](docs/DatasetUsageCount.md)
 - [DefaultError](docs/DefaultError.md)
 - [DeleteBookmarkPathData](docs/DeleteBookmarkPathData.md)
 - [DeleteCollectionData](docs/DeleteCollectionData.md)
 - [DeleteDatasetRequest](docs/DeleteDatasetRequest.md)
 - [DeleteTopicData](docs/DeleteTopicData.md)
 - [DeleteUserApiKeyRequest](docs/DeleteUserApiKeyRequest.md)
 - [EditMessageData](docs/EditMessageData.md)
 - [File](docs/File.md)
 - [FileDTO](docs/FileDTO.md)
 - [FileUploadCompletedNotificationWithName](docs/FileUploadCompletedNotificationWithName.md)
 - [GenerateChunksRequest](docs/GenerateChunksRequest.md)
 - [GenerateOffCollectionData](docs/GenerateOffCollectionData.md)
 - [GetAllBookmarksData](docs/GetAllBookmarksData.md)
 - [GetCollectionsForChunksData](docs/GetCollectionsForChunksData.md)
 - [GetDirectPaymentLinkData](docs/GetDirectPaymentLinkData.md)
 - [GetUserWithChunksData](docs/GetUserWithChunksData.md)
 - [InvitationData](docs/InvitationData.md)
 - [Message](docs/Message.md)
 - [Notification](docs/Notification.md)
 - [NotificationId](docs/NotificationId.md)
 - [NotificationReturn](docs/NotificationReturn.md)
 - [Organization](docs/Organization.md)
 - [OrganizationUsageCount](docs/OrganizationUsageCount.md)
 - [OrganizationWithSubAndPlan](docs/OrganizationWithSubAndPlan.md)
 - [RecommendChunksRequest](docs/RecommendChunksRequest.md)
 - [RegenerateMessageData](docs/RegenerateMessageData.md)
 - [ReturnCreatedChunk](docs/ReturnCreatedChunk.md)
 - [ScoreChunkDTO](docs/ScoreChunkDTO.md)
 - [SearchChunkData](docs/SearchChunkData.md)
 - [SearchChunkDataTimeRangeInner](docs/SearchChunkDataTimeRangeInner.md)
 - [SearchChunkDataWeightsInner](docs/SearchChunkDataWeightsInner.md)
 - [SearchChunkQueryResponseBody](docs/SearchChunkQueryResponseBody.md)
 - [SearchCollectionsData](docs/SearchCollectionsData.md)
 - [SearchCollectionsResult](docs/SearchCollectionsResult.md)
 - [SetUserApiKeyRequest](docs/SetUserApiKeyRequest.md)
 - [SetUserApiKeyResponse](docs/SetUserApiKeyResponse.md)
 - [SlimCollection](docs/SlimCollection.md)
 - [SlimUser](docs/SlimUser.md)
 - [StripePlan](docs/StripePlan.md)
 - [StripeSubscription](docs/StripeSubscription.md)
 - [SuggestedQueriesRequest](docs/SuggestedQueriesRequest.md)
 - [SuggestedQueriesResponse](docs/SuggestedQueriesResponse.md)
 - [Topic](docs/Topic.md)
 - [UpdateChunkByTrackingIdData](docs/UpdateChunkByTrackingIdData.md)
 - [UpdateChunkCollectionData](docs/UpdateChunkCollectionData.md)
 - [UpdateChunkData](docs/UpdateChunkData.md)
 - [UpdateDatasetRequest](docs/UpdateDatasetRequest.md)
 - [UpdateOrganizationData](docs/UpdateOrganizationData.md)
 - [UpdateSubscriptionData](docs/UpdateSubscriptionData.md)
 - [UpdateTopicData](docs/UpdateTopicData.md)
 - [UpdateUserData](docs/UpdateUserData.md)
 - [UploadFileData](docs/UploadFileData.md)
 - [UploadFileResult](docs/UploadFileResult.md)
 - [UserCollectionQuery](docs/UserCollectionQuery.md)
 - [UserDTO](docs/UserDTO.md)
 - [UserDTOWithChunks](docs/UserDTOWithChunks.md)
 - [UserOrganization](docs/UserOrganization.md)
 - [UserRole](docs/UserRole.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




