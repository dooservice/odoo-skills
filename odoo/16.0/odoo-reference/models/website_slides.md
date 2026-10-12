# website_slides — eLearning

Depends on: portal_rating, website, website_mail, website_profile.

## `gamification.challenge` (extends)

- `challenge_category` Selection

## `ir.binary` (extends)


## `res.config.settings` (extends)

- `website_slide_google_app_key` Char (related=website_id.website_slide_google_app_key)
- `module_website_sale_slides` Boolean “Sell on eCommerce”
- `module_website_slides_forum` Boolean “Forum”
- `module_website_slides_survey` Boolean “Certifications”
- `module_mass_mailing_slides` Boolean “Mailing”

## `res.groups` (extends)


Public methods: `write`

## `res.partner` (extends)

- `slide_channel_ids` Many2many → `slide.channel` “eLearning Courses”
- `slide_channel_completed_ids` One2many → `slide.channel` “Completed Courses” (compute=_compute_slide_channel_completed_ids)
- `slide_channel_count` Integer “Course Count” (compute=_compute_slide_channel_count)
- `slide_channel_company_count` Integer “Company Course Count” (compute=_compute_slide_channel_company_count)

Public methods: `action_view_courses`

## `res.users` (extends)


Public methods: `create`, `get_gamification_redirection_data`, `write`

## `slide.channel.partner` (defines)

Channel / Partners (Members)

- `channel_id` Many2one → `slide.channel` (required, index)
- `completed` Boolean “Is Completed”
- `completion` Integer “% Completed Slides”
- `completed_slides_count` Integer “# Completed Slides”
- `partner_id` Many2one → `res.partner` (required, index)
- `partner_email` Char (readonly, related=partner_id.email)
- `channel_user_id` Many2one → `res.users` “Responsible” (related=channel_id.user_id)
- `channel_type` Selection (related=channel_id.channel_type)
- `channel_visibility` Selection (related=channel_id.visibility)
- `channel_enroll` Selection (related=channel_id.enroll)
- `channel_website_id` Many2one → `website` “Website” (related=channel_id.website_id)

Public methods: `unlink`

## `slide.channel` (defines)

Course

Inherits: `mail.thread`, `rating.mixin`, `mail.activity.mixin`, `image.mixin`, `website.cover_properties.mixin`, `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`

