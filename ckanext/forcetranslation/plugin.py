import os
import ckan.plugins as plugins
from ckan.lib.plugins import DefaultTranslation
import importlib


class ForceTranslationPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurable)

    def configure(self, config):
        self.module_name = config.get('ckanext.forcetranslation.module')

        if self.module_name is None:
            raise Exception("Config option ckanext.forcetranslation.module must be set to use forcetranslation")

        self.path = config.get('ckanext.forcetranslation.path', '')
        self.domain = config.get('ckanext.forcetranslation.domain')

        if self.module_name:
            module = importlib.import_module(self.module_name)
            module_path = module.__path__[0]
            self.translation_path = os.path.join(module_path, self.path)

    def i18n_directory(self):
        return self.translation_path

    def i18n_domain(self):
        return self.domain or super(ForceTranslationPlugin, self).i18n_domain()
