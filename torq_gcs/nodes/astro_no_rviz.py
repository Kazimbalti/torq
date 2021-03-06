"""
Copyright 2016, by the California Institute of Technology. ALL RIGHTS
RESERVED. United States Government Sponsorship acknowledged. Any commercial
use must be negotiated with the Office of Technology Transfer at the
California Institute of Technology.

This software may be subject to U.S. export control laws. By accepting this
software, the user agrees to comply with all applicable U.S. export laws and
regulations. User has the responsibility to obtain export licenses, or other
export authority as may be required before exporting such information to
foreign countries or providing access to foreign persons.
"""

import os
import signal
import sys

from px4_msgs.msg import PolyTraj as PolyTraj_msg

import rospkg, rospy
from python_qt_binding import loadUi
from python_qt_binding.QtGui import *
from python_qt_binding.QtCore import *
from python_qt_binding.QtWidgets import *
import torq_gcs
from torq_gcs.plan.astro_plan import QRPolyTrajGUI


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.conops_widget = Tabs(self)
        self.setCentralWidget(self.conops_widget)

class Tabs(QTabWidget):
    def __init__(self, parent=None):

        super(Tabs, self).__init__(parent)

        self.setMinimumSize(400, 800)

        global_dict = dict()

        self.rdp_gui = torq_gcs.disc.line_simpl.RDPGUI(global_dict)
        self.addTab(self.rdp_gui, "RDP")#Ramer-Douglas-Peucker discretization"

        self.astro = torq_gcs.plan.astro_plan.QRPolyTrajGUI(global_dict,defer=False,curv_func=False)
        self.addTab(self.astro, "ASTRO")

        self.esdf = torq_gcs.fsp.voxblox_widgets.ESDFGUI(global_dict)
        self.addTab(self.esdf, "ESDF")#Euclidean signed-distance field")
def main():
    app = QApplication( sys.argv )
    rospy.init_node('race_conops')
    rc = MainWindow()
    rc.show()

    return app.exec_()


if __name__=="__main__":
    sys.exit(main())
