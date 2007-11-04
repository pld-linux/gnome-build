Summary:	GNOME Build Framework (GBF)
Summary(pl.UTF-8):	Struktura GNOME Build (GBF)
Name:		gnome-build
Version:	0.2.0
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-build/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	97ba7c81f47c39b191d9aae9ea173084
BuildRequires:	automake
BuildRequires:	gdl-devel >= 0.7.5
BuildRequires:	gnome-vfs2-devel >= 2.18.1
BuildRequires:	libbonoboui-devel >= 2.18.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.18.1
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	perl-base
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Build Framework (GBF).

%description -l pl.UTF-8
Struktura GNOME Build (GBF).

%package devel
Summary:	Header files for gnome-build
Summary(pl.UTF-8):	Pliki nagłówkowe gnome-build
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdl-devel >= 0.7.5

%description devel
Header files for gnome-build.

%description devel -l pl.UTF-8
Pliki nagłówkowe gnome-build.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--enable-compile-warnings=maximum
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
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
%{_libdir}/%{name}-1.0/backends/gbf-mkfile.server
%{_datadir}/%{name}
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-1.0
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
