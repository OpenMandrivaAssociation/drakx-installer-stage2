%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define	family	drakx-installer

Summary:	DrakX installer stage2 image
Name:		%{family}-stage2
Version:	16.29
Release:	1
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.mandriva.com/Tools/DrakX

# needed for tracing what files to collect
BuildRequires:	strace
# for compiling the c module:
BuildRequires:	perl-devel ldetect-devel >= 0.13.9
BuildRequires:	parted-devel
# for pcmcia-probe.o:
BuildRequires:	drakx-installer-binaries 
# graphical stack:
BuildRequires:	task-x11
BuildRequires:	x11-data-xkbdata >= 1.8-2
BuildRequires:	xmodmap xset monitor-edid
# toolkit
BuildRequires:	gdk-pixbuf2.0 
BuildRequires:	perl-Gtk3 >= 0.14.0-8
BuildRequires:	perl-Gtk3-WebKit
BuildRequires:	adwaita-icon-theme >= 3.13.1
# for introspection:
BuildRequires:	%{_lib}atk-gir1.0
BuildRequires:	%{_lib}cairo-gir1.0
BuildRequires:	%{_lib}gdk_pixbuf-gir2.0
BuildRequires:	%{_lib}glib-gir2.0
BuildRequires:	%{_lib}gtk-gir3.0 >= 3.10.5-2
BuildRequires:	%{_lib}pango-gir1.0
BuildRequires:	%{_lib}xlib-gir2.0
# wm:
# (to be replaced by sg else? mutter?)
BuildRequires:	drakx-installer-matchbox
# drivers:
BuildRequires:	x11-driver-input-keyboard x11-driver-input-mouse
BuildRequires:	x11-driver-input-vmmouse x11-driver-input-wacom
BuildRequires:	x11-driver-video-fbdev x11-driver-video-vesa
# theme:
BuildRequires:	adwaita-gtk3-theme
BuildRequires:	oxygen-gtk3
# for matchbox WM:
BuildRequires:	ia_ora-gnome
# Text mode:
BuildRequires:	perl(Curses) perl(Curses::UI) perl(Term::ReadKey)
# Misc perl modules:
BuildRequires:	drakx-kbd-mouse-x11 >= 1.0
BuildRequires:	drakx-net >= 2.0
BuildRequires:	perl(Clone)
BuildRequires:	perl(MDK::Common) >= 1.2.28
BuildRequires:	perl(Net::Ping)
BuildRequires:	perl(XML::Parser) perl(XML::SAX::Base) perl(XML::LibXML)
# urpmi:
BuildRequires:	aria2 >= 1.18.1-2
BuildRequires:	urpmi >= 7.29
# for compssUsers.pl:
BuildRequires:	meta-task
# HW enumeration:
BuildRequires:	ldetect-lst >= 0.1.327
BuildRequires:	pciutils
# Fonts:
BuildRequires:	fonts-ttf-bengali fonts-ttf-bitstream-vera fonts-ttf-lohit
BuildRequires:	fonts-ttf-dejavu fonts-ttf-thai fonts-ttf-devanagari
BuildRequires:	fonts-ttf-wqy-microhei
# locales:
BuildRequires:	gettext glibc-i18ndata locales
BuildRequires:	perl_checker perl-Locale-gettext 
# for mime.cache:
BuildRequires:	shared-mime-info
# display for blind people:
BuildRequires:	brltty
# for screenshots:
BuildRequires:	fb2png
# misc:
BuildRequires:	draksnapshot
# help:
BuildRequires:	drakx-installer-help

BuildRequires:	kbd
BuildRequires:	digger
BuildRequires:	gimp gimp-python pngrewrite
BuildRequires:	gtk3-modules oxygen-gtk3-engine gtk+3.0-common
BuildRequires:	typelib(GdkX11) = 3.0 #typelib(JavaScriptCore) = 3.0
BuildRequires:	pkgconfig(libtirpc)
BuildRequires:	perl(Parse::EDID)
# workaround..
BuildConflicts: %{name}
BuildRequires:	xauth iceauth rgb x11-data-cursor-themes xhost x11-font-misc-misc x11-font-cursor-misc 
BuildRequires:	x11-font-alias setxkbmap x11-server-xorg xinit fonts-ttf-dejavu fonts-ttf-liberation xev
BuildRequires:	digger


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
%{_libdir}/%{family}/root/install/stage2/VERSION
%{_libdir}/%{family}/root/install/stage2/mdkinst.cpio.xz
%dir %{_libdir}/%{family}/root/misc
%{_libdir}/%{family}/root/misc/*
