Summary:	GNOME Build Framework (GBF)
Summary(pl.UTF-8):	Struktura GNOME Build (GBF)
Name:		gnome-build
Version:	2.24.1
Release:	2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-build/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	b35c918b6c0c70652e9eb1d2e45138f1
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gdl-devel >= 2.24.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libbonoboui-devel >= 2.24.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.24.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	perl-Locale-gettext
BuildRequires:	perl-base >= 5.005
BuildRequires:	pkgconfig
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
Requires:	gdl-devel >= 2.24.0

%description devel
Header files for gnome-build.

%description devel -l pl.UTF-8
Pliki nagłówkowe gnome-build.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}-1.0/backends/*.la

%find_lang gbf-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f gbf-1.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/gbf-am-parse
%attr(755,root,root) %{_bindir}/gbf-mkfile-parse
%attr(755,root,root) %{_libdir}/libgbf-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgbf-1.so.2
%attr(755,root,root) %{_libdir}/libgbf-widgets-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgbf-widgets-1.so.2
%dir %{_libdir}/%{name}-1.0
%dir %{_libdir}/%{name}-1.0/backends
%attr(755,root,root) %{_libdir}/%{name}-1.0/backends/libgbf-am.so
%attr(755,root,root) %{_libdir}/%{name}-1.0/backends/libgbf-mkfile.so
%{_libdir}/%{name}-1.0/backends/gbf-am.server
%{_libdir}/%{name}-1.0/backends/gbf-mkfile.server
%{_datadir}/%{name}
%{_pixmapsdir}/gbf-*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgbf-1.so
%attr(755,root,root) %{_libdir}/libgbf-widgets-1.so
%{_libdir}/libgbf-1.la
%{_libdir}/libgbf-widgets-1.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/gnome-build-1.0.pc
