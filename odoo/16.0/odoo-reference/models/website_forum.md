# website_forum — Forum

Depends on: auth_signup, website_mail, website_profile.

## `forum.forum` (defines)

Forum

Inherits: `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.multi.mixin`, `website.searchable.mixin`

- `name` Char “Forum Name” (required)
- `sequence` Integer “Sequence”
- `mode` Selection “Mode” (required)
- `privacy` Selection
- `authorized_group_id` Many2one → `res.groups`
- `menu_id` Many2one → `website.menu`
- `active` Boolean
- `faq` Html “Guidelines”
- `description` Text “Description”
- `teaser` Text “Teaser” (store, compute=_compute_teaser)
- `welcome_message` Html “Welcome Message”
- `default_order` Selection “Default” (required)
- `relevancy_post_vote` Float “First Relevance Parameter”
- `relevancy_time_decay` Float “Second Relevance Parameter”
- `allow_bump` Boolean “Allow Bump”
- `allow_share` Boolean “Sharing Options”
- `post_ids` One2many → `forum.post` “Posts”
- `last_post_id` Many2one → `forum.post` (compute=_compute_last_post)
- `total_posts` Integer “# Posts” (compute=_compute_forum_statistics)
- `total_views` Integer “# Views” (compute=_compute_forum_statistics)
- `total_answers` Integer “# Answers” (compute=_compute_forum_statistics)
- `total_favorites` Integer “# Favorites” (compute=_compute_forum_statistics)
- `count_posts_waiting_validation` Integer “Number of posts waiting for validation” (compute=_compute_count_posts_waiting_validation)
- `count_flagged_posts` Integer “Number of flagged posts” (compute=_compute_count_flagged_posts)
- `karma_gen_question_new` Integer “Asking a question”
- `karma_gen_question_upvote` Integer “Question upvoted”
- `karma_gen_question_downvote` Integer “Question downvoted”
- `karma_gen_answer_upvote` Integer “Answer upvoted”
- `karma_gen_answer_downvote` Integer “Answer downvoted”
- `karma_gen_answer_accept` Integer “Accepting an answer”
- `karma_gen_answer_accepted` Integer “Answer accepted”
- `karma_gen_answer_flagged` Integer “Answer flagged”
- `karma_ask` Integer “Ask questions”
- `karma_answer` Integer “Answer questions”
- `karma_edit_own` Integer “Edit own posts”
- `karma_edit_all` Integer “Edit all posts”
- `karma_edit_retag` Integer “Change question tags”
- `karma_close_own` Integer “Close own posts”
- `karma_close_all` Integer “Close all posts”
- `karma_unlink_own` Integer “Delete own posts”
- `karma_unlink_all` Integer “Delete all posts”
- `karma_tag_create` Integer “Create new tags”
- `karma_upvote` Integer “Upvote”
- `karma_downvote` Integer “Downvote”
- `karma_answer_accept_own` Integer “Accept an answer on own questions”
- `karma_answer_accept_all` Integer “Accept an answer to all questions”
- `karma_comment_own` Integer “Comment own posts”
- `karma_comment_all` Integer “Comment all posts”
- `karma_comment_convert_own` Integer “Convert own answers to comments and vice versa”
- `karma_comment_convert_all` Integer “Convert all answers to comments and vice versa”
- `karma_comment_unlink_own` Integer “Unlink own comments”
- `karma_comment_unlink_all` Integer “Unlink all comments”
- `karma_flag` Integer “Flag a post as offensive”
- `karma_dofollow` Integer “Nofollow links”
- `karma_editor` Integer “Editor Features: image and links”
- `karma_user_bio` Integer “Display detailed user biography”
- `karma_post` Integer “Ask questions without validation”
- `karma_moderate` Integer “Moderate posts”

Public methods: `create`, `get_tags_first_char`, `go_to_website`, `unlink`, `write`

## `forum.post` (defines)

Forum Post

Inherits: `mail.thread`, `website.seo.metadata`, `website.searchable.mixin`

