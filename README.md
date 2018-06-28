# `tn` - timenow 

Sublime Text plugin to insert **timestamp**, **date**, **time** and **datetime**.

### Install
1. Open [packagecontrol.io](packagecontro.io) - (<kbd>ctrl</kbd> or <kbd>⌘</kbd>) +  <kbd>⇧</kbd> + <kbd>p</kbd>
2. Type Timenow
3. :white_check_mark: Installed!

### Usage
`Edit` ⇢ `Timenow`

![Timenow usage](media/screenshot.png)

### Custom formats
`Preferences` ⇢ `Package Settings` ⇢ `Timenow` ⇢ `Settings User`

```python
{
  "date_format":     "%Y-%m-%d",
  "time_format":     "%H:%M:%S",
  "datetime_format": "%Y-%m-%d %H:%M",
  "stamp_format":    "%y%m%d%H%M%S"
}
```

### Custom key bindings
`Preferences` ⇢ `Key Bindings`  

Add your key binding in the `Default (Windows).sublime-keymap--User` like this.

```json
[
    {"keys": ["ctrl+t"], "command": "tn_date"}
]
```
(change `ctrl` to `super` when you use OSX)

**Commands**: `tn_date`  `tn_stamp`  `tn_time`  `tn_datetime`  

### License
● **filipe** - [WTFPL](LICENSE.md)
