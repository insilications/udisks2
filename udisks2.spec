#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : udisks2
Version  : 2.9.2
Release  : 22
URL      : file:///aot/build/clearlinux/packages/udisks2/udisks2-v2.9.2.tar.gz
Source0  : file:///aot/build/clearlinux/packages/udisks2/udisks2-v2.9.2.tar.gz
Summary  : Disk Manager
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0+ LGPL-2.1+
Requires: udisks2-bin = %{version}-%{release}
Requires: udisks2-config = %{version}-%{release}
Requires: udisks2-data = %{version}-%{release}
Requires: udisks2-lib = %{version}-%{release}
Requires: udisks2-libexec = %{version}-%{release}
Requires: udisks2-locales = %{version}-%{release}
Requires: udisks2-man = %{version}-%{release}
Requires: udisks2-services = %{version}-%{release}
Requires: libatasmart
Requires: libblockdev
Requires: libbytesize
Requires: libiscsi
Requires: libstoragemgmt
Requires: volume_key
BuildRequires : LVM2-dev
BuildRequires : acl-dev
BuildRequires : acl-staticdev
BuildRequires : dbus
BuildRequires : dbus-broker
BuildRequires : dbus-dev
BuildRequires : dbus-glib
BuildRequires : dbus-glib-dev
BuildRequires : dbus-python
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : glib
BuildRequires : glib-dev
BuildRequires : gnome-common-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libatasmart
BuildRequires : libblockdev
BuildRequires : libblockdev-dev
BuildRequires : libblockdev-staticdev
BuildRequires : libbytesize
BuildRequires : libconfig-dev
BuildRequires : libconfig-staticdev
BuildRequires : libgudev
BuildRequires : libgudev-dev
BuildRequires : libiscsi
BuildRequires : libiscsi-dev
BuildRequires : libstoragemgmt
BuildRequires : libstoragemgmt-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(blockdev)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libatasmart)
BuildRequires : pkgconfig(libconfig)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(mount)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(uuid)
BuildRequires : pygobject
BuildRequires : pygobject-dev
BuildRequires : python-dbusmock
BuildRequires : python-systemd
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : xdg-dbus-proxy
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-support-for-a-stateless-configuration-file.patch

%description
The Udisks project provides a daemon, tools and libraries to access and
manipulate disks, storage devices and technologies.

%package bin
Summary: bin components for the udisks2 package.
Group: Binaries
Requires: udisks2-data = %{version}-%{release}
Requires: udisks2-libexec = %{version}-%{release}
Requires: udisks2-config = %{version}-%{release}
Requires: udisks2-services = %{version}-%{release}

%description bin
bin components for the udisks2 package.


%package config
Summary: config components for the udisks2 package.
Group: Default

%description config
config components for the udisks2 package.


%package data
Summary: data components for the udisks2 package.
Group: Data

%description data
data components for the udisks2 package.


%package dev
Summary: dev components for the udisks2 package.
Group: Development
Requires: udisks2-lib = %{version}-%{release}
Requires: udisks2-bin = %{version}-%{release}
Requires: udisks2-data = %{version}-%{release}
Provides: udisks2-devel = %{version}-%{release}
Requires: udisks2 = %{version}-%{release}

%description dev
dev components for the udisks2 package.


%package lib
Summary: lib components for the udisks2 package.
Group: Libraries
Requires: udisks2-data = %{version}-%{release}
Requires: udisks2-libexec = %{version}-%{release}

%description lib
lib components for the udisks2 package.


%package libexec
Summary: libexec components for the udisks2 package.
Group: Default
Requires: udisks2-config = %{version}-%{release}

%description libexec
libexec components for the udisks2 package.


%package locales
Summary: locales components for the udisks2 package.
Group: Default

%description locales
locales components for the udisks2 package.


%package man
Summary: man components for the udisks2 package.
Group: Default

%description man
man components for the udisks2 package.


%package services
Summary: services components for the udisks2 package.
Group: Systemd services

%description services
services components for the udisks2 package.


%package staticdev
Summary: staticdev components for the udisks2 package.
Group: Default
Requires: udisks2-dev = %{version}-%{release}

%description staticdev
staticdev components for the udisks2 package.


%prep
%setup -q -n udisks2
cd %{_builddir}/udisks2
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628698629
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
##
export CXXFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CFFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags1 end
sd -r '\s--dirty\s' ' ' .
sd -r 'git describe' 'git describe --abbrev=0' .
%autogen  --enable-bcache \
--enable-btrfs \
--disable-lsm \
--disable-lvm2 \
--disable-lvmcache \
--disable-zram
make  %{?_smp_mflags}    V=1 VERBOSE=1


%install
export SOURCE_DATE_EPOCH=1628698629
rm -rf %{buildroot}
%make_install
%find_lang udisks2
## install_append content
mkdir -p %{buildroot}/usr/share/dbus-1/system.d/
cp data/org.freedesktop.UDisks2.conf %{buildroot}/usr/share/dbus-1/system.d/

mkdir -p %{buildroot}/usr/lib/udev/rules.d/
cp data/80-udisks2.rules %{buildroot}/usr/lib/udev/rules.d/

install -D udisks/udisks2.conf %{buildroot}/usr/share/defaults/udisks2/udisks2.conf
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/udisksctl
/usr/bin/umount.udisks2

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/udisks2.conf
/usr/lib/udev/rules.d/80-udisks2.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/UDisks-2.0.typelib
/usr/share/bash-completion/completions/udisksctl
/usr/share/dbus-1/system-services/org.freedesktop.UDisks2.service
/usr/share/dbus-1/system.d/org.freedesktop.UDisks2.conf
/usr/share/defaults/udisks2/udisks2.conf
/usr/share/gir-1.0/*.gir
/usr/share/polkit-1/actions/org.freedesktop.UDisks2.bcache.policy
/usr/share/polkit-1/actions/org.freedesktop.UDisks2.btrfs.policy
/usr/share/polkit-1/actions/org.freedesktop.UDisks2.policy

%files dev
%defattr(-,root,root,-)
/usr/include/udisks2/udisks/udisks-generated.h
/usr/include/udisks2/udisks/udisks.h
/usr/include/udisks2/udisks/udisksclient.h
/usr/include/udisks2/udisks/udisksenums.h
/usr/include/udisks2/udisks/udisksenumtypes.h
/usr/include/udisks2/udisks/udiskserror.h
/usr/include/udisks2/udisks/udisksobjectinfo.h
/usr/include/udisks2/udisks/udiskstypes.h
/usr/include/udisks2/udisks/udisksversion.h
/usr/lib64/libudisks2.so
/usr/lib64/pkgconfig/udisks2-bcache.pc
/usr/lib64/pkgconfig/udisks2-btrfs.pc
/usr/lib64/pkgconfig/udisks2.pc
/usr/lib64/udisks2/modules/libudisks2_bcache.so
/usr/lib64/udisks2/modules/libudisks2_btrfs.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libudisks2.so.0
/usr/lib64/libudisks2.so.0.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/udisks2/udisksd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/udisksctl.1
/usr/share/man/man5/udisks2.conf.5
/usr/share/man/man8/udisks.8
/usr/share/man/man8/udisksd.8
/usr/share/man/man8/umount.udisks2.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/udisks2.service

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libudisks2.a
/usr/lib64/udisks2/modules/libudisks2_bcache.a
/usr/lib64/udisks2/modules/libudisks2_btrfs.a

%files locales -f udisks2.lang
%defattr(-,root,root,-)