- `name` Char “Title”
- `forum_id` Many2one → `forum.forum` “Forum” (required)
- `content` Html “Content”
- `plain_content` Text “Plain Content” (store, compute=_get_plain_content)
- `tag_ids` Many2many → `forum.tag` “Tags”
- `state` Selection “Status”
- `views` Integer “Views” (readonly)
- `active` Boolean “Active”
- `website_message_ids` One2many
- `website_url` Char “Website URL” (compute=_compute_website_url)
- `website_id` Many2one (readonly, related=forum_id.website_id)
- `create_date` Datetime “Asked on” (readonly, index)
- `create_uid` Many2one → `res.users` “Created by” (readonly, index)
- `write_date` Datetime “Updated on” (readonly, index)
- `bump_date` Datetime “Bumped on” (readonly)
- `write_uid` Many2one → `res.users` “Updated by” (readonly, index)
- `relevancy` Float “Relevance” (store, compute=_compute_relevancy)
- `vote_ids` One2many → `forum.post.vote` “Votes”
- `user_vote` Integer “My Vote” (compute=_get_user_vote)
- `vote_count` Integer “Total Votes” (store, compute=_get_vote_count)
- `favourite_ids` Many2many → `res.users` “Favourite”
- `user_favourite` Boolean “Is Favourite” (compute=_get_user_favourite)
- `favourite_count` Integer “Favorite” (store, compute=_get_favorite_count)
- `is_correct` Boolean “Correct”
- `parent_id` Many2one → `forum.post` “Question” (readonly, index)
- `self_reply` Boolean “Reply to own question” (store, compute=_is_self_reply)
- `child_ids` One2many → `forum.post` “Post Answers”
- `child_count` Integer “Answers” (store, compute=_get_child_count)
- `uid_has_answered` Boolean “Has Answered” (compute=_get_uid_has_answered)
- `has_validated_answer` Boolean “Is answered” (store, compute=_get_has_validated_answer)
- `flag_user_id` Many2one → `res.users` “Flagged by”
- `moderator_id` Many2one → `res.users` “Reviewed by” (readonly)
- `closed_reason_id` Many2one → `forum.post.reason` “Reason”
- `closed_uid` Many2one → `res.users` “Closed by” (readonly)
- `closed_date` Datetime “Closed on” (readonly)
- `karma_accept` Integer “Convert comment to answer” (compute=_get_post_karma_rights)
- `karma_edit` Integer “Karma to edit” (compute=_get_post_karma_rights)
- `karma_close` Integer “Karma to close” (compute=_get_post_karma_rights)
- `karma_unlink` Integer “Karma to unlink” (compute=_get_post_karma_rights)
- `karma_comment` Integer “Karma to comment” (compute=_get_post_karma_rights)
- `karma_comment_convert` Integer “Karma to convert comment to answer” (compute=_get_post_karma_rights)
- `karma_flag` Integer “Flag a post as offensive” (compute=_get_post_karma_rights)
- `can_ask` Boolean “Can Ask” (compute=_get_post_karma_rights)
- `can_answer` Boolean “Can Answer” (compute=_get_post_karma_rights)
- `can_accept` Boolean “Can Accept” (compute=_get_post_karma_rights)
- `can_edit` Boolean “Can Edit” (compute=_get_post_karma_rights)
- `can_close` Boolean “Can Close” (compute=_get_post_karma_rights)
- `can_unlink` Boolean “Can Unlink” (compute=_get_post_karma_rights)
- `can_upvote` Boolean “Can Upvote” (compute=_get_post_karma_rights)
- `can_downvote` Boolean “Can Downvote” (compute=_get_post_karma_rights)
- `can_comment` Boolean “Can Comment” (compute=_get_post_karma_rights)
- `can_comment_convert` Boolean “Can Convert to Comment” (compute=_get_post_karma_rights)
- `can_view` Boolean “Can View” (compute=_get_post_karma_rights)
- `can_display_biography` Boolean “Is the author's biography visible from his post” (compute=_get_post_karma_rights)
- `can_post` Boolean “Can Automatically be Validated” (compute=_get_post_karma_rights)
- `can_flag` Boolean “Can Flag” (compute=_get_post_karma_rights)
- `can_moderate` Boolean “Can Moderate” (compute=_get_post_karma_rights)
- `can_use_full_editor` Boolean (compute=_get_post_karma_rights)

Public methods: `bump`, `close`, `convert_answer_to_comment`, `convert_comment_to_answer`, `create`, `flag`, `go_to_website`, `mark_as_offensive`, `mark_as_offensive_batch`, `message_post`, `post_notification`, `refuse`, `reopen`, `unlink`, `unlink_comment`, `validate`, `vote`, `write`

Extension points: `_check_parent_id`, `_get_access_action`, `_get_child_count`, `_get_favorite_count`, `_get_has_validated_answer`, `_get_mail_message_access`, `_get_plain_content`, `_get_post_karma_rights`, `_get_uid_has_answered`, `_get_user_favourite`, `_get_user_vote`, `_get_vote_count`

## `forum.post.reason` (defines)

Post Closing Reason

- `name` Char “Closing Reason” (required)
- `reason_type` Selection “Reason Type”

## `forum.post.vote` (defines)

Post Vote

- `post_id` Many2one → `forum.post` “Post” (required)
- `user_id` Many2one → `res.users` “User” (required)
- `vote` Selection “Vote” (required)
- `create_date` Datetime “Create Date” (readonly, index)
- `forum_id` Many2one → `forum.forum` “Forum” (store, related=post_id.forum_id)
- `recipient_id` Many2one → `res.users` “To” (store, related=post_id.create_uid)

Public methods: `create`, `write`

Extension points: `_check_general_rights`, `_check_karma_rights`, `_get_karma_value`

## `forum.tag` (defines)

Forum Tag

Inherits: `mail.thread`, `website.seo.metadata`

- `name` Char “Name” (required)
- `forum_id` Many2one → `forum.forum` “Forum” (required)
- `post_ids` Many2many → `forum.post` “Posts”
- `posts_count` Integer “Number of Posts” (store, compute=_get_posts_count)

Public methods: `create`

Extension points: `_get_posts_count`

## `gamification.challenge` (extends)

- `challenge_category` Selection

## `ir.attachment` (extends)


## `res.users` (extends)

- `create_date` Datetime “Create Date” (readonly, index)
- `forum_waiting_posts_count` Integer “Waiting post” (compute=_get_user_waiting_post)

Public methods: `get_gamification_redirection_data`, `open_website_url`

Extension points: `_get_user_waiting_post`

## `website` (extends)

- `forums_count` Integer (readonly)

Public methods: `configurator_get_footer_links`, `configurator_set_menu_links`, `get_default_forum_count`, `get_suggested_controllers`
