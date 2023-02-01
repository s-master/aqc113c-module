RPM / XCP-ng package with the driver for the Marvell® AQtion AQC113CS 10Gb Ethernet network adapter.
I used https://github.com/xcp-ng-rpms/aqc111u-module as a template for creating this package.
For compiling I used https://github.com/xcp-ng-rpms/kernel-driver-template

This network adapter is for example onboard on the ASUS ProArt X570-CREATOR WIFI motherboard.

The driver is taken from https://www.marvell.com/content/dam/marvell/en/drivers/Marvell_Linux_2.4.11.zip

The driver in this package is compatible with ethernet adapters based on:
 - AQC-100,
 - AQC-107,
 - AQC-108,
 - AQC-109,
 - AQC-111,
 - AQC-112,
 - AQC-113.
 
as stated in the readme file of the source.