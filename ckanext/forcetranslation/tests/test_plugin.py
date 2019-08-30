"""Tests for plugin.py."""
import ckanext.forcetranslation.plugin as plugin
import os


def test_plugin():
    p = plugin.ForceTranslationPlugin()

    module_name = 'ckanext.forcetranslation'
    i18n_path = 'i18n'
    domain = 'test_domain'

    p.configure({
        'ckanext.forcetranslation.module': module_name,
        'ckanext.forcetranslation.path': i18n_path,
        'ckanext.forcetranslation.domain': domain
        })

    path, should_be_i18n_path = os.path.split(p.i18n_directory())
    path, should_be_forcetranslation = os.path.split(path)
    path, should_be_ckanext = os.path.split(path)

    assert should_be_i18n_path == i18n_path
    assert should_be_forcetranslation == 'forcetranslation'
    assert should_be_ckanext == 'ckanext'
    assert p.i18n_domain() == domain
