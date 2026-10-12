# website_slides — eLearning

Depends on: portal_rating, website, website_mail, website_profile, digest.

## `base.partner.merge.automatic.wizard` (extends)


## `digest.digest` (extends)

- `kpi_nbr_of_certified_attendees` Boolean “Certified Attendees”
- `kpi_nbr_of_certified_attendees_value` Integer (compute=_compute_kpi_nbr_of_certified_attendees_value)
- `kpi_nbr_of_new_attendees` Boolean “Attendee Registrations”
- `kpi_nbr_of_new_attendees_value` Integer (compute=_compute_kpi_nbr_of_new_attendees_value)

Extension points: `_get_kpi_custom_settings`

## `gamification.challenge` (extends)

- `challenge_category` Selection

## `gamification.karma.tracking` (extends)


Extension points: `_get_origin_selection_values`

## `mail.activity` (extends)

- `request_partner_id` Many2one → `res.partner` “Requesting Partner”

## `mail.message` (extends)


## `res.config.settings` (extends)

- `website_slide_google_app_key` Char (related=website_id.website_slide_google_app_key)
- `module_website_sale_slides` Boolean “Sell on eCommerce”
- `module_website_slides_forum` Boolean “Forum”
- `module_website_slides_survey` Boolean “Certifications”
- `module_mass_mailing_slides` Boolean “Mailing”

## `res.groups` (extends)


Public methods: `write`

## `res.partner` (extends)

- `slide_channel_ids` Many2many → `slide.channel` “eLearning Courses” (compute=_compute_slide_channel_values)
- `slide_channel_completed_ids` One2many → `slide.channel` “Completed Courses” (compute=_compute_slide_channel_values)
- `slide_channel_count` Integer “Course Count” (compute=_compute_slide_channel_values)
- `slide_channel_company_count` Integer “Company Course Count” (compute=_compute_slide_channel_company_count)

Public methods: `action_view_courses`

## `res.users` (extends)


Public methods: `create`, `get_gamification_redirection_data`, `write`

## `slide.channel` (defines)

Course

Inherits: `rating.mixin`, `mail.activity.mixin`, `image.mixin`, `website.cover_properties.mixin`, `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`, `website.structured_data.mixin`, `website.trackable.mixin`

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
- `allow_comment` Boolean “Allow rating on Course” (store, compute=_compute_allow_comment)
- `publish_template_id` Many2one → `mail.template` “New Content Notification”
- `share_channel_template_id` Many2one → `mail.template` “Channel Share Template”
- `share_slide_template_id` Many2one → `mail.template` “Share Template”
- `completed_template_id` Many2one → `mail.template` “Completion Notification”
- `enroll` Selection “Enroll Policy” (required, store, compute=_compute_enroll)
- `enroll_msg` Html “Enroll Message”
- `enroll_group_ids` Many2many → `res.groups` “Auto Enroll Groups”
- `visibility` Selection “Show Course To” (required)
- `upload_group_ids` Many2many → `res.groups` “Upload Groups”
- `website_default_background_image_url` Char “Background image URL” (compute=_compute_website_default_background_image_url)
- `channel_partner_ids` One2many → `slide.channel.partner` “Enrolled Attendees Information”
- `channel_partner_all_ids` One2many → `slide.channel.partner` “All Attendees Information”
- `members_count` Integer “# Enrolled Attendees” (compute=_compute_members_counts)
- `members_all_count` Integer “# Enrolled or Invited Attendees” (compute=_compute_members_counts)
- `members_engaged_count` Integer “# Active Attendees” (compute=_compute_members_counts)
- `members_completed_count` Integer “# Completed Attendees” (compute=_compute_members_counts)
- `members_invited_count` Integer “# Invited Attendees” (compute=_compute_members_counts)
- `partner_ids` Many2many → `res.partner` “Attendees” (compute=_compute_partners)
- `completed` Boolean “Done” (compute=_compute_user_statistics)
- `completion` Integer “Completion” (compute=_compute_user_statistics)
- `can_upload` Boolean “Can Upload” (compute=_compute_can_upload)
- `has_requested_access` Boolean “Access Requested” (compute=_compute_has_requested_access)
- `is_member` Boolean “Is Enrolled Attendee” (compute=_compute_membership_values)
- `is_member_invited` Boolean “Is Invited Attendee” (compute=_compute_membership_values)
- `is_visible` Boolean “Is Visible On Website” (compute=_compute_is_visible)
- `partner_has_new_content` Boolean (compute=_compute_partner_has_new_content)
- `karma_gen_channel_rank` Integer “Course ranked”
- `karma_gen_channel_finish` Integer “Course finished”
- `karma_review` Integer “Add Review”
- `karma_slide_comment` Integer “Add Comment”
- `karma_slide_vote` Integer “Vote”
- `can_review` Boolean “Can Review” (compute=_compute_action_rights)
- `can_comment` Boolean “Can Comment” (compute=_compute_action_rights)
- `can_vote` Boolean “Can Vote” (compute=_compute_action_rights)
- `prerequisite_channel_ids` Many2many → `slide.channel` “Prerequisites”
- `prerequisite_of_channel_ids` Many2many → `slide.channel` “Prerequisite Of”
- `prerequisite_user_has_completed` Boolean “Has Completed Prerequisite” (compute=_compute_prerequisite_user_has_completed)

