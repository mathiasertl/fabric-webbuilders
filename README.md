fabric-webbuilders
==================

**fabric-webbuilders** is a collection of [Fabric](http://www.fabfile.org/) tasks to easily build
customized up-to-date versions of various HTML/JavaScript/CSS libraries. Currently supported are
[jQuery](http://jquery.com/) and [Bootstrap](http://getbootstrap.com/).

The fabfile tasks in this package are just a frontend to the "build from source" instructions of
the respective packages. This means that any command-line requirements for building the libraries
from source have to be satisfied as well.

Quickstart
----------

1. Install fabric-webbuilders:

   ```
   pip install fabric-webbuilders
   ```

2. Add tasks to your ``fabfile.py``:

   ```python
   from fabric_webbuilders import BuildJqueryTask, BuildBootstrapTask

   build_jquery = BuildJqueryTask()
   build_bootstrap = BuildBootstrapTask()
   ```

3. Start building the latest versions of jQuery and Bootstrap:

   ```
   fab build_jquery build_bootstrap
   ```

Configuration
-------------

**fabric-webbuilders** is designed to be very configurable. Every global and task-specific
configuration variable can be configured via your ``env`` dictionary, either as
``<library>_<option>`` or just ``<option>`` (the former has precedence), the tasks constructor or
via the command-line. For example, this would all configure were libraries get built:

```python
from fabric.state import env

from fabric_webbuilders import BuildJqueryTask

# global build_dir for all libraries:
env['build_dir'] = 'build/'
# just for jquery, takes precedence over above option:
env['jquery_build_dir'] = 'build/jquery/'

# overrides any env variables:
build_jquery = BuildJquery_task(build_dir='build/jquery/')
```

and then executing:

```
fab build_jquery:build_dir=build/jquery/  # overrides env and task constructor
```

The following configuration options are avialable for all tasks:

* ``build_dir``: The build-directory where the libraries are downloaded and build. The default is
  ``./<library>/`` or ``$(VIRTUALENV_DIR)/build/<library>/`` inside a virtualenv. Note that
  ``env['build_dir']`` should not contain a library name, e.g. this would both build jquery in
  ``build/jquery/``:

  ```python
  env['build_dir'] = 'build/'
  env['jquery_build_dir'] = 'build/jquery/'
  ```

* ``origin``: The default origin to download the source from. For git-based tasks (jQuery and
  Bootstrap) this is their respective official git repositories. When overriden, it follow the same
  semantics as the default, e.g. a fork of the original repository.
* ``version``: The version to build. By default the latest version found is build. 

  For git-based tasks this can be ``HEAD`` (which will build the current HEAD of the master
  branch), any treeish object (e.g.  a tag or branch found in the git-repository) or a string
  starting with ``~``, which will build the latest release mathing the version, e.g.
  ``build_jquery:version=~1`` would build the latest jQuery 1.x version.

  Note that ``env['version']`` is ignored because it's populated by fabric.
* ``dest-dir``: Where to copy the built libraries after building.


jQuery
------

**Requires:** git, npm, grunt (if ``excludes`` are given), bower (jQuery <= 2.1.1)

``fabric_webbuilders.BuildJqueryTask`` clones/updates the official git repository and builds jQuery
with ``npm run build`` or with ``grunt custom:<excludes>`` if excludes are given.

Additional options;

* ``exclude``: Excludes passed to ``grunt custom`` to exclude parts of jQuery. Note that without
  this option there really isn't much difference to just downloading the latest minified version.

Bootstrap
---------

**Requires:** git, npm, grunt

``fabric_webbuilders.BuildBootstrap`` clones/updates the official git repository and builds
Bootstrap with ``grunt dist``.

The Gruntfile unfortunately doesn't allow much automatic customization (or it's at least not
documented) so if you pass a ``config.json`` with the ``config`` parameter, the task dynamically
rewrites ``less/variables.less`` and ``less/bootstrap.less`` and removes any unwanted javascript
(as
[recommended](http://stackoverflow.com/questions/25389975/grunt-does-not-load-config-json-to-build-bootstrap)).
This works for some common cases I've tested but might break in some cases. Please don't be shy to
file an issue.

Additional options:

* ``config``: Use a ``config.json`` generated by Bootstrap's
  [customizer](http://getbootstrap.com/customize/). This may be rather fragile, see above.


ChangeLog
---------

### 0.2

* Fix ``dest_dir`` parameter for bootstrap.

### 0.1 (2014-11-30)

* initial release, featuring builders for jQuery and Bootstrap
