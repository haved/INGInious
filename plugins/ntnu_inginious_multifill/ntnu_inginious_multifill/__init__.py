# -*- coding: utf-8 -*-

import os
import re
import itertools
from random import Random

from flask import send_from_directory
from inginious.common.tasks_problems import Problem
from inginious.frontend.pages.utils import INGIniousPage
from inginious.frontend.task_problems import DisplayableProblem
from inginious.frontend.parsable_text import ParsableText


__version__ = "0.1"

PATH_TO_PLUGIN = os.path.abspath(os.path.dirname(__file__))
PATH_TO_TEMPLATES = os.path.join(PATH_TO_PLUGIN, "templates")


class StaticMockPage(INGIniousPage):
    def GET(self, path):
        return send_from_directory(os.path.join(PATH_TO_PLUGIN, "static"), path)

    def POST(self, path):
        return self.GET(path)

class SubtaskString:
    """
    A string like 1;1/2,1 means always display the 1st subtask,
    then pick one of the next two subtasks, and always include the last one.
    The semicolon forces the first task to come first, while commas allow re-ordering.
    """

    def __init__(self, string):
        # Ignore whitespace
        self.string = string.replace(" ", "")

        # How many subtasks are pulled, and how many are there to pull from
        self.total_pull = 0
        self.total_bag = 0
        self.groups = []

        for loose_group in self.string.split(";"):
            loose_group_result = []
            for group in loose_group.split(","):
                try:
                    if "/" in group:
                        pull, bag = group.split("/")
                    else:
                        pull = group
                        bag = group

                    pull = int(pull)
                    bag = int(bag)
                except ValueError:
                    raise Exception(f"Subtask string contains illegal group: {self.string}")

                loose_group_result.append((pull, bag))

                self.total_pull += pull
                self.total_bag += bag

                if pull < 0:
                    raise Exception(f"Subtask string contains negative pull: {self.string}")
                if bag < 1:
                    raise Exception(f"Subtask string contains empty bag: {self.string}")
                if pull > bag:
                    raise Exception(f"Subtask string has pull > bag size: {self.string}")

            self.groups.append(loose_group_result)

    def sample_subtasks(self, task_id, seed):
        """
        Draws a list of subtasks conforming to the Subtask String.
        For a subtask string like 1;2/3, the result can for example be
        [0, 2, 1] or [0, 1, 3]
        """

        rand = Random(f"{task_id}#{seed}")

        result = []
        bag_counter = 0

        for loose_group in self.groups:
            shuffler = []
            for pull, bag in loose_group:
                this_bag = list(range(bag_counter, bag_counter + bag))
                bag_counter += bag

                shuffler.extend(rand.sample(this_bag, pull))

            rand.shuffle(shuffler)
            result.extend(shuffler)

        return result

class MultifillProblem(Problem):
    """
    A problem where the inputs are placed inline with the text using rst roles.

    The problem allows multiple subtasks, and can use a control string to display random subsets
    """
    def __init__(self, problemid, content, translations, taskfs):
        Problem.__init__(self, problemid, content, translations, taskfs)
        self._header = content.get('header', "")

        if "subtasks" not in content or not isinstance(content['subtasks'], (list, tuple)):
            raise Exception(f"Multifill problem {problemid} does not have any subtasks")

        self._subtasks = content['subtasks']
        for index, subtask in enumerate(self._subtasks):
            if "text" not in subtask:
                raise Exception(f"Subtask {index} is missing text")

        # The subtask string describes which subtasks to display.
        # The default is to display all subtasks
        # If there is only one displayed subtask, the subtask letter (a) is omitted
        self._subtask_string = None
        if content.get("subtask_string", "").strip() != "":
            self._subtask_string = SubtaskString(content["subtask_string"])

            # Check that the subtask string adds up to the correct amount of subtasks
            num_subtasks = len(self._subtasks)
            total_bag = self._subtask_string.total_bag
            if num_subtasks != total_bag:
                raise Exception(f"Problem {problemid} has {num_subtasks} subtasks, but expects to pick from {total_bag}")

    @classmethod
    def get_type(cls):
        return "multifill"

    @classmethod
    def input_type(self):
        return dict

    @classmethod
    def parse_problem(cls, problem_content):
        """
        Takes the data returned from the studio and converts it into the storage format
        """
        problem_content = Problem.parse_problem(problem_content)

        # Turn subtasks into a list, instead of a dict
        if "subtasks" in problem_content:
            subtasks = [(int(key), value) for key, value in problem_content["subtasks"].items()]
            subtasks.sort()
            subtasks = [val for _, val in subtasks]
            # Ensure all subtasks are dicts with a text field
            for subtask in subtasks:
                if "text" not in subtask:
                    subtask["text"] = ""
            problem_content["subtasks"] = subtasks

        return problem_content

    @classmethod
    def get_text_fields(cls):
        fields = Problem.get_text_fields()
        fields.update({"header": True, "subtask_string": True, "subtasks": [{"text": True}]})
        return fields

    def input_is_consistent(self, task_input, default_allowed_extension, default_max_size):
        # Check that the user submission contains everything we expect

        if self.get_id() not in task_input:
            return False
        if not isinstance(task_input[self.get_id()], dict):
            return False

        return True

    def check_answer(self, task_input, language):

        print("================ task_input =================")
        print(task_input)

        return True, None, ["MyCoolMessage"], 0, ""

