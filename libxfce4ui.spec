%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 0
%define api 1
%define majorkbd 0
%define apikbd 2
%define libname %mklibname xfce4ui %{api} %{major}
%define libnamekbd %mklibname xfce4kbd-private %{apikbd} %{majorkbd}
%define develname %mklibname xfce4ui -d

Summary:	Various Xfce widgets for Xfce desktop environment
Name:		libxfce4ui
Version: 	4.9.1
Release: 	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/libxfce4ui/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel >= 2.0.6
BuildRequires:	libxfce4util-devel >= 4.9.0
BuildRequires:	startup-notification-devel
BuildRequires:	xfce4-dev-tools >= 4.9.0
BuildRequires:	glade3-devel
BuildRequires:	xfconf-devel >= 4.9.0
BuildRequires:	libsm-devel

%description
Various Xfce widgets for Xfce desktop environment.

%package -n %{libname}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Requires:	%{name}-common = %{version}-%{release}

%description -n %{libname}
Gui libraries for Xfce desktop environment.

%package -n %{libnamekbd}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Requires:	%{name}-common = %{version}-%{release}
Conflicts:	%{_lib}xfce4ui1_0 < 4.8.1-1

%description -n %{libnamekbd}
Gui libraries for Xfce desktop environment.

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
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnamekbd} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-startup-notification \
	--enable-gladeui \
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
%{_libdir}/libxfce4kbd-private-%{apikbd}.so.%{majorkbd}*

%files -n %{name}-glade
%{_libdir}/glade3/modules/%{name}*
%{_datadir}/glade3/catalogs/%{name}.*
%{_datadir}/glade3/pixmaps/hicolor/*/*/*%{name}*.png

%files -n %{develname}
%doc AUTHORS ChangeLog README NEWS
%doc %{_datadir}/gtk-doc/html/%{name}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*xfce4kbd-private-%{apikbd}.so
%{_includedir}/xfce4/%{name}-*
%{_includedir}/xfce4/*xfce4kbd-private-%{apikbd}
