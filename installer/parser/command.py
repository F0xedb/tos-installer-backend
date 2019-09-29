import yaml
import installer.config as config


def populateMissingNetwork(content):
    """
    See if a piece of the dictionary is missing. If it is then we set it to the hardcoded values defined in config.py
    This function should not be called externally. It fills all data related to network configuration options
    """
    if not exists(content, "IP"):
        content["IP"] = config.IP
    if not exists(content, "WIFI_CONNECT_COMMAND"):
        content["WIFI_CONNECT_COMMAND"] = config.WIFI_CONNECT_COMMAND
    if not exists(content, "WIFI_CONNECT_COMMAND_WITH_PASSWORD"):
        content["WIFI_CONNECT_COMMAND_WITH_PASSWORD"] = config.WIFI_CONNECT_COMMAND_WITH_PASSWORD
    return content


def populateMissingUser(content):
    """
    See if a piece of the dictionary is missing. If it is then we set it to the hardcoded values defined in config.py
    This function should not be called externally. It fills all data related to user configuration options
    """
    if not exists(content, "DEFAULT_SHELL"):
        content["DEFAULT_SHELL"] = config.DEFAULT_SHELL
    if not exists(content, "USERADD"):
        content["USERADD"] = config.USERADD
    if not exists(content, "MOUNTPOINT"):
        content["MOUNTPOINT"] = config.MOUNTPOINT
    return content


def populateMissingBootloader(content):
    """
    See if a piece of the dictionary is missing. If it is then we set it to the hardcoded values defined in config.py
    This function should not be called externally. It fills all data related to bootloader configuration options
    """
    if not exists(content, "BOOTLOADER_EFI"):
        content["BOOTLOADER_EFI"] = config.BOOTLOADER_EFI
    if not exists(content, "BOOTLOADER_DOS"):
        content["BOOTLOADER_DOS"] = config.BOOTLOADER_DOS
    if not exists(content, "BOOTLOADER_CONFIG"):
        content["BOOTLOADER_CONFIG"] = config.BOOTLOADER_CONFIG
    return content


def populateMissingSystem(content):
    """
    See if a piece of the dictionary is missing. If it is then we set it to the hardcoded values defined in config.py
    This function should not be called externally. It fills all data related to system configuration options
    """
    if not exists(content, "LOCAL"):
        content["LOCAL"] = config.LOCALE
    if not exists(content, "KEYMAP"):
        content["KEYMAP"] = config.KEYMAP
    if not exists(content, "HOSTNAME"):
        content["HOSTNAME"] = config.HOSTNAME
    if not exists(content, "ROOT_PWD"):
        content["ROOT_PWD"] = config.ROOT_PWD
    return content


def populateMissingLUKS(content):
    """
    See if a piece of the dictionary is missing. If it is then we set it to the hardcoded values defined in config.py
    This function should not be called externally. It fills all data related to LUKS encryption configuration options
    """
    if not exists(content, "LUKS"):
        content["LUKS"] = config.LUKS
    if not exists(content, "LUKS_OPEN"):
        content["LUKS_OPEN"] = config.LUKS_OPEN
    if not exists(content, "LUKS_NAME"):
        content["LUKS_NAME"] = config.LUKS_NAME
    if not exists(content, "LUKS_DEVICE"):
        content["LUKS_DEVICE"] = config.LUKS_DEVICE
    return content


def populateMissingMisc(content):
    """
    See if a piece of the dictionary is missing. If it is then we set it to the hardcoded values defined in config.py
    This function should not be called externally. It fills all data related to Miscellanous configuration options
    """
    if not exists(content, "INSTALLCOMMAND"):
        content["INSTALLCOMMAND"] = config.INSTALLCOMMAND
    if not exists(content, "CHROOT"):
        content["CHROOT"] = config.CHROOT

    if not exists(content, "FSTAB"):
        content["FSTAB"] = config.FSTAB

    if not exists(content, "GROUPS"):
        content["GROUPS"] = config.GROUPS

    if not exists(content, "HERESTRING"):
        content["HERESTRING"] = config.HERESTRING

    if not exists(content, "BOOTSTRAP"):
        content["BOOTSTRAP"] = config.BOOTSTRAP

    if not exists(content, "BOOTSTRAP_PACKAGES"):
        content["BOOTSTRAP_PACKAGES"] = config.BOOTSTRAP_PACKAGES
    if not exists(content, "KERNEL"):
        content["KERNEL"] = config.KERNEL
    return content


def populateMissingPieces(content):
    """
    See if a piece of the dictionary is missing. If it is then we set it to the hardcoded values defined in config.py
    """

    content = populateMissingNetwork(content)
    content = populateMissingUser(content)
    content = populateMissingBootloader(content)
    content = populateMissingSystem(content)
    content = populateMissingMisc(content)

    return content


def exists(dict, key):
    """
    Check if a key exists in a dict
    """
    return key in dict.keys()


def parse(filename):
    """
    Returns a config dictionary
    """
    try:
        with open(filename, 'r') as stream:
            try:
                content = yaml.load(stream, Loader=yaml.Loader)
            except yaml.YAMLError as exc:
                print(exc)
    except FileNotFoundError as err:
        return populateMissingPieces({"CONFIG": "config.py"})
    return populateMissingPieces(content)
