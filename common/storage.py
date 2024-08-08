from whitenoise.storage import CompressedManifestStaticFilesStorage
import PAD.settings as settings


class CustomStaticFilesStorage(CompressedManifestStaticFilesStorage):
    def url(self, name, force=False):
        if name.startswith(settings.MEDIA_URL.lstrip('/')):
            return settings.MEDIA_URL + name[len(settings.MEDIA_URL.lstrip('/')):]
        return super().url(name, force)