- `name` Char “Name” (required)
- `active` Boolean
- `description` Html “Description”
- `description_short` Html “Short Description”
- `description_html` Html “Detailed Description”
- `channel_type` Selection “Course type” (required)
- `sequence` Integer
- `user_id` Many2one → `res.users` “Responsible”
- `color` Integer “Color Index”
- `tag_ids` Many2many → `slide.channel.tag` “Tags”
- `slide_ids` One2many → `slide.slide` “Slides and categories”
- `slide_content_ids` One2many → `slide.slide` “Content” (compute=_compute_category_and_slide_ids)
- `slide_category_ids` One2many → `slide.slide` “Categories” (compute=_compute_category_and_slide_ids)
- `slide_last_update` Date “Last Update” (store, compute=_compute_slide_last_update)
- `slide_partner_ids` One2many → `slide.slide.partner` “Slide User Data”
- `promote_strategy` Selection “Featured Content”
- `promoted_slide_id` Many2one → `slide.slide` “Promoted Slide”
- `access_token` Char “Security Token”
- `nbr_document` Integer “Documents” (store, compute=_compute_slides_statistics)
- `nbr_video` Integer “Videos” (store, compute=_compute_slides_statistics)
- `nbr_infographic` Integer “Infographics” (store, compute=_compute_slides_statistics)
- `nbr_article` Integer “Articles” (store, compute=_compute_slides_statistics)
- `nbr_quiz` Integer “Number of Quizs” (store, compute=_compute_slides_statistics)
- `total_slides` Integer “Number of Contents” (store, compute=_compute_slides_statistics)
- `total_views` Integer “Visits” (store, compute=_compute_slides_statistics)
- `total_votes` Integer “Votes” (store, compute=_compute_slides_statistics)
- `total_time` Float “Duration” (store, compute=_compute_slides_statistics)
- `rating_avg_stars` Float “Rating Average (Stars)” (compute=_compute_rating_stats)
- `allow_comment` Boolean “Allow rating on Course”
- `publish_template_id` Many2one → `mail.template` “New Content Notification”
- `share_channel_template_id` Many2one → `mail.template` “Channel Share Template”
- `share_slide_template_id` Many2one → `mail.template` “Share Template”
- `completed_template_id` Many2one → `mail.template` “Completion Notification”
- `enroll` Selection “Enroll Policy” (required)
- `enroll_msg` Html “Enroll Message”
- `enroll_group_ids` Many2many → `res.groups` “Auto Enroll Groups”
- `visibility` Selection “Visibility” (required)
- `partner_ids` Many2many → `res.partner` “Members”
- `members_count` Integer “Attendees count” (compute=_compute_members_count)
- `members_done_count` Integer “Attendees Done Count” (compute=_compute_members_done_count)
- `has_requested_access` Boolean “Access Requested” (compute=_compute_has_requested_access)
- `is_member` Boolean “Is Member” (compute=_compute_is_member)
- `channel_partner_ids` One2many → `slide.channel.partner` “Members Information”
- `upload_group_ids` Many2many → `res.groups` “Upload Groups”
- `website_background_image_url` Char “Background image URL” (compute=_compute_website_background_image_url)
- `completed` Boolean “Done” (compute=_compute_user_statistics)
- `completion` Integer “Completion” (compute=_compute_user_statistics)
- `can_upload` Boolean “Can Upload” (compute=_compute_can_upload)
- `partner_has_new_content` Boolean (compute=_compute_partner_has_new_content)
- `karma_gen_slide_vote` Integer “Lesson voted”
- `karma_gen_channel_rank` Integer “Course ranked”
- `karma_gen_channel_finish` Integer “Course finished”
- `karma_review` Integer “Add Review”
- `karma_slide_comment` Integer “Add Comment”
- `karma_slide_vote` Integer “Vote”
- `can_review` Boolean “Can Review” (compute=_compute_action_rights)
- `can_comment` Boolean “Can Comment” (compute=_compute_action_rights)
- `can_vote` Boolean “Can Vote” (compute=_compute_action_rights)

Public methods: `action_add_member`, `action_channel_invite`, `action_grant_access`, `action_redirect_to_done_members`, `action_redirect_to_members`, `action_refuse_access`, `action_request_access`, `action_view_ratings`, `action_view_slides`, `copy_data`, `create`, `get_backend_menu_id`, `message_post`, `open_website_url`, `toggle_active`, `write`

Extension points: `_action_add_members`, `_action_request_access`, `_get_can_publish_error_message`, `_get_categorized_slides`, `_get_default_enroll_msg`, `_get_earned_karma`, `_get_placeholder_filename`

## `slide.channel.tag.group` (defines)

Channel/Course Groups

Inherits: `website.published.mixin`

- `name` Char “Group Name” (required)
- `sequence` Integer “Sequence” (required, index)
- `tag_ids` One2many → `slide.channel.tag` “Tags”

## `slide.channel.tag` (defines)

Channel/Course Tag

- `name` Char “Name” (required)
- `sequence` Integer “Sequence” (required, index)
- `group_id` Many2one → `slide.channel.tag.group` “Group” (required, index)
- `group_sequence` Integer “Group sequence” (readonly, store, index, related=group_id.sequence)
- `channel_ids` Many2many → `slide.channel` “Channels”
- `color` Integer “Color Index”

## `slide.embed` (defines)

Embedded Slides View Counter

