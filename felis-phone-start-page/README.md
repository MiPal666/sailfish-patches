# Phone Start Page

Patchmanager patch for Sailfish OS Phone.

Allows choosing which tab is shown when the Phone application is opened.

## Available start pages

- Dialer
- History
- Contacts

Configuration is available directly from the patch entry in Patchmanager.

After changing the selected page, deactivate and activate the patch once for the change to take effect.

## How it works

Sailfish Phone normally resets the application to Call History when it is activated.

This patch replaces that behaviour with a configurable start page.

Configuration key:

`/feliscatus/phone/startPage`

Values:

- `0` — Dialer
- `1` — History
- `2` — Contacts

## Compatibility

Tested on:

- Jolla Phone 2026
- Sailfish OS 5.2.0.17
- Patchmanager 3

## Files

- `unified_diff.patch` — system QML changes
- `main.qml` — Patchmanager configuration page
- `patch.json` — Patchmanager metadata

## Version

1.0.0
