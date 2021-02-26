# Copyright (c) 2021 Autodesk, Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Autodesk, Inc.

import sgtk
from sgtk.platform.qt import QtCore, QtGui
from tank.util import sgre as re

HookClass = sgtk.get_hook_baseclass()


class ViewConfiguration(HookClass):
    """
    Hook to define how the list view data is displayed.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """

        super(ViewConfiguration, self).__init__(*args, **kwargs)

    def get_item_title(self, item, sg_data):
        """
        """

        template_str = None

        if sg_data:
            item_def = self.parent.execute_hook_method(
                "shotgun_fields_hook",
                "get_list_item_definition",
                entity_type=sg_data["type"],
            )
            template_str = item_def.get("top_left", "")

        return (template_str, sg_data)

    def get_item_subtitle(self, item, sg_data):
        """
        """

        template_str = None

        if sg_data:
            item_def = self.parent.execute_hook_method(
                "shotgun_fields_hook",
                "get_list_item_definition",
                entity_type=sg_data["type"],
            )
            template_str = item_def.get("top_right", "")

        return (template_str, sg_data)

    def get_item_details(self, item, sg_data):
        """
        Returns the details data to display for this model index item.

        :return: The details data.
        :rtype: list
        """

        template_str = None

        if sg_data:
            item_def = self.parent.execute_hook_method(
                "shotgun_fields_hook",
                "get_list_item_definition",
                entity_type=sg_data["type"],
            )
            template_str = item_def.get("body", "")

        return (template_str, sg_data)

    def get_item_short_text(self, item, sg_data):
        """
        Returns the short text data to display for this model index item.

        :return: The details data.
        :rtype: list
        """

        template_str = None
        # if is_folder:
        #     # delegate_publish_list format_folder

        #     # NOTE for simplicity at the moment, this does not handle getting the
        #     # data from SG_ASSOCIATED_FIELD_ROLE

        #     if sg_data:
        #         template_str = (
        #             "<b>%s</b><br/>"
        #             "{type::showtype}"
        #         ) % display

        if sg_data:
            # delegate_publish_list format_publish

            # NOTE does not support "show subfolders mode"

            template_str = (
                "<b>{name|Unnamed} {[(]task::nolink[)]}</b><br/>"
                "<small>{published_file_type::nolink}</small>"
            )

        return (template_str, sg_data)
