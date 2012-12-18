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
Version: 	4.10.0
Release: 	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/libxfce4ui/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gdk-2.0) >= 2.0.6
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.10.0
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	xfce4-dev-tools >= 4.10.0
BuildRequires:	pkgconfig(gladeui-1.0)
BuildRequires:	xfconf-devel >= 4.9.0
BuildRequires:	pkgconfig(sm)

%description
Various Xfce widgets for Xfce desktop environment.

%package -n %{libname}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Requires:	%{name}-common = %{version}

%description -n %{libname}
Gui libraries for Xfce desktop environment.

%package -n %{libnamekbd}
Summary:	Gui libraries for Xfce
Group:		Graphical desktop/Xfce
Requires:	%{name}-common = %{version}
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
Requires:	%{libname} = %{version}
Requires:	%{libnamekbd} = %{version}
Provides:	%{name}-devel = %{EVRD}

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
#rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

%find_lang %{name} %{name}.lang

%files common -f %{name}.lang
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/*.xml
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


%changelog
* Mon Apr 30 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 794637
- update to new version 4.10.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.2-1
+ Revision: 791036
- update to new version 4.9.2

* Tue Apr 03 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.1-2
+ Revision: 788903
- subpackage common is no more noarch

* Tue Apr 03 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.1-1
+ Revision: 788897
- drop patch 0
- fix file list
- update to new version 4.9.1
- remove old stuff from spec file

* Fri Jan 06 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-2
+ Revision: 757980
- add missing requires to develname subpackage

* Tue Dec 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-1
+ Revision: 745813
- Patch0: fix linking
- drop la files
- split out glade and xfce4kbd-private libraries into subpackages
- update to new version 4.8.1

* Thu Sep 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-2
+ Revision: 700918
- rebuild for new libpng15
- rebuild for new libpng15

* Thu Jan 20 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 631890
- update to new version 4.8.0

* Thu Jan 06 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.6-1mdv2011.0
+ Revision: 629093
- update to new version 4.7.6

* Fri Dec 17 2010 Götz Waschk <waschk@mandriva.org> 4.7.5-2mdv2011.0
+ Revision: 622587
- rebuild for new libgladeui

* Thu Dec 02 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.5-1mdv2011.0
+ Revision: 605586
- update to new version 4.7.5

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.4-1mdv2011.0
+ Revision: 593800
- update to new version 4.7.4
- use rm instead of %%exclude macro

* Fri Sep 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.3-2mdv2011.0
+ Revision: 579286
- rebuild

* Thu Sep 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.3-1mdv2011.0
+ Revision: 579050
- update to new version 4.7.3

* Sat Aug 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-1mdv2011.0
+ Revision: 567410
- update to new version 4.7.2

* Fri Aug 06 2010 Götz Waschk <waschk@mandriva.org> 4.7.1-2mdv2011.0
+ Revision: 566636
- rebuild for new glade3

* Thu Feb 25 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.1-1mdv2010.1
+ Revision: 511200
- update to new version 4.7.1
- import libxfce4ui


