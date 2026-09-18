# Gateiros Valheim Core

This package is the compatibility baseline for the Gateiros Valheim server.
The complete dependency set was tested in a clean r2modman profile and used to
join the server successfully on 18 September 2026.

It does not contain the server address, password, world data, Discord webhook,
or any player-specific client-only mods.

## Player use

Install this modpack into a dedicated `Gateiros` r2modman profile. Players may
then add their own client-only UI, visual, or accessibility mods. Do not use a
shared r2modman profile code to update an existing personal profile: that
operation replaces the profile.

## Compatibility testing

The clean-profile test verified that r2modman resolves the Longship Upgrades
dependency chain to the required Conditional Config Sync `1.0.8`.

No `BepInEx/config` files are included in this draft. Add only configurations
that are required by the server; never package personal UI, keybind, or visual
settings.
