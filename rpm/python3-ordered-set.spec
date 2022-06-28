Name:       python3-ordered-set
Summary:    Mutable data structure that is a hybrid of a list and a set
Version:    3.1
Release:    1
License:    MIT
URL:        https://github.com/sailfishos/python3-ordered-set
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
An OrderedSet is a mutable data structure that is a hybrid of a list and a set. It remembers the order of its entries, and every entry has an index number that can be looked up.

%prep
%setup -q -n %{name}-%{version}/ordered-set

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/ordered_set.py
%{python3_sitelib}/ordered_set-*.egg-info
%{python3_sitelib}/__pycache__/*
