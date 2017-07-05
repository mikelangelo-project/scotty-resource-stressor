import logging

from scotty import utils

logger = logging.getLogger(__name__)


def result(context):
    pass

def run(context):
    workload = context.v1.workload
    experiment_helper = utils.ExperimentHelper(context)
    test_resource = experiment_helper.get_resource(workload.resources['test_resource'])
    print 'Resource ({}) loaded'.format(test_resource.name)
    print 'Resource endpoint: {}'.format(test_resource.endpoint)
