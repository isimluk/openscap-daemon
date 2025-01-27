#!/usr/bin/python2

# Copyright 2015 Red Hat Inc., Durham, North Carolina.
# All Rights Reserved.
#
# openscap-daemon is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.
#
# openscap-daemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with openscap-daemon.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#   Martin Preisler <mpreisle@redhat.com>

import tests.harness


class GenerateReportTest(tests.harness.APITest):
    def setup_data(self):
        super(GenerateReportTest, self).setup_data()
        self.copy_to_data("tasks/1.xml")
        #self.ensure_dir("results/1/1")
        #self.copy_to_data("results/1/1")

    def test(self):
        super(GenerateReportTest, self).test()

        self.system.load_tasks()
        assert(len(self.system.tasks) == 1)

        #print(self.system.generate_report_for_task_result(1, 1))


if __name__ == "__main__":
    GenerateReportTest.run()
