Name:       felis-phone-start-page
Version:    1.0.0
Release:    2
Summary:    Configurable start page for Sailfish Phone
Group:      System/Tools
License:    MIT
URL:        https://github.com/MiPal666/sailfish-patches/tree/main/felis-phone-start-page
Source0:    %{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   patchmanager
Requires:   sailfish-version >= 5.2.0
Requires:   sailfish-version < 5.3.0

%description
Patchmanager patch for Sailfish OS Phone.

Allows choosing whether the Phone application opens with Dialer,
History or Contacts. The setting is available from the patch
configuration page in Patchmanager.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -p -m 0644 -D unified_diff.patch %{buildroot}%{_datadir}/patchmanager/patches/%{name}/unified_diff.patch
install -p -m 0644 -D patch.json %{buildroot}%{_datadir}/patchmanager/patches/%{name}/patch.json
install -p -m 0644 -D main.qml %{buildroot}%{_datadir}/patchmanager/patches/%{name}/main.qml

%pre
if [ -d /tmp/patchmanager3/patches/%{name} ]; then
    /usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /tmp/patchmanager3/patches/%{name} ]; then
    /usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}/unified_diff.patch
%{_datadir}/patchmanager/patches/%{name}/patch.json
%{_datadir}/patchmanager/patches/%{name}/main.qml
