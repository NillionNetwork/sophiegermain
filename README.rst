=============
sophiegermain
=============

Pure-Python library that provides a selection of `Sophie Germain primes <https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes>`__ that are organized by representation size.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/sophiegermain.svg
   :target: https://badge.fury.io/py/sophiegermain
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/sophiegermain/badge/?version=latest
   :target: https://sophiegermain.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/NillionNetwork/sophiegermain/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/NillionNetwork/sophiegermain/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/NillionNetwork/sophiegermain/badge.svg?branch=main
   :target: https://coveralls.io/github/NillionNetwork/sophiegermain?branch=main
   :alt: Coveralls test coverage summary.

Purpose
-------
Some cryptographic protocols involve the use of `Sophie Germain and safe primes <https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes>`__. In such cases, it is often useful to choose a Sophie Germain or safe prime based on the range of values (*i.e.*, `congruence classes of integers <https://en.wikipedia.org/wiki/Modular_arithmetic>`__ or `finite field <https://en.wikipedia.org/wiki/Finite_field>`__ elements) that an instantiation of a protocol must accommodate. This library provides immediate access to the smallest Sophie Germain prime for each possible binary representation length (up to and including 2049 bits).

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/sophiegermain>`__:

.. code-block:: bash

    python -m pip install sophiegermain

The library can be imported in the usual way:

.. code-block:: python

    import sophiegermain
    from sophiegermain import sophiegermain

This library makes it possible to retrieve instantly the smallest Sophie Germain prime that is of a given bit length (up to and including 2049 bits):

.. code-block:: python

    >>> sophiegermain(2)
    2
    >>> sophiegermain(8)
    131
    >>> sophiegermain(16)
    32771
    >>> sophiegermain(32)
    2147483693
    >>> sophiegermain(257)
    115792089237316195423570985008687907853269984665640564039457584007913129658411
    >>> sophiegermain(1025).bit_length()
    1025
    >>> sophiegermain(2049).bit_length()
    2049

Implementation
--------------

.. |isprime| replace:: ``isprime``
.. _isprime: https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.primetest.isprime

The function used to generate the collection of Sophie Germain primes made available by this library can be `found in the source code <https://sophiegermain.readthedocs.io/en/1.0.0/_modules/sophiegermain/sophiegermain.html>`__. The entries were tested using the |isprime|_ function found in the `SymPy <https://www.sympy.org/en/index.html>`__ library. This means that all values made available by this library that can be represented using 63 bits or fewer are definitively prime. For larger values, |isprime|_ relies on the `Baillie-PSW primality test <https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test>`__.

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__:

.. code-block:: bash

    python -m pip install .[docs,lint]

Documentation
^^^^^^^^^^^^^
The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__:

.. code-block:: bash

    python -m pip install .[docs]
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details):

.. code-block:: bash

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__:

.. code-block:: bash

    python src/sophiegermain/sophiegermain.py -v

Style conventions are enforced using `Pylint <https://pylint.readthedocs.io>`__:

.. code-block:: bash

    python -m pip install .[lint]
    python -m pylint src/sophiegermain

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

Ensure that the correct version number appears in ``pyproject.toml``, and that any links in this README document to the Read the Docs documentation of this package (or its dependencies) have appropriate version numbers. Also ensure that the Read the Docs project for this library has an `automation rule <https://docs.readthedocs.io/en/stable/automation-rules.html>`__ that activates and sets as the default all tagged versions. Create and push a tag for this version (replacing ``?.?.?`` with the version number):

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
