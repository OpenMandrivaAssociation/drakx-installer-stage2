%define name drakx-installer-stage2
%define version 10.4.224
%define release %mkrel 1

%define ldetect_lst_version %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' ldetect-lst)

Summary: DrakX installer stage2 image
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+
Group: Development/Other
Url: http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: squashfs-tools
BuildRequires: librpm >= 4.4.8-21mdv2008.0
BuildRequires: libx11-devel perl-devel libldetect-devel drakx-installer-binaries
BuildRequires: perl-Gtk2 perl-Glib perl-XML-Parser perl-Curses perl-Curses-UI perl-Term-ReadKey
BuildRequires: perl-Locale-gettext packdrake
BuildRequires: drakx-net >= 0.11
BuildRequires: drakx-kbd-mouse-x11 >= 0.32
BuildRequires: rpm-mandriva-setup >= 1.48
BuildRequires: perl-MDK-Common >= 1.2.7
BuildRequires: urpmi >= 4.10.1
BuildRequires: perl-URPM >= 2.07
BuildRequires: meta-task
# progs
BuildRequires: e2fsprogs dosfstools 
BuildRequires: task-x11 libx11-devel libxxf86misc-devel x11-driver-video-fbdev
BuildRequires: setserial pciutils mt-st reiserfsprogs jfsprogs
BuildRequires: xfsprogs pcmcia-cs gettext ash linuxwacom
BuildRequires: fonts-ttf-bengali fonts-ttf-bitstream-vera fonts-ttf-gurmukhi fonts-ttf-thai fonts-ttf-devanagari
BuildRequires: fb2png ntfsprogs ia_ora-gnome brltty
BuildRequires: lvm2 glibc-i18ndata
BuildRequires: dmraid mdadm quota
BuildRequires: losetup xmodmap xset monitor-edid locales
BuildRequires: perl-Gtk2-Html2 mandriva-doc-installer-help
BuildRequires: nfs-utils-clients

#- require the version used during build
Requires: ldetect-lst = %ldetect_lst_version

%description
This is the stage2 image for Mandriva DrakX installer.

%prep
%setup -q

%build
make -C tools
make -C perl-install/install

%install
rm -rf $RPM_BUILD_ROOT

dest=$RPM_BUILD_ROOT%{_libdir}/%name
mkdir -p $dest
make -C perl-install/install install ROOTDEST=$dest
make -C tools install ROOTDEST=$dest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/%name


