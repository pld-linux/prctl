Summary:	Utility to perform process operations
Summary(pl):	Narz�dzie do wykonywania operacji na procesach
Name:		prctl
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/prctl/%{name}-%{version}.tar.gz
# Source0-md5:	f494842da5edc7c84adf506685301052
URL:		http://sourceforge.net/projects/prctl/
BuildRequires:	sed >= 4.0
# could be useful on other archs (alpha, hppa, s390), but Linux doesn't support it...
ExclusiveArch:	ia64
ExclusiveOS:	linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The prctl utility allows a user to control certain process behavior in
the runtime environment. Supported process behavior is handling of
unaligned memory access and handling of floating point software assist
faults (on IPF systems). This utility works on Linux 2.4 and higher
kernels only.

%description -l pl
Narz�dzie prctl umo�liwia sterowanie zachowaniem proces�w w �rodowisku
uruchomieniowym. Obs�ugiwane zachowania to obs�uga niewyr�wnanego
dost�pu do pami�ci oraz obs�uga wyj�tk�w dla programowej obs�ugi
operacji zmiennoprzecinkowych (na systemach IPF). Narz�dzie to dzia�a
tylko pod Linuksem 2.4 i nowszym.

%prep
%setup -q

# take prctl() prototype from libc
sed -i -e 's,linux/prctl\.h,sys/prctl.h,' prctl.c

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
