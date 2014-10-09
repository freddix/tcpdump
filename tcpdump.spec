Summary:	Powerful command-line packet analyzer
Name:		tcpdump
Version:	4.6.2
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	74d0d3728b3cdc60db872d842e7f1598
URL:		http://www.tcpdump.org/
BuildRequires:	libcap-ng-devel
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpdump prints out a description of the contents of packets on
a network interface that match the boolean expression.

%prep
%setup -q

# freddix specific fix, avoid searching local directries
%{__sed} -i '446,447d' aclocal.m4

%build
export CFLAGS="%{rpmcflags} %{rpmcppflags}"
export LDFLAGS="%{rpmldflags}"
%{__aclocal}
%{__autoconf}
%configure \
	--enable-ipv6 \
	--with-crypto
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_sbindir}/tcpdump.%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE
%attr(755,root,root) %{_sbindir}/tcpdump
%{_mandir}/man1/tcpdump.1*

