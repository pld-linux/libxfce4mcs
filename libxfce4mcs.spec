Summary: 	Multi-channel settings management support for xfce
Name: 		libxfce4mcs
Version: 	3.90.0
Release: 	0.1
License:	LGPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	3efa99233d3c221cdb7465c89b2c2211
Group: 		Development/Libraries
Requires:	libxfce4util >= 3.90.0
BuildRequires: 	libxfce4util-devel >= 3.90.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-channel settings management support for xfce.

%package devel
Summary:	Development tools for libxfce4mcs library
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for the libxfce4mcs library.

%package static
Summary:	Static libraries for libxfce4mcs
Group:		Development/Libriaries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for libxfce4mcs.


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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/libxfce4mcs

%files static
%defattr(644,root,root,755)
%{_libdir}/*a
