from demo.models import TestModel
from model_subscription.constants import OperationType
from model_subscription.decorators import (
    subscribe, create_subscription, unsubscribe_create,
    bulk_create_subscription, update_subscription,
    delete_subscription)


@subscribe(OperationType.CREATE, TestModel)
def handle_create_1(instance):
    print('1. Created {}'.format(instance.name))


@create_subscription(TestModel)
def handle_create_2(instance):
    print('2. Created {}'.format(instance.name))


unsubscribe_create(TestModel, handle_create_2)


@bulk_create_subscription(TestModel)
def handle_bulk_create(instances):
    for instance in instances:
        print('Bulk Created {}'.format(instance.name))

@create_subscription(TestModel)
def handle_create_1(instance):
    print('3. Created {}'.format(instance.name))


@update_subscription(TestModel)
def handle_update(instance, changed_data):
    print('Updated {}: {}'.format(instance.name, changed_data))


@delete_subscription(TestModel)
def handle_delete(instance):
    print('Deleted {}: "{}"'.format(instance.__class__.__name__, instance.name))