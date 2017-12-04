# NEWTODO: most of this file should be removed, not all this stuff needs to be imported early and all these optimizations are dumb

# Copyright 2004-2008 Nanorex, Inc.  See LICENSE file for details.
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *  # <- lol NEWTODO: remove all * imports
import time
import os

from PyQt5.QtWidgets import QApplication, QSplashScreen
import foundation.undo_internals as undo_internals
import utilities.icon_utilities as icon_utilities

from ne1_ui.MWsemantics import MWsemantics
from ne1_startup import startup_misc

from platform_dependent.PlatformDependent import screen_pos_size


def load_splashscreen():
    splash_pixmap = icon_utilities.imagename_to_pixmap( "images/splash.png" )
    if not splash_pixmap.isNull():
        splash = QSplashScreen(splash_pixmap) # create the splashscreen
        splash.show()
        MINIMUM_SPLASH_TIME = 2.0
        splash_start = time.time()
    else:
        print("note: splash.png was not found")

def init_main_window():
    main_window = MWsemantics() # This does a lot of initialization (in MainWindow.__init__)
    # NEWTODO: remove


def initialize_backend():
    # TODO: refactor funciton, perhaps the backend doesn't even need early initialization
    
    from model_updater import master_model_updater
    master_model_updater.initialize()

    import model.assembly
    model.assembly.Assembly.initialize()

    import PM.GroupButtonMixin as GroupButtonMixin
    GroupButtonMixin.GroupButtonMixin.initialize()

    import model.Comment as Comment
    Comment.register_MMP_RecordParser_for_Comment()

    import analysis.GAMESS.jig_Gamess as jig_Gamess
    jig_Gamess.register_MMP_RecordParser_for_Gamess()

    import model.PovrayScene as PovrayScene
    PovrayScene.register_MMP_RecordParser_for_PovrayScene()

    try:
        import dna.model.DnaMarker as DnaMarker
        DnaMarker.register_MMP_RecordParser_for_DnaMarkers()
    except:
        print_compact_traceback("bug: ignoring exception in register_MMP_RecordParser_for_DnaMarkers: ")


        
def load_application():
    undo_internals.call_asap_after_QWidget_and_platform_imports_are_ok()
    ### TODO: this imports undo, env, debug, and it got moved earlier
    # in the startup process at some point. Those imports are probably not
    # too likely to pull in a lot of others, but if possible we should put up
    # the splash screen before doing most of them. Sometime try to figure out
    # how to do that. The point of this function is mostly to wrap every signal->slot
    # connection -- maybe it's sufficient to do that before creating the main
    # window rather than before creating the app? [bruce 071008 comment]

    icon_utilities.initialize_icon_utilities()

    # Create the application object (an instance of QApplication).
    QApplication.setColorSpec(QApplication.CustomColor)
    app = QApplication(sys.argv)
    load_splashscreen()
    app.lastWindowClosed .connect(app.quit)
    
    initialize_backend()

    startup_misc.pre_main_show(main_window) # this sets main_window's geometry, among other things

    main_window._init_after_geometry_is_set()

    if not splash_pixmap.isNull():
        # If the MINIMUM_SPLASH_TIME duration has not expired, sleep for a moment.
        while time.time() - splash_start < MINIMUM_SPLASH_TIME:
            time.sleep(0.1)
        splash.finish( main_window ) # Take away the splashscreen

    main_window.show()

    # do other things after showing the main window
    startup_misc.post_main_show(main_window)

    # Do other post-startup, pre-event-loop, non-profiled things, if any
    # (such as run optional startup commands for debugging).
    startup_misc.just_before_event_loop()

    app.exec_()
