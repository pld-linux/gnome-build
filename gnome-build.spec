Summary:	GNOME Build Framework (GBF)
Summary(pl):	Struktura GNOME Build (GBF)
Name:		gnome-build
Version:	0.1.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-build/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	713fc135e7d3471736f0480d633bf180
BuildRequires:	automake
BuildRequires:	gdl-devel >= 0.5.0
BuildRequires:	gnome-vfs2-devel >= 2.3.5
BuildRequires:	libbonoboui-devel >= 2.3.3
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.3.3
BuildRequires:	libxml2-devel >= 2.5.8
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Build Framework (GBF).

%description -l pl
Struktura GNOME Build (GBF).

%package devel
Summary:	Header files for gnome-build
Summary(pl):	Pliki nag³ówkowe gnome-build
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gnome-build.

%description devel -l pl
Pliki nag³ówkowe gnome-build.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--enable-compile-warnings=maximum
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang gbf-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f gbf-1.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}-1.0
%dir %{_libdir}/%{name}-1.0/backends
%attr(755,root,root) %{_libdir}/%{name}-1.0/backends/lib*.so*
%{_libdir}/%{name}-1.0/backends/lib*.la
%{_libdir}/%{name}-1.0/backends/gbf-am.server
%{_datadir}/%{name}
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-1.0
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
