%global debug_package %{nil}

# Run tests in check section
%bcond_without check

# https://github.com/BurntSushi/toml
%global goipath		github.com/BurntSushi/toml
%global forgeurl	https://github.com/BurntSushi/toml
Version:		1.4.0

%gometa

Summary:	TOML parser for Golang with reflection
Name:		golang-github-BurntSushi-toml

Release:	1
Source0:	https://github.com/BurntSushi/toml/archive/v%{version}/toml-%{version}.tar.gz
URL:		https://github.com/BurntSushi/toml
License:	BSD
Group:		Development/Other
BuildRequires:	compiler(go-compiler)

%description
TOML stands for Tom's Obvious, Minimal Language. This Go package
provides a reflection interface similar to Go's standard library
json and xml packages.

Compatible with TOML version v1.0.0.

%files
%license COPYING
%doc README.md
%{_bindir}/*

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

%files devel -f devel.file-list
%license COPYING
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n toml-%{version}

%build
%gobuildroot
for cmd in $(ls -1 cmd) ; do
	%gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done

%install
%goinstall
for cmd in $(ls -1 _bin) ; do
  install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done

%check
%if %{with check}
%gochecks
%endif

