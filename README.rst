======
skisolr
======

.. image:: https://img.shields.io/travis/django-searchstack/skisolr/master.svg?style=flat-square  
   :target: https://travis-ci.org/django-searchstack/skisolr?branch=master
.. image:: https://img.shields.io/coveralls/django-searchstack/skisolr/master.svg?style=flat-square
   :target: https://coveralls.io/github/django-searchstack/skisolr?branch=master

``skisolr`` is a lightweight Python wrapper for `Apache Solr`_. It provides an
interface that queries the server and returns results based on the query. It's a fork of pysolr and 
is mainly intended to serve as internal dependency for `Django-Searchstack`_. Therefore, not much 
guarantees are provided regarding API stability at the moment.

.. _`Apache Solr`: http://lucene.apache.org/solr/
.. _`Django-Searchstack`: http://github.com/django-searchstack/django-searchstack/


Features
========

* Basic operations such as selecting, updating & deleting.
* Index optimization.
* `"More Like This" <http://wiki.apache.org/solr/MoreLikeThis>`_ support (if set up in Solr).
* `Spelling correction <http://wiki.apache.org/solr/SpellCheckComponent>`_ (if set up in Solr).
* Timeout support.
* Core administration.


Requirements
============

* Python 2.7 - 3.5
* Requests 2.0+
* **Optional** - ``simplejson``


Installation
============

``sudo python setup.py install`` or drop the ``pysolr.py`` file anywhere on your
PYTHONPATH.


Usage
=====

Basic usage looks like:

.. code-block:: python

    # If on Python 2.X
    from __future__ import print_function
    import pysolr

    # Setup a Solr instance. The timeout is optional.
    solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)

    # How you'd index data.
    solr.add([
        {
            "id": "doc_1",
            "title": "A test document",
        },
        {
            "id": "doc_2",
            "title": "The Banana: Tasty or Dangerous?",
        },
    ])

    # Later, searching is easy. In the simple case, just a plain Lucene-style
    # query is fine.
    results = solr.search('bananas')

    # The ``Results`` object stores total results found, by default the top
    # ten most relevant results and any additional data like
    # facets/highlighting/spelling/etc.
    print("Saw {0} result(s).".format(len(results)))

    # Just loop over it to access the results.
    for result in results:
        print("The title is '{0}'.".format(result['title']))

    # For a more advanced query, say involving highlighting, you can pass
    # additional options to Solr.
    results = solr.search('bananas', **{
        'hl': 'true',
        'hl.fragsize': 10,
    })

    # You can also perform More Like This searches, if your Solr is configured
    # correctly.
    similar = solr.more_like_this(q='id:doc_2', mltfl='text')

    # Finally, you can delete either individual documents...
    solr.delete(id='doc_1')

    # ...or all documents.
    solr.delete(q='*:*')


LICENSE
=======

``skisolr`` is licensed under the New BSD license.


Running Tests
=============

Running a test Solr instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Downloading, configuring and running Solr 4 looks like this::

    tests/start-solr-test-server.sh

Running the tests
~~~~~~~~~~~~~~~~~

The test suite requires the nose library::

    python setup.py nosetests
