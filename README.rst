=============
sophiegermain
=============

Pure-Python library that provides a selection of `Sophie Germain primes <https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes>`__.

|pypi|

.. |pypi| image:: https://badge.fury.io/py/sophiegermain.svg
   :target: https://badge.fury.io/py/sophiegermain
   :alt: PyPI version and link.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/sophiegermain>`__:

.. code-block:: bash

    python -m pip install sophiegermain

The library can be imported in the usual way:

.. code-block:: python

    import sophiegermain
    from sophiegermain import sophiegermain

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks.

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/sophiegermain>`__ for this library.

Versioning
^^^^^^^^^^
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/sophiegermain>`__ by a package maintainer. First, install the dependencies required for packaging and publishing:

.. code-block:: bash

    python -m pip install .[publish]

Ensure that the correct version number appears in ``pyproject.toml``, and that any links in this README document have appropriate version numbers. Create and push a tag for this version (replacing ``?.?.?`` with the version number):

.. code-block:: bash

    git tag ?.?.?
    git push origin ?.?.?

Remove any old build/distribution files. Then, package the source into a distribution archive:

.. code-block:: bash

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__:

.. code-block:: bash

    python -m twine upload dist/*
