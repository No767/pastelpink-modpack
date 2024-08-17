=============================
Installation (Prism Launcher)
=============================

This method is one out of the two recommended ways to install this modpack. In short,
this launcher allows for custom installations to be easily distributed and installed.

Prerequisites
=============

You will need to have these installed or to be able to
access these:

- `Prism Launcher <https://prismlauncher.org/>`_
- Java 21 or higher (Adoptium JDK is recommended)
- Valid Minecraft Account (Java Edition)

.. note::

    If you need to install Java 21, it is recommended to use a vendor
    such as `Adoptium <https://adoptium.net/>`_ or `Amazon Corretto <https://aws.amazon.com/corretto/>`_.

    *Technically* `GraalVM <https://www.graalvm.org/>`_ works, but it has been shown to be unstable
    with Minecraft.

Step 1 - Download the required files
====================================

In order to use the modpack, we first need to download the files. The download is here:
https://github.com/No767/pastelpink-modpack/releases/latest/download/Pastelpink-0.1.0.mrpack. 
Save it into your downloads folder (or where you usually download stuff). 

If you prefer the more technical method, use the following command listed below:

.. code-block:: bash

    curl -o Pastelpink.mrpack https://github.com/No767/pastelpink-modpack/releases/latest/download/Pastelpink-0.1.0.mrpack

Step 2 - Navigating to Prism Launcher
=====================================

Once you have the file, open up "Prism Launcher" within your computer. It should like this:

.. image:: /_static/prism_home.png

I will note that this is my personal instance of Prism Launcher, but yours should be entirely
blank. 

Step 3 - Installing the modpack
===============================

On the top left of the launcher, click on the "Add Instance" button. Once you click on this button,
it brings up a screen to create the instance. The modpack needs to be imported, thus you would need to
find the "Import" option within the selection of platforms and navigate to it.

.. image:: /_static/prism_create.png

Once this is done, you can either click the "Browse" button and find the modpack that you just downloaded
(file extension is ``.mrpack``), directly insert the download link. Click on the "OK" button to continue,
and you should see it download the modpack and set everything up.

You should now see a new instance, which should be named "Pastelpink-0.1.0". Clicking on the icon selects
the instance, and there should be a "Launch button"

.. image:: /_static/prism_launch.png

Once you launch the instance, that should be it! The modpack is ready to go, and anytime
you want to play on the server, all you need to do is to open up Prism Launcher and launch
that instance.
