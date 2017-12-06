import logging

logger = logging.getLogger(__name__)


def endpoint(context):
    endpoint = {'url': 'testurl'}
    return endpoint


def deploy(context):
    resource = context.v1.resource
    logger.info('Deploy resource {}'.format(resource.name))


def clean(context):
    pass
