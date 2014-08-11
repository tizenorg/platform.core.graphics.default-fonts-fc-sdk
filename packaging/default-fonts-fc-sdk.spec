#sbs-git:slp/sdk/default-fonts-fc-sdk default-fonts-fc-sdk 0.0.2 8414dbd3e62b6f7a864ba031e043dd7604b3d86d
Name:       default-fonts-fc-sdk
Summary:    Font configuration package for SDK
Version:    0.0.4
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/default-fonts-fc-sdk.manifest
Requires:    smack-utils

%description
Font configuration package for SDK
This package is maintained by SDK team

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
export FONT_CONF_FILE="99-slp.conf"

rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/etc/fonts/conf.avail/
mkdir -p %{buildroot}/etc/opt/init/ && cp -a default-fonts-fc-sdk.init.sh %{buildroot}/etc/opt/init/
mkdir -p %{buildroot}/usr/etc/fonts/conf.d/
mkdir -p %{buildroot}/usr/opt/etc/fonts/conf.avail/ && cp -a sdk_fonts_fc/* %{buildroot}/usr/opt/etc/fonts/conf.avail/
cd %{buildroot}/usr/etc/fonts/conf.d/
ln -s ../../../../opt/etc/fonts/conf.avail/$FONT_CONF_FILE %{buildroot}/usr/etc/fonts/conf.d/$FONT_CONF_FILE

%post
chown root:app /usr/opt/etc/fonts/conf.avail/99-slp.conf
chmod 664 /usr/opt/etc/fonts/conf.avail/99-slp.conf
/etc/opt/init/default-fonts-fc-sdk.init.sh
chsmack -a '*' /opt/etc/fonts/conf.avail/99-slp.conf

%files
%manifest default-fonts-fc-sdk.manifest
%defattr(-,root,root,-)
/usr/opt/etc/fonts/conf.avail/99-slp.conf
/usr/etc/fonts/conf.d/99-slp.conf
/etc/opt/init/default-fonts-fc-sdk.init.sh
/opt/etc/fonts/conf.avail/
%exclude /usr/etc/fonts/conf.d/documentation.list
