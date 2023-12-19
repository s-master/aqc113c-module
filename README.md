This RPM/XCP-ng package contains the driver for the Marvell® AQtion AQC113CS 10Gb Ethernet network adapter. I utilized the template provided by https://github.com/xcp-ng-rpms/aqc111u-module as a foundation for creating this package. The compilation process was performed using https://github.com/xcp-ng-rpms/kernel-driver-template.

Notably, this network adapter is integrated into motherboards such as the ASUS ProArt X570-CREATOR WIFI.

The driver used in this package has been sourced from https://www.marvell.com/content/dam/marvell/en/drivers/Marvell_Linux_2.4.11.zip.

The driver within this package is compatible with Ethernet adapters based on the following models, as indicated in the source's readme file:

- AQC-100
- AQC-107
- AQC-108
- AQC-109
- AQC-111
- AQC-112
- AQC-113


Discussion about this driver can be found here
https://xcp-ng.org/forum/topic/6910/marvell-aqc113cs-10gb-network-adapter-driver-on-proart-x570-creator-wifi

And on Andrew's XCP-NG Page you'll find a cleaner created rpm package
https://users.ntplx.net/~andrew/xcp/

As of today my driver-package is working properly on a production system of myself without any errors.
