Summary:	A GTK+ widget for VNC clients
Summary(pl.UTF-8):	Widget GTK+ dla klientów VNC
Name:		gtk-vnc
Version:	0.3.7
Release:	4
License:	LGPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtk-vnc/%{name}-%{version}.tar.gz
# Source0-md5:	41c613be4b554b71d63d30f844d60add
Patch0:		%{name}-codegen.patch
URL:		http://gtk-vnc.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gnutls-devel >= 1.4.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygtk-devel >= 2:2.0.0
BuildRequires:	rpm-pythonprov
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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls-devel >= 1.4.0
Requires:	gtk+2-devel >= 1:2.0.0

%description devel
Header files for gtk-vnc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtk-vnc.

%package static
Summary:	Static gtk-vnc library
Summary(pl.UTF-8):	Statyczna biblioteka gtk-vnc
Group:		Development/Libraries
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

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}

install examples/gvncviewer.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/gvncviewer.py $RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgtk-vnc-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtk-vnc-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk-vnc-1.0.so
%{_libdir}/libgtk-vnc-1.0.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/%{name}-1.0.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtk-vnc-1.0.a

%files -n python-gtk-vnc
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtkvnc.so
%{_examplesdir}/python-%{name}-%{version}
