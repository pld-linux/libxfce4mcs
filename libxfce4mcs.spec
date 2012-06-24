Summary:	Multi-channel settings management support for XFce
Summary(pl):	Obs�uga zarz�dzania ustawieniami wielokana�owymi dla XFce
Name:		libxfce4mcs
Version:	4.1.99.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7f9823b4e73788bc428031deae022160
URL:		http://www.xfce.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= 4.1.13
BuildRequires:	pkgconfig >= 0.9.0
Requires:	libxfce4util >= 4.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-channel settings management support for XFce.

%description -l pl
Obs�uga zarz�dzania ustawieniami wielokana�owymi dla XFce.

%package devel
Summary:	Development files for libxfce4mcs libraries
Summary(pl):	Pliki nag��wkowe bibliotek libxfce4mcs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel
Requires:	gtk-doc-common
Requires:	libxfce4util-devel >= 4.1.13

%description devel
Development files for the libxfce4mcs libraries.

%description devel -l pl
Pliki nag��wkowe bibliotek libxfce4mcs.

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
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--with-html-dir=%{_gtkdocdir}
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
%{_gtkdocdir}/libxfce4mcs

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
