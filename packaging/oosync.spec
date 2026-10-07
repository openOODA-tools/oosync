Name:           oosync
Version:        0.1.0
Release:        1%{?dist}
Summary:        Flushes cached filesystem data from page cache buffers to non-volatile disks.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosync
Source0:        oosync-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosync is a sovereign, capability-bounded DIRTY FLUSHER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosync
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosync-uninstall

%files
/usr/bin/oosync
/usr/bin/oosync-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
