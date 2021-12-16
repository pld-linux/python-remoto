#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	remoto
Summary:	Execute remote commands or processes
Summary(pl.UTF-8):	Uruchamianie zdalnych poleceń lub procesów
Name:		python-%{module}
Version:	0.0.25
Release:	7
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/r/remoto/%{module}-%{version}.tar.gz
# Source0-md5:	94fa964c08d9c4619ef63201c58091e3
URL:		https://github.com/alfredodeza/remoto
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools >= 1:7.0
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools >= 1:7.0
%endif
Requires:	python-execnet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A very simplistic remote-command-executor using ssh and Python in the
remote end.

All the heavy lifting is done by execnet, while this minimal API
provides the bare minimum to handle easy logging and connections from
the remote end.

%description -l pl.UTF-8
Bardzo proste narzędzie do uruchamiania zdalnych poleceń przez SSH z
Pythonem po drugiej stronie.

Cała ciężka robota jest wykonywana przez execnet, a ten moduł jest
minimalnym API zapewniającym minimum do obsługi łatwego logowania i
połączeń ze zdalnej strony.

%package -n python3-%{module}
Summary:	Execute remote commands or processes
Summary(pl.UTF-8):	Uruchamianie zdalnych poleceń lub procesów
Group:		Libraries/Python
Requires:	python3-execnet

%description -n python3-%{module}
A very simplistic remote-command-executor using ssh and Python in the
remote end.

All the heavy lifting is done by execnet, while this minimal API
provides the bare minimum to handle easy logging and connections from
the remote end.

%description -n python3-%{module} -l pl.UTF-8
Bardzo proste narzędzie do uruchamiania zdalnych poleceń przez SSH z
Pythonem po drugiej stronie.

Cała ciężka robota jest wykonywana przez execnet, a ten moduł jest
minimalnym API zapewniającym minimum do obsługi łatwego logowania i
połączeń ze zdalnej strony.

%prep
%setup -q -n %{module}-%{version}

%build
export REMOTO_NO_VENDOR=1
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

export REMOTO_NO_VENDOR=1
%if %{with python2}
%py_install
# no %%py_postclean !
# remoto needs the source code to run it on the target
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
