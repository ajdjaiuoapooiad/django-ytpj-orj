from django.contrib import admin

from channel.models import Channel, Community, CommunityComment

admin.site.register(Channel)
admin.site.register(Community)
admin.site.register(CommunityComment)