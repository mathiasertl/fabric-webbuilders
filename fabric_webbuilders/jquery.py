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
from fabric.state import env

from fabric_webbuilders import BuildTask
from fabric_webbuilders import GitMixin


class BuildJquery(BuildTask, GitMixin):
    prefix = 'jquery'
    default_origin = 'https://github.com/jquery/jquery.git'

    def __init__(self, origin=None, version=None, build_dir=None, dest_dir=None, excludes=None):
        self.excludes = excludes
        super(BuildJquery, self).__init__(origin, version, build_dir, dest_dir)

    def run(self, origin=None, version=None, build_dir=None, dest_dir=None, excludes=None):
        if excludes is not None:
            self.excludes = excludes
        elif self.excludes is None:
            self.excludes = env.get('%s_excludes' % self.prefix)

        super(BuildJquery, self).run(origin, version, build_dir, dest_dir)

    def build(self):
        local('npm install')  # install dependencies

        # build jquery
        if self.excludes:
            local('grunt custom:%s' % self.excludes)
        else:
            local('npm run build')

        # copy to custom dist dir
        if self.dest_dir is not None:
            local('grunt dist:%s' % self.dest_dir)
