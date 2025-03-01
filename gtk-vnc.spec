#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static libraries
%bcond_without	vala		# Vala API

Summary:	A GTK+ widget for VNC clients
Summary(pl.UTF-8):	Widget GTK+ dla klientów VNC
Name:		gtk-vnc
Version:	1.5.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/gtk-vnc/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	6e9815e7960636e95f626a3f164eb01d
URL:		https://wiki.gnome.org/Projects/gtk-vnc
BuildRequires:	cairo-devel >= 1.15.0
BuildRequires:	cyrus-sasl-devel >= 2.1.27
BuildRequires:	gdk-pixbuf2-devel >= 2.36.0
BuildRequires:	gettext-tools
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gmp-devel >= 6.0.0
BuildRequires:	gnutls-devel >= 3.6.0
BuildRequires:	gobject-introspection-devel >= 1.56.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 11.0
BuildRequires:	python3 >= 1:3
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 0.14.0}
BuildRequires:	xorg-lib-libX11-devel >= 1.6.5
BuildRequires:	xz
BuildRequires:	zlib-devel >= 1.2.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

%description -l pl.UTF-8
gtk-vnc to widget przeglądarki VNC dla GTK+. Jest skonstruowany z
użyciem korutyn, dzięki czemu mogą być w pełni asynchroniczne
pozostając jednowątkowymi.

%package -n gtk3-vnc
Summary:	A GTK+ widget for VNC clients (GTK+ 3.x version)
Summary(pl.UTF-8):	Widget GTK+ dla klientów VNC (wersja GTK+ 3.x)
Group:		X11/Libraries
Requires:	cairo >= 1.15.0
Requires:	gtk+3 >= 3.22.0
Requires:	libgvnc = %{version}-%{release}
Requires:	xorg-lib-libX11 >= 1.6.5

%description -n gtk3-vnc
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

This package contains version for GTK+ 3.x.

%description -n gtk3-vnc -l pl.UTF-8
gtk-vnc to widget przeglądarki VNC dla GTK+. Jest skonstruowany z
użyciem korutyn, dzięki czemu mogą być w pełni asynchroniczne
pozostając jednowątkowymi.

Ten pakiet zawiera wersję dla GTK+ 3.x.

%package -n gtk3-vnc-devel
Summary:	Header files for gtk-vnc library (GTK+ 3.x version)
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtk-vnc (wersja dla GTK+ 3.x)
Group:		X11/Development/Libraries
Requires:	cairo-devel >= 1.15.0
Requires:	gtk+3-devel >= 3.22.0
Requires:	gtk3-vnc = %{version}-%{release}
Requires:	libgvnc-devel = %{version}-%{release}
Requires:	xorg-lib-libX11-devel >= 1.6.5

%description -n gtk3-vnc-devel
Header files for gtk-vnc library (GTK+ 3.x version).

%description -n gtk3-vnc-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtk-vnc (wersja dla GTK+ 3.x).

%package -n gtk3-vnc-static
Summary:	Static gtk-vnc library (GTK+ 3.x version)
Summary(pl.UTF-8):	Statyczna biblioteka gtk-vnc (wersja dla GTK+ 3.x)
Group:		X11/Development/Libraries
Requires:	gtk3-vnc-devel = %{version}-%{release}
Requires:	libgvnc-static = %{version}-%{release}

%description -n gtk3-vnc-static
Static gtk-vnc library (GTK+ 3.x version).

%description -n gtk3-vnc-static -l pl.UTF-8
Statyczna biblioteka gtk-vnc (wersja dla GTK+ 3.x).

%package -n vala-gtk3-vnc
Summary:	Vala API for gtk-vnc library (GTK+ 3.x version)
Summary(pl.UTF-8):	API języka Vala dla biblioteki gtk-vnc (wersja dla GTK+3)
Group:		Development/Languages
Requires:	gtk3-vnc-devel = %{version}-%{release}
Requires:	vala-libgvnc = %{version}-%{release}
BuildArch:	noarch

%description -n vala-gtk3-vnc
Vala API for gtk-vnc library (GTK+ 3.x version).

%description -n vala-gtk3-vnc -l pl.UTF-8
API języka Vala dla biblioteki gtk-vnc (wersja dla GTK+3).

%package -n gtk3-vnc-apidocs
Summary:	API documentation for gtk-vnc library
Summary(pl.UTF-8):	Dokumentacja API biblioteki gtk-vnc
Group:		Documentation
BuildArch:	noarch

%description -n gtk3-vnc-apidocs
API documentation for gtk-vnc library.

%description -n gtk3-vnc-apidocs -l pl.UTF-8
Dokumentacja API biblioteki gtk-vnc.

%package -n libgvnc
Summary:	A library for VNC clients
Summary(pl.UTF-8):	Biblioteka dla klientów VNC
Group:		X11/Libraries
Requires:	cyrus-sasl-libs >= 2.1.27
Requires:	gdk-pixbuf2 >= 2.36.0
Requires:	glib2 >= 1:2.56.0
Requires:	gmp >= 6.0.0
Requires:	gnutls >= 3.6.0
Requires:	pulseaudio-libs >= 11.0
Requires:	zlib >= 1.2.11

%description -n libgvnc
A library for VNC clients.

%description -n libgvnc -l pl.UTF-8
Biblioteka dla klientów VNC.

