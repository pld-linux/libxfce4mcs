
%define		_snap 20040816

Summary:	Multi-channel settings management support for XFce
Summary(pl):	Obs³uga zarz±dzania ustawieniami wielokana³owymi dla XFce
Name:		libxfce4mcs
Version:	4.1.3
Release:	0.%{_snap}.1
License:	LGPL
Group:		Libraries
Source0:	http://ep09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	6d3e7f1432bd42eafa95e9cc1a4be762
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= 4.1.13
BuildRequires:	pkgconfig >= 0.9.0
Requires:	libxfce4util >= 4.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-channel settings management support for XFce.

%description -l pl
Obs³uga zarz±dzania ustawieniami wielokana³owymi dla XFce.

%package devel
Summary:	Development files for libxfce4mcs libraries
Summary(pl):	Pliki nag³ówkowe bibliotek libxfce4mcs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxfce4util-devel >= 4.1.13

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
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
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