- `slide_id` Many2one → `slide.slide` “Presentation” (required, index)
- `url` Char “Third Party Website URL”
- `website_name` Char “Website” (compute=_compute_website_name)
- `count_views` Integer “# Views”

## `slide.question` (defines)

Content Quiz Question

- `sequence` Integer “Sequence”
- `question` Char “Question Name” (required)
- `slide_id` Many2one → `slide.slide` “Content” (required)
- `answer_ids` One2many → `slide.answer` “Answer”
- `attempts_count` Integer (compute=_compute_statistics)
- `attempts_avg` Float (compute=_compute_statistics)
- `done_count` Integer (compute=_compute_statistics)

Extension points: `_check_answers_integrity`

## `slide.answer` (defines)

Slide Question's Answer

- `sequence` Integer “Sequence”
- `question_id` Many2one → `slide.question` “Question” (required)
- `text_value` Char “Answer” (required)
- `is_correct` Boolean “Is correct answer”
- `comment` Text “Comment”

## `slide.slide.partner` (defines)

Slide / Partner decorated m2m

- `slide_id` Many2one → `slide.slide` “Content” (required, index)
- `slide_category` Selection (related=slide_id.slide_category)
- `channel_id` Many2one → `slide.channel` “Channel” (store, index, related=slide_id.channel_id)
- `partner_id` Many2one → `res.partner` (required, index)
- `vote` Integer “Vote”
- `completed` Boolean “Completed”
- `quiz_attempts_count` Integer “Quiz attempts count”

Public methods: `create`, `write`

## `slide.tag` (defines)

Slide Tag

- `name` Char “Name” (required)

## `slide.slide` (defines)

Slides

Inherits: `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.published.mixin`, `website.searchable.mixin`

