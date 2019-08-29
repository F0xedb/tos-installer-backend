from model.model.partition import partition, EFilesystem
import config
import shell
import os
import sys
sys.path.append("...")  # set all imports to root imports


def buildPrimaryPartition(disk, Partition, index=0, name="root"):
    """
    Alter the partition table to include a primary typed partition on a certain disk
    @disk is the device to alter its partition table
    @Partition is the model of a partition
    @index is the index of the partition in the partition table
    @name is the name to assign this partition in the table
    """
    commands = []
    commands.append(getBaseCommand(
        disk) + "mkpart primary {} {}".format(Partition.start, Partition.end))
    commands.append(getBaseCommand(disk) + "name {} {}".format(index, name))
    return commands


def buildBootablePartition(disk, Partition, index=0, name="boot", bIsGPT=True):
    """
    Alter the partition table to include a primary typed partition on a certain disk
    @disk is the device to alter its partition table
    @Partition is the model of a partition
    @index is the index of the partition in the partition table
    @name is the name to assign this partition in the table
    @bIsGPT tells us if the partition table ig GPT, if it isn't a msdos boot partition will be generated
    """
    commands = []
    if bIsGPT:
        commands.append(getBaseCommand(
            disk) + "mkpart ESP fat32 {} {}".format(Partition.start, Partition.end))
    else:
        commands.append(getBaseCommand(
            disk) + "mkpart primary {} {}".format(Partition.start, Partition.end))

    commands.append(getBaseCommand(disk) + "set {} boot on".format(index))
    commands.append(getBaseCommand(disk) + "name {} {}".format(index, name))
    return commands


def buildSwapPartition(disk, Partition, index=0, name="swap"):
    """
    Alter the partition table to include a primary typed partition on a certain disk
    @disk is the device to alter its partition table
    @Partition is the model of a partition
    @index is the index of the partition in the partition table
    @name is the name to assign this partition in the table
    """
    return buildPrimaryPartition(disk, Partition, index, name)


def buildEncryptedPrimaryPartition(disk, Partition, index=0, name="root"):
    """
    Alter the partition table to include a primary typed partition on a certain disk
    @disk is the device to alter its partition table
    @Partition is the model of a partition
    @index is the index of the partition in the partition table
    @name is the name to assign this partition in the table
    """
    commands = []
    commands.append(getBaseCommand(
        disk) + "mkpart primary {} {}".format(Partition.start, Partition.end))
    commands.append(getBaseCommand(disk) + "set {} lvm on".format(index))
    commands.append(getBaseCommand(disk) + "name {} {}".format(index, name))
    return commands


def getBaseCommand(disk):
    """
    returns the base of the parted command
    """
    return "parted --script '{}' ".format(disk.device)


def format(part):
    """
    format a partition based on the filesystem. 
    It returns the return code to indicate if it was succesfull or not.
    If no matching filesystem was found we return None
    """
    if part.filesystem == EFilesystem.EXT4:
        return shell.Command("mkfs.ext4 {}".format(part.device)).GetReturnCode()
    elif part.filesystem == EFilesystem.BTRFS:
        return shell.Command("mkfs.btrfs {}".format(part.device)).GetReturnCode()
    elif part.filesystem == EFilesystem.FAT32:
        return shell.Command("mkfs.fat -F32 {}".format(part.device)).GetReturnCode()
    return None
