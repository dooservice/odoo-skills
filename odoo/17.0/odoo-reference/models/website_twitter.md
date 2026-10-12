# website_twitter — Twitter Snippet

Depends on: website.

## `res.config.settings` (extends)

- `twitter_api_key` Char “API Key” (related=website_id.twitter_api_key)
- `twitter_api_secret` Char “API secret” (related=website_id.twitter_api_secret)
- `twitter_screen_name` Char “Favorites From” (related=website_id.twitter_screen_name)
- `twitter_server_uri` Char “Twitter server uri” (readonly)

Public methods: `create`, `get_values`, `write`

Extension points: `_check_twitter_authorization`, `_get_twitter_exception_message`

## `website` (extends)

- `twitter_api_key` Char “Twitter API key”
- `twitter_api_secret` Char “Twitter API secret”
- `twitter_screen_name` Char “Get favorites from this screen name”

Public methods: `fetch_favorite_tweets`

Extension points: `_get_access_token`

## `website.twitter.tweet` (defines)

Website Twitter

- `website_id` Many2one → `website` “Website”
- `screen_name` Char “Screen Name”
- `tweet` Text “Tweets”
- `tweet_id` Float “Tweet ID”
