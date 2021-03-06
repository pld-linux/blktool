Summary:	Replacement for "hdparm"
Summary(pl.UTF-8):	Zamiennik programu hdparm
Name:		blktool
Version:	4
Release:	0.2
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/gkernel/%{name}-%{version}.tar.gz
# Source0-md5:	9272a47c6254b506548ba10a2a9f8bb3
URL:		http://sourceforge.net/projects/gkernel/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
blktool aims to be an easier to use, and more generic version of the
existing utility 'hdparm'.

%description -l pl.UTF-8
blktool ma być łatwiejszą w użyciu i bardziej ogólną wersją
istniejącego narzędzia "hdparm".

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
