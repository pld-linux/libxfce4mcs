Summary: 	Multi-channel settings management support for xfce
Summary(pl):	Obs³uga zarz±dzania ustawieniami wielokana³owymi dla xfce
Name: 		libxfce4mcs
Version: 	3.91.0
Release: 	0.1
License:	LGPL
Group: 		Libraries
Source0: 	http://dl.sourceforge.net/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	9f3bf8d17993100f10c79a239aed0c54
URL: 		http://www.xfce.org/
BuildRequires: 	libxfce4util-devel >= 3.90.0
BuildRequires:	pkgconfig >= 0.9.0
Requires:	libxfce4util >= 3.90.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-channel settings management support for xfce.

%description -l pl
Obs³uga zarz±dzania ustawieniami wielokana³owymi dla xfce.

%package devel
Summary:	Development files for libxfce4mcs libraries
Summary(pl):	Pliki nag³ówkowe bibliotek libxfce4mcs
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libxfce4util-devel

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
