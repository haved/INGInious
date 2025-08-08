# -*- coding: utf-8 -*-

import os

from flask import send_from_directory
from inginious.frontend.pages.utils import INGIniousPage
from inginious.frontend.environment_types import register_env_type

from .problem import MultifillProblem, DisplayableMultifillProblem
from .common import PATH_TO_STATIC
from .multifill_env_type import MultifillEnvType

__version__ = "0.1"


class StaticMockPage(INGIniousPage):
    def GET(self, path):
        return send_from_directory(PATH_TO_STATIC, path)

    def POST(self, path):
        return self.GET(path)


def init(plugin_manager, course_factory, client, plugin_config):
    plugin_manager.add_page('/plugins/ntnu_inginious_multifill/static/<path:path>', StaticMockPage.as_view('multifillstaticpage'))

    # Add css and js to every page
    plugin_manager.add_hook("css", lambda: "/plugins/ntnu_inginious_multifill/static/css/multifill.css")
    plugin_manager.add_hook("javascript_header", lambda: "/plugins/ntnu_inginious_multifill/static/js/multifill.js")

    # Add the multifill problem type to the task pages and task studio
    course_factory.get_task_factory().add_problem_type(DisplayableMultifillProblem)

    # Add the multifill grading environment type
    register_env_type(MultifillEnvType())
