%global pypi_name python-utils
%global pkgname utils

Name:		python-%{pkgname}
Version:	3.9.1
Release:	1
Summary:	Python Utils is a module with some convenient utilities
Group:		Development/Python
License:	BSD
URL:		https://github.com/WoLpH/python-utils
Source0:	https://files.pythonhosted.org/packages/source/p/python_utils/python_utils-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)

%description
Python Utils is a module with some convenient utilities not included with the
standard Python install.

%files
%{python_sitelib}/python_utils
%{python_sitelib}/python_utils-%{version}.dist-info
