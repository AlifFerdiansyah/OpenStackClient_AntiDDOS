#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
from antiddosclient.common import display
from antiddosclient.common import resource
from antiddosclient.common import utils


class AntiDDos(resource.Resource, display.Display):
    """AntiDDos resource instance."""

    status_list = [
        "normal",
        "configging",
        "notConfig",
        "packetcleaning",
        "packetdropping",
    ]

    list_column_names = (
        'Floating IP id',
        'floating ip address',
        'network type',
        'status',
    )

    show_column_names = (
        'Enable L7',
        'Traffic pos id',
        'Http request pos id',
        'Cleaning access pos id',
        'App Type id'
    )

    @property
    def enable_l7(self):
        return "true" if self.enable_L7 else "false"


class AntiDDosTask(resource.Resource, display.Display):
    """AntiDDos task resource instance."""

    show_column_names = (
        'Task Status',
        'Extra Description',
    )

    @property
    def extra_description(self):
        return self.task_msg


class AntiDDosStatus(resource.Resource, display.Display):
    """AntiDDos task resource instance."""

    show_column_names = (
        'Status',
    )


class AntiDDosConfig(resource.Resource, display.Display):
    """AntiDDos configuration resource instance."""

    status_list = [
        "normal",
        "configging",
        "notConfig",
        "packetcleaning",
        "packetdropping",
    ]

    show_column_names = (
        'floating ip id',
        'floating ip address',
        'network type',
        'status',
    )


class AntiDDosDailyReport(resource.Resource, display.Display):
    """AntiDDos report(every 5min) of past 24h"""

    list_column_names = (
        'Start Time',
        'BPS In',
        'BPS Attack',
        'BPS Total',
        'PPS In',
        'PPS Attack',
        'PPS Total',
    )

    @property
    def start_time(self):
        return utils.format_time(self.period_start)


class AntiDDosLog(resource.Resource, display.Display):
    """AntiDDos log for every five minutes."""

    list_column_names = (
        'Log Start Time',
        "Log End Time",
        "AntiDDos Status",
        "Trigger BPS",
        "Trigger PPS",
        "Trigger HTTP PPS",
    )

    @property
    def log_start_time(self):
        return utils.format_time(self.start_time)

    @property
    def log_end_time(self):
        return utils.format_time(self.end_time)

    @property
    def antiddos_status(self):
        if self.status == 1:
            return 'Packet Cleaning'
        elif self.status == 2:
            return 'Packet Dropping'
        return ''


class AntiDDosWeeklyReport(resource.Resource, display.Display):
    """AntiDDos weekly summary report"""