# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hou_Export.ui'
#
# Created: Mon Sep 24 19:52:39 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_wg_Export(object):
    def setupUi(self, wg_Export):
        wg_Export.setObjectName("wg_Export")
        wg_Export.resize(340, 700)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wg_Export.sizePolicy().hasHeightForWidth())
        wg_Export.setSizePolicy(sizePolicy)
        wg_Export.setMinimumSize(QtCore.QSize(340, 0))
        wg_Export.setMaximumSize(QtCore.QSize(340, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(wg_Export)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtGui.QWidget(wg_Export)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 18, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_name = QtGui.QLabel(self.widget_4)
        self.l_name.setObjectName("l_name")
        self.horizontalLayout_2.addWidget(self.l_name)
        self.e_name = QtGui.QLineEdit(self.widget_4)
        self.e_name.setMinimumSize(QtCore.QSize(0, 0))
        self.e_name.setMaximumSize(QtCore.QSize(9999, 16777215))
        self.e_name.setObjectName("e_name")
        self.horizontalLayout_2.addWidget(self.e_name)
        self.l_class = QtGui.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_class.setFont(font)
        self.l_class.setObjectName("l_class")
        self.horizontalLayout_2.addWidget(self.l_class)
        self.verticalLayout.addWidget(self.widget_4)
        self.groupBox_2 = QtGui.QGroupBox(wg_Export)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.f_taskName = QtGui.QWidget(self.groupBox_2)
        self.f_taskName.setObjectName("f_taskName")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.f_taskName)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.l_taskName = QtGui.QLabel(self.f_taskName)
        self.l_taskName.setObjectName("l_taskName")
        self.horizontalLayout_11.addWidget(self.l_taskName)
        self.l_taskName2 = QtGui.QLabel(self.f_taskName)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_taskName2.sizePolicy().hasHeightForWidth())
        self.l_taskName2.setSizePolicy(sizePolicy)
        self.l_taskName2.setText("")
        self.l_taskName2.setAlignment(QtCore.Qt.AlignCenter)
        self.l_taskName2.setObjectName("l_taskName2")
        self.horizontalLayout_11.addWidget(self.l_taskName2)
        self.b_changeTask = QtGui.QPushButton(self.f_taskName)
        self.b_changeTask.setEnabled(True)
        self.b_changeTask.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_changeTask.setObjectName("b_changeTask")
        self.horizontalLayout_11.addWidget(self.b_changeTask)
        self.verticalLayout_3.addWidget(self.f_taskName)
        self.f_frameRange = QtGui.QWidget(self.groupBox_2)
        self.f_frameRange.setObjectName("f_frameRange")
        self.horizontalLayout = QtGui.QHBoxLayout(self.f_frameRange)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.f_frameRange)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.chb_globalRange = QtGui.QCheckBox(self.f_frameRange)
        self.chb_globalRange.setChecked(True)
        self.chb_globalRange.setObjectName("chb_globalRange")
        self.horizontalLayout.addWidget(self.chb_globalRange)
        self.l_rangeStart = QtGui.QLabel(self.f_frameRange)
        self.l_rangeStart.setEnabled(False)
        self.l_rangeStart.setObjectName("l_rangeStart")
        self.horizontalLayout.addWidget(self.l_rangeStart)
        self.sp_rangeStart = QtGui.QSpinBox(self.f_frameRange)
        self.sp_rangeStart.setEnabled(False)
        self.sp_rangeStart.setMaximumSize(QtCore.QSize(55, 16777215))
        self.sp_rangeStart.setMaximum(99999)
        self.sp_rangeStart.setObjectName("sp_rangeStart")
        self.horizontalLayout.addWidget(self.sp_rangeStart)
        spacerItem1 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.l_rangeEnd = QtGui.QLabel(self.f_frameRange)
        self.l_rangeEnd.setEnabled(False)
        self.l_rangeEnd.setObjectName("l_rangeEnd")
        self.horizontalLayout.addWidget(self.l_rangeEnd)
        self.sp_rangeEnd = QtGui.QSpinBox(self.f_frameRange)
        self.sp_rangeEnd.setEnabled(False)
        self.sp_rangeEnd.setMaximumSize(QtCore.QSize(55, 16777215))
        self.sp_rangeEnd.setMaximum(99999)
        self.sp_rangeEnd.setProperty("value", 100)
        self.sp_rangeEnd.setObjectName("sp_rangeEnd")
        self.horizontalLayout.addWidget(self.sp_rangeEnd)
        self.verticalLayout_3.addWidget(self.f_frameRange)
        self.widget_6 = QtGui.QWidget(self.groupBox_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtGui.QLabel(self.widget_6)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.cb_outType = QtGui.QComboBox(self.widget_6)
        self.cb_outType.setMinimumSize(QtCore.QSize(124, 0))
        self.cb_outType.setObjectName("cb_outType")
        self.horizontalLayout_5.addWidget(self.cb_outType)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.f_cam = QtGui.QWidget(self.groupBox_2)
        self.f_cam.setObjectName("f_cam")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.f_cam)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.l_cam = QtGui.QLabel(self.f_cam)
        self.l_cam.setMinimumSize(QtCore.QSize(40, 0))
        self.l_cam.setMaximumSize(QtCore.QSize(95, 16777215))
        self.l_cam.setObjectName("l_cam")
        self.horizontalLayout_6.addWidget(self.l_cam)
        self.cb_cam = QtGui.QComboBox(self.f_cam)
        self.cb_cam.setObjectName("cb_cam")
        self.horizontalLayout_6.addWidget(self.cb_cam)
        self.verticalLayout_3.addWidget(self.f_cam)
        self.w_sCamShot = QtGui.QWidget(self.groupBox_2)
        self.w_sCamShot.setObjectName("w_sCamShot")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.w_sCamShot)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.l_sCamShot = QtGui.QLabel(self.w_sCamShot)
        self.l_sCamShot.setMinimumSize(QtCore.QSize(40, 0))
        self.l_sCamShot.setMaximumSize(QtCore.QSize(95, 16777215))
        self.l_sCamShot.setObjectName("l_sCamShot")
        self.horizontalLayout_8.addWidget(self.l_sCamShot)
        self.cb_sCamShot = QtGui.QComboBox(self.w_sCamShot)
        self.cb_sCamShot.setObjectName("cb_sCamShot")
        self.horizontalLayout_8.addWidget(self.cb_sCamShot)
        self.verticalLayout_3.addWidget(self.w_sCamShot)
        self.f_convertExport = QtGui.QWidget(self.groupBox_2)
        self.f_convertExport.setObjectName("f_convertExport")
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.f_convertExport)
        self.horizontalLayout_15.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.l_convertExport = QtGui.QLabel(self.f_convertExport)
        self.l_convertExport.setObjectName("l_convertExport")
        self.horizontalLayout_15.addWidget(self.l_convertExport)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.chb_convertExport = QtGui.QCheckBox(self.f_convertExport)
        self.chb_convertExport.setText("")
        self.chb_convertExport.setChecked(False)
        self.chb_convertExport.setObjectName("chb_convertExport")
        self.horizontalLayout_15.addWidget(self.chb_convertExport)
        self.verticalLayout_3.addWidget(self.f_convertExport)
        self.f_localOutput = QtGui.QWidget(self.groupBox_2)
        self.f_localOutput.setObjectName("f_localOutput")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.f_localOutput)
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.l_localOutput = QtGui.QLabel(self.f_localOutput)
        self.l_localOutput.setObjectName("l_localOutput")
        self.horizontalLayout_13.addWidget(self.l_localOutput)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.chb_localOutput = QtGui.QCheckBox(self.f_localOutput)
        self.chb_localOutput.setText("")
        self.chb_localOutput.setObjectName("chb_localOutput")
        self.horizontalLayout_13.addWidget(self.chb_localOutput)
        self.verticalLayout_3.addWidget(self.f_localOutput)
        self.f_status = QtGui.QWidget(self.groupBox_2)
        self.f_status.setObjectName("f_status")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.f_status)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(self.f_status)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.l_status = QtGui.QLabel(self.f_status)
        self.l_status.setAlignment(QtCore.Qt.AlignCenter)
        self.l_status.setObjectName("l_status")
        self.horizontalLayout_4.addWidget(self.l_status)
        self.b_goTo = QtGui.QPushButton(self.f_status)
        self.b_goTo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_goTo.setObjectName("b_goTo")
        self.horizontalLayout_4.addWidget(self.b_goTo)
        self.verticalLayout_3.addWidget(self.f_status)
        self.f_connect = QtGui.QWidget(self.groupBox_2)
        self.f_connect.setObjectName("f_connect")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.f_connect)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_connect = QtGui.QPushButton(self.f_connect)
        self.b_connect.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_connect.setObjectName("b_connect")
        self.horizontalLayout_3.addWidget(self.b_connect)
        self.verticalLayout_3.addWidget(self.f_connect)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gb_submit = QtGui.QGroupBox(wg_Export)
        self.gb_submit.setCheckable(True)
        self.gb_submit.setChecked(True)
        self.gb_submit.setObjectName("gb_submit")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.gb_submit)
        self.verticalLayout_7.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.f_manager = QtGui.QWidget(self.gb_submit)
        self.f_manager.setObjectName("f_manager")
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.f_manager)
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.l_manager = QtGui.QLabel(self.f_manager)
        self.l_manager.setObjectName("l_manager")
        self.horizontalLayout_17.addWidget(self.l_manager)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem5)
        self.cb_manager = QtGui.QComboBox(self.f_manager)
        self.cb_manager.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_manager.setObjectName("cb_manager")
        self.horizontalLayout_17.addWidget(self.cb_manager)
        self.verticalLayout_7.addWidget(self.f_manager)
        self.f_rjPrio = QtGui.QWidget(self.gb_submit)
        self.f_rjPrio.setObjectName("f_rjPrio")
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.f_rjPrio)
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.l_rjPrio = QtGui.QLabel(self.f_rjPrio)
        self.l_rjPrio.setObjectName("l_rjPrio")
        self.horizontalLayout_21.addWidget(self.l_rjPrio)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem6)
        self.sp_rjPrio = QtGui.QSpinBox(self.f_rjPrio)
        self.sp_rjPrio.setMaximum(100)
        self.sp_rjPrio.setProperty("value", 50)
        self.sp_rjPrio.setObjectName("sp_rjPrio")
        self.horizontalLayout_21.addWidget(self.sp_rjPrio)
        self.verticalLayout_7.addWidget(self.f_rjPrio)
        self.f_rjWidgetsPerTask = QtGui.QWidget(self.gb_submit)
        self.f_rjWidgetsPerTask.setObjectName("f_rjWidgetsPerTask")
        self.horizontalLayout_22 = QtGui.QHBoxLayout(self.f_rjWidgetsPerTask)
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_15 = QtGui.QLabel(self.f_rjWidgetsPerTask)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_22.addWidget(self.label_15)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem7)
        self.sp_rjFramesPerTask = QtGui.QSpinBox(self.f_rjWidgetsPerTask)
        self.sp_rjFramesPerTask.setMaximum(9999)
        self.sp_rjFramesPerTask.setProperty("value", 999)
        self.sp_rjFramesPerTask.setObjectName("sp_rjFramesPerTask")
        self.horizontalLayout_22.addWidget(self.sp_rjFramesPerTask)
        self.verticalLayout_7.addWidget(self.f_rjWidgetsPerTask)
        self.f_rjTimeout = QtGui.QWidget(self.gb_submit)
        self.f_rjTimeout.setObjectName("f_rjTimeout")
        self.horizontalLayout_28 = QtGui.QHBoxLayout(self.f_rjTimeout)
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.l_rjTimeout = QtGui.QLabel(self.f_rjTimeout)
        self.l_rjTimeout.setObjectName("l_rjTimeout")
        self.horizontalLayout_28.addWidget(self.l_rjTimeout)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem8)
        self.sp_rjTimeout = QtGui.QSpinBox(self.f_rjTimeout)
        self.sp_rjTimeout.setMinimum(1)
        self.sp_rjTimeout.setMaximum(9999)
        self.sp_rjTimeout.setProperty("value", 360)
        self.sp_rjTimeout.setObjectName("sp_rjTimeout")
        self.horizontalLayout_28.addWidget(self.sp_rjTimeout)
        self.verticalLayout_7.addWidget(self.f_rjTimeout)
        self.f_rjSuspended = QtGui.QWidget(self.gb_submit)
        self.f_rjSuspended.setObjectName("f_rjSuspended")
        self.horizontalLayout_26 = QtGui.QHBoxLayout(self.f_rjSuspended)
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_18 = QtGui.QLabel(self.f_rjSuspended)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_26.addWidget(self.label_18)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem9)
        self.chb_rjSuspended = QtGui.QCheckBox(self.f_rjSuspended)
        self.chb_rjSuspended.setText("")
        self.chb_rjSuspended.setChecked(False)
        self.chb_rjSuspended.setObjectName("chb_rjSuspended")
        self.horizontalLayout_26.addWidget(self.chb_rjSuspended)
        self.verticalLayout_7.addWidget(self.f_rjSuspended)
        self.f_osDependencies = QtGui.QWidget(self.gb_submit)
        self.f_osDependencies.setObjectName("f_osDependencies")
        self.horizontalLayout_27 = QtGui.QHBoxLayout(self.f_osDependencies)
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_19 = QtGui.QLabel(self.f_osDependencies)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_27.addWidget(self.label_19)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem10)
        self.chb_osDependencies = QtGui.QCheckBox(self.f_osDependencies)
        self.chb_osDependencies.setText("")
        self.chb_osDependencies.setChecked(True)
        self.chb_osDependencies.setObjectName("chb_osDependencies")
        self.horizontalLayout_27.addWidget(self.chb_osDependencies)
        self.verticalLayout_7.addWidget(self.f_osDependencies)
        self.f_osUpload = QtGui.QWidget(self.gb_submit)
        self.f_osUpload.setObjectName("f_osUpload")
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.f_osUpload)
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_16 = QtGui.QLabel(self.f_osUpload)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_23.addWidget(self.label_16)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem11)
        self.chb_osUpload = QtGui.QCheckBox(self.f_osUpload)
        self.chb_osUpload.setText("")
        self.chb_osUpload.setChecked(True)
        self.chb_osUpload.setObjectName("chb_osUpload")
        self.horizontalLayout_23.addWidget(self.chb_osUpload)
        self.verticalLayout_7.addWidget(self.f_osUpload)
        self.f_osPAssets = QtGui.QWidget(self.gb_submit)
        self.f_osPAssets.setObjectName("f_osPAssets")
        self.horizontalLayout_24 = QtGui.QHBoxLayout(self.f_osPAssets)
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_17 = QtGui.QLabel(self.f_osPAssets)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_24.addWidget(self.label_17)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem12)
        self.chb_osPAssets = QtGui.QCheckBox(self.f_osPAssets)
        self.chb_osPAssets.setText("")
        self.chb_osPAssets.setChecked(True)
        self.chb_osPAssets.setObjectName("chb_osPAssets")
        self.horizontalLayout_24.addWidget(self.chb_osPAssets)
        self.verticalLayout_7.addWidget(self.f_osPAssets)
        self.gb_osSlaves = QtGui.QGroupBox(self.gb_submit)
        self.gb_osSlaves.setObjectName("gb_osSlaves")
        self.horizontalLayout_25 = QtGui.QHBoxLayout(self.gb_osSlaves)
        self.horizontalLayout_25.setContentsMargins(9, 3, 9, 3)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.e_osSlaves = QtGui.QLineEdit(self.gb_osSlaves)
        self.e_osSlaves.setObjectName("e_osSlaves")
        self.horizontalLayout_25.addWidget(self.e_osSlaves)
        self.b_osSlaves = QtGui.QPushButton(self.gb_osSlaves)
        self.b_osSlaves.setMaximumSize(QtCore.QSize(25, 16777215))
        self.b_osSlaves.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_osSlaves.setObjectName("b_osSlaves")
        self.horizontalLayout_25.addWidget(self.b_osSlaves)
        self.verticalLayout_7.addWidget(self.gb_osSlaves)
        self.f_dlGroup = QtGui.QWidget(self.gb_submit)
        self.f_dlGroup.setObjectName("f_dlGroup")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.f_dlGroup)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtGui.QLabel(self.f_dlGroup)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.cb_dlGroup = QtGui.QComboBox(self.f_dlGroup)
        self.cb_dlGroup.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_dlGroup.setObjectName("cb_dlGroup")
        self.horizontalLayout_7.addWidget(self.cb_dlGroup)
        self.verticalLayout_7.addWidget(self.f_dlGroup)
        self.verticalLayout.addWidget(self.gb_submit)
        self.groupBox = QtGui.QGroupBox(wg_Export)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(18, -1, 18, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.l_pathLast = QtGui.QLabel(self.groupBox)
        self.l_pathLast.setObjectName("l_pathLast")
        self.verticalLayout_4.addWidget(self.l_pathLast)
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.b_openLast = QtGui.QPushButton(self.widget_2)
        self.b_openLast.setEnabled(False)
        self.b_openLast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_openLast.setObjectName("b_openLast")
        self.horizontalLayout_14.addWidget(self.b_openLast)
        self.b_copyLast = QtGui.QPushButton(self.widget_2)
        self.b_copyLast.setEnabled(False)
        self.b_copyLast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_copyLast.setObjectName("b_copyLast")
        self.horizontalLayout_14.addWidget(self.b_copyLast)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(wg_Export)
        QtCore.QMetaObject.connectSlotsByName(wg_Export)

    def retranslateUi(self, wg_Export):
        wg_Export.setWindowTitle(QtGui.QApplication.translate("wg_Export", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.l_name.setText(QtGui.QApplication.translate("wg_Export", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_class.setText(QtGui.QApplication.translate("wg_Export", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("wg_Export", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.l_taskName.setText(QtGui.QApplication.translate("wg_Export", "Taskname:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_changeTask.setText(QtGui.QApplication.translate("wg_Export", "change", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("wg_Export", "Framerange:", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_globalRange.setText(QtGui.QApplication.translate("wg_Export", "global", None, QtGui.QApplication.UnicodeUTF8))
        self.l_rangeStart.setText(QtGui.QApplication.translate("wg_Export", "from:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_rangeEnd.setText(QtGui.QApplication.translate("wg_Export", "to:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("wg_Export", "Outputtype:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_cam.setText(QtGui.QApplication.translate("wg_Export", "Camera:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_sCamShot.setText(QtGui.QApplication.translate("wg_Export", "Shot:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_convertExport.setText(QtGui.QApplication.translate("wg_Export", "Additional export in centimeters:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_localOutput.setText(QtGui.QApplication.translate("wg_Export", "Local output:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("wg_Export", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_status.setText(QtGui.QApplication.translate("wg_Export", "Not connected", None, QtGui.QApplication.UnicodeUTF8))
        self.b_goTo.setText(QtGui.QApplication.translate("wg_Export", "Go to Node", None, QtGui.QApplication.UnicodeUTF8))
        self.b_connect.setText(QtGui.QApplication.translate("wg_Export", "Connect with selected ROP Node", None, QtGui.QApplication.UnicodeUTF8))
        self.gb_submit.setTitle(QtGui.QApplication.translate("wg_Export", "Submit Render Job", None, QtGui.QApplication.UnicodeUTF8))
        self.l_manager.setText(QtGui.QApplication.translate("wg_Export", "Manager:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_rjPrio.setText(QtGui.QApplication.translate("wg_Export", "Priority:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("wg_Export", "Frames per Task:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_rjTimeout.setText(QtGui.QApplication.translate("wg_Export", "Task Timeout (min)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("wg_Export", "Submit suspended:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("wg_Export", "Submit dependent files:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("wg_Export", "Upload output:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("wg_Export", "Use Project Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.gb_osSlaves.setTitle(QtGui.QApplication.translate("wg_Export", "Assign to slaves:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_osSlaves.setText(QtGui.QApplication.translate("wg_Export", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("wg_Export", "Assign to group:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("wg_Export", "Last export", None, QtGui.QApplication.UnicodeUTF8))
        self.l_pathLast.setText(QtGui.QApplication.translate("wg_Export", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.b_openLast.setText(QtGui.QApplication.translate("wg_Export", "Open in explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.b_copyLast.setText(QtGui.QApplication.translate("wg_Export", "Copy path to clipboard", None, QtGui.QApplication.UnicodeUTF8))

