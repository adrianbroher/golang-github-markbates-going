# Generated by go2rpm 1
%bcond_without check

# https://github.com/markbates/going
%global goipath         github.com/markbates/going
Version:                1.0.3

%gometa

%global common_description %{expand:
Some helpful packages for writing Go apps.}

%global golicenses      LICENSE.txt
%global godocs          README.md imt/README.md validate/README.md\\\
                        wait/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Some helpful packages for writing Go apps

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/serenize/snaker)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Jan 25 16:20:48 CET 2020 Marcel Metz <mmetz@adrian-broher.net> - 1.0.3-1
- Initial package
