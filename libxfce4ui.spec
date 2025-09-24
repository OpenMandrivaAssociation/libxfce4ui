%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 0
%define api 2
%define gmajor	2.0
%define libname %mklibname xfce4ui
%define oldlibname %mklibname xfce4ui 2 0
%define libnamekbd %mklibname xfce4kbd-private %{apikbd} %{major}
%define oldlibnamekbd %mklibname xfce4kbd-private 3 0
%define develname %mklibname xfce4ui -d
%define girname %mklibname %{name}-gir

%define api3 2
%define apikbd 3


Summary:	Various Xfce widgets for Xfce desktop environment
Name:		libxfce4ui
Version:	4.20.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://www.xfce.org
Source0:	https://archive.xfce.org/src/xfce/libxfce4ui/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	intltool
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(harfbuzz-gobject)
BuildRequires:	xfce4-dev-tools

%description
Various Xfce widgets for Xfce desktop environment.

%package -n %{libname}
Summary:	GTK3 Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Requires:	%{name}-common = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
GTK3 Gui libraries for Xfce desktop environment.

%files -n %{libname}
%{_libdir}/libxfce4ui-%{api3}.so.%{major}*


#---------------------------------------------------------------------------

%package -n %{libnamekbd}
Summary:	GTK3 GUI libraries for Xfce
Group:		Graphical desktop/Xfce
%rename %{oldlibnamekbd}

%description -n %{libnamekbd}
GTK3 GUI libraries for Xfce desktop environment.

%files -n %{libnamekbd}
%{_libdir}/libxfce4kbd-private-%{apikbd}.so.%{major}*

#---------------------------------------------------------------------------

%package common
Summary:	Common files for %{name}
Group:		Graphical desktop/Xfce
Conflicts:      %{_lib}xfce4ui1_0 < 4.8.1-1

%description common
This package contains common files for %{name}.

%files common -f %{name}.lang
%{_bindir}/xfce4-about
%{_datadir}/applications/xfce4-about.desktop
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
%{_iconsdir}/hicolor/*/apps/org.xfce.about.{png,svg}
%{_iconsdir}/hicolor/*/apps/xfce4-logo.{png,svg}

#---------------------------------------------------------------------------

%package -n %{name}-glade
Summary:	Glade modules for %{name}
Group:		Graphical desktop/Xfce
Requires:	glade
Conflicts:	%{_lib}xfce4ui1_0 < 4.8.1-1

%description -n %{name}-glade
This package provides a catalog for Glade which allows the use of the
provided Xfce widgets in Glade.

%files -n %{name}-glade
%{_libdir}/glade/modules/libxfce4uiglade2.so
%{_datadir}/glade/catalogs/libxfce4ui-2.xml
%{_datadir}/glade/pixmaps/hicolor/*x*/actions/widget-libxfce4ui-xfce-titled-dialog.png

#---------------------------------------------------------------------------

%package -n %{girname}
Summary: GObject Introspection interface for %{name}
Group: System/Libraries
Requires: %{libname} >= %{EVRD}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/Libxfce4ui-%{gmajor}.typelib

#---------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files and headers for the %{name} library using GTK3
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	%{libnamekbd} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{_lib}xfce4ui-devel < 4.12.1-1

%description -n %{develname}
Development files and headers for the %{name} library using GTK3.

%files -n %{develname}
%doc AUTHORS ChangeLog README.md NEWS
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/pkgconfig/libxfce4kbd-private-%{apikbd}.pc
%{_libdir}/pkgconfig/libxfce4ui-%{api3}.pc
%{_libdir}/%{name}-%{api3}.so
%{_libdir}/libxfce4kbd-private-%{apikbd}.so
%{_includedir}/xfce4/%{name}-%{api3}/
%{_includedir}/xfce4/libxfce4kbd-private-%{apikbd}/
%{_datadir}/gir-1.0/Libxfce4ui-%{gmajor}.gir
%{_datadir}/vala/vapi/libxfce4ui-2.{deps,vapi}

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure \
	--enable-gtk3 \
	--enable-introspection \
	--enable-startup-notification \
	--with-vendor-info=%{vendor}
%make_build

%install
%make_install

# (tpg) this file is in distro-xfce-config package
#rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

# locales
%find_lang %{name} %{name}.lang
