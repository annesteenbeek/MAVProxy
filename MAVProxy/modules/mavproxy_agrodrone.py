#!/usr/bin/env python

import os
import os.path
import sys
from pymavlink import mavutil
import errno
import time

from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib import mp_util
from MAVProxy.modules.lib import mp_settings
from MAVProxy.modules.lib import agro_mode_conversions as convert_agro


class agroDrone(mp_module.MPModule):
    def __init__(self, mpstate):
        """Initialise module"""
        super(agroDrone, self).__init__(mpstate, " agrodrone", "")
        self.packets_mytarget = 0
        self.packets_othertarget = 0
        self.verbose = False
        self.modes = ['autospray', 'rtd', 'inactive']

        self.example_settings = mp_settings.MPSettings(
            [ ('verbose', bool, False),
          ])
        self.add_command('agromode', self.cmd_agromode, "set agromode", ['set <autospray|rtd|inactive>'])

    def usage(self):
        '''show help on command line options'''
        return "Usage:  agromode set <autospray|rtd|inactive>"

    def cmd_agromode(self, args):
        '''control behaviour of the module'''
        if len(args) == 0:
            print self.usage()
        elif args[0] == "set":
            if args[1] in self.modes:
                setmode = args[1].lower()
                enum = convert_agro.string_to_mode(setmode)
                self.master.mav.set_agro_mode_send(0,
                                                   0,
                                                    enum)
                # self.master.mav.command_long_send(
                #     self.target_system,  # target_system
                #     self.target_component,
                    # mavutil.mavlink.MAV_CMD_GET_HOME_POSITION, # command
                    # 0, # confirmation
                    # 1, # param1 (1 to indicate arm)
                    # 0, # param2 (all other params meaningless)
                    # 0, # param3
                    # 0, # param4
                    # 0, # param5
                    # 0, # param6
                    # 0) # param7
        else:
            print self.usage()

    
def init(mpstate):
    '''initialise module'''
    return agroDrone(mpstate)
