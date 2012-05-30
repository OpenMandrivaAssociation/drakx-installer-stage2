%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	DrakX installer stage2 image
Name:		drakx-installer-stage2
Version:	14.22
Release:	2
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.mandriva.com/Tools/DrakX

BuildRequires:	squashfs-tools >= 4.0
BuildRequires:	libx11-devel perl-devel ldetect-devel >= 0.9.1
BuildRequires:	drakx-installer-binaries parted-devel
BuildRequires:	libgdk_pixbuf2.0 parted-devel
BuildRequires:	perl-Gtk2 perl-Glib perl-XML-Parser perl-Curses perl-Curses-UI
BuildRequires:	perl-Term-ReadKey perl-Net-Ping pixman-devel >= 0.15.18
BuildRequires:	perl-Locale-gettext packdrake perl-Clone
BuildRequires:	drakx-net >= 0.97 drakx-kbd-mouse-x11 >= 0.83
BuildRequires:	perl-MDK-Common >= 1.2.25
BuildRequires:	urpmi >= 6.27
BuildRequires:	perl-URPM >= 3.26
BuildRequires:	perl_checker
BuildRequires:	meta-task
BuildRequires:	ldetect-lst >= 0.1.277
BuildRequires:	draksnapshot
# progs
BuildRequires:	drakx-installer-matchbox
BuildRequires:	e2fsprogs >= 1.41.6
BuildRequires:	dosfstools mtools
BuildRequires:	task-x11 libx11-devel libxxf86misc-devel
BuildRequires:	x11-driver-video-fbdev x11-driver-input-vmmouse
BuildRequires:	x11-data-xkbdata >= 1.8-2
BuildRequires:	setserial pciutils mt-st reiserfsprogs jfsutils
BuildRequires:	xfsprogs pcmcia-cs gettext ash linuxwacom
BuildRequires:	fonts-ttf-bengali fonts-ttf-bitstream-vera fonts-ttf-lohit
BuildRequires:	fonts-ttf-thai fonts-ttf-devanagari fonts-ttf-wqy-microhei fonts-ttf-dejavu
BuildRequires:	fb2png ntfsprogs ia_ora-gnome brltty
BuildRequires:	lvm2 glibc-i18ndata
BuildRequires:	dmraid mdadm quota
BuildRequires:	losetup xmodmap xset monitor-edid locales
BuildRequires:	perl-Gtk2-WebKit mandriva-doc-installer-help
BuildRequires:	nfs-utils-clients
BuildRequires:	ntfs-3g
BuildRequires:	btrfs-progs
BuildRequires:	nilfs-utils
BuildRequires:	aria2
BuildRequires:	parted
BuildRequires:	cryptsetup
BuildRequires:	x11-driver-video-vesa
BuildRequires:	x11-driver-input-keyboard
BuildRequires:	x11-driver-input-mouse
BuildRequires:	shared-mime-info

%description
This is the stage2 image for Mandriva DrakX installer.

%prep
%setup -q

%build
make -C tools
make -C perl-install/install
rpm -qa | sort > build-rpms.lst

%install
dest=%{buildroot}%{_libdir}/%{name}
mkdir -p $dest
make -C perl-install/install install ROOTDEST=$dest
make -C tools install ROOTDEST=$dest

%check
cd perl-install
%make check_perl_checker

%files
%doc build-rpms.lst
%{_libdir}/%{name}
