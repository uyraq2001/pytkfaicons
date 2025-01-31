%define _unpackaged_files_terminate_build 1
%define pypi_name pytkfaicons

# no tests provided by the author
%def_without check

Name: python3-module-%pypi_name
Version: 0.0.11
Release: alt1
Summary: fontawesome font based icons support for tkinter
License: AGPL-3.0
Group: Development/Tools
Url: https://pypi.org/project/%pypi_name
Vcs: https://github.com/kr-g/%pypi_name
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Nov 29 2024 Yuri Kozyrev <kozyrevid@altlinux.org> 0.0.11-alt1
- initial build
