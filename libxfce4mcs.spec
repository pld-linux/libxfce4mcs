Summary:	Multi-channel settings management support for XFce
Summary(pl):	Obs³uga zarz±dzania ustawieniami wielokana³owymi dla XFce
Name:		libxfce4mcs
Version:	4.0.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	cfd437f55f324c4b6c1908b17a1741b3
URL:		http://www.xfce.org/
BuildRequires:	automake
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
Requires:	libxfce4util >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-channel settings management support for XFce.

%description -l pl
Obs³uga zarz±dzania ustawieniami wielokana³owymi dla XFce.

%package devel
Summary:	Development files for libxfce4mcs libraries
Summary(pl):	Pliki nag³ówkowe bibliotek libxfce4mcs
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libxfce4util-devel >= %{version}

%description devel
Development files for the libxfce4mcs libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek libxfce4mcs.

%package static
Summary:	Static libxfce4mcs libraries
Summary(pl):	Statyczne biblioteki libxfce4mcs
Group:		Development/Libriaries
Requires:	%{name}-devel = %{version}

%description static
Static libxfce4mcs libraries.

%description static -l pl
Statyczne biblioteki libxfce4mcs.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/xfce4/libxfce4mcs
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
