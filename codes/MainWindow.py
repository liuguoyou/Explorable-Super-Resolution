# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


def ReturnSizePolicy(policy,hasHeightForWidth):
    sizePolicy = QtWidgets.QSizePolicy(policy, policy)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(hasHeightForWidth)
    return sizePolicy


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(10,10)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Maximum,self.centralWidget.sizePolicy().hasHeightForWidth()))
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Maximum,self.widget.sizePolicy().hasHeightForWidth()))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.selectrectButton = QtWidgets.QPushButton(self.widget)
        self.selectrectButton.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Fixed,self.selectrectButton.sizePolicy().hasHeightForWidth()))
        self.selectrectButton.setMinimumSize(QtCore.QSize(30, 30))
        self.selectrectButton.setMaximumSize(QtCore.QSize(30, 30))
        self.selectrectButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/selection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectrectButton.setIcon(icon2)
        self.selectrectButton.setCheckable(True)
        self.selectrectButton.setObjectName("selectrectButton")
        self.gridLayout.addWidget(self.selectrectButton, 0, 1, 1, 1)

        self.selectpolyButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectpolyButton.sizePolicy().hasHeightForWidth())
        self.selectpolyButton.setSizePolicy(sizePolicy)
        self.selectpolyButton.setMinimumSize(QtCore.QSize(30, 30))
        self.selectpolyButton.setMaximumSize(QtCore.QSize(30, 30))
        self.selectpolyButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/selection-poly.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectpolyButton.setIcon(icon6)
        self.selectpolyButton.setCheckable(True)
        self.selectpolyButton.setObjectName("selectpolyButton")
        self.gridLayout.addWidget(self.selectpolyButton, 0, 0, 1, 1)

        self.UnselectButton = QtWidgets.QPushButton(self.widget)
        self.UnselectButton.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Fixed,self.UnselectButton.sizePolicy().hasHeightForWidth()))
        self.UnselectButton.setMinimumSize(QtCore.QSize(30, 30))
        self.UnselectButton.setMaximumSize(QtCore.QSize(30, 30))
        self.UnselectButton.setText("")
        icon6_0 = QtGui.QIcon()
        icon6_0.addPixmap(QtGui.QPixmap("images/unselect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UnselectButton.setIcon(icon6_0)
        self.UnselectButton.setCheckable(False)
        self.UnselectButton.setObjectName("UnselectButton")
        self.gridLayout.addWidget(self.UnselectButton,3,1, 1, 1)

        self.invertSelectionButton = QtWidgets.QPushButton(self.widget)
        self.invertSelectionButton.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Fixed,self.invertSelectionButton.sizePolicy().hasHeightForWidth()))
        self.invertSelectionButton.setMinimumSize(QtCore.QSize(30, 30))
        self.invertSelectionButton.setMaximumSize(QtCore.QSize(30, 30))
        self.invertSelectionButton.setText("")
        icon6_0 = QtGui.QIcon()
        icon6_0.addPixmap(QtGui.QPixmap("images/invertSelection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.invertSelectionButton.setIcon(icon6_0)
        self.invertSelectionButton.setCheckable(False)
        self.invertSelectionButton.setObjectName("invertSelectionButton")
        self.gridLayout.addWidget(self.invertSelectionButton,4,1, 1, 1)

        self.uniformZButton = QtWidgets.QPushButton(self.widget)
        self.uniformZButton.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Fixed,self.uniformZButton.sizePolicy().hasHeightForWidth()))
        self.uniformZButton.setMinimumSize(QtCore.QSize(30, 30))
        self.uniformZButton.setMaximumSize(QtCore.QSize(30, 30))
        self.uniformZButton.setText("")
        icon6_0 = QtGui.QIcon()
        icon6_0.addPixmap(QtGui.QPixmap("images/uniform_Z.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uniformZButton.setIcon(icon6_0)
        self.uniformZButton.setCheckable(False)
        self.uniformZButton.setObjectName("uniformZButton")
        self.gridLayout.addWidget(self.uniformZButton,5,1, 1, 1)

        self.desiredImageHistModeButton = QtWidgets.QPushButton(self.widget)
        self.desiredImageHistModeButton.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Fixed,self.desiredImageHistModeButton.sizePolicy().hasHeightForWidth()))
        self.desiredImageHistModeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.desiredImageHistModeButton.setMaximumSize(QtCore.QSize(30, 30))
        self.desiredImageHistModeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/image_hist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.desiredImageHistModeButton.setIcon(icon4)
        self.desiredImageHistModeButton.setCheckable(True)
        self.desiredImageHistModeButton.setObjectName("desiredImageHistModeButton")
        self.gridLayout.addWidget(self.desiredImageHistModeButton, 4, 0, 1, 1)

        self.desiredHistModeButton = QtWidgets.QPushButton(self.widget)
        self.desiredHistModeButton.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Fixed,self.desiredHistModeButton.sizePolicy().hasHeightForWidth()))
        self.desiredHistModeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.desiredHistModeButton.setMaximumSize(QtCore.QSize(30, 30))
        self.desiredHistModeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/hist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.desiredHistModeButton.setIcon(icon4)
        self.desiredHistModeButton.setCheckable(True)
        self.desiredHistModeButton.setObjectName("desiredHistModeButton")
        self.gridLayout.addWidget(self.desiredHistModeButton, 5, 0, 1, 1)

        self.ZdisplayButton = QtWidgets.QPushButton(self.widget)
        self.ZdisplayButton.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Fixed,self.ZdisplayButton.sizePolicy().hasHeightForWidth()))
        self.ZdisplayButton.setMinimumSize(QtCore.QSize(30, 30))
        self.ZdisplayButton.setMaximumSize(QtCore.QSize(30, 30))
        self.ZdisplayButton.setText("")
        icon_Zdisplay = QtGui.QIcon()
        icon_Zdisplay.addPixmap(QtGui.QPixmap("images/Z_letter.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ZdisplayButton.setIcon(icon_Zdisplay)
        self.ZdisplayButton.setCheckable(True)
        self.ZdisplayButton.setObjectName("ZdisplayButton")
        self.gridLayout.addWidget(self.ZdisplayButton, 6, 1, 1, 1)

        self.auto_hist_temperature_mode_button = QtWidgets.QPushButton(self.widget)
        self.auto_hist_temperature_mode_button.setSizePolicy(ReturnSizePolicy(QtWidgets.QSizePolicy.Fixed,self.auto_hist_temperature_mode_button.sizePolicy().hasHeightForWidth()))
        self.auto_hist_temperature_mode_button.setMinimumSize(QtCore.QSize(30, 30))
        self.auto_hist_temperature_mode_button.setMaximumSize(QtCore.QSize(30, 30))
        self.auto_hist_temperature_mode_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/auto_temperature.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.auto_hist_temperature_mode_button.setIcon(icon5)
        self.auto_hist_temperature_mode_button.setCheckable(True)
        self.auto_hist_temperature_mode_button.setObjectName("auto_hist_temperature_mode_button")
        self.gridLayout.addWidget(self.auto_hist_temperature_mode_button, 6, 0, 1, 1)

        self.penButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.penButton.sizePolicy().hasHeightForWidth())
        self.penButton.setSizePolicy(sizePolicy)
        self.penButton.setMinimumSize(QtCore.QSize(30, 30))
        self.penButton.setMaximumSize(QtCore.QSize(30, 30))
        self.penButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.penButton.setIcon(icon8)
        self.penButton.setCheckable(True)
        self.penButton.setObjectName("penButton")
        self.gridLayout.addWidget(self.penButton, 3, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.canvas = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.horizontalLayout.addWidget(self.canvas)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 549, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFIle = QtWidgets.QMenu(self.menuBar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuImage = QtWidgets.QMenu(self.menuBar)
        self.menuImage.setObjectName("menuImage")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.fileToolbar = QtWidgets.QToolBar(MainWindow)
        self.fileToolbar.setIconSize(QtCore.QSize(16, 16))
        self.fileToolbar.setObjectName("fileToolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.fileToolbar)

        MainWindow.addToolBarBreak()#.addItem(spacerItem2)

        self.ZToolbar = QtWidgets.QToolBar(MainWindow)
        self.ZToolbar.setIconSize(QtCore.QSize(25,25))
        self.ZToolbar.setObjectName("ZToolbar")
        self.ZToolbar.setOrientation(QtCore.Qt.Horizontal)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.ZToolbar)

        self.ZToolbar2 = QtWidgets.QToolBar(MainWindow)
        self.ZToolbar2.setIconSize(QtCore.QSize(25,25))
        self.ZToolbar2.setObjectName("ZToolbar2")
        self.ZToolbar2.setOrientation(QtCore.Qt.Horizontal)
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.ZToolbar2)

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionClearImage = QtWidgets.QAction(MainWindow)
        self.actionClearImage.setObjectName("actionClearImage")
        self.actionOpenImage = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("images/blue-folder-open-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenImage.setIcon(icon16)
        self.actionOpenImage.setObjectName("actionOpenImage")

        self.actionProcessRandZ = QtWidgets.QAction(MainWindow)
        # self.actionProcessRandZ.setText("Random Z")
        icon_randomZ = QtGui.QIcon()
        icon_randomZ.addPixmap(QtGui.QPixmap("images/random_l1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProcessRandZ.setIcon(icon_randomZ)
        self.actionProcessRandZ.setObjectName("actionProcessRandZ")

        self.actionProcessLimitedRandZ = QtWidgets.QAction(MainWindow)
        icon_limited_randomZ = QtGui.QIcon()
        icon_limited_randomZ.addPixmap(QtGui.QPixmap("images/random_l1_limited.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProcessLimitedRandZ.setIcon(icon_limited_randomZ)
        self.actionProcessLimitedRandZ.setObjectName("actionProcessLimitedRandZ")

        # self.randomLimitingWeightBox = QtWidgets.QLineEdit(MainWindow)
        self.randomLimitingWeightBox = QtWidgets.QDoubleSpinBox(MainWindow)
        self.randomLimitingWeightBox.setObjectName("randomLimitingWeightBox")
        self.randomLimitingWeightBox.setValue(1.)
        # self.randomLimitingWeightBox.setText('1')
        self.randomLimitingWeightBox.setMaximum(200)
        # self.randomLimitingWeightBox.setSingleStep(0.1)

        icon_copyRandZ = QtGui.QIcon()
        # icon_copyRandZ = QtGui.QIcon(QtGui.QPixmap("images/randoms2default.png"))
        icon_copyRandZ.addPixmap(QtGui.QPixmap("images/randoms2default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopyFromRandom = QtWidgets.QAction(icon=icon_copyRandZ,parent=MainWindow)
        # self.actionCopyFromRandom.setIcon(icon_copyRandZ)
        self.actionCopyFromRandom.setObjectName("actionCopyFromRandom")
        self.actionCopyFromRandom.setEnabled(False)

        self.actionCopy2Random = QtWidgets.QAction(MainWindow)
        icon_copyDefault2RandZ = QtGui.QIcon()
        icon_copyDefault2RandZ = QtGui.QIcon()
        icon_copyDefault2RandZ.addPixmap(QtGui.QPixmap("images/default2randoms.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy2Random.setIcon(icon_copyDefault2RandZ)
        self.actionCopy2Random.setObjectName("actionCopy2Random")
        # self.actionCopy2Random.setEnabled(True)

        self.DisplayedImageSelectionButton = QtWidgets.QComboBox(MainWindow)
        # self.DisplayedImageSelectionButton.setText("Random Z")
        # self.DisplayedImageSelectionButton.addItem('')
        # self.DisplayedImageSelectionButton.addItems([str(i+1) for i in range(self.num_random_Zs)])
        self.DisplayedImageSelectionButton.setObjectName("DisplayedImageSelectionButton")
        self.DisplayedImageSelectionButton.setEnabled(False)

        self.actionIncreaseSTD = QtWidgets.QAction(MainWindow)
        # self.actionIncreaseSTD.setText("Increase STD")
        self.actionIncreaseSTD.setObjectName("actionIncreaseSTD")
        icon_sigmaUp = QtGui.QIcon()
        icon_sigmaUp.addPixmap(QtGui.QPixmap("images/sigma_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIncreaseSTD.setIcon(icon_sigmaUp)

        self.actionDecreaseSTD = QtWidgets.QAction(MainWindow)
        # self.actionDecreaseSTD.setText("Decrease STD")
        self.actionDecreaseSTD.setObjectName("actionDecreaseSTD")
        icon_sigmadown = QtGui.QIcon()
        icon_sigmadown.addPixmap(QtGui.QPixmap("images/sigma_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDecreaseSTD.setIcon(icon_sigmadown)

        self.actionDecreaseTV = QtWidgets.QAction(MainWindow)
        self.actionDecreaseTV.setObjectName("actionDecreaseTV")
        icon_TVdown = QtGui.QIcon()
        icon_TVdown.addPixmap(QtGui.QPixmap("images/TV_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDecreaseTV.setIcon(icon_TVdown)

        self.actionImitateHist = QtWidgets.QAction(MainWindow)
        self.actionImitateHist.setObjectName("actionImitateHist")
        icon_hist_imitation = QtGui.QIcon()
        icon_hist_imitation.addPixmap(QtGui.QPixmap("images/hist_imitation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImitateHist.setIcon(icon_hist_imitation)
        self.actionImitateHist.setEnabled(False)

        self.actionImitatePatchHist = QtWidgets.QAction(MainWindow)
        self.actionImitatePatchHist.setObjectName("actionImitatePatchHist")
        icon_patch_hist_imitation = QtGui.QIcon()
        icon_patch_hist_imitation.addPixmap(QtGui.QPixmap("images/hist_imitation_patch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImitatePatchHist.setIcon(icon_patch_hist_imitation)
        self.actionImitatePatchHist.setEnabled(False)

        self.actionMatchSliders = QtWidgets.QAction(MainWindow)
        self.actionMatchSliders.setObjectName("actionMatchSliders")
        icon_match_sliders = QtGui.QIcon()
        icon_match_sliders.addPixmap(QtGui.QPixmap("images/sliders_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMatchSliders.setIcon(icon_match_sliders)

        self.actionFoolAdversary = QtWidgets.QAction(MainWindow)
        self.actionFoolAdversary.setObjectName("actionFoolAdversary")
        icon_pixmap = QtGui.QPixmap("images/adversary.png")
        # icon_pixmap.scaledToWidth(40)
        icon_adversary = QtGui.QIcon()
        icon_adversary.addPixmap(icon_pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon_adversary.actualSize(QtCore.QSize(60, 60))
        self.actionFoolAdversary.setIcon(icon_adversary)

        self.actionAutoSaveImage = QtWidgets.QAction(MainWindow)
        icon17_0 = QtGui.QIcon()
        icon17_0.addPixmap(QtGui.QPixmap("images/Save-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAutoSaveImage.setIcon(icon17_0)
        self.actionAutoSaveImage.setObjectName("actionAutoSaveImage")

        self.actionSaveImage = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("images/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveImage.setIcon(icon17)
        self.actionSaveImage.setObjectName("actionSaveImage")
        self.actionInvertColors = QtWidgets.QAction(MainWindow)
        self.actionInvertColors.setObjectName("actionInvertColors")
        self.actionFlipHorizontal = QtWidgets.QAction(MainWindow)
        self.actionFlipHorizontal.setObjectName("actionFlipHorizontal")
        self.actionFlipVertical = QtWidgets.QAction(MainWindow)
        self.actionFlipVertical.setObjectName("actionFlipVertical")
        self.actionNewImage = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("images/document-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewImage.setIcon(icon18)
        self.actionNewImage.setObjectName("actionNewImage")
        self.actionBold = QtWidgets.QAction(MainWindow)
        self.actionBold.setCheckable(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("images/edit-bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon19)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtWidgets.QAction(MainWindow)
        self.actionItalic.setCheckable(True)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("images/edit-italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon20)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtWidgets.QAction(MainWindow)
        self.actionUnderline.setCheckable(True)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("images/edit-underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon21)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionFillShapes = QtWidgets.QAction(MainWindow)
        self.actionFillShapes.setCheckable(True)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("images/paint-can-color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFillShapes.setIcon(icon22)
        self.actionFillShapes.setObjectName("actionFillShapes")
        self.menuFIle.addAction(self.actionNewImage)
        self.menuFIle.addAction(self.actionOpenImage)
        self.menuFIle.addAction(self.actionSaveImage)
        self.menuFIle.addAction(self.actionAutoSaveImage)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClearImage)
        self.menuImage.addAction(self.actionInvertColors)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionFlipHorizontal)
        self.menuImage.addAction(self.actionFlipVertical)
        self.menuBar.addAction(self.menuFIle.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuImage.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.fileToolbar.addAction(self.actionNewImage)
        self.fileToolbar.addAction(self.actionOpenImage)
        self.fileToolbar.addAction(self.actionSaveImage)
        self.fileToolbar.addAction(self.actionAutoSaveImage)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editable SR"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuImage.setTitle(_translate("MainWindow", "Image"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.fileToolbar.setWindowTitle(_translate("MainWindow", "toolBar"))
        # self.drawingToolbar.setWindowTitle(_translate("MainWindow", "toolBar"))
        # self.fontToolbar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionClearImage.setText(_translate("MainWindow", "Clear Image"))
        self.actionOpenImage.setText(_translate("MainWindow", "Open Image..."))
        self.actionSaveImage.setText(_translate("MainWindow", "Save Image As..."))
        self.actionAutoSaveImage.setText(_translate("MainWindow", "Save Image & Z map"))
        self.actionInvertColors.setText(_translate("MainWindow", "Invert Colors"))
        self.actionFlipHorizontal.setText(_translate("MainWindow", "Flip Horizontal"))
        self.actionFlipVertical.setText(_translate("MainWindow", "Flip Vertical"))
        self.actionNewImage.setText(_translate("MainWindow", "New Image"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionBold.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionItalic.setText(_translate("MainWindow", "Italic"))
        self.actionItalic.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionUnderline.setText(_translate("MainWindow", "Underline"))
        self.actionFillShapes.setText(_translate("MainWindow", "Fill Shapes?"))

