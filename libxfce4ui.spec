%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 0
%define api 1
%define apikbd 2
%define libname %mklibname xfce4ui %{api} %{major}
%define libnamekbd %mklibname xfce4kbd-private %{apikbd} %{major}
%define develname %mklibname xfce4ui -d

%define api3 2
%define apikbd3 3
%define libname3 %mklibname xfce4ui %{api3} %{major}
%define libnamekbd3 %mklibname xfce4kbd-private %{apikbd3} %{major}
%define develname3 %mklibname xfce4ui %{api3} -d

Summary:	Various Xfce widgets for Xfce desktop environment
Name:		libxfce4ui
Version: 	4.12.1
Release: 	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/libxfce4ui/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gdk-2.0) >= 2.0.6
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	pkgconfig(gladeui-1.0)
BuildRequires:	xfconf-devel >= 4.12.0
BuildRequires:	pkgconfig(sm)

%description
Various Xfce widgets for Xfce desktop environment.

%package -n %{libname}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Requires:	%{name}-common = %{EVRD}

%description -n %{libname}
Gui libraries for Xfce desktop environment.

%package -n %{libnamekbd}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Requires:	%{name}-common = %{EVRD}
Conflicts:	%{_lib}xfce4ui1_0 < 4.8.1-1

%description -n %{libnamekbd}
Gui libraries for Xfce desktop environment.

%package -n %{libname3}
Summary:	GTK3 GUI libraries for Xfce
Group:		Graphical desktop/Xfce
Requires:	%{name} >= %{EVRD}

%description -n %{libname3}
GTK3 GUI libraries for Xfce desktop environment.

%package -n %{libnamekbd3}
Summary:	GTK3 GUI libraries for Xfce
Group:		Graphical desktop/Xfce

%description -n %{libnamekbd3}
GTK3 GUI libraries for Xfce desktop environment

%package common
Summary:	Common files for %{name}
Group:		Graphical desktop/Xfce
Conflicts:      %{_lib}xfce4ui1_0 < 4.8.1-1

%description common
This package contains common files for %{name}.

%package -n %{name}-glade
Summary:	Glade modules for %{name}
Group:		Graphical desktop/Xfce
Requires:	glade3
Conflicts:	%{_lib}xfce4ui1_0 < 4.8.1-1

%description -n %{name}-glade
This package provides a catalog for Glade which allows the use of the
provided Xfce widgets in Glade.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	%{libnamekbd} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}xfce4ui-devel < 4.12.1-1

%description -n %{develname}
Libraries and header files for the %{name} library.

%package -n %{develname3}
Summary:	Development files and headers for the %{name} library using GTK3
Group:		Development/Other
Requires:	%{libname3} = %{EVRD}
Requires:	%{libnamekbd3} = %{EVRD}
Conflicts:	%{_lib}xfce4ui-devel < 4.12.1-1

%description -n %{develname3}
Development files and headers for the %{name} library using GTK3.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-gtk-doc \
	--enable-startup-notification \
	--enable-gladeui \
	--enable-gtk3 \
	--with-vendor-info=%{vendor}

%make

%install
%makeinstall_std

# (tpg) this file is in mandriva-xfce-config package
rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

%find_lang %{name} %{name}.lang

%files common -f %{name}.lang
%{_bindir}/xfce4-about
%{_datadir}/applications/xfce4-about.desktop
%{_iconsdir}/hicolor/*/apps/xfce4-logo.png

%files -n %{libname}
%{_libdir}/libxfce4ui-%{api}.so.%{major}*

%files -n %{libnamekbd}
%{_libdir}/libxfce4kbd-private-%{apikbd}.so.%{major}*

%files -n %{libname3}
%{_libdir}/libxfce4ui-%{api3}.so.%{major}*

%files -n %{libnamekbd3}
%{_libdir}/libxfce4kbd-private-%{apikbd3}.so.%{major}*

%files -n %{name}-glade
%{_libdir}/glade3/modules/%{name}*
%{_datadir}/glade3/catalogs/%{name}.*
%{_datadir}/glade3/pixmaps/hicolor/*/*/*%{name}*.png

%files -n %{develname}
%doc AUTHORS ChangeLog README NEWS
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/%{name}-%{api}.so
%{_libdir}/libxfce4kbd-private-%{apikbd}.so
%{_libdir}/pkgconfig/libxfce4kbd-private-%{apikbd}.pc
%{_libdir}/pkgconfig/libxfce4ui-%{api}.pc
%{_includedir}/xfce4/%{name}-%{api}/
%{_includedir}/xfce4/libxfce4kbd-private-%{apikbd}/

%files -n %{develname3}
%{_libdir}/pkgconfig/libxfce4kbd-private-%{apikbd3}.pc
%{_libdir}/pkgconfig/libxfce4ui-%{api3}.pc
%{_libdir}/%{name}-%{api3}.so
%{_libdir}/libxfce4kbd-private-%{apikbd3}.so
%{_includedir}/xfce4/%{name}-%{api3}/
%{_includedir}/xfce4/libxfce4kbd-private-%{apikbd3}/
