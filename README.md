# Gateiros Valheim Core

This repository publishes the version-pinned Valheim client compatibility pack
for the Gateiros server. It contains no server credentials, world data, or
private configuration.

## Release process

1. Change the approved dependency versions in `package/manifest.json`.
2. Update `package/CHANGELOG.md` and increment `version_number`.
3. Test the exact profile against the server.
4. Commit and push the changes.
5. Create and push an identical semantic-version tag, for example `0.1.0`.

The GitHub Actions workflow builds the ZIP and publishes it to Thunderstore.
It requires the `THUNDERSTORE_TOKEN` repository Actions secret, created from a
restricted Thunderstore service account belonging to the `Gaiteiros` Team.
