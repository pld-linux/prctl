Summary:	Utility to perform process operations
Summary(pl.UTF-8):	Narzędzie do wykonywania operacji na procesach
Name:		prctl
Version:	1.6
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/prctl/%{name}-%{version}.tar.gz
# Source0-md5:	ba1e0ad94d6529c5adaab0895f385443
# emulate PR_[GS]ET_UNALIGN on alpha using osf_[gs]etsysinfo
Patch0:		%{name}-alpha-sysinfo.patch
URL:		http://sourceforge.net/projects/prctl/
ExclusiveOS:	linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The prctl utility allows a user to control certain process behavior in
the runtime environment. Supported process behavior is handling of
MCE memory faults, unaligned memory access (on Alpha, IA64/IPF,
PA-RISC PPC, SH and Tile systems) and floating point software assist
faults (on IA64/IPF systems). This utility works on Linux 2.4 and
higher kernels only.

%description -l pl.UTF-8
Narzędzie prctl umożliwia sterowanie zachowaniem procesów w środowisku
uruchomieniowym. Obsługiwane zachowania to obsługa błędów pamięci MCE,
niewyrównanego dostępu do pamięci (na systemach Alpha, IA64/IPF,
PA-RISC, PPC, SH i Tile) oraz wyjątków dla programowej obsługi
operacji zmiennoprzecinkowych (na systemach IA64/IPF). Narzędzie to
działa tylko pod Linuksem 2.4 i nowszym.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/prctl
%{_mandir}/man1/prctl.1*
