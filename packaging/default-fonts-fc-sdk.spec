Name:       default-fonts-fc-sdk
Summary:    Font configuration package for SDK
Version:    0.0.2
Release:    0
Group:      TO_BE/FILLED_IN
License:    Samsung Proprietary License 
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/default-fonts-fc-sdk.manifest 

%description
Font configuration package for SDK
This package is maintained by SDK team

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_prefix}/etc/fonts/conf.d/
mkdir -p %{buildroot}%{_prefix}/etc/fonts/conf.avail/ && cp -a sdk_fonts_fc/* %{buildroot}%{_prefix}/etc/fonts/conf.avail/
cd %{buildroot}%{_prefix}/etc/fonts/conf.d/
ln -s ../conf.avail/99-slp.conf %{buildroot}%{_prefix}/etc/fonts/conf.d/99-slp.conf

%files
%manifest default-fonts-fc-sdk.manifest
%defattr(-,root,root,-) 
%{_prefix}/etc/fonts/conf.avail/99-slp.conf
%{_prefix}/etc/fonts/conf.d/99-slp.conf
%exclude %{_prefix}/etc/fonts/conf.d/documentation.list
