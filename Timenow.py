import sublime
import sublime_plugin
import time
from collections import namedtuple

Settings = namedtuple('Settings', 'date_format time_format datetime_format stamp_format')

def settings():
    settings = sublime.load_settings('Timenow.sublime-settings')
    date_format = settings.get('date_format')
    time_format = settings.get('time_format')
    datetime_format = settings.get('datetime_format')
    stamp_format = settings.get('stamp_format')
    return Settings(date_format, time_format, datetime_format, stamp_format)


def time_to_view(view, edit, fmt):
    """Add time in specified format to the view"""
    for s in view.sel():
        if s.empty():
            view.insert(edit, s.a, time.strftime(fmt))
        else:
            view.replace(edit, s, time.strftime(fmt))


class tn_stampCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        time_to_view(self.view, edit, settings().stamp_format)


class tn_dateCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        time_to_view(self.view, edit, settings().date_format)


class tn_timeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        time_to_view(self.view, edit, settings().time_format)


class tn_datetimeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        time_to_view(self.view, edit, settings().datetime_format)
