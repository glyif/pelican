![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)

# Your Document Title

## Author: Bobby Yang (Description)

## Paragraph Header
You can type any text information in this paragraph block. All the
Markdown (md) decorators can be use inside here in order to markup
your text, they will be keep as-is while being parsed.

## File Breakdown

### 1 - get_access_token.py


##### Function: get_access_token

```python
def get_access_token(consumer_key, consumer_secret):
```

##### Function: main

```python
def main():
```

### 2 - setup.py


##### Function: read

```python
def read(filename):
```

##### Function: extract_metaitem

```python
def extract_metaitem(meta):
```

### 3 - examples/shorten_url.py


##### Class: ShortenURL

```python
class ShortenURL(object):
```

A class that defines the default URL Shortener.  TinyURL is provided as the default and as an example helper class to make URL Shortener calls if/when required.

##### Function: \_\_init\_\_

```python
class ShortenURL(object):
	def __init__(self,
                 userid=None,
                 password=None):
```

Instantiate a new ShortenURL object. TinyURL, which is used for this example, does not require a userid or password, so you can try this out without specifying either.

###### Params
- `@userid` userid for any required authorization call [optional]
- `@password` password for any required authorization call [optional]

##### Function: Shorten

```python
class ShortenURL(object):
	def Shorten(self,
                long_url):
```

Call TinyURL API and returned shortened URL result.

###### Params
- `@long_url` URL string to shorten

###### Returns
- `Note` long_url is required and no checks are made to ensure completeness

##### Function: _get_api

```python
def _get_api():
```

##### Function: PostStatusWithShortenedURL

```python
def PostStatusWithShortenedURL(status):
```

### 4 - examples/tweet.py


##### Function: PrintUsageAndExit

```python
def PrintUsageAndExit():
```

##### Function: GetConsumerKeyEnv

```python
def GetConsumerKeyEnv():
```

##### Function: GetConsumerSecretEnv

```python
def GetConsumerSecretEnv():
```

##### Function: GetAccessKeyEnv

```python
def GetAccessKeyEnv():
```

##### Function: GetAccessSecretEnv

```python
def GetAccessSecretEnv():
```

##### Class: TweetRc

```python
class TweetRc(object):
```

##### Function: \_\_init\_\_

```python
def __init__(self):
```

##### Function: GetConsumerKey

```python
def __init__(self):
	def GetConsumerKey(self):
```

##### Function: GetConsumerSecret

```python
def __init__(self):
	def GetConsumerSecret(self):
```

##### Function: GetAccessKey

```python
def __init__(self):
	def GetAccessKey(self):
```

##### Function: GetAccessSecret

```python
def __init__(self):
	def GetAccessSecret(self):
```

##### Function: _GetOption

```python
def __init__(self):
	def _GetOption(self, option):
```

##### Function: _GetConfig

```python
def __init__(self):
	def _GetConfig(self):
```

##### Function: main

```python
def main():
```

### 5 - examples/twitter-to-xhtml.py


##### Function: main

```python
def main(**kwargs):
```

### 6 - examples/streaming/track_users.py


##### Function: main

```python
def main():
```

### 7 - tests/test_api_30.py


##### Class: ErrNull

```python
class ErrNull(object):
```

Suppress output of tests while writing to stdout or stderr. This just takes in data and does nothing with it.

##### Function: write

```python
class ErrNull(object):
	def write(self, data):
```

##### Class: ApiTest

```python
class ApiTest(unittest.TestCase):
```

##### Function: setUp

```python
def setUp(self):
```

##### Function: tearDown

```python
def setUp(self):
	def tearDown(self):
```

##### Function: testApiSetUp

```python
def setUp(self):
	def testApiSetUp(self):
```

##### Function: testSetAndClearCredentials

```python
def setUp(self):
	def testSetAndClearCredentials(self):
```

##### Function: testApiRaisesAuthErrors

```python
def setUp(self):
	def testApiRaisesAuthErrors(self):
```

##### Function: testGetHelpConfiguration

```python
def setUp(self):
	def testGetHelpConfiguration(self):
```

##### Function: testGetShortUrlLength

```python
def setUp(self):
	def testGetShortUrlLength(self):
```

##### Function: testGetSearch

```python
def setUp(self):
	def testGetSearch(self):
```

##### Function: testGetSeachRawQuery

```python
def setUp(self):
	def testGetSeachRawQuery(self):
```

##### Function: testGetSearchGeocode

```python
def setUp(self):
	def testGetSearchGeocode(self):
```

##### Function: testGetUsersSearch

```python
def setUp(self):
	def testGetUsersSearch(self):
```

##### Function: testGetTrendsCurrent

```python
def setUp(self):
	def testGetTrendsCurrent(self):
```

##### Function: testGetHomeTimeline

```python
def setUp(self):
	def testGetHomeTimeline(self):
```

##### Function: testGetHomeTimelineWithExclusions

```python
def setUp(self):
	def testGetHomeTimelineWithExclusions(self):
```

##### Function: testGetUserTimelineByUserID

```python
def setUp(self):
	def testGetUserTimelineByUserID(self):
```

##### Function: testGetUserTimelineByScreenName

```python
def setUp(self):
	def testGetUserTimelineByScreenName(self):
```

##### Function: testGetRetweets

```python
def setUp(self):
	def testGetRetweets(self):
```

##### Function: testGetRetweetsCount

```python
def setUp(self):
	def testGetRetweetsCount(self):
```

##### Function: testGetRetweeters

```python
def setUp(self):
	def testGetRetweeters(self):
```

##### Function: testGetBlocks

```python
def setUp(self):
	def testGetBlocks(self):
```

##### Function: testGetBlocksPaged

```python
def setUp(self):
	def testGetBlocksPaged(self):
```

##### Function: testGetBlocksIDs

```python
def setUp(self):
	def testGetBlocksIDs(self):
```

##### Function: testGetBlocksIDsPaged

```python
def setUp(self):
	def testGetBlocksIDsPaged(self):
```

##### Function: testGetFriendIDs

```python
def setUp(self):
	def testGetFriendIDs(self):
```

##### Function: testGetFriendIDsPaged

```python
def setUp(self):
	def testGetFriendIDsPaged(self):
```

##### Function: testGetFriendsPaged

```python
def setUp(self):
	def testGetFriendsPaged(self):
```

##### Function: testGetFriendsPagedUID

```python
def setUp(self):
	def testGetFriendsPagedUID(self):
```

##### Function: testGetFriendsAdditionalParams

```python
def setUp(self):
	def testGetFriendsAdditionalParams(self):
```

##### Function: testGetFriends

```python
def setUp(self):
	def testGetFriends(self):
```

This is tedious, but the point is to add a responses endpoint for each call that GetFriends() is going to make against the API and have it return the appropriate json data.

##### Function: testGetFriendsWithLimit

```python
def setUp(self):
	def testGetFriendsWithLimit(self):
```

##### Function: testFriendsErrorChecking

```python
def setUp(self):
	def testFriendsErrorChecking(self):
```

##### Function: testGetFollowersIDs

```python
def setUp(self):
	def testGetFollowersIDs(self):
```

##### Function: testGetFollowers

```python
def setUp(self):
	def testGetFollowers(self):
```

##### Function: testGetFollowersPaged

```python
def setUp(self):
	def testGetFollowersPaged(self):
```

##### Function: testGetFollowerIDsPaged

```python
def setUp(self):
	def testGetFollowerIDsPaged(self):
```

##### Function: testUsersLookup

```python
def setUp(self):
	def testUsersLookup(self):
```

##### Function: testGetUser

```python
def setUp(self):
	def testGetUser(self):
```

##### Function: testGetDirectMessages

```python
def setUp(self):
	def testGetDirectMessages(self):
```

##### Function: testGetSentDirectMessages

```python
def setUp(self):
	def testGetSentDirectMessages(self):
```

##### Function: testGetFavorites

```python
def setUp(self):
	def testGetFavorites(self):
```

##### Function: testGetMentions

```python
def setUp(self):
	def testGetMentions(self):
```

##### Function: testGetListTimeline

```python
def setUp(self):
	def testGetListTimeline(self):
```

##### Function: testPostUpdate

```python
def setUp(self):
	def testPostUpdate(self):
```

##### Function: testPostUpdateExtraParams

```python
def setUp(self):
	def testPostUpdateExtraParams(self):
```

##### Function: testVerifyCredentials

```python
def setUp(self):
	def testVerifyCredentials(self):
```

##### Function: testVerifyCredentialsIncludeEmail

```python
def setUp(self):
	def testVerifyCredentialsIncludeEmail(self):
```

##### Function: testUpdateBanner

```python
def setUp(self):
	def testUpdateBanner(self):
```

##### Function: testUpdateBanner422Error

```python
def setUp(self):
	def testUpdateBanner422Error(self):
```

##### Function: testUpdateBanner400Error

```python
def setUp(self):
	def testUpdateBanner400Error(self):
```

##### Function: testGetMemberships

```python
def setUp(self):
	def testGetMemberships(self):
```

##### Function: testGetListsList

```python
def setUp(self):
	def testGetListsList(self):
```

##### Function: testGetLists

```python
def setUp(self):
	def testGetLists(self):
```

##### Function: testGetListMembers

```python
def setUp(self):
	def testGetListMembers(self):
```

##### Function: testGetListMembersPaged

```python
def setUp(self):
	def testGetListMembersPaged(self):
```

##### Function: testGetListTimeline

```python
def setUp(self):
	def testGetListTimeline(self):
```

##### Function: testCreateList

```python
def setUp(self):
	def testCreateList(self):
```

##### Function: testDestroyList

```python
def setUp(self):
	def testDestroyList(self):
```

##### Function: testCreateSubscription

```python
def setUp(self):
	def testCreateSubscription(self):
```

##### Function: testDestroySubscription

```python
def setUp(self):
	def testDestroySubscription(self):
```

##### Function: testShowSubscription

```python
def setUp(self):
	def testShowSubscription(self):
```

##### Function: testGetSubscriptions

```python
def setUp(self):
	def testGetSubscriptions(self):
```

##### Function: testGetSubscriptionsSN

```python
def setUp(self):
	def testGetSubscriptionsSN(self):
```

##### Function: testGetMemberships

```python
def setUp(self):
	def testGetMemberships(self):
```

##### Function: testCreateListsMember

```python
def setUp(self):
	def testCreateListsMember(self):
```

##### Function: testCreateListsMemberMultiple

```python
def setUp(self):
	def testCreateListsMemberMultiple(self):
```

##### Function: testDestroyListsMember

```python
def setUp(self):
	def testDestroyListsMember(self):
```

##### Function: testDestroyListsMemberMultiple

```python
def setUp(self):
	def testDestroyListsMemberMultiple(self):
```

##### Function: testPostUpdateWithMedia

```python
def setUp(self):
	def testPostUpdateWithMedia(self):
```

##### Function: testLookupFriendship

```python
def setUp(self):
	def testLookupFriendship(self):
```

##### Function: testLookupFriendshipMute

```python
def setUp(self):
	def testLookupFriendshipMute(self):
```

##### Function: testLookupFriendshipBlockMute

```python
def setUp(self):
	def testLookupFriendshipBlockMute(self):
```

##### Function: testPostMediaMetadata

```python
def setUp(self):
	def testPostMediaMetadata(self):
```

##### Function: testGetStatusWithExtAltText

```python
def setUp(self):
	def testGetStatusWithExtAltText(self):
```

##### Function: testGetStatus

```python
def setUp(self):
	def testGetStatus(self):
```

##### Function: testGetStatusExtraParams

```python
def setUp(self):
	def testGetStatusExtraParams(self):
```

##### Function: testGetStatusOembed

```python
def setUp(self):
	def testGetStatusOembed(self):
```

##### Function: testGetMutes

```python
def setUp(self):
	def testGetMutes(self):
```

##### Function: testGetMutesIDs

```python
def setUp(self):
	def testGetMutesIDs(self):
```

##### Function: testCreateBlock

```python
def setUp(self):
	def testCreateBlock(self):
```

##### Function: testDestroyBlock

```python
def setUp(self):
	def testDestroyBlock(self):
```

##### Function: testCreateMute

```python
def setUp(self):
	def testCreateMute(self):
```

##### Function: testDestroyMute

```python
def setUp(self):
	def testDestroyMute(self):
```

##### Function: testMuteBlockParamsAndErrors

```python
def setUp(self):
	def testMuteBlockParamsAndErrors(self):
```

##### Function: testPostUploadMediaChunkedInit

```python
def setUp(self):
	def testPostUploadMediaChunkedInit(self):
```

##### Function: testPostUploadMediaChunkedAppend

```python
def setUp(self):
	def testPostUploadMediaChunkedAppend(self):
```

##### Function: testPostUploadMediaChunkedAppendNonASCIIFilename

```python
def setUp(self):
	def testPostUploadMediaChunkedAppendNonASCIIFilename(self):
```

##### Function: testPostUploadMediaChunkedFinalize

```python
def setUp(self):
	def testPostUploadMediaChunkedFinalize(self):
```

##### Function: testGetUserSuggestionCategories

```python
def setUp(self):
	def testGetUserSuggestionCategories(self):
```

##### Function: testGetUserSuggestion

```python
def setUp(self):
	def testGetUserSuggestion(self):
```

##### Function: testGetUserTimeSinceMax

```python
def setUp(self):
	def testGetUserTimeSinceMax(self):
```

##### Function: testGetUserTimelineCount

```python
def setUp(self):
	def testGetUserTimelineCount(self):
```

##### Function: testDestroyStatus

```python
def setUp(self):
	def testDestroyStatus(self):
```

##### Function: testCreateFavorite

```python
def setUp(self):
	def testCreateFavorite(self):
```

##### Function: testDestroyFavorite

```python
def setUp(self):
	def testDestroyFavorite(self):
```

##### Function: testPostDirectMessage

```python
def setUp(self):
	def testPostDirectMessage(self):
```

##### Function: testDestroyDirectMessage

```python
def setUp(self):
	def testDestroyDirectMessage(self):
```

##### Function: testShowFriendship

```python
def setUp(self):
	def testShowFriendship(self):
```

##### Function: test_UpdateBackgroundImage_deprecation

```python
def setUp(self):
	def test_UpdateBackgroundImage_deprecation(self):
```

##### Function: test_UploadSmallVideoUsesChunkedData

```python
def setUp(self):
	def test_UploadSmallVideoUsesChunkedData(self, mocker):
```

### 8 - tests/test_error_handling.py


##### Class: ApiTest

```python
class ApiTest(unittest.TestCase):
```

##### Function: setUp

```python
def setUp(self):
```

##### Function: testGetShortUrlLength

```python
def setUp(self):
	def testGetShortUrlLength(self):
```

### 9 - tests/test_filecache.py


##### Class: FileCacheTest

```python
class FileCacheTest(unittest.TestCase):
```

##### Function: testInit

```python
def testInit(self):
```

Test the twitter._FileCache constructor

##### Function: testSet

```python
def testInit(self):
	def testSet(self):
```

Test the twitter._FileCache.Set method

##### Function: testRemove

```python
def testInit(self):
	def testRemove(self):
```

Test the twitter._FileCache.Remove method

##### Function: testGet

```python
def testInit(self):
	def testGet(self):
```

Test the twitter._FileCache.Get method

##### Function: testGetCachedTime

