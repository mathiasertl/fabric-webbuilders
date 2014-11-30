# -*- coding: utf-8 -*-
#
# This file is part of fabric-web-builder (https://github.com/mathiasertl/fabric-web-builder).
#
# fabric-web-builder is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# fabric-web-builder is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
# the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with fabric-web-builder.
# If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from fabric_webbuilders.jquery import BuildJqueryTask
from fabric_webbuilders.bootstrap import BuildBootstrapTask


build_jquery = BuildJqueryTask()
build_bootstrap = BuildBootstrapTask()
