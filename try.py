import wmi
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from typing import overload
import pyperclip as pclp
import os
import shelve



class Control_brigthness:
    c = wmi.WMI(namespace= "wmi")
    def __init__(self):...

    @classmethod
    def get_brightness(cls):
        brightness = cls.c.WmiMonitorBrightness()[0]
        return brightness.CurrentBrightness
    
    @classmethod
    def set_brightness(cls, brightness:int):
        if type(brightness) != int: raise TypeError("Not int")
        if  0 <= brightness <= 100:
            method = cls.c.WmiMonitorBrightnessMethods()[0]
            method.WmiSetBrightness(brightness, 1)
        else: raise ValueError("Number should be between 0-100")

    @classmethod
    def dim_brightness(cls):
        method = cls.c.WmiMonitorBrightnessMethods()[0]
        method.WmiSetBrightness(0, 1)

class Control_sound:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    def __init__(self): ...

    @overload
    def set_sound(self, val:int):
        """
        fuck you
        """
        ...
    @overload
    def set_sound(self, val:float):
        """
        suck my cock
        """
        ...
    
    @classmethod
    def set_sound(cls, val):
        typ = isinstance(val, int)
        if not typ and not isinstance(val, float): raise TypeError('Invalid type. Expected int or float.')
        val /= (100 if typ else 1)
        if not (0.0 <= val <= 1.0): raise ValueError("The value should be between 0.00-%s0"% (100/(100**(not typ))))
        cls.volume.SetMasterVolumeLevelScalar(round(val,3), None)
    
    @classmethod
    def get_sound(cls, typ=0):
        return cls.volume.GetMasterVolumeLevelScalar() * (100 if not typ else 1)

    @classmethod
    def mute_sound(cls):
        # add unmute
        cls.volume.SetMasterVolumeLevelScalar(0, None)

class Control_clipboard:
    LIMIT = 3
    def __init__(self) -> None:
        pass
    @staticmethod
    def _oread():
        with shelve.open("clipboard_") as data:
            df = data["li"]
        return df
    @staticmethod
    def _owrite(li):
        with shelve.open("clipboard_") as data:
            data["li"] = li
    @staticmethod
    def _oclear():
        with shelve.open("clipboard_") as data:
            data["li"] = []
    @classmethod
    def _osavtoclip(cls):
        df = cls._oread() if os.path.exists("clipboard_.bak") else []
        clipboard = pclp.paste()
        if len(clipboard.strip()) != 0: 
            df += [clipboard]
            if len(df) > cls.LIMIT: df.pop(0)
            cls._owrite(df)
        return clipboard


# Control_clipboard._oclear()
# print(Control_clipboard._osavtoclip())
# print(Control_clipboard._oread())

# Control_sound.set_sound(88)
# print(Control_sound.get_sound())
Control_brigthness.set_brightness(20)
# print(Control_brigthness.get_brightness())


