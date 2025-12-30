Name:		python-matrix-common
Version:	1.3.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/m/matrix-common/matrix_common-%{version}.tar.gz
Summary:	Common utilities for Synapse, Sydent and Sygnal
URL:		https://pypi.org/project/matrix-common/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Common utilities for Synapse, Sydent and Sygnal

%prep
%autosetup -p1 -n matrix_common-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/matrix_common
%{py_sitedir}/matrix_common-*.*-info