```python
def testInit(self):
	def testGetCachedTime(self):
```

Test the twitter._FileCache.GetCachedTime method

### 10 - tests/test_media.py


##### Class: MediaTest

```python
class MediaTest(unittest.TestCase):
```

##### Function: _GetSampleMedia

```python
class MediaTest(unittest.TestCase):
	def _GetSampleMedia(self):
```

##### Function: testInit

```python
class MediaTest(unittest.TestCase):
	def testInit(self):
```

Test the twitter.Media constructor

##### Function: testProperties

```python
class MediaTest(unittest.TestCase):
	def testProperties(self):
```

Test all of the twitter.Media properties

##### Function: testAsJsonString

```python
class MediaTest(unittest.TestCase):
	def testAsJsonString(self):
```

Test the twitter.User AsJsonString method

##### Function: testAsDict

```python
class MediaTest(unittest.TestCase):
	def testAsDict(self):
```

Test the twitter.Media AsDict method

##### Function: testEq

```python
class MediaTest(unittest.TestCase):
	def testEq(self):
```

Test the twitter.Media __eq__ method

##### Function: testHash

```python
class MediaTest(unittest.TestCase):
	def testHash(self):
```

Test the twitter.Media __hash__ method

##### Function: testNewFromJsonDict

```python
class MediaTest(unittest.TestCase):
	def testNewFromJsonDict(self):
```

Test the twitter.Media NewFromJsonDict method

##### Function: test_media_info

```python
class MediaTest(unittest.TestCase):
	def test_media_info(self):
```

### 11 - tests/test_models.py


##### Class: ModelsTest

```python
class ModelsTest(unittest.TestCase):
```

##### Function: test_category

```python
class ModelsTest(unittest.TestCase):
	def test_category(self):
```

Test twitter.Category object

##### Function: test_direct_message

```python
class ModelsTest(unittest.TestCase):
	def test_direct_message(self):
```

Test twitter.DirectMessage object

##### Function: test_direct_message_sender_is_user_model

```python
class ModelsTest(unittest.TestCase):
	def test_direct_message_sender_is_user_model(self):
```

Test that each Direct Message object contains a fully hydrated twitter.models.User object for both ``dm.sender`` & ``dm.recipient``.

##### Function: test_direct_message_recipient_is_user_model

```python
class ModelsTest(unittest.TestCase):
	def test_direct_message_recipient_is_user_model(self):
```

Test that each Direct Message object contains a fully hydrated twitter.models.User object for both ``dm.sender`` & ``dm.recipient``.

##### Function: test_hashtag

```python
class ModelsTest(unittest.TestCase):
	def test_hashtag(self):
```

Test twitter.Hashtag object

##### Function: test_list

```python
class ModelsTest(unittest.TestCase):
	def test_list(self):
```

Test twitter.List object

##### Function: test_media

```python
class ModelsTest(unittest.TestCase):
	def test_media(self):
```

Test twitter.Media object

##### Function: test_status

```python
class ModelsTest(unittest.TestCase):
	def test_status(self):
```

Test twitter.Status object

##### Function: test_status_quoted_tweet

```python
class ModelsTest(unittest.TestCase):
	def test_status_quoted_tweet(self):
```

Test that quoted tweets are properly handled.

##### Function: test_status_quoted_tweet_with_media

```python
class ModelsTest(unittest.TestCase):
	def test_status_quoted_tweet_with_media(self):
```

Test that quoted tweet properly handles attached media.

##### Function: test_status_no_user

```python
class ModelsTest(unittest.TestCase):
	def test_status_no_user(self):
```

Test twitter.Status object which does not contain a 'user' entity.

##### Function: test_trend

```python
class ModelsTest(unittest.TestCase):
	def test_trend(self):
```

Test twitter.Trend object

##### Function: test_url

```python
class ModelsTest(unittest.TestCase):
	def test_url(self):
```

##### Function: test_user

```python
class ModelsTest(unittest.TestCase):
	def test_user(self):
```

Test the twitter.User NewFromJsonDict method

##### Function: test_user_status

```python
class ModelsTest(unittest.TestCase):
	def test_user_status(self):
```

Test twitter.UserStatus object

### 12 - tests/test_parse_tweet.py


##### Class: ParseTest

```python
class ParseTest(unittest.TestCase):
```

Test the ParseTweet class

##### Function: testParseTweets

```python
class ParseTest(unittest.TestCase):
	def testParseTweets(self):
```

##### Function: testEmoticon

```python
class ParseTest(unittest.TestCase):
	def testEmoticon(self):
```

### 13 - tests/test_rate_limit.py


##### Class: ErrNull

```python
class ErrNull(object):
```

Suppress output of tests while writing to stdout or stderr. This just takes in data and does nothing with it.

##### Function: write

```python
class ErrNull(object):
	def write(self, data):
```

##### Class: RateLimitTests

```python
class RateLimitTests(unittest.TestCase):
```

Tests for RateLimit object

##### Function: setUp

```python
class RateLimitTests(unittest.TestCase):
	def setUp(self):
```

##### Function: tearDown

```python
class RateLimitTests(unittest.TestCase):
	def tearDown(self):
```

##### Function: testInitializeRateLimit

```python
class RateLimitTests(unittest.TestCase):
	def testInitializeRateLimit(self):
```

##### Function: testCheckRateLimit

```python
class RateLimitTests(unittest.TestCase):
	def testCheckRateLimit(self):
```

##### Class: RateLimitMethodsTests

```python
class RateLimitMethodsTests(unittest.TestCase):
```

Tests for RateLimit object

##### Function: setUp

```python
class RateLimitMethodsTests(unittest.TestCase):
	def setUp(self):
```

##### Function: tearDown

```python
class RateLimitMethodsTests(unittest.TestCase):
	def tearDown(self):
```

##### Function: testGetRateLimit

```python
class RateLimitMethodsTests(unittest.TestCase):
	def testGetRateLimit(self):
```

##### Function: testNonStandardEndpointRateLimit

```python
class RateLimitMethodsTests(unittest.TestCase):
	def testNonStandardEndpointRateLimit(self):
```

##### Function: testSetRateLimit

```python
class RateLimitMethodsTests(unittest.TestCase):
	def testSetRateLimit(self):
```

##### Function: testFamilyNotFound

```python
class RateLimitMethodsTests(unittest.TestCase):
	def testFamilyNotFound(self):
```

##### Function: testSetUnknownRateLimit

```python
class RateLimitMethodsTests(unittest.TestCase):
	def testSetUnknownRateLimit(self):
```

##### Function: testSetUnknownRateLimit

```python
class RateLimitMethodsTests(unittest.TestCase):
	def testSetUnknownRateLimit(self):
```

##### Function: testLimitsViaHeadersNoSleep

```python
class RateLimitMethodsTests(unittest.TestCase):
	def testLimitsViaHeadersNoSleep(self):
```

##### Function: testLimitsViaHeadersWithSleep

```python
class RateLimitMethodsTests(unittest.TestCase):
	def testLimitsViaHeadersWithSleep(self):
```

### 14 - tests/test_status.py


##### Class: StatusTest

```python
class StatusTest(unittest.TestCase):
```

##### Function: _GetSampleUser

```python
class StatusTest(unittest.TestCase):
	def _GetSampleUser(self):
```

##### Function: _GetSampleStatus

```python
class StatusTest(unittest.TestCase):
	def _GetSampleStatus(self):
```

##### Function: testInit

```python
class StatusTest(unittest.TestCase):
	def testInit(self):
```

Test the twitter.Status constructor

##### Function: testProperties

```python
class StatusTest(unittest.TestCase):
	def testProperties(self):
```

Test all of the twitter.Status properties

##### Function: testAsJsonString

```python
class StatusTest(unittest.TestCase):
	def testAsJsonString(self):
```

Test the twitter.Status AsJsonString method

##### Function: testAsDict

```python
class StatusTest(unittest.TestCase):
	def testAsDict(self):
```

Test the twitter.Status AsDict method

##### Function: testEq

```python
class StatusTest(unittest.TestCase):
	def testEq(self):
```

Test the twitter.Status __eq__ method

##### Function: testHash

```python
class StatusTest(unittest.TestCase):
	def testHash(self):
```

Test the twitter.Status __hash__ method

##### Function: testNewFromJsonDict

```python
class StatusTest(unittest.TestCase):
	def testNewFromJsonDict(self):
```

Test the twitter.Status NewFromJsonDict method

### 15 - tests/test_trend.py


##### Class: TrendTest

```python
class TrendTest(unittest.TestCase):
```

##### Function: _GetSampleTrend

```python
class TrendTest(unittest.TestCase):
	def _GetSampleTrend(self):
```

##### Function: testInit

```python
class TrendTest(unittest.TestCase):
	def testInit(self):
```

Test the twitter.Trend constructor

##### Function: testProperties

```python
class TrendTest(unittest.TestCase):
	def testProperties(self):
```

Test all of the twitter.Trend properties

##### Function: testNewFromJsonDict

```python
class TrendTest(unittest.TestCase):
	def testNewFromJsonDict(self):
```

Test the twitter.Trend NewFromJsonDict method

##### Function: testEq

```python
class TrendTest(unittest.TestCase):
	def testEq(self):
```

Test the twitter.Trend __eq__ method

##### Function: testHash

```python
class TrendTest(unittest.TestCase):
	def testHash(self):
```

Test the twitter.Trent __hash__ method

### 16 - tests/test_tweet_changes.py


##### Class: ModelsChangesTest

```python
class ModelsChangesTest(unittest.TestCase):
```

Test how changes to tweets affect model creation

##### Function: setUp

```python
class ModelsChangesTest(unittest.TestCase):
	def setUp(self):
```

##### Function: test_extended_in_compat_mode

```python
class ModelsChangesTest(unittest.TestCase):
	def test_extended_in_compat_mode(self):
```

API is in compatibility mode, but we call GetStatus on a tweet that was written in extended mode.  The tweet in question is exactly 140 characters and attaches a photo.

##### Function: test_extended_in_extended_mode

```python
class ModelsChangesTest(unittest.TestCase):
	def test_extended_in_extended_mode(self):
```

API is in extended mode, and we call GetStatus on a tweet that was written in extended mode.  The tweet in question is exactly 140 characters and attaches a photo.

### 17 - tests/test_tweet_length.py


##### Class: TestTweetLength

```python
class TestTweetLength(unittest.TestCase):
```

##### Function: setUp

```python
def setUp(self):
```

##### Function: test_find_urls

```python
def setUp(self):
	def test_find_urls(self):
```

##### Function: test_split_tweets

```python
def setUp(self):
	def test_split_tweets(self):
```

### 18 - tests/test_twitter_utils.py


##### Class: ApiTest

```python
class ApiTest(unittest.TestCase):
```

##### Function: setUp

```python
def setUp(self):
```

##### Function: test_parse_media_file_http

```python
def setUp(self):
	def test_parse_media_file_http(self):
```

##### Function: test_parse_media_file_local_file

```python
def setUp(self):
	def test_parse_media_file_local_file(self):
```

##### Function: test_parse_media_file_fileobj

```python
def setUp(self):
	def test_parse_media_file_fileobj(self):
```

##### Function: test_utils_error_checking

```python
def setUp(self):
	def test_utils_error_checking(self):
```

##### Function: test_calc_expected_status_length

```python
def setUp(self):
	def test_calc_expected_status_length(self):
```

##### Function: test_calc_expected_status_length_with_url

```python
def setUp(self):
	def test_calc_expected_status_length_with_url(self):
```

##### Function: test_calc_expected_status_length_with_url_and_extra_spaces

```python
def setUp(self):
	def test_calc_expected_status_length_with_url_and_extra_spaces(self):
```

### 19 - tests/test_unicode.py


##### Class: ErrNull

```python
class ErrNull(object):
```

Suppress output of tests while writing to stdout or stderr. This just takes in data and does nothing with it.

##### Function: write

```python
class ErrNull(object):
	def write(self, data):
```

##### Class: ApiTest

```python
class ApiTest(unittest.TestCase):
```

##### Function: setUp

```python
def setUp(self):
```

##### Function: tearDown

```python
def setUp(self):
	def tearDown(self):
```

##### Function: test_trend_repr1

```python
def setUp(self):
	def test_trend_repr1(self):
```

##### Function: test_trend_repr2

```python
def setUp(self):
	def test_trend_repr2(self):
```

##### Function: test_trend_repr3

```python
def setUp(self):
	def test_trend_repr3(self):
```

##### Function: test_unicode_get_search

```python
def setUp(self):
	def test_unicode_get_search(self):
```

##### Function: test_constructed_status

```python
def setUp(self):
	def test_constructed_status(self):
```

### 20 - tests/test_url_regex.py


##### Class: TestUrlRegex

```python
class TestUrlRegex(unittest.TestCase):
```

##### Function: test_yes_urls

```python
def test_yes_urls(self):
```

##### Function: test_no_urls

```python
def test_yes_urls(self):
	def test_no_urls(self):
```

##### Function: test_regex_finds_unicode

```python
def test_yes_urls(self):
	def test_regex_finds_unicode(self):
```

### 21 - tests/test_user.py


##### Class: UserTest

```python
class UserTest(unittest.TestCase):
```

##### Function: _GetSampleStatus

```python
class UserTest(unittest.TestCase):
	def _GetSampleStatus(self):
```

##### Function: _GetSampleUser

```python
class UserTest(unittest.TestCase):
	def _GetSampleUser(self):
```

##### Function: testInit

```python
class UserTest(unittest.TestCase):
	def testInit(self):
```

Test the twitter.User constructor

##### Function: testProperties

```python
class UserTest(unittest.TestCase):
	def testProperties(self):
```

Test all of the twitter.User properties

##### Function: testAsJsonString

```python
class UserTest(unittest.TestCase):
	def testAsJsonString(self):
```

Test the twitter.User AsJsonString method

##### Function: testAsDict

```python
class UserTest(unittest.TestCase):
	def testAsDict(self):
```

Test the twitter.User AsDict method

##### Function: testEq

```python
class UserTest(unittest.TestCase):
	def testEq(self):
```

Test the twitter.User __eq__ method

##### Function: testHash

```python
class UserTest(unittest.TestCase):
	def testHash(self):
```

Test the twitter.User __hash__ method

##### Function: testNewFromJsonDict

```python
class UserTest(unittest.TestCase):
	def testNewFromJsonDict(self):
```

Test the twitter.User NewFromJsonDict method

### 22 - twitter/_file_cache.py


##### Class: _FileCacheError

```python
class _FileCacheError(Exception):
```

Base exception class for FileCache related errors

##### Class: _FileCache

```python
class _FileCache(object):
```

##### Function: \_\_init\_\_

```python
class _FileCache(object):
	def __init__(self, root_directory=None):
```

##### Function: Get

```python
class _FileCache(object):
	def Get(self, key):
```

##### Function: Set

```python
class _FileCache(object):
	def Set(self, key, data):
```

##### Function: Remove

```python
class _FileCache(object):
	def Remove(self, key):
```

##### Function: GetCachedTime

```python
class _FileCache(object):
	def GetCachedTime(self, key):
```

##### Function: _GetUsername

```python
class _FileCache(object):
	def _GetUsername(self):
```

Attempt to find the username in a cross-platform fashion.

##### Function: _GetTmpCachePath

```python
class _FileCache(object):
	def _GetTmpCachePath(self):
```

