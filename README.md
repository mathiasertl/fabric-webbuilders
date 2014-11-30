fabric-webbuilders
==================

**fabric-webbuilders** is a collection of [Fabric](http://www.fabfile.org/) tasks to easily build
customized up-to-date versions of various HTML/JavaScript/CSS libraries.

Quickstart
----------

1. Install fabric-webbuilders

   ```
   pip install fabric-webbuilders
   ```

2. Add tasks to your fabfile.py

   ```
   from fabric_webbuilders import BuildJqueryTask, BuildBootstrapTask

   build_jquery = BuildJqueryTask()
   build_bootstrap = BuildBootstrapTask()
   ```

3. Start building the latest versions of JQuery and Bootstrap:

   ```
   fab build_jquery build_bootstrap
   ```
