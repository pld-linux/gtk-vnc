Summary:	A GTK widget for VNC clients
Name:		gtk-vnc
Version:	0.3.0
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/gtk-vnc/%{name}-%{version}.tar.gz
# Source0-md5:	6ef6cd8862ba4edd797fe4df48db647d
Patch0:		%{name}-codegen.patch
URL:		http://gtk-vnc.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

%package devel
Summary:	Libraries, includes, etc. to compile with the gtk-vnc library
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk2+-devel
Requires:	python-pygtk-devel

%description devel
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

Libraries, includes, etc. to compile with the gtk-vnc library

%package -n python-gtk-vnc
Summary:	Python bindings for the gtk-vnc library
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description -n python-gtk-vnc
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

A module allowing use of the GTK-VNC widget from python

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
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.a
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la

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
%{_libdir}/lib*.so
%dir %{_includedir}/%{name}-1.0/
%{_includedir}/%{name}-1.0/*.h
%{_pkgconfigdir}/%{name}-1.0.pc

%files -n python-gtk-vnc
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README COPYING.LIB examples/gvncviewer.py
%{py_sitedir}/gtkvnc.so
