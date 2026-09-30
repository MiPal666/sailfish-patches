Name:       felis-sharp-caller-photo
Version:    1.0.0
Release:    2
Summary:    Sharp caller photo and cleaner call screen for Sailfish Phone
Group:      System/Tools
License:    MIT
URL:        https://github.com/MiPal666/sailfish-patches/tree/main/felis-sharp-caller-photo
Source0:    %{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   patchmanager
Requires:   sailfish-version >= 5.2.0
Requires:   sailfish-version < 5.3.0

%description
Patchmanager patch for Sailfish OS Phone.

Shows caller photos without blur, uses a clean black call screen layout
and removes the large green incoming-call swipe overlay while keeping
the answer/reject gesture functional.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -p -m 0644 -D unified_diff.patch %{buildroot}%{_datadir}/patchmanager/patches/%{name}/unified_diff.patch
install -p -m 0644 -D patch.json %{buildroot}%{_datadir}/patchmanager/patches/%{name}/patch.json

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
