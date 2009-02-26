#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	ShareDir
Summary:	File::ShareDir - Locate per-dist and per-module shared files
Name:		perl-File-ShareDir
Version:	1.00
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	28f47081e7d678410bc5e0881b286a8b
URL:		http://search.cpan.org/dist/File-ShareDir/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl(Class::Inspector) >= 1.12
BuildRequires:	perl(Params::Util) >= 0.07
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The intent of File::ShareDir is to provide a companion to
Class::Inspector and File::HomeDir, modules that take a process that
is well-known by advanced Perl developers but gets a little tricky,
and make it more available to the larger Perl community.

Quite often you want or need your Perl module (CPAN or otherwise) to
have access to a large amount of read-only data that is stored on the
file-system at run-time.

On a linux-like system, this would be in a place such as /usr/share,
however Perl runs on a wide variety of different systems, and so the
use of any one location is unreliable.

Perl provides a little-known method for doing this, but almost nobody
is aware that it exists. As a result, module authors often go through
some very strange ways to make the data available to their code.

The most common of these is to dump the data out to an enormous Perl
data structure and save it into the module itself. The result are
enormous multi-megabyte .pm files that chew up a lot of memory
needlessly.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/auto/share/dist

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/*.pm
%{perl_vendorlib}/auto/share
%{_mandir}/man3/*
