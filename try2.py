# import wmi
# c = wmi.WMI()
# for os in c.Win32_OperatingSystem():
#     print(os.Caption)
# import wmi
# c = wmi.WMI()
# for service in c.Win32_Service(Name="seclogon"):
#   result, = service.StopService()
#   if result == 0:
#     print("Service", service.Name, "stopped")
#   else:
#     print("Some problem")
#   break
# else:
#   print("Service not found")
# import wmi
# c = wmi.WMI()
# print(c.Win32_ComputerSystem.methods.keys())
# import wmi
# c = wmi.WMI()
# os = c.Win32_OperatingSystem
# for method_name in os.methods:
#   method = getattr(os, method_name)
#   print(method)
# import wmi
# c = wmi.WMI(namespace= "wmi")
# print(c.methods)

# import wmi
# c = wmi.WMI(namespace= "wmi")
# process_class = c.Win32_Process
# methods = process_class.methods
# for method_name in methods.keys():
#     print(method_name)

# import 

# import wmi
# c = wmi.WMI()  # Connect to the local machine

# type_needed = 0
# type_needed = type_needed % 3

# name = ['usb audio', 'microphones']
# sound_devices = c.Win32_SoundDevice()

# for device in sound_devices:
#     if type_needed != 0:
#         if name[type_needed-1] in device.Name.lower():
#             sound_device = device
#     else:
#         if name[0] not in device.Name.lower() and name[1] not in device.Name.lower():
#             sound_device = device

# print(sound_device)
# sound_device

    # Change the volume of the sound device to 50%
    # sound_device.SetDefaultVolume(0.5)

# from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# def main():
#     sessions = AudioUtilities.GetAllSessions()
#     for session in sessions:
#         volume = session._ctl.QueryInterface(ISimpleAudioVolume)
#         if session.Process and session.Process.name() == "vlc.exe":
#             print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
#             volume.SetMasterVolume(0.6, None)

# if __name__ == "__main__":
#     main()

# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# # Get default audio device using PyCAW
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))

# # Control volume
# volume.SetMasterVolumeLevelScalar(0.1, None) # Set volume to maximum
# currentVolumeDb = volume.GetMasterVolumeLevelScalar()


import pprint

pprint.pformat()
# con