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

import os

from fabric_webbuilders import BuildJqueryTask
from fabric_webbuilders import BuildBootstrapTask
from fabric_webbuilders import MinifyCSSTask
from fabric_webbuilders import MinifyJSTask


build_jquery = BuildJqueryTask()
build_bootstrap = BuildBootstrapTask()
minify_css = MinifyCSSTask(dest=os.path.join('test', 'output.min.css'), files=(
    os.path.join('test', 'custom.css'),
    os.path.join('test', 'gone.css'),
    {
        'src_dir': os.path.join('test', 'dir'),
        'patterns': [
            '*.css',
            '!*.min.css',
            '!%sexcluded%s' % (os.sep, os.sep, ),
        ],
    }
))
minify_js = MinifyJSTask(dest=os.path.join('test', 'output.min.js'), files=(
    os.path.join('test', 'custom.js'),
    os.path.join('test', 'gone.js'),
    {
        'src_dir': os.path.join('test', 'dir'),
        'patterns': [
            '*.js',
            '!*.min.js',
            '!%sexcluded%s' % (os.sep, os.sep, ),
        ],
    }
))