%package -n libgvnc-devel
Summary:	Header files for libgvnc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgvnc
Group:		X11/Development/Libraries
Requires:	cyrus-sasl-devel >= 2.1.27
Requires:	gdk-pixbuf2-devel >= 2.36.0
Requires:	glib2-devel >= 1:2.56.0
Requires:	gmp-devel >= 6.0.0
Requires:	gnutls-devel >= 3.6.0
Requires:	libgvnc = %{version}-%{release}
Requires:	zlib-devel >= 1.2.11

%description -n libgvnc-devel
Header files for libgvnc library.

%description -n libgvnc-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgvnc.

%package -n libgvnc-static
Summary:	Static libgvnc library
Summary(pl.UTF-8):	Statyczna biblioteka libgvnc
Group:		X11/Development/Libraries
Requires:	libgvnc-devel = %{version}-%{release}

%description -n libgvnc-static
Static libgvnc library.

%description -n libgvnc-static -l pl.UTF-8
Statyczna biblioteka libgvnc.

%package -n vala-libgvnc
Summary:	Vala API for libgvnc library
Summary(pl.UTF-8):	API języka Vala dla biblioteki libgvnc
Group:		Development/Languages
Requires:	libgvnc-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-libgvnc
Vala API for libgvnc library.

%description -n vala-libgvnc -l pl.UTF-8
API języka Vala dla biblioteki libgvnc.

%package -n libgvnc-apidocs
Summary:	API documentation for libgvnc library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgvnc
Group:		Documentation
BuildArch:	noarch

%description -n libgvnc-apidocs
API documentation for libgvnc library.

%description -n libgvnc-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgvnc.

%package tools
Summary:	Command line tools for VNC
Summary(pl.UTF-8):	Narzędzia linii poleceń dla VNC
Group:		Applications/Networking
Requires:	libgvnc = %{version}-%{release}

%description tools
Command line utilities for interacting with VNC servers.

%description tools -l pl.UTF-8
Narzędzia linii poleceń do interakcji z serwerami VNC.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/python$,%{__python},' examples/gvncviewer.py

%build
%meson \
	%{!?with_apidocs:-Dgi-docs=false}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/gtk3-vnc-%{version}
cp -p examples/gvncviewer.{c,js,pl,py} $RPM_BUILD_ROOT%{_examplesdir}/gtk3-vnc-%{version}

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/{gtk-vnc,gvnc} $RPM_BUILD_ROOT%{_gidocdir}
%{__rm} $RPM_BUILD_ROOT%{_docdir}/*.toml
%endif

# not supported by glibc (as of 2.40)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{guc,ie}

%find_lang gtk-vnc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n gtk3-vnc -p /sbin/ldconfig
%postun	-n gtk3-vnc -p /sbin/ldconfig

%post	-n libgvnc -p /sbin/ldconfig
%postun	-n libgvnc -p /sbin/ldconfig

%files -n gtk3-vnc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk-vnc-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtk-vnc-2.0.so.0
%{_libdir}/girepository-1.0/GtkVnc-2.0.typelib

%files -n gtk3-vnc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk-vnc-2.0.so
%{_includedir}/gtk-vnc-2.0
%{_datadir}/gir-1.0/GtkVnc-2.0.gir
%{_pkgconfigdir}/gtk-vnc-2.0.pc
%{_examplesdir}/gtk3-vnc-%{version}

%if %{with static_libs}
%files -n gtk3-vnc-static
%defattr(644,root,root,755)
%{_libdir}/libgtk-vnc-2.0.a
%endif

%if %{with vala}
%files -n vala-gtk3-vnc
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gtk-vnc-2.0.deps
%{_datadir}/vala/vapi/gtk-vnc-2.0.vapi
%endif

%if %{with apidocs}
%files -n gtk3-vnc-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/gtk-vnc
%endif

%files -n libgvnc -f gtk-vnc.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgvnc-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgvncpulse-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvnc-1.0.so.0
%attr(755,root,root) %ghost %{_libdir}/libgvncpulse-1.0.so.0
%{_libdir}/girepository-1.0/GVnc-1.0.typelib
%{_libdir}/girepository-1.0/GVncPulse-1.0.typelib

%files -n libgvnc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgvnc-1.0.so
%attr(755,root,root) %{_libdir}/libgvncpulse-1.0.so
%{_datadir}/gir-1.0/GVnc-1.0.gir
%{_datadir}/gir-1.0/GVncPulse-1.0.gir
%{_includedir}/gvnc-1.0
%{_includedir}/gvncpulse-1.0
%{_pkgconfigdir}/gvnc-1.0.pc
%{_pkgconfigdir}/gvncpulse-1.0.pc

%if %{with static_libs}
%files -n libgvnc-static
%defattr(644,root,root,755)
%{_libdir}/libgvnc-1.0.a
%{_libdir}/libgvncpulse-1.0.a
%endif

%if %{with vala}
%files -n vala-libgvnc
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gvnc-1.0.deps
%{_datadir}/vala/vapi/gvnc-1.0.vapi
%{_datadir}/vala/vapi/gvncpulse-1.0.deps
%{_datadir}/vala/vapi/gvncpulse-1.0.vapi
%endif

%if %{with apidocs}
%files -n libgvnc-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/gvnc
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvnccapture
%{_mandir}/man1/gvnccapture.1*
