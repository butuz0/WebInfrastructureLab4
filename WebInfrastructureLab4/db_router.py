class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'mongodb_app':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'mongodb_app':
            return 'mongodb'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'mongodb_app':
            return db == 'mongodb'
        return db == 'default'