##### Function: _InitializeRootDirectory

```python
class _FileCache(object):
	def _InitializeRootDirectory(self, root_directory):
```

##### Function: _GetPath

```python
class _FileCache(object):
	def _GetPath(self, key):
```

##### Function: _GetPrefix

```python
class _FileCache(object):
	def _GetPrefix(self, hashed_key):
```

### 23 - twitter/api.py


##### Class: Api

```python
class Api(object):
```

A python interface into the Twitter API  By default, the Api caches results for 1 minute.  Example usage:  To create an instance of the twitter.Api class, with no authentication:  >>> import twitter >>> api = twitter.Api()  To fetch a single user's public status messages, where "user" is either a Twitter "short name" or their user id.  >>> statuses = api.GetUserTimeline(user) >>> print([s.text for s in statuses])  To use authentication, instantiate the twitter.Api class with a consumer key and secret; and the oAuth key and secret:  >>> api = twitter.Api(consumer_key='twitter consumer key', consumer_secret='twitter consumer secret', access_token_key='the_key_given', access_token_secret='the_key_secret')  To fetch your friends (after being authenticated):  >>> users = api.GetFriends() >>> print([u.name for u in users])  To post a twitter status message (after being authenticated):  >>> status = api.PostUpdate('I love python-twitter!') >>> print(status.text) I love python-twitter!  There are many other methods, including:  >>> api.PostUpdates(status) >>> api.PostDirectMessage(user, text) >>> api.GetUser(user) >>> api.GetReplies() >>> api.GetUserTimeline(user) >>> api.GetHomeTimeline() >>> api.GetStatus(status_id) >>> api.DestroyStatus(status_id) >>> api.GetFriends(user) >>> api.GetFollowers() >>> api.GetFeatured() >>> api.GetDirectMessages() >>> api.GetSentDirectMessages() >>> api.PostDirectMessage(user, text) >>> api.DestroyDirectMessage(message_id) >>> api.DestroyFriendship(user) >>> api.CreateFriendship(user) >>> api.LookupFriendship(user) >>> api.VerifyCredentials()

##### Function: \_\_init\_\_

```python
class Api(object):
	def __init__(self,
                 consumer_key=None,
                 consumer_secret=None,
                 access_token_key=None,
                 access_token_secret=None,
                 application_only_auth=False,
                 input_encoding=None,
                 request_headers=None,
                 cache=DEFAULT_CACHE,
                 base_url=None,
                 stream_url=None,
                 upload_url=None,
                 chunk_size=1024 * 1024,
                 use_gzip_compression=False,
                 debugHTTP=False,
                 timeout=None,
                 sleep_on_rate_limit=False,
                 tweet_mode='compat',
                 proxies=None):
```

Instantiate a new twitter.Api object.

###### Params
- `@consumer_key (str)` Your Twitter user's consumer_key.
- `@consumer_secret (str)` Your Twitter user's consumer_secret.
- `@access_token_key (str)` The oAuth access token key value you retrieved from running get_access_token.py.
- `@access_token_secret (str)` The oAuth access token's secret, also retrieved from the get_access_token.py run.
- `@application_only_auth` Use Application-Only Auth instead of User Auth. Defaults to False [Optional]
- `@input_encoding (str, optional)` The encoding used to encode input strings.
- `@request_header (dict, optional)` A dictionary of additional HTTP request headers.
- `@cache (object, optional)` The cache instance to use. Defaults to DEFAULT_CACHE. Use None to disable caching.
- `@base_url (str, optional)` The base URL to use to contact the Twitter API. Defaults to https://api.twitter.com.
- `@stream_url (str, optional)` The base URL to use for streaming endpoints. Defaults to 'https://stream.twitter.com/1.1'.
- `@upload_url (str, optional)` The base URL to use for uploads. Defaults to 'https://upload.twitter.com/1.1'.
- `@chunk_size (int, optional)` Chunk size to use for chunked (multi-part) uploads of images/videos/gifs. Defaults to 1MB. Anything under 16KB and you run the risk of erroring out on 15MB files.
- `@use_gzip_compression (bool, optional)` Set to True to tell enable gzip compression for any call made to Twitter.  Defaults to False.
- `@debugHTTP (bool, optional)` Set to True to enable debug output from urllib2 when performing any HTTP requests.  Defaults to False.
- `@timeout (int, optional)` Set timeout (in seconds) of the http/https requests. If None the requests lib default will be used.  Defaults to None.
- `@sleep_on_rate_limit (bool, optional)` Whether to sleep an appropriate amount of time if a rate limit is hit for an endpoint.
- `@tweet_mode (str, optional)` Whether to use the new (as of Sept. 2016) extended tweet mode. See docs for details. Choices are ['compatibility', 'extended'].
- `@proxies (dict, optional)` A dictionary of proxies for the request to pass through, if not specified allows requests lib to use environmental variables for proxy if any.

##### Function: GetAppOnlyAuthToken

```python
class Api(object):
	def GetAppOnlyAuthToken(self, consumer_key, consumer_secret):
```

Generate a Bearer Token from consumer_key and consumer_secret

##### Function: SetCredentials

```python
class Api(object):
	def SetCredentials(self,
                       consumer_key,
                       consumer_secret,
                       access_token_key=None,
                       access_token_secret=None,
                       application_only_auth=False):
```

Set the consumer_key and consumer_secret for this instance

###### Params
- `@consumer_key` The consumer_key of the twitter account.
- `@consumer_secret` The consumer_secret for the twitter account.
- `@access_token_key` The oAuth access token key value you retrieved from running get_access_token.py.
- `@access_token_secret` The oAuth access token's secret, also retrieved from the get_access_token.py run.
- `@application_only_auth` Whether to generate a bearer token and use Application-Only Auth

##### Function: GetHelpConfiguration

```python
class Api(object):
	def GetHelpConfiguration(self):
```

Get basic help configuration details from Twitter.

###### Params
- None

###### Returns
- `dict` Sets self._config and returns dict of help config values.

##### Function: GetShortUrlLength

```python
class Api(object):
	def GetShortUrlLength(self, https=False):
```

Returns number of characters reserved per URL included in a tweet.

###### Params
- `@https (bool, optional)` If True, return number of characters reserved for https urls or, if False, return number of character reserved for http urls.

###### Returns
- `(int)` Number of characters reserved per URL.

##### Function: ClearCredentials

```python
class Api(object):
	def ClearCredentials(self):
```

Clear any credentials for this instance

##### Function: GetSearch

```python
class Api(object):
	def GetSearch(self,
                  term=None,
                  raw_query=None,
                  geocode=None,
                  since_id=None,
                  max_id=None,
                  until=None,
                  since=None,
                  count=15,
                  lang=None,
                  locale=None,
                  result_type="mixed",
                  include_entities=None):
```

Return twitter search results for a given term. You must specify one of term, geocode, or raw_query.

###### Params
- `@term (str, optional)` Term to search by. Optional if you include geocode.
- `@raw_query (str, optional)` A raw query as a string. This should be everything after the "?" in the URL (i.e., the query parameters). You are responsible for all type checking and ensuring that the query string is properly formatted, as it will only be URL-encoded before be passed directly to Twitter with no other checks performed. For advanced usage only. *This will override any other parameters passed*
- `@since_id (int, optional)` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available.
- `@max_id (int, optional)` Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
- `@until (str, optional)` Returns tweets generated before the given date. Date should be formatted as YYYY-MM-DD.
- `@since (str, optional)` Returns tweets generated since the given date. Date should be formatted as YYYY-MM-DD.
- `@geocode (str or list or tuple, optional)` Geolocation within which to search for tweets. Can be either a string in the form of "latitude,longitude,radius" where latitude and longitude are floats and radius is a string such as "1mi" or
- `@"1km" ("mi" or "km" are the only units allowed). For example` >>> api.GetSearch(geocode="37.781157,-122.398720,1mi"). Otherwise, you can pass a list of either floats or strings for
- `@lat/long and a string for radius` >>> api.GetSearch(geocode=[37.781157, -122.398720, "1mi"])
- `@>>> # or` >>> api.GetSearch(geocode=(37.781157, -122.398720, "1mi"))
- `@>>> # or` >>> api.GetSearch(geocode=("37.781157", "-122.398720", "1mi"))
- `@count (int, optional)` Number of results to return.  Default is 15 and maxmimum that Twitter returns is 100 irrespective of what you type in.
- `@lang (str, optional)` Language for results as ISO 639-1 code.  Default is None (all languages).
- `@locale (str, optional)` Language of the search query. Currently only 'ja' is effective. This is intended for language-specific consumers and the default should work in the majority of cases.
- `@result_type (str, optional)` Type of result which should be returned. Default is "mixed". Valid options are "mixed, "recent", and "popular".
- `@include_entities (bool, optional)` If True, each tweet will include a node called "entities". This node offers a variety of metadata about the tweet in a
- `@discrete structure, including` user_mentions, urls, and hashtags.

###### Returns
- `list` A sequence of twitter.Status instances, one for each message containing the term, within the bounds of the geocoded area, or given by the raw_query.

##### Function: GetUsersSearch

```python
class Api(object):
	def GetUsersSearch(self,
                       term=None,
                       page=1,
                       count=20,
                       include_entities=None):
```

Return twitter user search results for a given term.

###### Params
- `@term` Term to search by.
- `@page` Page of results to return. Default is 1 [Optional]
- `@count` Number of results to return.  Default is 20 [Optional]
- `@include_entities` If True, each tweet will include a node called "entities,". This node offers a variety of metadata about the tweet in a
- `@discrete structure, including` user_mentions, urls, and hashtags. [Optional]

###### Returns
- A sequence of twitter.User instances, one for each message containing the term

##### Function: GetTrendsCurrent

```python
class Api(object):
	def GetTrendsCurrent(self, exclude=None):
```

Get the current top trending topics (global)

###### Params
- `@exclude` Appends the exclude parameter as a request parameter. Currently only exclude=hashtags is supported. [Optional]

###### Returns
- A list with 10 entries. Each entry contains a trend.

##### Function: GetTrendsWoeid

```python
class Api(object):
	def GetTrendsWoeid(self, woeid, exclude=None):
```

Return the top 10 trending topics for a specific WOEID, if trending information is available for it.

###### Params
- `@woeid` the Yahoo! Where On Earth ID for a location.
- `@exclude` Appends the exclude parameter as a request parameter. Currently only exclude=hashtags is supported. [Optional]

###### Returns
- A list with 10 entries. Each entry contains a trend.

##### Function: GetUserSuggestionCategories

```python
class Api(object):
	def GetUserSuggestionCategories(self):
```

Return the list of suggested user categories, this can be used in GetUserSuggestion function

###### Returns
- A list of categories

##### Function: GetUserSuggestion

```python
class Api(object):
	def GetUserSuggestion(self, category):
```

Returns a list of users in a category

###### Params
- `@category` The Category object to limit the search by

###### Returns
- A list of users in that category

##### Function: GetHomeTimeline

```python
class Api(object):
	def GetHomeTimeline(self,
                        count=None,
                        since_id=None,
                        max_id=None,
                        trim_user=False,
                        exclude_replies=False,
                        contributor_details=False,
                        include_entities=True):
```

Fetch a collection of the most recent Tweets and retweets posted by the authenticating user and the users they follow.  The home timeline is central to how most users interact with Twitter.

###### Params
- `@count` Specifies the number of statuses to retrieve. May not be greater than 200. Defaults to 20. [Optional]
- `@since_id` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available. [Optional]
- `@max_id` Returns results with an ID less than (that is, older than) or equal to the specified ID. [Optional]
- `@trim_user` When True, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. [Optional]
- `@exclude_replies` This parameter will prevent replies from appearing in the returned timeline. Using exclude_replies with the count parameter will mean you will receive up-to count tweets - this is because the count parameter retrieves that many tweets before filtering out retweets and replies. [Optional]
- `@contributor_details` This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included. [Optional]
- `@include_entities` The entities node will be disincluded when set to false. This node offers a variety of metadata about the tweet in a
- `@discreet structure, including` user_mentions, urls, and hashtags. [Optional]

###### Returns
- A sequence of twitter.Status instances, one for each message

##### Function: GetUserTimeline

```python
class Api(object):
	def GetUserTimeline(self,
                        user_id=None,
                        screen_name=None,
                        since_id=None,
                        max_id=None,
                        count=None,
                        include_rts=True,
                        trim_user=False,
                        exclude_replies=False):
```

Fetch the sequence of public Status messages for a single user.  The twitter.Api instance must be authenticated if the user is private.

###### Params
- `@user_id (int, optional)` Specifies the ID of the user for whom to return the user_timeline. Helpful for disambiguating when a valid user ID is also a valid screen name.
- `@screen_name (str, optional)` Specifies the screen name of the user for whom to return the user_timeline. Helpful for disambiguating when a valid screen name is also a user ID.
- `@since_id (int, optional)` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available.
- `@max_id (int, optional)` Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
- `@count (int, optional)` Specifies the number of statuses to retrieve. May not be greater than 200.
- `@include_rts (bool, optional)` If True, the timeline will contain native retweets (if they exist) in addition to the standard stream of tweets.
- `@trim_user (bool, optional)` If True, statuses will only contain the numerical user ID only. Otherwise a full user object will be returned for each status. exclude_replies (bool, optional) If True, this will prevent replies from appearing in the returned timeline. Using exclude_replies with the count parameter will mean you will receive up-to count tweets - this is because the count parameter retrieves that many tweets before filtering out retweets and replies. This parameter is only supported for JSON and XML responses.

###### Returns
- A sequence of Status instances, one for each message up to count

##### Function: GetStatus

```python
class Api(object):
	def GetStatus(self,
                  status_id,
                  trim_user=False,
                  include_my_retweet=True,
                  include_entities=True,
                  include_ext_alt_text=True):
```

Returns a single status message, specified by the status_id parameter.

###### Params
- `@status_id` The numeric ID of the status you are trying to retrieve.
- `@trim_user` When set to True, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. [Optional]
- `@include_my_retweet` When set to True, any Tweets returned that have been retweeted by the authenticating user will include an additional current_user_retweet node, containing the ID of the source status for the retweet. [Optional]
- `@include_entities` If False, the entities node will be disincluded. This node offers a variety of metadata about the tweet in a
- `@discreet structure, including` user_mentions, urls, and hashtags. [Optional]

###### Returns
- A twitter.Status instance representing that status message

##### Function: GetStatusOembed

```python
class Api(object):
	def GetStatusOembed(self,
                        status_id=None,
                        url=None,
                        maxwidth=None,
                        hide_media=False,
                        hide_thread=False,
                        omit_script=False,
                        align=None,
                        related=None,
                        lang=None):
```

Returns information allowing the creation of an embedded representation of a Tweet on third party sites.  Specify tweet by the id or url parameter.

###### Params
- `@status_id` The numeric ID of the status you are trying to embed.
- `@url` The url of the status you are trying to embed.
- `@maxwidth` The maximum width in pixels that the embed should be rendered at. This value is constrained to be between 250 and 550 pixels. [Optional]
- `@hide_media` Specifies whether the embedded Tweet should automatically expand images. [Optional]
- `@hide_thread` Specifies whether the embedded Tweet should automatically show the original message in the case that the embedded Tweet is a reply. [Optional]
- `@omit_script` Specifies whether the embedded Tweet HTML should include a <script> element pointing to widgets.js. [Optional]
- `@align` Specifies whether the embedded Tweet should be left aligned, right aligned, or centered in the page. [Optional]
- `@related` A comma sperated string of related screen names. [Optional]
- `@lang` Language code for the rendered embed. [Optional]

