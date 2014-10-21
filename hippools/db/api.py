from hippools.db import utils

__author__ = 'vfilippov'


IMPL = utils.LazyPluggable('db_backend',
                           sqlalchemy='db.sqlalchemy.api')


def get_session():
    return IMPL.get_session()


def pool_group_add(context, values):
    return IMPL.pool_group_add(context, values)


def pool_group_get_all(context):
    return IMPL.pool_group_get_all(context)


def initial_pool_add(context, values):
    return IMPL.initial_pool_add(context, values)


def initial_pool_get(context, pool_id):
    return IMPL.initial_pool_add(context, pool_id)


def initial_pool_delete(context, pool_id):
    return IMPL.initial_pool_delete(context, pool_id)


#--------------------------


def used_pool_add(context, values):
    return IMPL.used_pool_add(context, values)


def used_pool_get(context, values):
    return IMPL.used_pool_get(context, values)


def pool_delete(context, pool_id):
    return IMPL.pool_delete(context, pool_id)


# ----------------------------

def free_pool_add(context, values):
    return IMPL.free_pool_add(context, values)


def free_pool_get(context, pool_id):
    return IMPL.free_pool_get(context, pool_id)


def free_pool_find_by_netnask(context, netmask):
    return IMPL.free_pool_find_by_netnask(context, netmask)