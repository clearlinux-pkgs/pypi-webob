#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-webob
Version  : 1.8.7
Release  : 95
URL      : https://files.pythonhosted.org/packages/c7/45/ee5f034fb4ebe3236fa49e5a4fcbc54444dd22ecf33079cf56f9606d479d/WebOb-1.8.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/c7/45/ee5f034fb4ebe3236fa49e5a4fcbc54444dd22ecf33079cf56f9606d479d/WebOb-1.8.7.tar.gz
Summary  : WSGI request and response object
Group    : Development/Tools
License  : MIT
Requires: pypi-webob-license = %{version}-%{release}
Requires: pypi-webob-python = %{version}-%{release}
Requires: pypi-webob-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=====

%package license
Summary: license components for the pypi-webob package.
Group: Default

%description license
license components for the pypi-webob package.


%package python
Summary: python components for the pypi-webob package.
Group: Default
Requires: pypi-webob-python3 = %{version}-%{release}

%description python
python components for the pypi-webob package.


%package python3
Summary: python3 components for the pypi-webob package.
Group: Default
Requires: python3-core
Provides: pypi(webob)

%description python3
python3 components for the pypi-webob package.


%prep
%setup -q -n WebOb-1.8.7
cd %{_builddir}/WebOb-1.8.7
pushd ..
cp -a WebOb-1.8.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695158354
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-webob
cp %{_builddir}/WebOb-%{version}/docs/license.txt %{buildroot}/usr/share/package-licenses/pypi-webob/c6186941914c00e75b649dd640adcf534d0cefd6 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-webob/c6186941914c00e75b649dd640adcf534d0cefd6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