- `name` Char “Title” (required)
- `image_1920` Image (store, compute=_compute_image_1920)
- `active` Boolean
- `sequence` Integer “Sequence”
- `user_id` Many2one → `res.users` “Uploaded by”
- `description` Html “Description”
- `channel_id` Many2one → `slide.channel` “Course” (required)
- `tag_ids` Many2many → `slide.tag` “Tags”
- `is_preview` Boolean “Allow Preview”
- `is_new_slide` Boolean “Is New Slide” (compute=_compute_is_new_slide)
- `completion_time` Float “Duration”
- `is_category` Boolean “Is a category”
- `category_id` Many2one → `slide.slide` “Section” (store, compute=_compute_category_id)
- `slide_ids` One2many → `slide.slide` “Content”
- `partner_ids` Many2many → `res.partner` “Subscribers”
- `slide_partner_ids` One2many → `slide.slide.partner` “Subscribers information”
- `user_membership_id` Many2one → `slide.slide.partner` “Subscriber information” (compute=_compute_user_membership_id)
- `user_vote` Integer “User vote” (compute=_compute_user_membership_id)
- `user_has_completed` Boolean “Is Member” (compute=_compute_user_membership_id)
- `question_ids` One2many → `slide.question` “Questions”
- `questions_count` Integer “Numbers of Questions” (compute=_compute_questions_count)
- `quiz_first_attempt_reward` Integer “Reward: first attempt”
- `quiz_second_attempt_reward` Integer “Reward: second attempt”
- `quiz_third_attempt_reward` Integer “Reward: third attempt”
- `quiz_fourth_attempt_reward` Integer “Reward: every attempt after the third try”
- `can_self_mark_completed` Boolean “Can Mark Completed” (compute=_compute_mark_complete_actions)
- `can_self_mark_uncompleted` Boolean “Can Mark Uncompleted” (compute=_compute_mark_complete_actions)
- `slide_category` Selection “Category” (required)
- `source_type` Selection (required)
- `url` Char “External URL”
- `binary_content` Binary “File”
- `slide_resource_ids` One2many → `slide.slide.resource` “Additional Resource for this slide”
- `slide_resource_downloadable` Boolean “Allow Download”
- `google_drive_id` Char “Google Drive ID of the external URL” (compute=_compute_google_drive_id)
- `html_content` Html “HTML Content”
- `image_binary_content` Binary “Image Content” (related=binary_content)
- `image_google_url` Char “Image Link” (related=url)
- `slide_type` Selection “Slide Type” (store, compute=_compute_slide_type)
- `document_google_url` Char “Document Link” (related=url)
- `document_binary_content` Binary “PDF Content” (related=binary_content)
- `video_url` Char “Video Link” (related=url)
- `video_source_type` Selection “Video Source” (compute=_compute_video_source_type)
- `youtube_id` Char “Video YouTube ID” (compute=_compute_youtube_id)
- `vimeo_id` Char “Video Vimeo ID” (compute=_compute_vimeo_id)
- `website_id` Many2one (readonly, related=channel_id.website_id)
- `date_published` Datetime “Publish Date” (readonly)
- `likes` Integer “Likes” (store, compute=_compute_like_info)
- `dislikes` Integer “Dislikes” (store, compute=_compute_like_info)
- `embed_code` Html “Embed Code” (readonly, compute=_compute_embed_code)
- `embed_code_external` Html “External Embed Code” (readonly, compute=_compute_embed_code)
- `website_share_url` Char “Share URL” (compute=_compute_website_share_url)
- `embed_ids` One2many → `slide.embed` “External Slide Embeds”
- `embed_count` Integer “# of Embeds” (compute=_compute_embed_counts)
- `slide_views` Integer “# of Website Views” (store, compute=_compute_slide_views)
- `public_views` Integer “# of Public Views” (readonly)
- `total_views` Integer “# Total Views” (store, compute=_compute_total)
- `comments_count` Integer “Number of comments” (compute=_compute_comments_count)
- `channel_type` Selection “Channel type” (related=channel_id.channel_type)
- `channel_allow_comment` Boolean “Allows comment” (related=channel_id.allow_comment)
- `nbr_document` Integer “Number of Documents” (store, compute=_compute_slides_statistics)
- `nbr_video` Integer “Number of Videos” (store, compute=_compute_slides_statistics)
- `nbr_infographic` Integer “Number of Images” (store, compute=_compute_slides_statistics)
- `nbr_article` Integer “Number of Articles” (store, compute=_compute_slides_statistics)
- `nbr_quiz` Integer “Number of Quizs” (store, compute=_compute_slides_statistics)
- `total_slides` Integer (store, compute=_compute_slides_statistics)
- `is_published` Boolean
- `website_published` Boolean

Public methods: `action_dislike`, `action_like`, `action_mark_completed`, `action_mark_uncompleted`, `action_set_viewed`, `action_view_embeds`, `copy`, `create`, `get_backend_menu_id`, `message_post`, `open_website_url`, `toggle_active`, `unlink`, `write`

Extension points: `_action_mark_completed`, `_action_set_quiz_done`, `_action_set_viewed`, `_action_vote`, `_get_access_action`, `_get_can_publish_error_message`, `_get_completion_time_pdf`, `_post_publication`

## `slide.slide.resource` (defines)

Additional resource for a particular slide

- `slide_id` Many2one → `slide.slide` (required)
- `resource_type` Selection (required)
- `name` Char “Name” (store, compute=_compute_name)
- `data` Binary “Resource” (store, compute=_compute_reset_resources)
- `file_name` Char (store)
- `link` Char “Link” (store, compute=_compute_reset_resources)

Extension points: `_check_link_type`, `_get_download_url`

## `website` (extends)

- `website_slide_google_app_key` Char “Google Doc Key”

Public methods: `get_suggested_controllers`

## `slide.channel.invite` (defines)

Channel Invitation Wizard

Inherits: `mail.composer.mixin`

- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `partner_ids` Many2many → `res.partner` “Recipients”
- `channel_id` Many2one → `slide.channel` “Slide channel” (required)

Public methods: `action_invite`

Extension points: `_prepare_mail_values`
