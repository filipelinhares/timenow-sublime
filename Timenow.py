import sublime
import sublime_plugin
import time

settings = sublime.load_settings('Timenow.sublime-settings')
date_format = settings.get('date_format')
time_format = settings.get('time_format')
datetime_format = settings.get('datetime_format')
stamp_format = settings.get('stamp_format')


class tn_stampCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            self.view.replace(edit, sel, time.strftime(stamp_format))


class tn_dateCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            self.view.replace(edit, sel, time.strftime(date_format))


class tn_timeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            self.view.replace(edit, sel, time.strftime(time_format))


class tn_datetimeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            self.view.replace(edit, sel, time.strftime(datetime_format))