class DisplayableMultifillProblem(MultifillProblem, DisplayableProblem):

    def __init__(self, problemid, content, translations, taskfs):
        MultifillProblem.__init__(self, problemid, content, translations, taskfs)

    @classmethod
    def get_type_name(self, gettext):
        return "multifill"

    def show_input(self, template_helper, language, seed):
        """ Show MultifillProblem """

        if self._header.strip() != "":
            header = ParsableText(self.gettext(language, self._header), "rst",
                                  translation=self.get_translation_obj(language))
        else:
            header = None

        if self._subtask_string is not None:
            shown_subtask_ids = self._subtask_string.sample_subtasks(self.get_id(), seed)
        else:
            # Include all subtasks
            shown_subtask_ids = list(range(len(self._subtasks)))

        # Rendered html and metadata for the template
        subtasks = []
        for visual_index, subtask_id in enumerate(shown_subtask_ids):
            subtask = { "id": subtask_id }

            if len(shown_subtask_ids) > 1:
                subtask["title"] = chr(ord("a") + visual_index) + ") "

            subtask_text = self._subtasks[subtask_id]["text"]

            INPUT_CHECK = '<input class="ntnu-inline-form-check-input" type="checkbox" name="problem[PID][subtask_string]"></input>'
            INPUT_CHECK = ':raw-html:`' + INPUT_CHECK + "`"
            subtask_text = re.sub(r':input:`[^`]*type=check[^`]*`', INPUT_CHECK, subtask_text)

            INPUT_TEXT = '<input class="ntnu-inline-form-control" type="text" name="problem[PID][subtask_string]"></input>'
            INPUT_TEXT = ':raw-html:`' + INPUT_TEXT + "`"
            subtask_text = re.sub(r':input:`[^`]*`', INPUT_TEXT, subtask_text)

            # Prefix subtask text with definition of raw-html rst role
            subtask_text = (".. role:: raw-html(raw)\n"
                            "   :format: html\n"
                            "\n") + subtask_text

            subtask_html = ParsableText(subtask_text, "rst",
                                  translation=self.get_translation_obj(language))
            subtask["html"] = subtask_html.parse()

            subtasks.append(subtask)

        return template_helper.render("tasks/multifill.html",
                template_folder=PATH_TO_TEMPLATES, inputId=self.get_id(),
                header=header, subtasks=subtasks)

    @classmethod
    def show_editbox(cls, template_helper, key, language):
        return template_helper.render("tasks/multifill_editbox.html",
                                      template_folder=PATH_TO_TEMPLATES, key=key)

    @classmethod
    def show_editbox_templates(cls, template_helper, key, language):
        return template_helper.render("tasks/multifill_editbox_templates.html",
                                      template_folder=PATH_TO_TEMPLATES, key=key)


def init(plugin_manager, course_factory, client, plugin_config):
    plugin_manager.add_page('/plugins/ntnu_inginious_multifill/static/<path:path>', StaticMockPage.as_view('multifillstaticpage'))
    plugin_manager.add_hook("css", lambda: "/plugins/ntnu_inginious_multifill/static/css/multifill.css")
    plugin_manager.add_hook("javascript_header", lambda: "/plugins/ntnu_inginious_multifill/static/js/multifill.js")
    course_factory.get_task_factory().add_problem_type(DisplayableMultifillProblem)