###### Returns
- A dictionary with the response.

##### Function: DestroyStatus

```python
class Api(object):
	def DestroyStatus(self, status_id, trim_user=False):
```

Destroys the status specified by the required ID parameter.  The authenticating user must be the author of the specified status.

###### Params
- `@status_id (int)` The numerical ID of the status you're trying to destroy.
- `@trim_user (bool, optional)` When set to True, each tweet returned in a timeline will include a user object including only the status authors numerical ID.

###### Returns
- A twitter.Status instance representing the destroyed status message

##### Function: PostUpdate

```python
class Api(object):
	def PostUpdate(self,
                   status,
                   media=None,
                   media_additional_owners=None,
                   media_category=None,
                   in_reply_to_status_id=None,
                   auto_populate_reply_metadata=False,
                   exclude_reply_user_ids=None,
                   latitude=None,
                   longitude=None,
                   place_id=None,
                   display_coordinates=False,
                   trim_user=False,
                   verify_status_length=True,
                   attachment_url=None):
```

Post a twitter status message from the authenticated user.  https://dev.twitter.com/docs/api/1.1/post/statuses/update

###### Params
- `@status (str)` The message text to be posted. Must be less than or equal to 140 characters.
- `@media (int, str, fp, optional)` A URL, a local file, or a file-like object (something with a read() method), or a list of any combination of the above.
- `@media_additional_owners (list, optional)` A list of user ids representing Twitter users that should be able to use the uploaded media in their tweets. If you pass a list of media, then additional_owners will apply to each object. If you need more granular control, please use the UploadMedia* methods.
- `@media_category (str, optional)` Only for use with the AdsAPI. See https://dev.twitter.com/ads/creative/promoted-video-overview if this applies to your application.
- `@in_reply_to_status_id (int, optional)` The ID of an existing status that the status to be posted is in reply to.  This implicitly sets the in_reply_to_user_id attribute of the resulting status to the user ID of the message being replied to.  Invalid/missing status IDs will be ignored.
- `@auto_populate_reply_metadata (bool, optional)` Automatically include the @usernames of the users mentioned or participating in the tweet to which this tweet is in reply.
- `@exclude_reply_user_ids (list, optional)` Remove given user_ids (*not* @usernames) from the tweet's automatically generated reply metadata.
- `@attachment_url (str, optional)` 
- `@URL to an attachment resource` one to four photos, a GIF, video, Quote Tweet, or DM deep link. If not specified and media parameter is not None, we will attach the first media object as the attachment URL. If a bad URL is passed, Twitter will raise an error.
- `@latitude (float, optional)` Latitude coordinate of the tweet in degrees. Will only work in conjunction with longitude argument. Both longitude and latitude will be ignored by twitter if the user has a false geo_enabled setting.
- `@longitude (float, optional)` Longitude coordinate of the tweet in degrees. Will only work in conjunction with latitude argument. Both longitude and latitude will be ignored by twitter if the user has a false geo_enabled setting.
- `@place_id (int, optional)` A place in the world. These IDs can be retrieved from GET geo/reverse_geocode.
- `@display_coordinates (bool, optional)` Whether or not to put a pin on the exact coordinates a tweet has been sent from.
- `@trim_user (bool, optional)` If True the returned payload will only contain the user IDs, otherwise the payload will contain the full user data item.
- `@verify_status_length (bool, optional)` If True, api throws a hard error that the status is over 140 characters. If False, Api will attempt to post the status.

###### Returns
- (twitter.Status) A twitter.Status instance representing the message posted.

##### Function: UploadMediaSimple

```python
class Api(object):
	def UploadMediaSimple(self,
                          media,
                          additional_owners=None,
                          media_category=None):
```

Upload a media file to Twitter in one request. Used for small file uploads that do not require chunked uploads.

###### Params
- `@media` File-like object to upload.
- `@additional_owners` additional Twitter users that are allowed to use The uploaded media. Should be a list of integers. Maximum number of additional owners is capped at 100 by Twitter.
- `@media_category` Category with which to identify media upload. Only use with Ads API & video files.

###### Returns
- `media_id` ID of the uploaded media returned by the Twitter API or 0.

##### Function: PostMediaMetadata

```python
class Api(object):
	def PostMediaMetadata(self,
                          media_id,
                          alt_text=None):
```

Provide addtional data for uploaded media.

###### Params
- `@media_id` ID of a previously uploaded media item.
- `@alt_text` Image Alternate Text.

##### Function: _UploadMediaChunkedInit

```python
class Api(object):
	def _UploadMediaChunkedInit(self,
                                media,
                                additional_owners=None,
                                media_category=None):
```

Start a chunked upload to Twitter.

###### Params
- `@media` File-like object to upload.
- `@additional_owners` additional Twitter users that are allowed to use The uploaded media. Should be a list of integers. Maximum number of additional owners is capped at 100 by Twitter.
- `@media_category` Category with which to identify media upload. Only use with Ads API & video files.

###### Returns
- `tuple` media_id (returned from Twitter), file-handler object (i.e., has .read() method), filename media file.

##### Function: _UploadMediaChunkedAppend

```python
class Api(object):
	def _UploadMediaChunkedAppend(self,
                                  media_id,
                                  media_fp,
                                  filename):
```

Appends (i.e., actually uploads) media file to Twitter.

###### Params
- `@media_id (int)` ID of the media file received from Init method.
- `@media_fp (file)` File-like object representing media file (must have .read() method)
- `@filename (str)` Filename of the media file being uploaded.

###### Returns
- True if successful. Raises otherwise.

##### Function: _UploadMediaChunkedFinalize

```python
class Api(object):
	def _UploadMediaChunkedFinalize(self, media_id):
```

Finalize chunked upload to Twitter.

###### Params
- `@media_id (int)` ID of the media file for which to finalize the upload.

###### Returns
- `json` JSON string of data from Twitter.

##### Function: UploadMediaChunked

```python
class Api(object):
	def UploadMediaChunked(self,
                           media,
                           additional_owners=None,
                           media_category=None):
```

Upload a media file to Twitter in multiple requests.

###### Params
- `@media` File-like object to upload.
- `@additional_owners` additional Twitter users that are allowed to use The uploaded media. Should be a list of integers. Maximum number of additional owners is capped at 100 by Twitter.
- `@media_category` Category with which to identify media upload. Only use with Ads API & video files.

###### Returns
- `media_id` ID of the uploaded media returned by the Twitter API. Raises if unsuccesful.

##### Function: PostMedia

```python
class Api(object):
	def PostMedia(self,
                  status,
                  media,
                  possibly_sensitive=None,
                  in_reply_to_status_id=None,
                  latitude=None,
                  longitude=None,
                  place_id=None,
                  display_coordinates=False):
```

Post a twitter status message from the user with a picture attached.

###### Params
- `@status` the text of your update
- `@media` This can be the location of media(PNG, JPG, GIF) on the local file system or at an HTTP URL, it can also be a file-like object
- `@possibly_sensitive` set true if content is "advanced." [Optional]
- `@in_reply_to_status_id` ID of a status that this is in reply to. [Optional]
- `@lat` latitude of location. [Optional]
- `@long` longitude of location. [Optional]
- `@place_id` A place in the world identified by a Twitter place ID. [Optional]
- `@display_coordinates` Set true if you want to display coordinates. [Optional]

###### Returns
- A twitter.Status instance representing the message posted.

##### Function: PostMultipleMedia

```python
class Api(object):
	def PostMultipleMedia(self, status, media, possibly_sensitive=None,
                          in_reply_to_status_id=None, latitude=None,
                          longitude=None, place_id=None,
                          display_coordinates=False):
```

Post a twitter status message from the authenticated user with multiple pictures attached.

###### Params
- `@status` the text of your update
- `@media` location of multiple media elements(PNG, JPG, GIF)
- `@possibly_sensitive` set true is content is "advanced"
- `@in_reply_to_status_id` ID of a status that this is in reply to
- `@lat` location in latitude
- `@long` location in longitude
- `@place_id` A place in the world identified by a Twitter place ID
- `@display_coordinates` 

###### Returns
- A twitter.Status instance representing the message posted.

##### Function: _TweetTextWrap

```python
class Api(object):
	def _TweetTextWrap(self,
                       status,
                       char_lim=140):
```

##### Function: PostUpdates

```python
class Api(object):
	def PostUpdates(self,
                    status,
                    continuation=None,
                    **kwargs):
```

Post one or more twitter status messages from the authenticated user.  Unlike api.PostUpdate, this method will post multiple status updates if the message is longer than 140 characters.

###### Params
- `@status` The message text to be posted. May be longer than 140 characters.
- `@continuation` The character string, if any, to be appended to all but the last message.  Note that Twitter strips trailing '...' strings from messages.  Consider using the unicode \u2026 character (horizontal ellipsis) instead. [Defaults to None]
- `@**kwargs` See api.PostUpdate for a list of accepted parameters.

###### Returns
- A of list twitter.Status instance representing the messages posted.

##### Function: PostRetweet

```python
class Api(object):
	def PostRetweet(self, status_id, trim_user=False):
```

Retweet a tweet with the Retweet API.

###### Params
- `@status_id` The numerical id of the tweet that will be retweeted
- `@trim_user` If True the returned payload will only contain the user IDs, otherwise the payload will contain the full user data item. [Optional]

###### Returns
- A twitter.Status instance representing the original tweet with retweet details embedded.

##### Function: GetUserRetweets

```python
class Api(object):
	def GetUserRetweets(self,
                        count=None,
                        since_id=None,
                        max_id=None,
                        trim_user=False):
```

Fetch the sequence of retweets made by the authenticated user.

###### Params
- `@count` The number of status messages to retrieve. [Optional]
- `@since_id` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available. [Optional]
- `@max_id` Returns results with an ID less than (that is, older than) or equal to the specified ID. [Optional]
- `@trim_user` If True the returned payload will only contain the user IDs, otherwise the payload will contain the full user data item. [Optional]

###### Returns
- A sequence of twitter.Status instances, one for each message up to count

##### Function: GetReplies

```python
class Api(object):
	def GetReplies(self,
                   since_id=None,
                   count=None,
                   max_id=None,
                   trim_user=False):
```

Get a sequence of status messages representing the 20 most recent replies (status updates prefixed with @twitterID) to the authenticating user.

###### Params
- `@since_id` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available. [Optional]
- `@max_id` Returns results with an ID less than (that is, older than) or equal to the specified ID. [Optional]
- `@trim_user` If True the returned payload will only contain the user IDs, otherwise the payload will contain the full user data item. [Optional]

###### Returns
- A sequence of twitter.Status instances, one for each reply to the user.

##### Function: GetRetweets

```python
class Api(object):
	def GetRetweets(self,
                    statusid,
                    count=None,
                    trim_user=False):
```

Returns up to 100 of the first retweets of the tweet identified by statusid

###### Params
- `@statusid (int)` The ID of the tweet for which retweets should be searched for
- `@count (int, optional)` The number of status messages to retrieve.
- `@trim_user (bool, optional)` If True the returned payload will only contain the user IDs, otherwise the payload will contain the full user data item.

###### Returns
- A list of twitter.Status instances, which are retweets of statusid

##### Function: GetRetweeters

```python
class Api(object):
	def GetRetweeters(self,
                      status_id,
                      cursor=None,
                      count=100,
                      stringify_ids=False):
```

Returns a collection of up to 100 user IDs belonging to users who have retweeted the tweet specified by the status_id parameter.

###### Params
- `@status_id` the tweet's numerical ID
- `@cursor` breaks the ids into pages of no more than 100.
- `@stringify_ids` returns the IDs as unicode strings. [Optional]

###### Returns
- A list of user IDs

##### Function: GetRetweetsOfMe

```python
class Api(object):
	def GetRetweetsOfMe(self,
                        count=None,
                        since_id=None,
                        max_id=None,
                        trim_user=False,
                        include_entities=True,
                        include_user_entities=True):
```

Returns up to 100 of the most recent tweets of the user that have been retweeted by others.

###### Params
- `@count` The number of retweets to retrieve, up to 100. Defaults to 20. [Optional]
- `@since_id` Returns results with an ID greater than (newer than) this ID. [Optional]
- `@max_id` Returns results with an ID less than or equal to this ID. [Optional]
- `@trim_user` When True, the user object for each tweet will only be an ID. [Optional]
- `@include_entities` When True, the tweet entities will be included. [Optional]
- `@include_user_entities` When True, the user entities will be included. [Optional]

##### Function: _GetBlocksMutesPaged

```python
class Api(object):
	def _GetBlocksMutesPaged(self,
                             endpoint,
                             action,
                             cursor=-1,
                             skip_status=False,
                             include_entities=False,
                             stringify_ids=False):
```

Fetch a page of the users (as twitter.User instances) blocked or muted by the currently authenticated user.

###### Params
- `@endpoint (str)` Either "mute" or "block".
- `@action (str)` Either 'list' or 'ids' depending if you want to return fully-hydrated twitter.User objects or a list of user IDs as ints.
- `@cursor (int, optional)` Should be set to -1 if you want the first page, thereafter denotes the page of users that you want to return.
- `@skip_status (bool, optional)` If True the statuses will not be returned in the user items.
- `@include_entities (bool, optional)` When True, the user entities will be included.

###### Returns
- next_cursor, previous_cursor, list of twitter.User instances, one for each user.

##### Function: GetBlocks

```python
class Api(object):
	def GetBlocks(self,
                  skip_status=False,
                  include_entities=False):
```

Fetch the sequence of all users (as twitter.User instances), blocked by the currently authenticated user.

###### Params
- `@skip_status (bool, optional)` If True the statuses will not be returned in the user items.
- `@include_entities (bool, optional)` When True, the user entities will be included.

###### Returns
- A list of twitter.User instances, one for each blocked user.

##### Function: GetBlocksPaged

```python
class Api(object):
	def GetBlocksPaged(self,
                       cursor=-1,
                       skip_status=False,
                       include_entities=False):
```

Fetch a page of the users (as twitter.User instances) blocked by the currently authenticated user.

###### Params
- `@cursor (int, optional)` Should be set to -1 if you want the first page, thereafter denotes the page of blocked users that you want to return.
- `@skip_status (bool, optional)` If True the statuses will not be returned in the user items.
- `@include_entities (bool, optional)` When True, the user entities will be included.

###### Returns
- next_cursor, previous_cursor, list of twitter.User instances, one for each blocked user.

##### Function: GetBlocksIDs

```python
class Api(object):
	def GetBlocksIDs(self,
                     stringify_ids=False):
```

Fetch the sequence of all user IDs blocked by the currently authenticated user.

###### Params
- `@stringify_ids (bool, optional)` If True user IDs will be returned as strings rather than integers.

###### Returns
- A list of user IDs for all blocked users.

##### Function: GetBlocksIDsPaged

```python
class Api(object):
	def GetBlocksIDsPaged(self,
                          cursor=-1,
                          stringify_ids=False):
```

Fetch a page of the user IDs blocked by the currently authenticated user.

