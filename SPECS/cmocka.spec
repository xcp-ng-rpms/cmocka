%global package_speccommit 3a3ae4da2132f078d8c08ed730870d8dfa4a12ab
%global usver 1.1.7
%global xsver 2
%global xsrel %{xsver}%{?xscount}%{?xshash}
Name:           cmocka
Version:        1.1.7
Release: %{?xsrel}%{?dist}

License:        Apache-2.0
Summary:        An elegant unit testing framework for C with support for mock objects
URL:            https://cmocka.org

Source0: cmocka-1.1.7.tar.xz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  glibc-devel
BuildRequires:  gnupg2

Obsoletes:      libcmocka-static < %{version}

%description
There are a variety of C unit testing frameworks available however many of them
are fairly complex and require the latest compiler technology. Some development
requires the use of old compilers which makes it difficult to use some unit
testing frameworks. In addition many unit testing frameworks assume the code
being tested is an application or module that is targeted to the same platform
that will ultimately execute the test. Because of this assumption many
frameworks require the inclusion of standard C library headers in the code
module being tested which may collide with the custom or incomplete
implementation of the C library utilized by the code under test.

Cmocka only requires a test application is linked with the standard C library
which minimizes conflicts with standard C library headers. Also, CMocka tries
to avoid the use of some of the newer features of C compilers.

This results in CMocka being a relatively small library that can be used to
test a variety of exotic code. If a developer wishes to simply test an
application with the latest compiler then other unit testing frameworks may be
preferable.

This is the successor of Google's Cmockery.

%package -n libcmocka
Summary:        Lightweight library to simplify and generalize unit tests for C

Conflicts: cmockery2

%description -n libcmocka
There are a variety of C unit testing frameworks available however many of them
are fairly complex and require the latest compiler technology. Some development
requires the use of old compilers which makes it difficult to use some unit
testing frameworks. In addition many unit testing frameworks assume the code
being tested is an application or module that is targeted to the same platform
that will ultimately execute the test. Because of this assumption many
frameworks require the inclusion of standard C library headers in the code
module being tested which may collide with the custom or incomplete
implementation of the C library utilized by the code under test.

CMocka only requires a test application is linked with the standard C library
which minimizes conflicts with standard C library headers. Also, CMocka tries
to avoid the use of some of the newer features of C compilers.

This results in CMocka being a relatively small library that can be used to
test a variety of exotic code. If a developer wishes to simply test an
application with the latest compiler then other unit testing frameworks may be
preferable.

This is the successor of Google's Cmockery.

%package -n libcmocka-devel
Summary:        Development headers for the cmocka library
Requires:       libcmocka = %{version}-%{release}

Conflicts: cmockery2-devel

%description -n libcmocka-devel
Development headers for the cmocka unit testing library.

%prep
%autosetup -p1

%build
# This package uses -Wl,-wrap to wrap calls at link time.  This is incompatible
# with LTO.
# Disable LTO
%define _lto_cflags %{nil}

%cmake \
  -DWITH_STATIC_LIB=ON \
  -DWITH_CMOCKERY_SUPPORT=ON \
  -DUNIT_TESTING=ON

%cmake_build

%install
%cmake_install
ln -s libcmocka.so %{buildroot}%{_libdir}/libcmockery.so

%ldconfig_scriptlets -n libcmocka

%check
%ctest

%files -n libcmocka
%doc AUTHORS README.md ChangeLog
%license COPYING
%{_libdir}/libcmocka.so.*

%files -n libcmocka-devel
%{_includedir}/cmocka.h
%{_includedir}/cmocka_pbc.h
%{_includedir}/cmockery/cmockery.h
%{_includedir}/cmockery/pbc.h
%{_libdir}/libcmocka.so
%{_libdir}/libcmockery.so
%{_libdir}/pkgconfig/cmocka.pc
%{_libdir}/cmake/cmocka/cmocka-config*.cmake

%changelog
* Thu Jan 16 2025 XenServer Rebuild <rebuild@xenserver.com> - 1.1.7-2
- CP-53241: XenServer 9 rebuild

* Fri Nov 10 2023 Lin Liu <lin.liu@citrix.com> - 1.1.7-1
- First imported release

