Summary:	Multi-channel settings management support for XFce
Summary(pl):	Obsługa zarządzania ustawieniami wielokanałowymi dla XFce
Name:		libxfce4mcs
Version:	4.0.5
Release:	1
License:	LGPL
Group:		Libraries
#Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	a8d19a7d754f6800eb73e4e22c91424d
URL:		http://www.xfce.org/
BuildRequires:	automake
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
Requires:	libxfce4util >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-channel settings management support for XFce.

%description -l pl
Obsługa zarządzania ustawieniami wielokanałowymi dla XFce.

%package devel
Summary:	Development files for libxfce4mcs libraries
Summary(pl):	Pliki nagłówkowe bibliotek libxfce4mcs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxfce4util-devel >= %{version}

%description devel
Development files for the libxfce4mcs libraries.

%description devel -l pl
Pliki nagłówkowe bibliotek libxfce4mcs.

%package static
Summary:	Static libxfce4mcs libraries
Summary(pl):	Statyczne biblioteki libxfce4mcs
Group:		Development/Libriaries
Requires:	%{name}-devel = %{version}-%{release}

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
