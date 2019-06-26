from django.contrib.staticfiles.storage import CachedFilesMixin, ManifestFilesMixin
from pipeline.storage import PipelineMixin
from storages.backends.s3boto import S3BotoStorage


class S3PipelineManifestStorage(PipelineMixin, CachedFilesMixin, S3BotoStorage):
    pass