###### Params
- `@cursor (int, optional)` Should be set to -1 if you want the first page, thereafter denotes the page of blocked users that you want to return.
- `@stringify_ids (bool, optional)` If True user IDs will be returned as strings rather than integers.

###### Returns
- next_cursor, previous_cursor, list of user IDs of blocked users.

##### Function: GetMutes

```python
class Api(object):
	def GetMutes(self,
                 skip_status=False,
                 include_entities=False):
```

Fetch the sequence of all users (as twitter.User instances), muted by the currently authenticated user.

###### Params
- `@skip_status (bool, optional)` If True the statuses will not be returned in the user items.
- `@include_entities (bool, optional)` When True, the user entities will be included.

###### Returns
- A list of twitter.User instances, one for each muted user.

##### Function: GetMutesPaged

```python
class Api(object):
	def GetMutesPaged(self,
                      cursor=-1,
                      skip_status=False,
                      include_entities=False):
```

Fetch a page of the users (as twitter.User instances) muted by the currently authenticated user.

###### Params
- `@cursor (int, optional)` Should be set to -1 if you want the first page, thereafter denotes the page of muted users that you want to return.
- `@skip_status (bool, optional)` If True the statuses will not be returned in the user items.
- `@include_entities (bool, optional)` When True, the user entities will be included.

###### Returns
- next_cursor, previous_cursor, list of twitter.User instances, one for each muted user.

##### Function: GetMutesIDs

```python
class Api(object):
	def GetMutesIDs(self,
                    stringify_ids=False):
```

Fetch the sequence of all user IDs muted by the currently authenticated user.

###### Params
- `@stringify_ids (bool, optional)` If True user IDs will be returned as strings rather than integers.

###### Returns
- A list of user IDs for all muted users.

##### Function: GetMutesIDsPaged

```python
class Api(object):
	def GetMutesIDsPaged(self,
                         cursor=-1,
                         stringify_ids=False):
```

Fetch a page of the user IDs muted by the currently authenticated user.

###### Params
- `@cursor (int, optional)` Should be set to -1 if you want the first page, thereafter denotes the page of muted users that you want to return.
- `@stringify_ids (bool, optional)` If True user IDs will be returned as strings rather than integers.

###### Returns
- next_cursor, previous_cursor, list of user IDs of muted users.

##### Function: _BlockMute

```python
class Api(object):
	def _BlockMute(self,
                   action,
                   endpoint,
                   user_id=None,
                   screen_name=None,
                   include_entities=True,
                   skip_status=False):
```

Create or destroy a block or mute on behalf of the authenticated user.

###### Params
- `@action (str)` Either 'create' or 'destroy'.
- `@endpoint (str)` Either 'block' or 'mute'. user_id (int, optional) The numerical ID of the user to block/mute.
- `@screen_name (str, optional)` The screen name of the user to block/mute.
- `@include_entities (bool, optional)` The entities node will not be included if set to False.
- `@skip_status (bool, optional)` When set to False, the blocked User's statuses will not be included with the returned User object.

###### Returns
- `twitter.User` twitter.User object representing the blocked/muted user.

##### Function: CreateBlock

```python
class Api(object):
	def CreateBlock(self,
                    user_id=None,
                    screen_name=None,
                    include_entities=True,
                    skip_status=False):
```

Blocks the user specified by either user_id or screen_name.

###### Params
- `@screen_name (str, optional)` The screen name of the user to block.
- `@include_entities (bool, optional)` The entities node will not be included if set to False.
- `@skip_status (bool, optional)` When set to False, the blocked User's statuses will not be included with the returned User object.

###### Returns
- A twitter.User instance representing the blocked user.

##### Function: DestroyBlock

```python
class Api(object):
	def DestroyBlock(self,
                     user_id=None,
                     screen_name=None,
                     include_entities=True,
                     skip_status=False):
```

Unlocks the user specified by either user_id or screen_name.

###### Params
- `@screen_name (str, optional)` The screen name of the user to block.
- `@include_entities (bool, optional)` The entities node will not be included if set to False.
- `@skip_status (bool, optional)` When set to False, the blocked User's statuses will not be included with the returned User object.

###### Returns
- A twitter.User instance representing the blocked user.

##### Function: CreateMute

```python
class Api(object):
	def CreateMute(self,
                   user_id=None,
                   screen_name=None,
                   include_entities=True,
                   skip_status=False):
```

Mutes the user specified by either user_id or screen_name.

###### Params
- `@screen_name (str, optional)` The screen name of the user to mute.
- `@include_entities (bool, optional)` The entities node will not be included if set to False.
- `@skip_status (bool, optional)` When set to False, the muted User's statuses will not be included with the returned User object.

###### Returns
- A twitter.User instance representing the muted user.

##### Function: DestroyMute

```python
class Api(object):
	def DestroyMute(self,
                    user_id=None,
                    screen_name=None,
                    include_entities=True,
                    skip_status=False):
```

Unlocks the user specified by either user_id or screen_name.

###### Params
- `@screen_name (str, optional)` The screen name of the user to mute.
- `@include_entities (bool, optional)` The entities node will not be included if set to False.
- `@skip_status (bool, optional)` When set to False, the muted User's statuses will not be included with the returned User object.

###### Returns
- A twitter.User instance representing the muted user.

##### Function: _GetIDsPaged

```python
class Api(object):
	def _GetIDsPaged(self,
                     url,
                     user_id,
                     screen_name,
                     cursor,
                     stringify_ids,
                     count):
```

This is the lowest level paging logic for fetching IDs. It is used solely by GetFollowerIDsPaged and GetFriendIDsPaged. It is not intended for other use.  See GetFollowerIDsPaged or GetFriendIDsPaged for an explanation of the input arguments.

##### Function: GetFollowerIDsPaged

```python
class Api(object):
	def GetFollowerIDsPaged(self,
                            user_id=None,
                            screen_name=None,
                            cursor=-1,
                            stringify_ids=False,
                            count=5000):
```

Make a cursor driven call to return a list of one page followers.  The caller is responsible for handling the cursor value and looping to gather all of the data

###### Params
- `@user_id` The twitter id of the user whose followers you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@screen_name` The twitter name of the user whose followers you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@cursor` Should be set to -1 for the initial call and then is used to control what result page Twitter returns.
- `@stringify_ids` if True then twitter will return the ids as strings instead of integers. [Optional]
- `@count` The number of user id's to retrieve per API request. Please be aware that this might get you rate-limited if set to a small number. By default Twitter will retrieve 5000 UIDs per call. [Optional]

###### Returns
- next_cursor, previous_cursor, data sequence of user ids, one for each follower

##### Function: GetFriendIDsPaged

```python
class Api(object):
	def GetFriendIDsPaged(self,
                          user_id=None,
                          screen_name=None,
                          cursor=-1,
                          stringify_ids=False,
                          count=5000):
```

Make a cursor driven call to return the list of all friends  The caller is responsible for handling the cursor value and looping to gather all of the data

###### Params
- `@user_id` The twitter id of the user whose friends you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@screen_name` The twitter name of the user whose friends you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@cursor` Should be set to -1 for the initial call and then is used to control what result page Twitter returns.
- `@stringify_ids` if True then twitter will return the ids as strings instead of integers. [Optional]
- `@count` The number of user id's to retrieve per API request. Please be aware that this might get you rate-limited if set to a small number. By default Twitter will retrieve 5000 UIDs per call. [Optional]

###### Returns
- next_cursor, previous_cursor, data sequence of twitter.User instances, one for each friend

##### Function: _GetFriendFollowerIDs

```python
class Api(object):
	def _GetFriendFollowerIDs(self,
                              url=None,
                              user_id=None,
                              screen_name=None,
                              cursor=None,
                              count=None,
                              stringify_ids=False,
                              total_count=None):
```

Common method for GetFriendIDs and GetFollowerIDs

##### Function: GetFollowerIDs

```python
class Api(object):
	def GetFollowerIDs(self,
                       user_id=None,
                       screen_name=None,
                       cursor=None,
                       stringify_ids=False,
                       count=None,
                       total_count=None):
```

Returns a list of twitter user id's for every person that is following the specified user.

###### Params
- `@user_id` The id of the user to retrieve the id list for. [Optional]
- `@screen_name` The screen_name of the user to retrieve the id list for. [Optional]
- `@cursor` Specifies the Twitter API Cursor location to start at.
- `@Note` there are pagination limits. [Optional]
- `@stringify_ids` if True then twitter will return the ids as strings instead of integers. [Optional]
- `@count` The number of user id's to retrieve per API request. Please be aware that this might get you rate-limited if set to a small number. By default Twitter will retrieve 5000 UIDs per call. [Optional]
- `@total_count` The total amount of UIDs to retrieve. Good if the account has many followers and you don't want to get rate limited. The data returned might contain more UIDs if total_count is not a multiple of count (5000 by default). [Optional]

###### Returns
- A list of integers, one for each user id.

##### Function: GetFriendIDs

```python
class Api(object):
	def GetFriendIDs(self,
                     user_id=None,
                     screen_name=None,
                     cursor=None,
                     count=None,
                     stringify_ids=False,
                     total_count=None):
```

Fetch a sequence of user ids, one for each friend. Returns a list of all the given user's friends' IDs. If no user_id or screen_name is given, the friends will be those of the authenticated user.

###### Params
- `@user_id` The id of the user to retrieve the id list for. [Optional]
- `@screen_name` The screen_name of the user to retrieve the id list for. [Optional]
- `@cursor` Specifies the Twitter API Cursor location to start at.
- `@Note` there are pagination limits. [Optional]
- `@stringify_ids` if True then twitter will return the ids as strings instead of integers. [Optional]
- `@count` The number of user id's to retrieve per API request. Please be aware that this might get you rate-limited if set to a small number. By default Twitter will retrieve 5000 UIDs per call. [Optional]
- `@total_count` The total amount of UIDs to retrieve. Good if the account has many followers and you don't want to get rate limited. The data returned might contain more UIDs if total_count is not a multiple of count (5000 by default). [Optional]

###### Returns
- A list of integers, one for each user id.

##### Function: _GetFriendsFollowersPaged

```python
class Api(object):
	def _GetFriendsFollowersPaged(self,
                                  url=None,
                                  user_id=None,
                                  screen_name=None,
                                  cursor=-1,
                                  count=200,
                                  skip_status=False,
                                  include_user_entities=True):
```

Make a cursor driven call to return the list of 1 page of friends or followers.

###### Params
- `@url` Endpoint from which to get data. Either base_url+'/followers/list.json' or base_url+'/friends/list.json'.
- `@user_id` The twitter id of the user whose followers you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@screen_name` The twitter name of the user whose followers you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@cursor` Should be set to -1 for the initial call and then is used to control what result page Twitter returns.
- `@count` The number of users to return per page, up to a maximum of 200. Defaults to 200. [Optional]
- `@skip_status` If True the statuses will not be returned in the user items. [Optional]
- `@include_user_entities` When True, the user entities will be included. [Optional]

###### Returns
- next_cursor, previous_cursor, data sequence of twitter.User instances, one for each follower

##### Function: GetFollowersPaged

```python
class Api(object):
	def GetFollowersPaged(self,
                          user_id=None,
                          screen_name=None,
                          cursor=-1,
                          count=200,
                          skip_status=False,
                          include_user_entities=True):
```

Make a cursor driven call to return the list of all followers

###### Params
- `@user_id` The twitter id of the user whose followers you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@screen_name` The twitter name of the user whose followers you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@cursor` Should be set to -1 for the initial call and then is used to control what result page Twitter returns.
- `@count` The number of users to return per page, up to a maximum of 200. Defaults to 200. [Optional]
- `@skip_status` If True the statuses will not be returned in the user items. [Optional]
- `@include_user_entities` When True, the user entities will be included. [Optional]

###### Returns
- next_cursor, previous_cursor, data sequence of twitter.User instances, one for each follower

##### Function: GetFriendsPaged

```python
class Api(object):
	def GetFriendsPaged(self,
                        user_id=None,
                        screen_name=None,
                        cursor=-1,
                        count=200,
                        skip_status=False,
                        include_user_entities=True):
```

Make a cursor driven call to return the list of all friends.

###### Params
- `@user_id` The twitter id of the user whose friends you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@screen_name` The twitter name of the user whose friends you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@cursor` Should be set to -1 for the initial call and then is used to control what result page Twitter returns.
- `@count` The number of users to return per page, up to a current maximum of 200. Defaults to 200. [Optional]
- `@skip_status` If True the statuses will not be returned in the user items. [Optional]
- `@include_user_entities` When True, the user entities will be included. [Optional]

###### Returns
- next_cursor, previous_cursor, data sequence of twitter.User instances, one for each follower

##### Function: _GetFriendsFollowers

```python
class Api(object):
	def _GetFriendsFollowers(self,
                             url=None,
                             user_id=None,
                             screen_name=None,
                             cursor=None,
                             count=None,
                             total_count=None,
                             skip_status=False,
                             include_user_entities=True):
```

Fetch the sequence of twitter.User instances, one for each friend or follower.

###### Params
- `@url` URL to get. Either base_url + ('/followers/list.json' or '/friends/list.json').
- `@user_id` The twitter id of the user whose friends you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@screen_name` The twitter name of the user whose friends you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@cursor` Should be set to -1 for the initial call and then is used to control what result page Twitter returns.
- `@count` The number of users to return per page, up to a maximum of 200. Defaults to 200. [Optional]
- `@total_count` The upper bound of number of users to return, defaults to None.
- `@skip_status` If True the statuses will not be returned in the user items. [Optional]
- `@include_user_entities` When True, the user entities will be included. [Optional]

###### Returns
- A sequence of twitter.User instances, one for each friend or follower

##### Function: GetFollowers

```python
class Api(object):
	def GetFollowers(self,
                     user_id=None,
                     screen_name=None,
                     cursor=None,
                     count=None,
                     total_count=None,
                     skip_status=False,
                     include_user_entities=True):
```

Fetch the sequence of twitter.User instances, one for each follower.  If both user_id and screen_name are specified, this call will return the followers of the user specified by screen_name, however this behavior is undocumented by Twitter and may change without warning.

###### Params
- `@user_id` The twitter id of the user whose followers you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@screen_name` The twitter name of the user whose followers you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@cursor` Should be set to -1 for the initial call and then is used to control what result page Twitter returns.
- `@count` The number of users to return per page, up to a maximum of 200. Defaults to 200. [Optional]
- `@total_count` The upper bound of number of users to return, defaults to None.
- `@skip_status` If True the statuses will not be returned in the user items. [Optional]
- `@include_user_entities` When True, the user entities will be included. [Optional]

###### Returns
- A sequence of twitter.User instances, one for each follower

##### Function: GetFriends

```python
class Api(object):
	def GetFriends(self,
                   user_id=None,
                   screen_name=None,
                   cursor=None,
                   count=None,
                   total_count=None,
                   skip_status=False,
                   include_user_entities=True):
```

Fetch the sequence of twitter.User instances, one for each friend.  If both user_id and screen_name are specified, this call will return the followers of the user specified by screen_name, however this behavior is undocumented by Twitter and may change without warning.

