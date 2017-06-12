import sublime
import sublime_plugin
import time

date_format = "%Y-%m-%d"            # 2013-10-02
time_format = "%H:%M:%S"            # 10:24:01
datetime_format = "%Y-%m-%d %H:%M"  # 2013-10-02 10:24
stamp_format = "%y%m%d%H%M%S"       # 131002102355


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
