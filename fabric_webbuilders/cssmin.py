# -*- coding: utf-8 -*-
#
# This file is part of fabric-webbuilders (https://github.com/mathiasertl/fabric-webbuilders).
#
# fabric-webbuilders is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# fabric-webbuilders is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
# the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with fabric-webbuilders.
# If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from fabric.api import local

from fabric_webbuilders.base import MinifyTask


class MinifyCSSTask(MinifyTask):
    default_suffix = 'css'

    def __init__(self, files, dest, keep_line_breaks=None, s0=None, s1=None, root=None,
                 skip_import=None, skip_rebase=None, skip_advanced=None,
                 skip_aggressive_merging=None, rounding_precision=None, compatibility=None,
                 debug=None):
        self.keep_line_breaks = keep_line_breaks
        self.s0 = s0
        self.s1 = s1
        self.root = root
        self.skip_import = skip_import
        self.skip_rebase = skip_rebase
        self.skip_advanced = skip_advanced
        self.skip_aggressive_merging = skip_aggressive_merging
        self.rounding_precision = rounding_precision
        self.compatibility =  compatibility
        self.debug = debug

        super(MinifyCSSTask, self).__init__(files=files, dest=dest)

    def run(self, verbose='n', keep_line_breaks=None, s0=None, s1=None, root=None,
                 skip_import=None, skip_rebase=None, skip_advanced=None,
                 skip_aggressive_merging=None, rounding_precision=None, compatibility=None,
                 debug=None):
        if keep_line_breaks is not None:
            self.keep_line_breaks = keep_line_breaks
        if s0 is not None:
            self.s0 = s0
        if s1 is not None:
            self.s1 = s1
        if root is not None:
            self.root = root
        if skip_import is not None:
            self.skip_import = skip_import
        if skip_rebase is not None:
            self.skip_rebase = skip_rebase
        if skip_advanced is not None:
            self.skip_advanced = skip_advanced
        if skip_aggressive_merging is not None:
            self.skip_aggressive_merging = self.skip_aggressive_merging
        if rounding_precision is not None:
            self.rounding_precision = rounding_precision
        if compatibility is not None:
            self.compatibility =  compatibility
        if debug is not None:
            self.debug = debug

        super(MinifyCSSTask, self).run(verbose=verbose)

    def minify(self, files, dest):
        local('cleancss -o %s %s' % (dest, ' '.join(files)))
