#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Multi-channel settings management support for Xfce
Summary(pl):	Obs³uga zarz±dzania ustawieniami wielokana³owymi dla Xfce
Name:		libxfce4mcs
Version:	4.4.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	224863509b7f546fa1ca198374c424d3
URL:		http://www.xfce.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk-doc-automake
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xfce4-dev-tools >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-channel settings management support for Xfce.

%description -l pl
Obs³uga zarz±dzania ustawieniami wielokana³owymi dla Xfce.

%package apidocs
Summary:	libxfce4mcs API documentation
Summary(pl):	Dokumentacja API libxfce4mcs
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfce4mcs API documentation.

%description apidocs -l pl
Dokumentacja API libxfce4mcs.

%package devel
Summary:	Development files for libxfce4mcs libraries
Summary(pl):	Pliki nag³ówkowe bibliotek libxfce4mcs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel
Requires:	libxfce4util-devel >= %{version}
Requires:	startup-notification-devel >= 0.8

%description devel
Development files for the libxfce4mcs libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek libxfce4mcs.

%package static
Summary:	Static libxfce4mcs libraries
Summary(pl):	Statyczne biblioteki libxfce4mcs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfce4mcs libraries.

%description static -l pl
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/xfce4/libxfce4mcs
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
