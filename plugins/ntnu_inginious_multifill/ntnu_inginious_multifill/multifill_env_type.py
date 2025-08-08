# -*- coding: utf-8 -*-
#
# This file is mostly stolen from inginious/frontent/environment_types/mcq.py from INGIninious

from inginious.frontend.environment_types.env_type import FrontendEnvType

class MultifillEnvType(FrontendEnvType):
    @property
    def id(self):
        return "multifill"

    @property
    def name(self):
        return _("Multifill grader")

    def check_task_environment_parameters(self, data):
        return {}

    def studio_env_template(self, templator, task, allow_html):
        return ""