###### Params
- `@user_id` The twitter id of the user whose friends you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@screen_name` The twitter name of the user whose friends you are fetching. If not specified, defaults to the authenticated user. [Optional]
- `@cursor` Should be set to -1 for the initial call and then is used to control what result page Twitter returns.
- `@count` The number of users to return per page, up to a maximum of 200. Defaults to 200. [Optional]
- `@total_count` The upper bound of number of users to return, defaults to None.
- `@skip_status` If True the statuses will not be returned in the user items. [Optional]
- `@include_user_entities` When True, the user entities will be included. [Optional]

###### Returns
- A sequence of twitter.User instances, one for each friend

##### Function: UsersLookup

```python
class Api(object):
	def UsersLookup(self,
                    user_id=None,
                    screen_name=None,
                    users=None,
                    include_entities=True):
```

Fetch extended information for the specified users.  Users may be specified either as lists of either user_ids, screen_names, or twitter.User objects. The list of users that are queried is the union of all specified parameters.

###### Params
- `@user_id (int, list, optional)` A list of user_ids to retrieve extended information.
- `@screen_name (str, optional)` A list of screen_names to retrieve extended information.
- `@users (list, optional)` A list of twitter.User objects to retrieve extended information.
- `@include_entities (bool, optional)` The entities node that may appear within embedded statuses will be excluded when set to False.

###### Returns
- A list of twitter.User objects for the requested users

##### Function: GetUser

```python
class Api(object):
	def GetUser(self,
                user_id=None,
                screen_name=None,
                include_entities=True):
```

Returns a single user.

###### Params
- `@user_id (int, optional)` The id of the user to retrieve.
- `@screen_name (str, optional)` The screen name of the user for whom to return results for. Either a user_id or screen_name is required for this method.
- `@include_entities (bool, optional)` The entities node will be omitted when set to False.

###### Returns
- A twitter.User instance representing that user

##### Function: GetDirectMessages

```python
class Api(object):
	def GetDirectMessages(self,
                          since_id=None,
                          max_id=None,
                          count=None,
                          include_entities=True,
                          skip_status=False,
                          full_text=False,
                          page=None):
```

Returns a list of the direct messages sent to the authenticating user.

###### Params
- `@since_id` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available. [Optional]
- `@max_id` Returns results with an ID less than (that is, older than) or equal to the specified ID. [Optional]
- `@count` Specifies the number of direct messages to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied. [Optional]
- `@include_entities` The entities node will be omitted when set to False. [Optional]
- `@skip_status` When set to True statuses will not be included in the returned user objects. [Optional]
- `@full_text` When set to True full message will be included in the returned message object if message length is bigger than 140 characters. [Optional]
- `@page` If you want more than 200 messages, you can use this and get 20 messages each time. You must recall it and increment the page value until it return nothing. You can't use count option with it. First value is 1 and not 0.

###### Returns
- A sequence of twitter.DirectMessage instances

##### Function: GetSentDirectMessages

```python
class Api(object):
	def GetSentDirectMessages(self,
                              since_id=None,
                              max_id=None,
                              count=None,
                              page=None,
                              include_entities=True):
```

Returns a list of the direct messages sent by the authenticating user.

###### Params
- `@since_id` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. [Optional]
- `@max_id` Returns results with an ID less than (that is, older than) or equal to the specified ID. [Optional]
- `@count` Specifies the number of direct messages to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied. [Optional]
- `@page` Specifies the page of results to retrieve.
- `@Note` there are pagination limits. [Optional]
- `@include_entities` The entities node will be omitted when set to False. [Optional]

###### Returns
- A sequence of twitter.DirectMessage instances

##### Function: PostDirectMessage

```python
class Api(object):
	def PostDirectMessage(self,
                          text,
                          user_id=None,
                          screen_name=None):
```

Post a twitter direct message from the authenticated user.

###### Params
- `@text` The message text to be posted.  Must be less than 140 characters.
- `@user_id` The ID of the user who should receive the direct message. [Optional]
- `@screen_name` The screen name of the user who should receive the direct message. [Optional]

###### Returns
- A twitter.DirectMessage instance representing the message posted

##### Function: DestroyDirectMessage

```python
class Api(object):
	def DestroyDirectMessage(self, message_id, include_entities=True):
```

Destroys the direct message specified in the required ID parameter.  The twitter.Api instance must be authenticated, and the authenticating user must be the recipient of the specified direct message.

###### Params
- `@message_id` The id of the direct message to be destroyed

###### Returns
- A twitter.DirectMessage instance representing the message destroyed

##### Function: CreateFriendship

```python
class Api(object):
	def CreateFriendship(self, user_id=None, screen_name=None, follow=True):
```

Befriends the user specified by the user_id or screen_name.

###### Params
- `@user_id` A user_id to follow [Optional]
- `@screen_name` A screen_name to follow [Optional]
- `@follow` Set to False to disable notifications for the target user

###### Returns
- A twitter.User instance representing the befriended user.

##### Function: _AddOrEditFriendship

```python
class Api(object):
	def _AddOrEditFriendship(self, user_id=None, screen_name=None, uri_end='create', follow_key='follow', follow=True):
```

Shared method for Create/Update Friendship.

##### Function: UpdateFriendship

```python
class Api(object):
	def UpdateFriendship(self, user_id=None, screen_name=None, follow=True, **kwargs):
```

##### Function: DestroyFriendship

```python
class Api(object):
	def DestroyFriendship(self, user_id=None, screen_name=None):
```

Discontinues friendship with a user_id or screen_name.

###### Params
- `@user_id` A user_id to unfollow [Optional]
- `@screen_name` A screen_name to unfollow [Optional]

###### Returns
- A twitter.User instance representing the discontinued friend.

##### Function: ShowFriendship

```python
class Api(object):
	def ShowFriendship(self,
                       source_user_id=None,
                       source_screen_name=None,
                       target_user_id=None,
                       target_screen_name=None):
```

Returns information about the relationship between the two users.

###### Params
- `@source_id` The user_id of the subject user [Optional]
- `@source_screen_name` The screen_name of the subject user [Optional]
- `@target_id` The user_id of the target user [Optional]
- `@target_screen_name` The screen_name of the target user [Optional]

###### Returns
- A Twitter Json structure.

##### Function: LookupFriendship

```python
class Api(object):
	def LookupFriendship(self,
                         user_id=None,
                         screen_name=None):
```

Lookup friendship status for user to authed user.  Users may be specified either as lists of either user_ids, screen_names, or twitter.User objects. The list of users that are queried is the union of all specified parameters.  Up to 100 users may be specified.

###### Params
- `@user_id (int, User, or list of ints or Users, optional)` A list of user_ids to retrieve extended information.
- `@screen_name (string, User, or list of strings or Users, optional)` A list of screen_names to retrieve extended information.

###### Returns
- `list` A list of twitter.UserStatus instance representing the friendship status between the specified users and the authenticated user.

##### Function: IncomingFriendship

```python
class Api(object):
	def IncomingFriendship(self,
                           cursor=None,
                           stringify_ids=None):
```

Returns a collection of user IDs belonging to users who have pending request to follow the authenticated user.

###### Params
- `@cursor` breaks the ids into pages of no more than 5000.
- `@stringify_ids` returns the IDs as unicode strings. [Optional]

###### Returns
- A list of user IDs

##### Function: OutgoingFriendship

```python
class Api(object):
	def OutgoingFriendship(self,
                           cursor=None,
                           stringify_ids=None):
```

Returns a collection of user IDs for every protected user for whom the authenticated user has a pending follow request.

###### Params
- `@cursor` breaks the ids into pages of no more than 5000.
- `@stringify_ids` returns the IDs as unicode strings. [Optional]

###### Returns
- A list of user IDs

##### Function: CreateFavorite

```python
class Api(object):
	def CreateFavorite(self,
                       status=None,
                       status_id=None,
                       include_entities=True):
```

Favorites the specified status object or id as the authenticating user.  Returns the favorite status when successful.

###### Params
- `@status_id (int, optional)` The id of the twitter status to mark as a favorite.
- `@status (twitter.Status, optional)` The twitter.Status object to mark as a favorite.
- `@include_entities (bool, optional)` The entities node will be omitted when set to False.

###### Returns
- A twitter.Status instance representing the newly-marked favorite.

##### Function: DestroyFavorite

```python
class Api(object):
	def DestroyFavorite(self,
                        status=None,
                        status_id=None,
                        include_entities=True):
```

Un-Favorites the specified status object or id as the authenticating user.  Returns the un-favorited status when successful.

###### Params
- `@status_id (int, optional)` The id of the twitter status to mark as a favorite.
- `@status (twitter.Status, optional)` The twitter.Status object to mark as a favorite.
- `@include_entities (bool, optional)` The entities node will be omitted when set to False.

###### Returns
- A twitter.Status instance representing the newly-unmarked favorite.

##### Function: GetFavorites

```python
class Api(object):
	def GetFavorites(self,
                     user_id=None,
                     screen_name=None,
                     count=None,
                     since_id=None,
                     max_id=None,
                     include_entities=True):
```

Return a list of Status objects representing favorited tweets.  Returns up to 200 most recent tweets for the authenticated user.

###### Params
- `@user_id (int, optional)` Specifies the ID of the user for whom to return the favorites. Helpful for disambiguating when a valid user ID is also a valid screen name.
- `@screen_name (str, optional)` Specifies the screen name of the user for whom to return the favorites. Helpful for disambiguating when a valid screen name is also a user ID.
- `@since_id (int, optional)` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available.
- `@max_id (int, optional)` Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
- `@count (int, optional)` Specifies the number of statuses to retrieve. May not be greater than 200.
- `@include_entities (bool, optional)` The entities node will be omitted when set to False.

###### Returns
- A sequence of Status instances, one for each favorited tweet up to count

##### Function: GetMentions

```python
class Api(object):
	def GetMentions(self,
                    count=None,
                    since_id=None,
                    max_id=None,
                    trim_user=False,
                    contributor_details=False,
                    include_entities=True):
```

Returns the 20 most recent mentions (status containing @screen_name) for the authenticating user.

###### Params
- `@count` Specifies the number of tweets to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. [Optional]
- `@since_id` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available. [Optional]
- `@max_id` Returns only statuses with an ID less than (that is, older than) the specified ID. [Optional]
- `@trim_user` When set to True, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. [Optional]
- `@contributor_details` If set to True, this parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included. [Optional]
- `@include_entities` The entities node will be disincluded when set to False. [Optional]

###### Returns
- A sequence of twitter.Status instances, one for each mention of the user.

##### Function: _IDList

```python
class Api(object):
	def _IDList(list_id, slug, owner_id, owner_screen_name):
```

##### Function: CreateList

```python
class Api(object):
	def CreateList(self, name, mode=None, description=None):
```

Creates a new list with the give name for the authenticated user.

###### Params
- `@name (str)` New name for the list
- `@mode (str, optional)` 'public' or 'private'. Defaults to 'public'.
- `@description (str, optional)` Description of the list.

###### Returns
- `twitter.list.List` A twitter.List instance representing the new list

##### Function: DestroyList

```python
class Api(object):
	def DestroyList(self,
                    owner_screen_name=None,
                    owner_id=None,
                    list_id=None,
                    slug=None):
```

Destroys the list identified by list_id or slug and one of owner_screen_name or owner_id.

###### Params
- `@owner_screen_name (str, optional)` The screen_name of the user who owns the list being requested by a slug.
- `@owner_id (int, optional)` The user ID of the user who owns the list being requested by a slug.
- `@list_id (int, optional)` The numerical id of the list.
- `@slug (str, optional)` You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the owner_id or owner_screen_name parameters.

###### Returns
- `twitter.list.List` A twitter.List instance representing the removed list.

##### Function: CreateSubscription

```python
class Api(object):
	def CreateSubscription(self,
                           owner_screen_name=None,
                           owner_id=None,
                           list_id=None,
                           slug=None):
```

Creates a subscription to a list by the authenticated user.

###### Params
- `@owner_screen_name (str, optional)` The screen_name of the user who owns the list being requested by a slug.
- `@owner_id (int, optional)` The user ID of the user who owns the list being requested by a slug.
- `@list_id (int, optional)` The numerical id of the list.
- `@slug (str, optional)` You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the owner_id or owner_screen_name parameters.

###### Returns
- `twitter.user.User` A twitter.User instance representing the user subscribed

##### Function: DestroySubscription

```python
class Api(object):
	def DestroySubscription(self,
                            owner_screen_name=None,
                            owner_id=None,
                            list_id=None,
                            slug=None):
```

Destroys the subscription to a list for the authenticated user.

###### Params
- `@owner_screen_name (str, optional)` The screen_name of the user who owns the list being requested by a slug.
- `@owner_id (int, optional)` The user ID of the user who owns the list being requested by a slug.
- `@list_id (int, optional)` The numerical id of the list.
- `@slug (str, optional)` You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the owner_id or owner_screen_name parameters.

###### Returns
- `twitter.list.List` A twitter.List instance representing the removed list.

##### Function: ShowSubscription

```python
class Api(object):
	def ShowSubscription(self,
                         owner_screen_name=None,
                         owner_id=None,
                         list_id=None,
                         slug=None,
                         user_id=None,
                         screen_name=None,
                         include_entities=False,
                         skip_status=False):
```

Check if the specified user is a subscriber of the specified list.  Returns the user if they are subscriber.

###### Params
- `@owner_screen_name (str, optional)` The screen_name of the user who owns the list being requested by a slug.
- `@owner_id (int, optional)` The user ID of the user who owns the list being requested by a slug.
- `@list_id (int, optional)` The numerical ID of the list.
- `@slug (str, optional)` You can identify a list by its slug instead of its numerical ID. If you decide to do so, note that you'll also have to specify the list owner using the owner_id or owner_screen_name parameters.
- `@user_id (int, optional)` The user_id or a list of user_id's to add to the list. If not given, then screen_name is required.
- `@screen_name (str, optional)` The screen_name or a list of screen_name's to add to the list. If not given, then user_id is required.
- `@include_entities (bool, optional)` If False, the timeline will not contain additional metadata. Defaults to True.
- `@skip_status (bool, optional)` If True the statuses will not be returned in the user items.

###### Returns
- `twitter.user.User` A twitter.User instance representing the user requested.

##### Function: GetSubscriptions

```python
class Api(object):
	def GetSubscriptions(self,
                         user_id=None,
                         screen_name=None,
                         count=20,
                         cursor=-1):
```

Obtain a collection of the lists the specified user is subscribed to. If neither user_id or screen_name is specified, the data returned will be for the authenticated user.  The list will contain a maximum of 20 lists per page by default.  Does not include the user's own lists.

###### Params
- `@user_id (int, optional)` The ID of the user for whom to return results for.
- `@screen_name (str, optional)` The screen name of the user for whom to return results for.
- `@count (int, optional)` The amount of results to return per page. No more than 1000 results will ever be returned in a single page. Defaults to 20.
- `@cursor (int, optional)` The "page" value that Twitter will use to start building the list sequence from. Use the value of -1 to start at the beginning. Twitter will return in the result the values for next_cursor and previous_cursor.

###### Returns
- `twitter.list.List` A sequence of twitter.List instances, one for each list

##### Function: GetMemberships

```python
class Api(object):
	def GetMemberships(self,
                       user_id=None,
                       screen_name=None,
                       count=20,
                       cursor=-1,
                       filter_to_owned_lists=False):
