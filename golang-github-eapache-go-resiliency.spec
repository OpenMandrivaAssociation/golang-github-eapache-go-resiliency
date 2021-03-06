# http://github.com/eapache/go-resiliency
%global goipath         github.com/eapache/go-resiliency
Version:                1.1.0

%gometa 

Name:           golang-github-eapache-go-resiliency
Release:        1%{?dist}
Summary:        Resiliency patterns for golang
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

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

%install
%goinstall glide.lock glide.yaml

%check
# -d deadline -d batcher
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Oct 29 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Release 1.1.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.12.gitb86b1ec
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Wed Oct 03 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.gitb86b1ec
- Skip batcher test
  resolves: #1555792

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.gitb86b1ec
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.20160104gitb86b1ec
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitb86b1ec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitb86b1ec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitb86b1ec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitb86b1ec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitb86b1ec
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Jun 02 2016 jchaloup <jchaloup@redhat.com> - 0-0.2.gitb86b1ec
- Enable devel and unit-test subpackages for epel7
  related: #1327307

* Thu Apr 14 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gitb86b1ec
- First package for Fedora
  resolves: #1327307
