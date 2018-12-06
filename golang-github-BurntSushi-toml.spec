# http://github.com/BurntSushi/toml
%global goipath         github.com/BurntSushi/toml
Version:                0.3.1

%gometa

Name:           golang-github-BurntSushi-toml
Release:        1%{?dist}
Summary:        TOML parser and encoder for Go with reflection
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .


%build
%gobuildroot
%gobuild -o _bin/tomlv %{goipath}/cmd/tomlv


%install
install -d %{buildroot}/%{_bindir}
install -p -m 755 _bin/tomlv %{buildroot}%{_bindir}/tomlv

%goinstall glide.lock glide.yaml


%check
%gochecks


%files
%license COPYING README.md
%{_bindir}/tomlv


%files devel -f devel.file-list
%license COPYING README.md
%doc README.md


%changelog
* Wed Oct 31 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.1-1
- Release 0.3.1

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.3.0-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.3.0-2
- Upload glide.lock and glide.yaml

* Sun Mar 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.3.0-1
- Update to 0.3.0
  resolves: #1423641

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.20140718git2ceedfe
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git2ceedfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git2ceedfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git2ceedfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git2ceedfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git2ceedfe
- Polish the spec file
  related: #1247656

* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 0-0.9.git2ceedfe
- Enable devel and unit-test for epel7
  related: #1247656

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git2ceedfe
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git2ceedfe
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git2ceedfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git2ceedfe
- Update to spec-2.1
  related: #1247656

* Tue Jul 28 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git2ceedfe
- Update of spec file to spec-2.0
  resolves: #1247656

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git2ceedfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 23 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.git2ceedfe
- Bump to upstream 2ceedfee35ad3848e49308ab0c9a4f640cfb5fb2
- spec file polishing to follow go draft
  related: #1120865

* Mon Sep 22 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.gitbd2bdf7
- do not own golang directories
- defattr and attr not needed

* Mon Sep 22 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.gitbd2bdf7
- accomodated changes from Vincent Batts
- gopath is in the rpm macros, and set exclusive arch too, to prevent s390 builds
- move the buildarch noarch to the devel, since it is source only
- preserve timestamps of source copied and as an added perk
- the tomlv command provided in this project is useful for validating *.toml files
- go test

* Thu Jul 17 2014 Colin Walters <walters@verbum.org>
- Initial package

