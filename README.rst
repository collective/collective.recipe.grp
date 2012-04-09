Introduction
*************

This is a one line recipe to allow buildout users to refer to ``${grp:GROUP}`` to obtain the current user's UNIX group id.  In other words, the results of::

    $ id -g -n

on UNIX systems, for the user executing the buildout. This can be used with `gocept.recipe.env`_ and `plone.recipe.command` to configure ownership of the buildout directory, e.g.::

    [env]
    recipe = gocept.recipe.env

    [grp]
    recipe = collective.recipe.grp

    [chown]
    recipe = plone.recipe.command
    command = chown -R  ${env:USER}:${grp:GROUP} ${buildout:directory}

.. _gocept.recipe.env: http://pythonpackages.com/package/gocept.recipe.env
.. _plone.recipe.command: http://pythonpackages.com/package/plone.recipe.command
