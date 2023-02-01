%define vendor_name Marvell
%define vendor_label marvell
%define driver_name aqc113c

%if %undefined module_dir
%define module_dir extra
%endif

Summary: %{vendor_name} %{driver_name} aQuantia AQtion Driver for the aQuantia Multi-Gigabit PCI Express Family of Ethernet Adapters
Name: %{driver_name}-module
Version: 2.5.5
Release: 2%{?dist}
License: GPL

#Source taken from https://www.marvell.com/content/dam/marvell/en/drivers/Marvell_Linux_2.4.11.zip
Source0: %{driver_name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: kernel-devel
Provides: %{driver_name}-module
Requires: kernel-uname-r = %{kernel_version}
Requires(post): /usr/sbin/depmod
Requires(postun): /usr/sbin/depmod

%description
%{vendor_name} %{driver_name} - Linux* aQuantia AQtion Driver for the aQuantia Multi-Gigabit PCI Express Family of Ethernet Adapters
version %{kernel_version}.

%prep
%autosetup -n %{driver_name}-%{version}

%build
%{make_build} -C /lib/modules/%{kernel_version}/build M=$(pwd) KSRC=/lib/modules/%{kernel_version}/build modules

%install
%{__make} %{?_smp_mflags} -C /lib/modules/%{kernel_version}/build M=$(pwd) INSTALL_MOD_PATH=%{buildroot} INSTALL_MOD_DIR=%{module_dir} DEPMOD=/bin/true modules_install

# remove extra files modules_install copies in
rm -f %{buildroot}/lib/modules/%{kernel_version}/modules.*

# mark modules executable so that strip-to-file can strip them
find %{buildroot}/lib/modules/%{kernel_version} -name "*.ko" -type f | xargs chmod u+x

%post
/sbin/depmod %{kernel_version}
%{regenerate_initrd_post}

%postun
/sbin/depmod %{kernel_version}
%{regenerate_initrd_postun}

%posttrans
%{regenerate_initrd_posttrans}

%files
/lib/modules/%{kernel_version}/*/*.ko

%changelog
* Thu Feb 02 2023 s-master - 2.5.5
- Re-packing for XCP-ng of Marvell AQC113C driver