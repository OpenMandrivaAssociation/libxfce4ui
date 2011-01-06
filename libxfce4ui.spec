%define url_ver %(echo %{version} | cut -c 1-3)
%define major 0
%define api 1
%define majorkbd 0
%define apikbd 2
%define libname %mklibname xfce4ui %{api} %{major}
%define develname %mklibname xfce4ui -d

Summary:	Various Xfce widgets for Xfce desktop environment
Name:		libxfce4ui
Version: 	4.7.6
Release: 	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/libxfce4ui/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel >= 2.0.6
BuildRequires:	libxfce4util-devel >= 4.6.0
BuildRequires:	startup-notification-devel
#BuildRequires:	gettext-devel
BuildRequires:	xfce4-dev-tools >= 4.6.0
#BuildRequires:	libglade2-devel
BuildRequires:	glade3-devel
BuildRequires:	xfconf-devel >= 4.6.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Various Xfce widgets for Xfce desktop environment.

%package -n %{libname}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce

%description -n %{libname}
Gui libraries for Xfce desktop environment.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q

%build
%configure2_5x \
%if %mdkversion < 200900
	--sysconfdir=%{_sysconfdir}/X11 \
%endif
	--disable-static \
	--enable-startup-notification

%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rr %{buildroot}%{_libdir}/*.la

# (tpg) this file is in mandriva-xfce-config package
rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/libxfce4ui-%{api}.so.%{major}*
%{_libdir}/libxfce4kbd-private-%{apikbd}.so.%{majorkbd}*
%{_libdir}/glade3/modules/%{name}*
%{_datadir}/glade3/catalogs/%{name}.*
%{_datadir}/glade3/pixmaps/hicolor/*/*/*%{name}*.png

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
%{_libdir}/%{name}-%{api}.so
%{_includedir}/xfce4/%{name}-*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/%{name}
%{_libdir}/*xfce4kbd-private-%{apikbd}.so
%{_includedir}/xfce4/*xfce4kbd-private-%{apikbd}
