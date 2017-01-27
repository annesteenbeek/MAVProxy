#!/usr/bin/env python
from pymavlink.mavutil import mavlink as ml


def mode_enum_to_string(agro_mode):
    if agro_mode == ml.AGRO_MODE_RTD: return "RTD"
    if agro_mode == ml.AGRO_MODE_AUTOSPRAY: return "Autospray"
    if agro_mode == ml.AGRO_MODE_INACTIVE: return "Inactive"
    if agro_mode == ml.AGRO_MODE_UNK: return "Unk"
    else: return ""
    # TODO cast error 
    pass


def string_to_mode(agro_mode):
    mode = agro_mode.lower()
    if mode == "rtd": return ml.AGRO_MODE_RTD
    if mode == "autospray": return ml.AGRO_MODE_AUTOSPRAY
    if mode == "inactive": return ml.AGRO_MODE_INACTIVE
    else: return 0
    # TODO send error

def sub_mode_enum_to_string(agro_sub_mode):
    if agro_sub_mode == ml.AGRO_SUB_MODE_UNK: return "Unk"
    if agro_sub_mode == ml.AGRO_SUB_MODE_PENDING: return "Pending"
    if agro_sub_mode == ml.AGRO_SUB_MODE_TRACK_SPRAY: return "Track spray"
    if agro_sub_mode == ml.AGRO_SUB_MODE_RESUME_SPRAY: return "Resume spray"
    if agro_sub_mode == ml.AGRO_SUB_MODE_DOCKED: return "Docked"
    if agro_sub_mode == ml.AGRO_SUB_MODE_POSITION_ABVOVE_DOCK: return "Position above dock"
    else: return ""
    #TODO cast error



