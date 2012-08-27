#sbs-git:slp/sdk/default-fonts-fc-sdk default-fonts-fc-sdk 0.0.2 8414dbd3e62b6f7a864ba031e043dd7604b3d86d
Name:       default-fonts-fc-sdk
Summary:    Font configuration package for SDK
Version:    0.0.2
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz

%description
Font configuration package for SDK
This package is maintained by SDK team

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_prefix}/etc/fonts/conf.d/
mkdir -p %{buildroot}/opt/etc/fonts/conf.avail/ && cp -a sdk_fonts_fc/* %{buildroot}/opt/etc/fonts/conf.avail/
cd %{buildroot}%{_prefix}/etc/fonts/conf.d/
ln -s ../../../../opt/etc/fonts/conf.avail/99-slp.conf %{buildroot}%{_prefix}/etc/fonts/conf.d/99-slp.conf

%post
chown :5000 /opt/etc/fonts/conf.avail/99-slp.conf
chmod 664 /opt/etc/fonts/conf.avail/99-slp.conf

%files
%defattr(-,root,root,-)
/opt/etc/fonts/conf.avail/99-slp.conf
%{_prefix}/etc/fonts/conf.d/99-slp.conf
%exclude %{_prefix}/etc/fonts/conf.d/documentation.list
