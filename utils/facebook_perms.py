# -*- coding: utf-8 -*-
"""A simple dict containing the permissions availabel on facebook."""


class FacebookPermissions(object):
    _user_perms = [
        'user_about_me',
        'user_activities',
        'user_birthday',
        'user_checkins',
        'user_education_history',
        'user_events',
        'user_groups',
        'user_hometown',
        'user_interests',
        'user_likes',
        'user_location',
        'user_notes',
        'user_photo_video_tags',
        'user_photos',
        'user_questions',
        'user_relationships',
        'user_relationship_details',
        'user_religion_politics',
        'user_status',
        'user_videos',
        'user_website',
        'user_work_history',
        'email',
    ]

    _friend_perms = [
        'friends_about_me',
        'friends_activities',
        'friends_birthday',
        'friends_checkins',
        'friends_education_history',
        'friends_events',
        'friends_groups',
        'friends_hometown',
        'friends_interests',
        'friends_likes',
        'friends_location',
        'friends_notes',
        'friends_photo_video_tags',
        'friends_photos',
        'friends_questions',
        'friends_relationships',
        'friends_relationship_details',
        'friends_religion_politics',
        'friends_status',
        'friends_videos',
        'friends_website',
        'friends_work_history',
    ]

    _extend_perms = [
        'read_friendlists',
        'read_insights',
        'read_mailbox',
        'read_requests',
        'read_stream',
        'xmpp_login',
        'ads_management',
        'create_event',
        'manage_friendlists',
        'manage_notifications',
        'offline_access',
        'user_online_presence',
        'friends_online_presence',
        'publish_checkins',
        'publish_stream',
        'rsvp_event',
        'publish_actions',
    ]

    def __getattr__(self, name):
        if name.startswith('list_'):
            attr = name.split('_', 1)[-1]

            try:
                return getattr(self, '_' + attr)
            except AttributeError:
                msg = u'The {0} is not a valid list of permissions.'
                raise AttributeError(msg.format(name))

        attr_in_user = name in self._user_perms
        attr_in_friend = name in self._friend_perms
        attr_in_extend = name in self._extend_perms

        try:
            assert attr_in_user or attr_in_friend or attr_in_extend
            return name
        except AssertionError:
            msg = u'The {0} is not a facebook permission.'
            raise AttributeError(msg.format(name))

    def create_scope(self, *args):
        for perm in args:
            try:
                getattr(self, perm)
            except AttributeError, e:
                raise AttributeError(e)

        return '&scope={0}'.format(','.join(args))


fb_perms = FacebookPermissions()
