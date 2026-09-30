# FelisCatus Sailfish OS Patches

Small patches for Patchmanager 3 on Sailfish OS.

Currently tested on Jolla Phone 2026 with Sailfish OS 5.2.0.17.

## Patches

### Sharp Caller Photo

Improves the Phone call screen:

- displays the caller photo without blur
- uses a clean black background
- keeps the original photo aspect ratio
- removes the large green incoming-call swipe overlay

Directory: `felis-sharp-caller-photo`

### Phone Start Page

Allows selecting which page the Phone application opens by default:

- Dialer
- History
- Contacts

The setting is available directly in Patchmanager.

After changing the default page, deactivate and activate the patch once for the new setting to take effect.

Directory: `felis-phone-start-page`

## Installation

The patches are intended for Patchmanager 3.

They can be installed manually or through the Patchmanager Web Catalog when available.

## Compatibility

Current versions are made for:

- Sailfish OS 5.2.0.17
- Jolla Phone 2026

System QML files may change between Sailfish OS releases, so compatibility should be checked after an OS update.
