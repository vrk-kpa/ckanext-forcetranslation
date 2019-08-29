=============
ckanext-forcetranslation
=============

Multilingual CKAN instances sometimes run into issues where translations
provided by extensions that conflict with each other cause missing or
incorrect translations. This can sometimes be fixed by changing the CKAN plugin
load order to match the translation priority, but if the functional dependencies
between plugins require another order, the only remaining option is to fix the
translations of the last plugin loaded that provides the conflicting translation.

This extension alleviates the issue by defining a plugin that can always be set
to be the last one in the plugin load order. Its translations therefore override
any previous translations. The plugin does not provide any translations by itself,
but is configured to provide the translations of another extension using configuration
values.

------------
Requirements
------------

Tested with CKAN 2.8.3

------------
Installation
------------

To install ckanext-forcetranslation:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-forcetranslation Python package into your virtual environment::

     pip install -e git+https://github.com/vrk-kpa/ckanext-forcetranslation.git#egg=ckanext-forcetranslation

3. Add ``forcetranslation`` to the end of ``ckan.plugins`` setting 
   and set the required variables described below in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The ckanext module to read translations from
    # (required).
    ckanext.forcetranslation.module = ckanext.ytp

    # The path under the module containing the translations
    # (optional, default='').
    ckanext.forcetranslation.path = i18n

    # The translation domain
    # (optional).
    ckanext.forcetranslation.domain

------------------------
Development Installation
------------------------

To install ckanext-forcetranslation for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/vrk-kpa/ckanext-forcetranslation.git
    cd ckanext-forcetranslation
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.forcetranslation --cover-inclusive --cover-erase --cover-tests


----------------------------------------
Copying and License
----------------------------------------

This material is copyright (c) 2019 Population Register Centre, Finland.

ckanext-forcetranslation is licensed under the GNU Affero General Public License (AGPL) v3.0
