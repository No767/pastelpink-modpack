=====================
Packaging the Modpack
=====================

Pastelpink's client-side modpack is packaged using `Packwiz <https://packwiz.infra.link/>`_.
As Packwiz is primarily built in `Go <https://go.dev/>`_, the way that I have installed it
is by using the nightly.link or compiling it and installing it.

Packwiz will be primarly used to package the modpack. All you need to do is to go to the root
of the repo, and just run ``packwiz modrinth export``. That's it. The auto-publishing workflows
are internally based off of `Rodhaj <https://github.com/transprogrammer/rodhaj/blob/main/.github/workflows/release.yml>`_.