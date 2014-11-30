fabric-webbuilders
==================

**fabric-webbuilders** is a collection of [Fabric](http://www.fabfile.org/) tasks to easily build
customized up-to-date versions of various HTML/JavaScript/CSS libraries. Currently supported are
[JQuery](http://jquery.com/) and [Bootstrap](http://getbootstrap.com/).

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

3. Start building the latest versions of JQuery and Bootstrap:

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
env['jquery_build_dir'] = 'build/'

# overrides any env variables:
build_jquery = BuildJquery_task(build_dir='build/')
```

and then executing:

```
fab build_jquery:build_dir=build/  # overrides env and task constructor
```

JQuery
------

**Requires:** git, npm, grunt, bower (JQuery <= 2.1.1)

Bootstrap
---------

**Requires:** git, npm, grunt
