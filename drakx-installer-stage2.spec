%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define	family	drakx-installer

Summary:	DrakX installer stage2 image
Name:		%{family}-stage2
Version:	14.33
Release:	2
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.mandriva.com/Tools/DrakX

BuildRequires:	squashfs-tools >= 4.0
BuildRequires:	perl-devel ldetect-devel >= 0.9.1
BuildRequires:	drakx-installer-binaries parted-devel
BuildRequires:	gdk-pixbuf2.0 gtk2-modules parted-devel
BuildRequires:	perl-Gtk2 perl-Glib perl-XML-Parser perl-Curses perl-Curses-UI
BuildRequires:	perl-Term-ReadKey perl-Net-Ping pixman-devel >= 0.15.18
BuildRequires:	perl-Locale-gettext packdrake perl-Clone
BuildRequires:	drakx-net >= 0.98 drakx-kbd-mouse-x11 >= 0.83
BuildRequires:	perl-MDK-Common >= 1.2.25 perl-Pango >= 1.223
BuildRequires:	urpmi >= 6.27
BuildRequires:	perl-URPM >= 4.43
BuildRequires:	perl_checker
BuildRequires:	meta-task
BuildRequires:	ldetect-lst >= 0.1.277
BuildRequires:	draksnapshot
# progs
BuildRequires:	drakx-installer-matchbox
BuildRequires:	e2fsprogs >= 1.41.6
BuildRequires:	dosfstools mtools
BuildRequires:	pkgconfig(x11) libxxf86misc-devel
BuildRequires:	x11-driver-video-fbdev x11-driver-input-vmmouse
BuildRequires:	x11-data-xkbdata >= 1.8-2
BuildRequires:	setserial pciutils mt-st reiserfsprogs jfsutils
BuildRequires:	xfsprogs pcmciautils gettext ash linuxwacom
BuildRequires:	fonts-ttf-bengali fonts-ttf-bitstream-vera fonts-ttf-lohit
BuildRequires:	fonts-ttf-thai fonts-ttf-devanagari fonts-ttf-wqy-microhei fonts-ttf-dejavu
BuildRequires:	fb2png ntfsprogs ia_ora-gnome brltty >= 4.4-1
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
BuildRequires:	pkgconfig(libtirpc)

%description
This is the stage2 image for Mandriva DrakX installer.

%prep
%setup -q

%build
%make -C tools CFLAGS="%{optflags} -Os" LDFLAGS="%{ldflags}"
%make -C perl-install/install CFLAGS="%{optflags} -Os" LDFLAGS="%{ldflags}"
rpm -qa | sort > build-rpms.lst

%install
%makeinstall_std -C perl-install/install
%makeinstall_std -C tools
rm -rf %{buildroot}%{_libdir}/%{family}/root/install/stage2/live

%check
%make -C perl-install check_perl_checker

%files
%doc build-rpms.lst
%dir %{_libdir}/%{family}
%dir %{_libdir}/%{family}/root
%dir %{_libdir}/%{family}/root/install
%dir %{_libdir}/%{family}/root/install/stage2
%{_libdir}/%{family}/root/install/stage2/VERSIONN
%{_libdir}/%{family}/root/install/stage2/mdkinst.cpio.xz
%dir %{_libdir}/%{family}/root/misc
%{_libdir}/%{family}/root/misc/*
