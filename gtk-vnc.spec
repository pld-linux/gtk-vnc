Summary:	A GTK+ widget for VNC clients
Summary(pl.UTF-8):	Widget GTK+ dla klientów VNC
Name:		gtk-vnc
Version:	0.3.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtk-vnc/%{name}-%{version}.tar.gz
# Source0-md5:	6ef6cd8862ba4edd797fe4df48db647d
Patch0:		%{name}-codegen.patch
URL:		http://gtk-vnc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
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
Requires:	gtk+2-devel
Requires:	python-pygtk-devel

%description devel
Header files for gtk-vnc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtk-vnc.

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

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%clean
rm -fr $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README COPYING.LIB
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README COPYING.LIB
%doc examples/gvncviewer.c
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/%{name}-1.0
%{_includedir}/%{name}-1.0/*.h
%{_pkgconfigdir}/%{name}-1.0.pc

%files -n python-gtk-vnc
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README COPYING.LIB examples/gvncviewer.py
%{py_sitedir}/gtkvnc.so
