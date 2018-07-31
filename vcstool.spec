#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vcstool
Version  : 0.1.36
Release  : 3
URL      : https://files.pythonhosted.org/packages/b5/ec/477043ca80ab60f46ef90dabf597d711226907f1037bd2e3fda39d304088/vcstool-0.1.36.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/ec/477043ca80ab60f46ef90dabf597d711226907f1037bd2e3fda39d304088/vcstool-0.1.36.tar.gz
Summary  : vcstool provides a command line tool to invoke vcs commands on multiple repositories.
Group    : Development/Tools
License  : Apache-2.0
Requires: vcstool-bin
Requires: vcstool-python3
Requires: vcstool-data
Requires: vcstool-python
Requires: PyYAML
Requires: setuptools
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
What is vcstool?
================
Vcstool is a version control system (VCS) tool, designed to make working with multiple repositories easier.

%package bin
Summary: bin components for the vcstool package.
Group: Binaries
Requires: vcstool-data

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
Requires: vcstool-python3

%description python
python components for the vcstool package.


%package python3
Summary: python3 components for the vcstool package.
Group: Default
Requires: python3-core

%description python3
python3 components for the vcstool package.


%prep
%setup -q -n vcstool-0.1.36

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533001724
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
