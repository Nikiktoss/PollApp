from django.contrib import admin
from .models import *


admin.site.site_header = 'PollsApp Administration'
admin.site.site_title = 'PollsApp Administration'


class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'date_publish', 'last_modified', 'is_active')
    ordering = ('-last_modified', 'title')
    list_display_links = ('id', 'title')
    list_editable = ('is_active',)
    list_filter = ('owner', 'date_publish', 'is_active')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'poll')


class VoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote, VoteAdmin)
