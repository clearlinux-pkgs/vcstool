#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vcstool
Version  : 0.2.4
Release  : 15
URL      : https://files.pythonhosted.org/packages/4b/98/2fa6e4da27656beb7bde585520a91f2973a537d8e3a6b5cc5f88c6c9c5a0/vcstool-0.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/4b/98/2fa6e4da27656beb7bde585520a91f2973a537d8e3a6b5cc5f88c6c9c5a0/vcstool-0.2.4.tar.gz
Summary  : vcstool provides a command line tool to invoke vcs commands on multiple repositories.
Group    : Development/Tools
License  : Apache-2.0
Requires: vcstool-bin = %{version}-%{release}
Requires: vcstool-data = %{version}-%{release}
Requires: vcstool-python = %{version}-%{release}
Requires: vcstool-python3 = %{version}-%{release}
Requires: PyYAML
Requires: setuptools
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : setuptools
BuildRequires : util-linux

%description
What is vcstool?
================
Vcstool is a version control system (VCS) tool, designed to make working with multiple repositories easier.

%package bin
Summary: bin components for the vcstool package.
Group: Binaries
Requires: vcstool-data = %{version}-%{release}

%description bin
bin components for the vcstool package.


%package data
Summary: data components for the vcstool package.
Group: Data

%description data
data components for the vcstool package.


%package python
Summary: python components for the vcstool package.
Group: Default
Requires: vcstool-python3 = %{version}-%{release}

%description python
python components for the vcstool package.


%package python3
Summary: python3 components for the vcstool package.
Group: Default
Requires: python3-core

%description python3
python3 components for the vcstool package.


%prep
%setup -q -n vcstool-0.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571684428
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vcs
/usr/bin/vcs-branch
/usr/bin/vcs-bzr
/usr/bin/vcs-custom
/usr/bin/vcs-diff
/usr/bin/vcs-export
/usr/bin/vcs-git
/usr/bin/vcs-help
/usr/bin/vcs-hg
/usr/bin/vcs-import
/usr/bin/vcs-log
/usr/bin/vcs-pull
/usr/bin/vcs-push
/usr/bin/vcs-remotes
/usr/bin/vcs-status
/usr/bin/vcs-svn
/usr/bin/vcs-validate

%files data
%defattr(-,root,root,-)
/usr/share/vcstool-completion/vcs.bash
/usr/share/vcstool-completion/vcs.tcsh
/usr/share/vcstool-completion/vcs.zsh

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
