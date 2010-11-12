Summary:	A GTK+ widget for VNC clients
Summary(pl.UTF-8):	Widget GTK+ dla klientów VNC
Name:		gtk-vnc
Version:	0.4.2
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-vnc/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	68fdeb71844c49d5d5ab4f32cbc8bddb
Patch0:		%{name}-codegen.patch
URL:		http://live.gnome.org/gtk-vnc
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnutls-devel >= 1.4.0
BuildRequires:	gobject-introspection-devel >= 0.9.4
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	perl-Text-CSV
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygtk-devel >= 2:2.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

%description -l pl.UTF-8
gtk-vnc to widget przeglądarki VNC dla GTK+. Jest skonstruowany z
użyciem korutyn, dzięki czemu mogą być w pełni asynchroniczne
pozostając jednowątkowymi.

%package devel
Summary:	Header files for gtk-vnc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtk-vnc
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls-devel >= 1.4.0
Requires:	gtk+2-devel >= 2:2.18.0

%description devel
Header files for gtk-vnc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtk-vnc.

%package static
Summary:	Static gtk-vnc library
Summary(pl.UTF-8):	Statyczna biblioteka gtk-vnc
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtk-vnc library.

%description static -l pl.UTF-8
Statyczna biblioteka gtk-vnc.

%package -n python-gtk-vnc
Summary:	Python bindings for the gtk-vnc library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki gtk-vnc
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%requires_eq	python-libs

%description -n python-gtk-vnc
A module allowing use of the GTK+ VNC widget from Python.

%description -n python-gtk-vnc -l pl.UTF-8
Moduł pozwalający na używanie widgetu GTK+ VNC z poziomu Pythona.

%package tools
Summary:	Command line tools for VNC
Summary(pl.UTF-8):	Narzędzia linii poleceń dla VNC
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description tools
Command line utilities for interacting with VNC servers.

%description tools -l pl.UTF-8
Narzędzia linii poleceń do interakcji z serwerami VNC.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}

install examples/gvncviewer.{c,js} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/gvncviewer.py $RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%find_lang %{name}

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgtk-vnc-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtk-vnc-1.0.so.0
%attr(755,root,root) %{_libdir}/libgvnc-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvnc-1.0.so.0
%{_libdir}/girepository-1.0/GVnc-1.0.typelib
%{_libdir}/girepository-1.0/GtkVnc-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk-vnc-1.0.so
%attr(755,root,root) %{_libdir}/libgvnc-1.0.so
%{_libdir}/libgtk-vnc-1.0.la
%{_libdir}/libgvnc-1.0.la
%{_includedir}/%{name}-1.0
%{_includedir}/gvnc-1.0
%{_datadir}/gir-1.0/GVnc-1.0.gir
%{_datadir}/gir-1.0/GtkVnc-1.0.gir
%{_pkgconfigdir}/%{name}-1.0.pc
%{_pkgconfigdir}/gvnc-1.0.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtk-vnc-1.0.a
%{_libdir}/libgvnc-1.0.a

%files -n python-gtk-vnc
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtkvnc.so
%{_examplesdir}/python-%{name}-%{version}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvnccapture
%{_mandir}/man1/gvnccapture.1*
