%global pypi_name python-utils
%global pkgname utils

Name:		python-%{pkgname}
Version:	3.1.0
Release:	1
Summary:	Python Utils is a module with some convenient utilities
Group:		Development/Python
License:	BSD
URL:		https://github.com/WoLpH/python-utils
Source0:	https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3dist(setuptools)

%description
Python Utils is a module with some convenient utilities not included with the
standard Python install.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%files
%{python3_sitelib}/python_utils
%{python3_sitelib}/python_utils-%{version}-py%{python3_version}.egg-info
