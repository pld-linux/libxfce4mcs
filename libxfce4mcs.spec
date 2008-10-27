#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Multi-channel settings management support for Xfce
Summary(pl.UTF-8):	Obsługa zarządzania ustawieniami wielokanałowymi dla Xfce
Name:		libxfce4mcs
Version:	4.4.3
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	c50846b0ad090c2434ca4df1d060cc98
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk-doc-automake
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xfce4-dev-tools >= 4.4.0.1
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-channel settings management support for Xfce.

%description -l pl.UTF-8
Obsługa zarządzania ustawieniami wielokanałowymi dla Xfce.

%package apidocs
Summary:	libxfce4mcs API documentation
Summary(pl.UTF-8):	Dokumentacja API libxfce4mcs
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfce4mcs API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxfce4mcs.

%package devel
Summary:	Development files for libxfce4mcs libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libxfce4mcs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxfce4util-devel >= %{version}
Requires:	startup-notification-devel >= 0.8
Requires:	xorg-lib-libX11-devel

%description devel
Development files for the libxfce4mcs libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libxfce4mcs.

%package static
Summary:	Static libxfce4mcs libraries
Summary(pl.UTF-8):	Statyczne biblioteki libxfce4mcs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfce4mcs libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libxfce4mcs.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-gtkdoc \
	--with-html-dir=%{_gtkdocdir} \
	--%{?with_static_libs:en}%{!?with_static_libs:dis}able-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxfce4mcs-client.so.*.*.*
%attr(755,root,root) %{_libdir}/libxfce4mcs-manager.so.*.*.*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4mcs-client.so
%attr(755,root,root) %{_libdir}/libxfce4mcs-manager.so
%{_libdir}/libxfce4mcs-client.la
%{_libdir}/libxfce4mcs-manager.la
%{_includedir}/xfce4/libxfce4mcs
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfce4mcs-client.a
%{_libdir}/libxfce4mcs-manager.a
%endif
