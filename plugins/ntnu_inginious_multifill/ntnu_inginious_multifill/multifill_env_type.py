# -*- coding: utf-8 -*-
#
# This file is mostly stolen from inginious/frontent/environment_types/mcq.py from INGIninious

from inginious.frontend.environment_types.env_type import FrontendEnvType

from ntnu_inginious_multifill.common import PATH_TO_TEMPLATES

class MultifillEnvType(FrontendEnvType):
    @property
    def id(self):
        return "multifill"

    @property
    def name(self):
        return _("Multifill Grader")

    def check_task_environment_parameters(self, data):
        """
        This function is called when the task is loaded from disk, not when saving.
        """

        req_score = data.get('required-score', '').strip()
        try:
            if req_score != '':
                req_score = float(req_score)
        except:
            raise ValueError(f"Required score was not a number: '{req_score}'")

        return { "required-score": req_score }

    def studio_env_template(self, templator, task, allow_html):
        return templator.render("course_admin/edit_tabs/env_multifill_agent.html", template_folder=PATH_TO_TEMPLATES, env_params=task.get("environment_parameters", {}), env_id=self.id)