Public methods: `action_archive`, `action_channel_enroll`, `action_channel_invite`, `action_grant_access`, `action_redirect_to_completed_members`, `action_redirect_to_engaged_members`, `action_redirect_to_invited_members`, `action_redirect_to_members`, `action_refuse_access`, `action_request_access`, `action_unarchive`, `action_view_ratings`, `action_view_slides`, `copy_data`, `create`, `get_backend_menu_id`, `message_post`, `unlink`, `write`

Extension points: `_action_add_members`, `_action_channel_open_invite_wizard`, `_action_request_access`, `_get_access_action`, `_get_breadcrumb_items`, `_get_can_publish_error_message`, `_get_categorized_slides`, `_get_customer_portal_message_types`, `_get_default_enroll_msg`, `_get_earned_karma`, `_get_jsonld_dict`, `_get_placeholder_filename`, `_prepare_jsonld_vals`

## `slide.channel.partner` (defines)

Channel / Partners (Members)

- `active` Boolean “Active”
- `channel_id` Many2one → `slide.channel` “Course” (required, index)
- `member_status` Selection “Attendee Status” (required, readonly)
- `completion` Integer “% Completed Contents”
- `completion_date` Datetime “Completion date” (store, compute=_compute_completion_date)
- `completed_slides_count` Integer “# Completed Contents”
- `partner_id` Many2one → `res.partner` (required, index)
- `partner_email` Char (readonly, related=partner_id.email)
- `channel_user_id` Many2one → `res.users` “Responsible” (related=channel_id.user_id)
- `channel_type` Selection (related=channel_id.channel_type)
- `channel_visibility` Selection (related=channel_id.visibility)
- `channel_enroll` Selection (related=channel_id.enroll)
- `channel_website_id` Many2one → `website` “Website” (related=channel_id.website_id)
- `next_slide_id` Many2one → `slide.slide` “Next Lesson” (compute=_compute_next_slide_id)
- `invitation_link` Char “Invitation Link” (compute=_compute_invitation_link)
- `last_invitation_date` Datetime “Last Invitation Date”

Public methods: `unlink`

Extension points: `_get_invitation_hash`, `_post_completion_update_hook`

## `slide.channel.tag.group` (defines)

Channel/Course Group

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
- `slide_id` Many2one → `slide.slide` “Content” (required, index)
- `answer_ids` One2many → `slide.answer` “Answer”
- `answers_validation_error` Char “Error on Answers” (compute=_compute_answers_validation_error)
- `attempts_count` Integer (compute=_compute_statistics)
- `attempts_avg` Float (compute=_compute_statistics)
- `done_count` Integer (compute=_compute_statistics)

Extension points: `_check_answers_integrity`

## `slide.answer` (defines)

Slide Question's Answer

- `sequence` Integer “Sequence”
- `question_id` Many2one → `slide.question` “Question” (required, index)
- `text_value` Char “Answer” (required)
- `is_correct` Boolean “Is correct answer”
- `comment` Text “Comment”

## `slide.slide` (defines)

Slide

Inherits: `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.published.mixin`, `website.searchable.mixin`, `website.structured_data.mixin`

