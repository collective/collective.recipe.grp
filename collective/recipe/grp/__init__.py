# -*- coding: utf-8 -*-
"""Recipe grp"""

import grp
import os

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

        # Make it so recipe users can refer to ${grp:GROUP} to get the current user's group.
        # In other words, the results of `id -g -n` on UNIX systems. This can be handy in 
        # combination with the 'gocept.recipe.env' recipe, when setting ownership on the 
        # contents of a buildout, e.g. chown -R  ${env:USER}:${grp:GROUP} ${buildout:directory}
        options['GROUP'] = str(grp.getgrgid(os.getgid())[0])

    def install(self):
        """Installer"""
        # XXX Implement recipe functionality here
        
        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.
        return tuple()

    def update(self):
        """Updater"""
        pass
