"""
BaseModel template for model generator
"""

TEMPLATE_ADMIN_BASEMODEL = """import logging

from django.contrib import admin

from baseapp.admin import BaseAdmin
from baseapp.utils import console

from ..models import {model_name_title}

__all__ = ['{model_name_title}Admin']

logger = logging.getLogger('app')
console = console(source=__name__)


@admin.register({model_name_title})
class {model_name_title}Admin(BaseAdmin):
    # sticky_list_filter = None
    pass

"""


__all__ = ['TEMPLATE_ADMIN_BASEMODEL']
