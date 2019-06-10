1. default user `pi:raspberry` gives ssh and user
cat /home/pi/Desktop/user.txt

2. `sudo su` gives pseudo root

# cat /root/root.txt
I lost my original root.txt! I think I may have a backup on my USB stick...

# fdisk -l

Disk /dev/sdb: 10 MiB, 10485760 bytes, 20480 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk /dev/sda: 10 GiB, 10737418240 bytes, 20971520 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0eddfb88

Device     Boot   Start      End  Sectors  Size Id Type
/dev/sda1  *         64  2709119  2709056  1.3G 17 Hidden HPFS/NTFS
/dev/sda2       2709504 20971519 18262016  8.7G 83 Linux
# mkdir /mnt/usb
# mount /dev/sda2 /mnt/usb
# cd /mnt/usb
cat root/root.txt
(same)

# cat /media/usbstick/damnit.txt
Damnit! Sorry man I accidentally deleted your files off the USB stick.
Do you know if there is any way to get them back?

-James

(wtf ...)

# lsof | grep "/root/root.txt"
(doesn't give anything)

// the usb stick is at /dev/sdb

# lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   10G  0 disk
├─sda1   8:1    0  1.3G  0 part /lib/live/mount/persistence/sda1
└─sda2   8:2    0  8.7G  0 part /lib/live/mount/persistence/sda2
sdb      8:16   0   10M  0 disk /media/usbstick

# strings /dev/sdb
gives the root flag