```

Obtain the lists the specified user is a member of. If no user_id or screen_name is specified, the data returned will be for the authenticated user.  Returns a maximum of 20 lists per page by default.

###### Params
- `@user_id (int, optional)` The ID of the user for whom to return results for.
- `@screen_name (str, optional)` The screen name of the user for whom to return results for.
- `@count (int, optional)` The amount of results to return per page. No more than 1000 results will ever be returned in a single page. Defaults to 20.
- `@cursor (int, optional)` The "page" value that Twitter will use to start building the list sequence from. Use the value of -1 to start at the beginning. Twitter will return in the result the values for next_cursor and previous_cursor.
- `@filter_to_owned_lists (bool, optional)` Set to True to return only the lists the authenticating user owns, and the user specified by user_id or screen_name is a member of. Default value is False.

###### Returns
- `list` A list of twitter.List instances, one for each list in which the user specified by user_id or screen_name is a member

##### Function: GetListsList

```python
class Api(object):
	def GetListsList(self,
                     screen_name=None,
                     user_id=None,
                     reverse=False):
```

Returns all lists the user subscribes to, including their own. If no user_id or screen_name is specified, the data returned will be for the authenticated user.

###### Params
- `@screen_name (str, optional)` Specifies the screen name of the user for whom to return the user_timeline. Helpful for disambiguating when a valid screen name is also a user ID.
- `@user_id (int, optional)` Specifies the ID of the user for whom to return the user_timeline. Helpful for disambiguating when a valid user ID is also a valid screen name.
- `@reverse (bool, optional)` If False, the owned lists will be returned first, othewise subscribed lists will be at the top. Returns a maximum of 100 entries regardless. Defaults to False.

###### Returns
- `list` A sequence of twitter.List instances.

##### Function: GetListTimeline

```python
class Api(object):
	def GetListTimeline(self,
                        list_id=None,
                        slug=None,
                        owner_id=None,
                        owner_screen_name=None,
                        since_id=None,
                        max_id=None,
                        count=None,
                        include_rts=True,
                        include_entities=True):
```

Fetch the sequence of Status messages for a given List ID.

###### Params
- `@list_id (int, optional)` Specifies the ID of the list to retrieve.
- `@slug (str, optional)` The slug name for the list to retrieve. If you specify None for the list_id, then you have to provide either a owner_screen_name or owner_id.
- `@owner_id (int, optional)` Specifies the ID of the user for whom to return the list timeline. Helpful for disambiguating when a valid user ID is also a valid screen name.
- `@owner_screen_name (str, optional)` Specifies the screen name of the user for whom to return the user_timeline. Helpful for disambiguating when a valid screen name is also a user ID.
- `@since_id (int, optional)` Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available.
- `@max_id (int, optional)` Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
- `@count (int, optional)` Specifies the number of statuses to retrieve. May not be greater than 200.
- `@include_rts (bool, optional)` If True, the timeline will contain native retweets (if they exist) in addition to the standard stream of tweets.
- `@include_entities (bool, optional)` If False, the timeline will not contain additional metadata. Defaults to True.

###### Returns
- `list` A list of twitter.status.Status instances, one for each message up to count.

##### Function: GetListMembersPaged

```python
class Api(object):
	def GetListMembersPaged(self,
                            list_id=None,
                            slug=None,
                            owner_id=None,
                            owner_screen_name=None,
                            cursor=-1,
                            count=100,
                            skip_status=False,
                            include_entities=True):
```

Fetch the sequence of twitter.User instances, one for each member of the given list_id or slug.

###### Params
- `@list_id (int, optional)` Specifies the ID of the list to retrieve.
- `@slug (str, optional)` The slug name for the list to retrieve. If you specify None for the list_id, then you have to provide either a owner_screen_name or owner_id.
- `@owner_id (int, optional)` Specifies the ID of the user for whom to return the list timeline. Helpful for disambiguating when a valid user ID is also a valid screen name.
- `@owner_screen_name (str, optional)` Specifies the screen name of the user for whom to return the user_timeline. Helpful for disambiguating when a valid screen name is also a user ID.
- `@cursor (int, optional)` Should be set to -1 for the initial call and then is used to control what result page Twitter returns.
- `@skip_status (bool, optional)` If True the statuses will not be returned in the user items.
- `@include_entities (bool, optional)` If False, the timeline will not contain additional metadata. Defaults to True.

###### Returns
- `list` A sequence of twitter.user.User instances, one for each member of the twitter.list.List.

##### Function: GetListMembers

```python
class Api(object):
	def GetListMembers(self,
                       list_id=None,
                       slug=None,
                       owner_id=None,
                       owner_screen_name=None,
                       skip_status=False,
                       include_entities=False):
```

Fetch the sequence of twitter.User instances, one for each member of the given list_id or slug.

###### Params
- `@list_id (int, optional)` Specifies the ID of the list to retrieve.
- `@slug (str, optional)` The slug name for the list to retrieve. If you specify None for the list_id, then you have to provide either a owner_screen_name or owner_id.
- `@owner_id (int, optional)` Specifies the ID of the user for whom to return the list timeline. Helpful for disambiguating when a valid user ID is also a valid screen name.
- `@owner_screen_name (str, optional)` Specifies the screen name of the user for whom to return the user_timeline. Helpful for disambiguating when a valid screen name is also a user ID.
- `@skip_status (bool, optional)` If True the statuses will not be returned in the user items.
- `@include_entities (bool, optional)` If False, the timeline will not contain additional metadata. Defaults to True.

###### Returns
- `list` A sequence of twitter.user.User instances, one for each member of the twitter.list.List.

##### Function: CreateListsMember

```python
class Api(object):
	def CreateListsMember(self,
                          list_id=None,
                          slug=None,
                          user_id=None,
                          screen_name=None,
                          owner_screen_name=None,
                          owner_id=None):
```

Add a new member (or list of members) to the specified list.

###### Params
- `@list_id (int, optional)` The numerical id of the list.
- `@slug (str, optional)` You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the owner_id or owner_screen_name parameters.
- `@user_id (int, optional)` The user_id or a list of user_id's to add to the list. If not given, then screen_name is required.
- `@screen_name (str, optional)` The screen_name or a list of screen_name's to add to the list. If not given, then user_id is required.
- `@owner_screen_name (str, optional)` The screen_name of the user who owns the list being requested by a slug.
- `@owner_id (int, optional)` The user ID of the user who owns the list being requested by a slug.

###### Returns
- `twitter.list.List` A twitter.List instance representing the list subscribed to.

##### Function: DestroyListsMember

```python
class Api(object):
	def DestroyListsMember(self,
                           list_id=None,
                           slug=None,
                           owner_screen_name=None,
                           owner_id=None,
                           user_id=None,
                           screen_name=None):
```

Destroys the subscription to a list for the authenticated user.

###### Params
- `@list_id (int, optional)` The numerical id of the list.
- `@slug (str, optional)` You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the owner_id or owner_screen_name parameters.
- `@owner_screen_name (str, optional)` The screen_name of the user who owns the list being requested by a slug.
- `@owner_id (int, optional)` The user ID of the user who owns the list being requested by a slug.
- `@user_id (int, optional)` The user_id or a list of user_id's to remove from the list. If not given, then screen_name is required.
- `@screen_name (str, optional)` The screen_name or a list of Screen_name's to remove from the list. If not given, then user_id is required.

###### Returns
- `twitter.list.List` A twitter.List instance representing the removed list.

##### Function: GetListsPaged

```python
class Api(object):
	def GetListsPaged(self,
                      user_id=None,
                      screen_name=None,
                      cursor=-1,
                      count=20):
```

Fetch the sequence of lists for a user. If no user_id or screen_name is passed, the data returned will be for the authenticated user.

###### Params
- `@user_id (int, optional)` The ID of the user for whom to return results for.
- `@screen_name (str, optional)` The screen name of the user for whom to return results for.
- `@count (int, optional)` The amount of results to return per page. No more than 1000 results will ever be returned in a single page. Defaults to 20.
- `@cursor (int, optional)` The "page" value that Twitter will use to start building the list sequence from. Use the value of -1 to start at the beginning. Twitter will return in the result the values for next_cursor and previous_cursor.

###### Returns
- next_cursor (int), previous_cursor (int), list of twitter.List instances, one for each list

##### Function: GetLists

```python
class Api(object):
	def GetLists(self,
                 user_id=None,
                 screen_name=None):
```

Fetch the sequence of lists for a user. If no user_id or screen_name is passed, the data returned will be for the authenticated user.

###### Params
- `@user_id` The ID of the user for whom to return results for. [Optional]
- `@screen_name` The screen name of the user for whom to return results for. [Optional]
- `@count` The amount of results to return per page. No more than 1000 results will ever be returned in a single page. Defaults to 20. [Optional]
- `@cursor` The "page" value that Twitter will use to start building the list sequence from. Use the value of -1 to start at the beginning. Twitter will return in the result the values for next_cursor and previous_cursor. [Optional]

###### Returns
- A sequence of twitter.List instances, one for each list

##### Function: UpdateProfile

```python
class Api(object):
	def UpdateProfile(self,
                      name=None,
                      profileURL=None,
                      location=None,
                      description=None,
                      profile_link_color=None,
                      include_entities=False,
                      skip_status=False):
```

Update's the authenticated user's profile data.

###### Params
- `@name` Full name associated with the profile. Maximum of 20 characters. [Optional]
- `@profileURL` URL associated with the profile. Will be prepended with "http://" if not present. Maximum of 100 characters. [Optional]
- `@location` The city or country describing where the user of the account is located. The contents are not normalized or geocoded in any way. Maximum of 30 characters. [Optional]
- `@description` A description of the user owning the account. Maximum of 160 characters. [Optional]
- `@profile_link_color` 
- `@hex value of profile color theme. formated without '#' or '0x'. Ex` FF00FF [Optional]
- `@include_entities` The entities node will be omitted when set to False. [Optional]
- `@skip_status` When set to either True, t or 1 then statuses will not be included in the returned user objects. [Optional]

###### Returns
- A twitter.User instance representing the modified user.

##### Function: UpdateBackgroundImage

```python
class Api(object):
	def UpdateBackgroundImage(self,
                              image,
                              tile=False,
                              include_entities=False,
                              skip_status=False):
```

Deprecated function. Used to update the background of a User's Twitter profile. Removed in approx. July, 2015

##### Function: UpdateImage

```python
class Api(object):
	def UpdateImage(self,
                    image,
                    include_entities=False,
                    skip_status=False):
```

Update a User's profile image. Change may not be immediately reflected due to image processing on Twitter's side.

###### Params
- `@image (str)` Location of local image file to use.
- `@include_entities (bool, optional)` Include the entities node in the return data.
- `@skip_status (bool, optional)` Include the User's last Status in the User entity returned.

###### Returns
- `(twitter.models.User)` Updated User object.

##### Function: UpdateBanner

```python
class Api(object):
	def UpdateBanner(self,
                     image,
                     include_entities=False,
                     skip_status=False):
```

Updates the authenticated users profile banner.

###### Params
- `@image` Location of image in file system
- `@include_entities` If True, each tweet will include a node called "entities." This node offers a variety of metadata about the tweet in a
- `@discrete structure, including` user_mentions, urls, and hashtags. [Optional]

###### Returns
- A twitter.List instance representing the list subscribed to

##### Function: GetStreamSample

```python
class Api(object):
	def GetStreamSample(self, delimited=False, stall_warnings=True):
```

Returns a small sample of public statuses.

###### Params
- `@delimited` Specifies a message length. [Optional]
- `@stall_warnings` Set to True to have Twitter deliver stall warnings. [Optional]

###### Returns
- A Twitter stream

##### Function: GetStreamFilter

```python
class Api(object):
	def GetStreamFilter(self,
                        follow=None,
                        track=None,
                        locations=None,
                        languages=None,
                        delimited=None,
                        stall_warnings=None,
                        filter_level=None):
```

Returns a filtered view of public statuses.

###### Params
- `@follow` A list of user IDs to track. [Optional]
- `@track` A list of expressions to track. [Optional]
- `@locations` A list of Longitude,Latitude pairs (as strings) specifying bounding boxes for the tweets' origin. [Optional]
- `@delimited` Specifies a message length. [Optional]
- `@stall_warnings` Set to True to have Twitter deliver stall warnings. [Optional]
- `@languages` A list of Languages. Will only return Tweets that have been detected as being written in the specified languages. [Optional]
- `@filter_level` Specifies level of filtering applied to stream. Set to None, 'low' or 'medium'. [Optional]

###### Returns
- A twitter stream

##### Function: GetUserStream

```python
class Api(object):
	def GetUserStream(self,
                      replies='all',
                      withuser='user',
                      track=None,
                      locations=None,
                      delimited=None,
                      stall_warnings=None,
                      stringify_friend_ids=False,
                      filter_level=None):
```

Returns the data from the user stream.

###### Params
- `@replies` Specifies whether to return additional @replies in the stream. Defaults to 'all'.
- `@withuser` Specifies whether to return information for just the authenticating user, or include messages from accounts the user follows. [Optional]
- `@track` A list of expressions to track. [Optional]
- `@locations` A list of Latitude,Longitude pairs (as strings) specifying bounding boxes for the tweets' origin. [Optional]
- `@delimited` Specifies a message length. [Optional]
- `@stall_warnings` Set to True to have Twitter deliver stall warnings. [Optional]
- `@stringify_friend_ids` Specifies whether to send the friends list preamble as an array of integers or an array of strings. [Optional]
- `@filter_level` Specifies level of filtering applied to stream. Set to None, low or medium. [Optional]

###### Returns
- A twitter stream

##### Function: VerifyCredentials

```python
class Api(object):
	def VerifyCredentials(self, include_entities=None, skip_status=None, include_email=None):
```

Returns a twitter.User instance if the authenticating user is valid.

###### Params
- `@include_entities` Specifies whether to return additional @replies in the stream.
- `@skip_status` When set to either true, t or 1 statuses will not be included in the returned user object.
- `@include_email` Use of this parameter requires whitelisting. When set to true email will be returned in the user objects as a string. If the user does not have an email address on their account, or if the email address is un-verified, null will be returned. If your app is not whitelisted, then the 'email' key will not be present in the json response.

###### Returns
- A twitter.User instance representing that user if the credentials are valid, None otherwise.

##### Function: SetCache

```python
class Api(object):
	def SetCache(self, cache):
```

Override the default cache.  Set to None to prevent caching.

###### Params
- `@cache` An instance that supports the same API as the twitter._FileCache

##### Function: SetUrllib

```python
class Api(object):
	def SetUrllib(self, urllib):
```

Override the default urllib implementation.

###### Params
- `@urllib` An instance that supports the same API as the urllib2 module

##### Function: SetCacheTimeout

```python
class Api(object):
	def SetCacheTimeout(self, cache_timeout):
```

Override the default cache timeout.

###### Params
- `@cache_timeout` Time, in seconds, that responses should be reused.

##### Function: SetUserAgent

```python
class Api(object):
	def SetUserAgent(self, user_agent):
```

Override the default user agent.

###### Params
- `@user_agent` A string that should be send to the server as the user-agent.

##### Function: SetXTwitterHeaders

```python
class Api(object):
	def SetXTwitterHeaders(self, client, url, version):
```

Set the X-Twitter HTTP headers that will be sent to the server.

###### Params
- `@client` The client name as a string.  Will be sent to the server as the 'X-Twitter-Client' header.
- `@url` The URL of the meta.xml as a string.  Will be sent to the server as the 'X-Twitter-Client-URL' header.
- `@version` The client version as a string.  Will be sent to the server as the 'X-Twitter-Client-Version' header.

##### Function: SetSource

```python
class Api(object):
	def SetSource(self, source):