- `name` Char “Title” (required)
- `image_1920` Image (store, compute=_compute_image_1920)
- `active` Boolean
- `sequence` Integer “Sequence”
- `user_id` Many2one → `res.users` “Uploaded by”
- `description` Html “Description”
- `channel_id` Many2one → `slide.channel` “Course” (required, index)
- `tag_ids` Many2many → `slide.tag` “Tags”
- `is_preview` Boolean “Allow Preview”
- `is_new_slide` Boolean “Is New Slide” (compute=_compute_is_new_slide)
- `completion_time` Float “Duration” (store, compute=_compute_category_completion_time)
- `is_category` Boolean “Is a category”
- `category_id` Many2one → `slide.slide` “Section” (store, compute=_compute_category_id)
- `slide_ids` One2many → `slide.slide` “Content”
- `partner_ids` Many2many → `res.partner` “Subscribers”
- `slide_partner_ids` One2many → `slide.slide.partner` “Subscribers information”
- `user_membership_id` Many2one → `slide.slide.partner` “Subscriber information” (compute=_compute_user_membership_id)
- `user_vote` Integer “User vote” (compute=_compute_user_membership_id)
- `user_has_completed` Boolean “Is Member” (compute=_compute_user_membership_id)
- `user_has_completed_category` Boolean “Is Category Completed” (compute=_compute_category_completed)
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
- `slide_icon_class` Char “Slide Icon oi-class” (compute=_compute_slide_icon_class)
- `slide_type` Selection “Slide Type” (store, compute=_compute_slide_type)
- `document_google_url` Char “Document Link” (related=url)
- `document_binary_content` Binary “PDF Content” (related=binary_content)
- `video_url` Char “Video Link” (related=url)
- `video_source_type` Selection “Video Source” (compute=_compute_video_source_type)
- `youtube_id` Char “Video YouTube ID” (compute=_compute_youtube_id)
- `vimeo_id` Char “Video Vimeo ID” (compute=_compute_vimeo_id)
- `website_id` Many2one (readonly, related=channel_id.website_id)
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

Public methods: `action_dislike`, `action_like`, `action_mark_completed`, `action_mark_uncompleted`, `action_set_viewed`, `action_view_embeds`, `copy_data`, `create`, `get_backend_menu_id`, `get_base_url`, `message_post`, `unlink`, `write`

Extension points: `_action_mark_completed`, `_action_set_quiz_done`, `_action_set_viewed`, `_action_vote`, `_get_access_action`, `_get_breadcrumb_items`, `_get_can_publish_error_message`, `_get_completion_time_pdf`, `_get_customer_portal_message_types`, `_get_jsonld_dict`, `_get_next_category`, `_get_placeholder_filename`, `_post_publication`, `_prepare_jsonld_vals`

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

## `slide.slide.resource` (defines)

Additional resource for a particular slide

- `slide_id` Many2one → `slide.slide` (required, index)
- `resource_type` Selection (required)
- `name` Char “Name” (store, compute=_compute_name)
- `data` Binary “Resource” (store, compute=_compute_reset_resources)
- `file_name` Char (store)
- `link` Char “Link” (store, compute=_compute_reset_resources)
- `download_url` Char “Download URL” (compute=_compute_download_url)
- `sequence` Integer “Sequence”

Extension points: `_check_link_type`

## `slide.tag` (defines)

Slide Tag

- `name` Char “Name” (required)

## `website` (extends)

- `website_slide_google_app_key` Char “Google Doc Key”

Public methods: `get_suggested_controllers`

Extension points: `_get_search_scopes`, `_get_settings_to_copy_onto_new_default_website`

## `website.track` (extends)

- `slide_channel_id` Many2one → `slide.channel` (readonly)

## `website.visitor` (extends)

- `visitor_slide_channel_count` Integer “Course Views” (compute=_compute_slide_channel_statistics)
- `slide_channel_ids` Many2many → `slide.channel` “Courses” (compute=_compute_slide_channel_statistics)

## `slide.channel.invite` (defines)

Channel Invitation Wizard

Inherits: `mail.composer.mixin`

- `attachment_ids` Many2many → `ir.attachment` “Attachments”
- `send_email` Boolean “Send Email” (store, compute=_compute_send_email)
- `partner_ids` Many2many → `res.partner` “Recipients”
- `channel_id` Many2one → `slide.channel` “Course” (required)
- `channel_invite_url` Char “Course Link” (compute=_compute_channel_invite_url)
- `channel_visibility` Selection (related=channel_id.visibility)
- `channel_published` Boolean (related=channel_id.is_published)
- `enroll_mode` Boolean “Enroll partners” (readonly)

Public methods: `action_invite`

Extension points: `_prepare_mail_values`
