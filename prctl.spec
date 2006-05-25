Summary:	Utility to perform process operations
Summary(pl):	Narzêdzie do wykonywania operacji na procesach
Name:		prctl
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/prctl/%{name}-%{version}.tar.gz
# Source0-md5:	487ffeec494bf91fa7b32115fb3a08f2
# emulate PR_[GS]ET_UNALIGN on alpha using osf_[gs]etsysinfo
Patch0:		%{name}-alpha-sysinfo.patch
URL:		http://sourceforge.net/projects/prctl/
BuildRequires:	sed >= 4.0
# could be useful on other archs (hppa, s390), but Linux doesn't support it...
ExclusiveArch:	alpha ia64
ExclusiveOS:	linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The prctl utility allows a user to control certain process behavior in
the runtime environment. Supported process behavior is handling of
unaligned memory access and handling of floating point software assist
faults (on IPF systems). This utility works on Linux 2.4 and higher
kernels only.

%description -l pl
Narzêdzie prctl umo¿liwia sterowanie zachowaniem procesów w ¶rodowisku
uruchomieniowym. Obs³ugiwane zachowania to obs³uga niewyrównanego
dostêpu do pamiêci oraz obs³uga wyj±tków dla programowej obs³ugi
operacji zmiennoprzecinkowych (na systemach IPF). Narzêdzie to dzia³a
tylko pod Linuksem 2.4 i nowszym.

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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/prctl.1*