```

Suggest the "from source" value to be displayed on the Twitter web site.  The value of the 'source' parameter must be first recognized by the Twitter server.  New source values are authorized on a case by case basis by the Twitter development team.

###### Params
- `@source` The source name as a string.  Will be sent to the server as the 'source' parameter.

##### Function: InitializeRateLimit

```python
class Api(object):
	def InitializeRateLimit(self):
```

Make a call to the Twitter API to get the rate limit status for the currently authenticated user or application.

###### Returns
- None.

##### Function: CheckRateLimit

```python
class Api(object):
	def CheckRateLimit(self, url):
```

Checks a URL to see the rate limit status for that endpoint.

###### Params
- `@url (str)` URL to check against the current rate limits.

###### Returns
- `namedtuple` EndpointRateLimit namedtuple.

##### Function: _BuildUrl

```python
class Api(object):
	def _BuildUrl(self, url, path_elements=None, extra_params=None):
```

##### Function: _InitializeRequestHeaders

```python
class Api(object):
	def _InitializeRequestHeaders(self, request_headers):
```

##### Function: _InitializeUserAgent

```python
class Api(object):
	def _InitializeUserAgent(self):
```

##### Function: _InitializeDefaultParameters

```python
class Api(object):
	def _InitializeDefaultParameters(self):
```

##### Function: _DecompressGzippedResponse

```python
class Api(object):
	def _DecompressGzippedResponse(response):
```

##### Function: _EncodeParameters

```python
class Api(object):
	def _EncodeParameters(parameters):
```

Return a string in key=value&key=value form.  Values of None are not included in the output string.

###### Params
- `@parameters (dict)` dictionary of query parameters to be converted into a string for encoding and sending to Twitter.

###### Returns
- A URL-encoded string in "key=value&key=value" form

##### Function: _ParseAndCheckTwitter

```python
class Api(object):
	def _ParseAndCheckTwitter(self, json_data):
```

Try and parse the JSON returned from Twitter and return an empty dictionary if there is any error.  This is a purely defensive check because during some Twitter network outages it will return an HTML failwhale page.

##### Function: _CheckForTwitterError

```python
class Api(object):
	def _CheckForTwitterError(data):
```

Raises a TwitterError if twitter returns an error message.

###### Params
- `@data (dict)` A python dict created from the Twitter json response

###### Raises
- `(twitter.TwitterError)` TwitterError wrapping the twitter error message if one exists.

##### Function: _RequestChunkedUpload

```python
class Api(object):
	def _RequestChunkedUpload(self, url, headers, data):
```

##### Function: _RequestUrl

```python
class Api(object):
	def _RequestUrl(self, url, verb, data=None, json=None, enforce_auth=True):
```

Request a url.

###### Params
- `@url` The web location we want to retrieve.
- `@verb` Either POST or GET.
- `@data` A dict of (str, unicode) key/value pairs.

###### Returns
- A JSON object.

##### Function: _RequestStream

```python
class Api(object):
	def _RequestStream(self, url, verb, data=None):
```

Request a stream of data.

###### Params
- `@url` The web location we want to retrieve.
- `@verb` Either POST or GET.
- `@data` A dict of (str, unicode) key/value pairs.

###### Returns
- A twitter stream.

### 24 - twitter/error.py


##### Class: TwitterError

```python
class TwitterError(Exception):
```

Base class for Twitter errors

##### Function: message

```python
class TwitterError(Exception):
	def message(self):
```

Returns the first argument used to construct this error.

##### Class: PythonTwitterDeprecationWarning

```python
class PythonTwitterDeprecationWarning(DeprecationWarning):
```

Base class for python-twitter deprecation warnings

##### Class: PythonTwitterDeprecationWarning330

```python
class PythonTwitterDeprecationWarning330(PythonTwitterDeprecationWarning):
```

Warning for features to be removed in version 3.3.0

### 25 - twitter/models.py


##### Class: TwitterModel

```python
class TwitterModel(object):
```

Base class from which all twitter models will inherit.

##### Function: \_\_init\_\_

```python
class TwitterModel(object):
	def __init__(self, **kwargs):
```

##### Function: \_\_str\_\_

```python
class TwitterModel(object):
	def __str__(self):
```

Returns a string representation of TwitterModel. By default this is the same as AsJsonString().

##### Function: \_\_eq\_\_

```python
class TwitterModel(object):
	def __eq__(self, other):
```

##### Function: \_\_ne\_\_

```python
class TwitterModel(object):
	def __ne__(self, other):
```

##### Function: \_\_hash\_\_

```python
class TwitterModel(object):
	def __hash__(self):
```

##### Function: AsJsonString

```python
class TwitterModel(object):
	def AsJsonString(self):
```

Returns the TwitterModel as a JSON string based on key/value pairs returned from the AsDict() method.

##### Function: AsDict

```python
class TwitterModel(object):
	def AsDict(self):
```

Create a dictionary representation of the object. Please see inline comments on construction when dictionaries contain TwitterModels.

##### Function: NewFromJsonDict

```python
class TwitterModel(object):
	def NewFromJsonDict(cls, data, **kwargs):
```

Create a new instance based on a JSON dict. Any kwargs should be supplied by the inherited, calling class.

###### Params
- `@data` A JSON dict, as converted from the JSON in the twitter API.

##### Class: Media

```python
class Media(TwitterModel):
```

A class representing the Media component of a tweet.

##### Function: \_\_init\_\_

```python
class Media(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: \_\_repr\_\_

```python
class Media(TwitterModel):
	def __repr__(self):
```

##### Class: List

```python
class List(TwitterModel):
```

A class representing the List structure used by the twitter API.

##### Function: \_\_init\_\_

```python
class List(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: \_\_repr\_\_

```python
class List(TwitterModel):
	def __repr__(self):
```

##### Class: Category

```python
class Category(TwitterModel):
```

A class representing the suggested user category structure.

##### Function: \_\_init\_\_

```python
class Category(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: \_\_repr\_\_

```python
class Category(TwitterModel):
	def __repr__(self):
```

##### Class: DirectMessage

```python
class DirectMessage(TwitterModel):
```

A class representing a Direct Message.

##### Function: \_\_init\_\_

```python
class DirectMessage(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: \_\_repr\_\_

```python
class DirectMessage(TwitterModel):
	def __repr__(self):
```

##### Class: Trend

```python
class Trend(TwitterModel):
```

A class representing a trending topic.

##### Function: \_\_init\_\_

```python
class Trend(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: \_\_repr\_\_

```python
class Trend(TwitterModel):
	def __repr__(self):
```

##### Function: volume

```python
class Trend(TwitterModel):
	def volume(self):
```

##### Class: Hashtag

```python
class Hashtag(TwitterModel):
```

A class representing a twitter hashtag.

##### Function: \_\_init\_\_

```python
class Hashtag(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: \_\_repr\_\_

```python
class Hashtag(TwitterModel):
	def __repr__(self):
```

##### Class: Url

```python
class Url(TwitterModel):
```

A class representing an URL contained in a tweet.

##### Function: \_\_init\_\_

```python
class Url(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: \_\_repr\_\_

```python
class Url(TwitterModel):
	def __repr__(self):
```

##### Class: UserStatus

```python
class UserStatus(TwitterModel):
```

A class representing the UserStatus structure. This is an abbreviated form of the twitter.User object.

##### Function: \_\_init\_\_

```python
class UserStatus(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: \_\_repr\_\_

```python
class UserStatus(TwitterModel):
	def __repr__(self):
```

##### Class: User

```python
class User(TwitterModel):
```

A class representing the User structure.

##### Function: \_\_init\_\_

```python
class User(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: \_\_repr\_\_

```python
class User(TwitterModel):
	def __repr__(self):
```

##### Function: NewFromJsonDict

```python
class User(TwitterModel):
	def NewFromJsonDict(cls, data, **kwargs):
```

##### Class: Status

```python
class Status(TwitterModel):
```

A class representing the Status structure used by the twitter API.

##### Function: \_\_init\_\_

```python
class Status(TwitterModel):
	def __init__(self, **kwargs):
```

##### Function: created_at_in_seconds

```python
class Status(TwitterModel):
	def created_at_in_seconds(self):
```

Get the time this status message was posted, in seconds since the epoch (1 Jan 1970).

###### Returns
- `int` The time this status message was posted, in seconds since the epoch.

##### Function: \_\_repr\_\_

```python
class Status(TwitterModel):
	def __repr__(self):
```

A string representation of this twitter.Status instance. The return value is the ID of status, username and datetime.

###### Returns
- `string` A string representation of this twitter.Status instance with the ID of status, username and datetime.

##### Function: NewFromJsonDict

```python
class Status(TwitterModel):
	def NewFromJsonDict(cls, data, **kwargs):
```

Create a new instance based on a JSON dict.

###### Params
- `@data` A JSON dict, as converted from the JSON in the twitter API

###### Returns
- A twitter.Status instance

### 26 - twitter/parse_tweet.py


##### Class: Emoticons

```python
class Emoticons:
```

##### Class: ParseTweet

```python
class ParseTweet(object):
```

##### Function: \_\_init\_\_

```python
class ParseTweet(object):
	def __init__(self, timeline_owner, tweet):
```

timeline_owner : twitter handle of user account. tweet - 140 chars from feed; object does all computation on construction properties: RT, MT - boolean URLs - list of URL Hashtags - list of tags

##### Function: \_\_str\_\_

```python
class ParseTweet(object):
	def __str__(self):
```

for display method

##### Function: getAttributeEmoticon

```python
class ParseTweet(object):
	def getAttributeEmoticon(tweet):
```

see if tweet is contains any emoticons, +ve, -ve or neutral

##### Function: getAttributeRT

```python
class ParseTweet(object):
	def getAttributeRT(tweet):
```

see if tweet is a RT

##### Function: getAttributeMT

```python
class ParseTweet(object):
	def getAttributeMT(tweet):
```

see if tweet is a MT

##### Function: getUserHandles

```python
class ParseTweet(object):
	def getUserHandles(tweet):
```

given a tweet we try and extract all user handles in order of occurrence

##### Function: getHashtags

```python
class ParseTweet(object):
	def getHashtags(tweet):
```

return all hashtags

##### Function: getURLs

```python
class ParseTweet(object):
	def getURLs(tweet):
```

URL : [http://]?[\w\.?/]+

### 27 - twitter/ratelimit.py


##### Class: RateLimit

```python
class RateLimit(object):
```

Object to hold the rate limit status of various endpoints for the twitter.Api object.  This object is generally attached to the API as Api.rate_limit, but is not created until the user makes a method call that uses _RequestUrl() or calls Api.InitializeRateLimit(), after which it get created and populated with rate limit data from Twitter.  Calling Api.InitializeRateLimit() populates the object with all of the rate limits for the endpoints defined by Twitter; more info is available here:  https://dev.twitter.com/rest/public/rate-limits  https://dev.twitter.com/rest/public/rate-limiting  https://dev.twitter.com/rest/reference/get/application/rate_limit_status  Once a resource (i.e., an endpoint) has been requested, Twitter's response will contain the current rate limit status as part of the headers, i.e.::  x-rate-limit-limit x-rate-limit-remaining x-rate-limit-reset  ``limit`` is the generic limit for that endpoint, ``remaining`` is how many more times you can make a call to that endpoint, and ``reset`` is the time (in seconds since the epoch) until remaining resets to its default for that endpoint.  Generally speaking, each endpoint has a 15-minute reset time and endpoints can either make 180 or 15 requests per window. According to Twitter, any endpoint not defined in the rate limit chart or the response from a GET request to ``application/rate_limit_status.json`` should be assumed to be 15 requests per 15 minutes.

##### Function: \_\_init\_\_

```python
class RateLimit(object):
	def __init__(self, **kwargs):
```

Instantiates the RateLimitObject. Takes a json dict as kwargs and maps to the object's dictionary. So for something like:  {"resources": { "help": { /help/privacy": { "limit": 15, "remaining": 15, "reset": 1452254278 } } } }  the RateLimit object will have an attribute 'resources' from which you can perform a lookup like:  api.rate_limit.get('help').get('/help/privacy')  and a dictionary of limit, remaining, and reset will be returned.

##### Function: url_to_resource

```python
class RateLimit(object):
	def url_to_resource(url):
```

Take a fully qualified URL and attempts to return the rate limit resource family corresponding to it. For example:  >>> RateLimit.url_to_resource('https://api.twitter.com/1.1/statuses/lookup.json?id=317') >>> '/statuses/lookup'

###### Params
- `@url (str)` URL to convert to a resource family.

###### Returns
- `string` Resource family corresponding to the URL.

##### Function: set_unknown_limit

```python
class RateLimit(object):
	def set_unknown_limit(self, url, limit, remaining, reset):
```

##### Function: set_limit

```python
class RateLimit(object):
	def set_limit(self, url, limit, remaining, reset):
```

If a resource family is unknown, add it to the object's dictionary. This is to deal with new endpoints being added to the API, but not necessarily to the information returned by ``/account/rate_limit_status.json`` endpoint.  For example, if Twitter were to add an endpoint ``/puppies/lookup.json``, the RateLimit object would create a resource family ``puppies`` and add ``/puppies/lookup`` as the endpoint, along with whatever limit, remaining hits available, and reset time would be applicable to that resource+endpoint pair.

###### Params
- `@url (str)` URL of the endpoint being fetched.
- `@limit (int)` Max number of times a user or app can hit the endpoint before being rate limited.
- `@remaining (int)` Number of times a user or app can access the endpoint before being rate limited.
- `@reset (int)` Epoch time at which the rate limit window will reset.

##### Function: get_limit

```python
class RateLimit(object):
	def get_limit(self, url):
```

Gets a EndpointRateLimit object for the given url.

###### Params
- `@url (str, optional)` URL of the endpoint for which to return the rate limit status.

###### Returns
- `namedtuple` EndpointRateLimit object containing rate limit information.

### 28 - twitter/twitter_utils.py


##### Function: calc_expected_status_length

```python
def calc_expected_status_length(status, short_url_length=23):
```

Calculates the length of a tweet, taking into account Twitter's replacement of URLs with https://t.co links.

###### Params
- `@status` text of the status message to be posted.
- `@short_url_length` the current published https://t.co links

###### Returns
- Expected length of the status message as an integer.

##### Function: is_url

```python
def is_url(text):
```

Checks to see if a bit of text is a URL.

###### Params
- `@text` text to check.

###### Returns
- Boolean of whether the text should be treated as a URL or not.

##### Function: http_to_file

```python
def http_to_file(http):
```

##### Function: parse_media_file

```python
def parse_media_file(passed_media):
```

Parses a media file and attempts to return a file-like object and information about the media file.

###### Params
- `@passed_media` media file which to parse.

###### Returns
- file-like object, the filename of the media file, the file size, and the type of media.

##### Function: enf_type

```python
def enf_type(field, _type, val):
```

Checks to see if a given val for a field (i.e., the name of the field) is of the proper _type. If it is not, raises a TwitterError with a brief explanation.

###### Params
- `@field` Name of the field you are checking.
- `@_type` Type that the value should be returned as.
- `@val` Value to convert to _type.

###### Returns
- val converted to type _type.

## License
MIT
More descriptions of your license go here if any