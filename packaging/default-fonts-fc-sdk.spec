#sbs-git:slp/sdk/default-fonts-fc-sdk default-fonts-fc-sdk 0.0.2 8414dbd3e62b6f7a864ba031e043dd7604b3d86d
Name:       default-fonts-fc-sdk
Summary:    Font configuration package for SDK
Version:    0.0.2
Release:    0
Group:      SDK/Configuration
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: default-fonts-fc-sdk.manifest
BuildArch:  noarch
BuildRequires: libtzplatform-config-devel

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
mkdir -p %{buildroot}%{TZ_SYS_ETC}/fonts/conf.avail/ && cp -a sdk_fonts_fc/* %{buildroot}%{TZ_SYS_ETC}/fonts/conf.avail/
cd %{buildroot}%{_prefix}/etc/fonts/conf.d/
ln -s ../../../..%{TZ_SYS_ETC}/fonts/conf.avail/99-slp.conf %{buildroot}%{_prefix}/etc/fonts/conf.d/99-slp.conf

%post
TZ_SYS_USER_GROUP_ID=$(getent group %{TZ_SYS_USER_GROUP} | cut -d: -f3)
chown :$TZ_SYS_USER_GROUP_ID %{TZ_SYS_ETC}/fonts/conf.avail/99-slp.conf
chmod 664 %{TZ_SYS_ETC}/fonts/conf.avail/99-slp.conf

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{TZ_SYS_ETC}/fonts/conf.avail/99-slp.conf
%{_prefix}/etc/fonts/conf.d/99-slp.conf
%exclude %{_prefix}/etc/fonts/conf.d/documentation.list
