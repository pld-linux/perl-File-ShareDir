#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	File
%define	pnam	ShareDir
Summary:	File::ShareDir - Locate per-dist and per-module shared files
Summary(pl.UTF-8):	File::ShareDir - położenie plików współdzielonych w dystrybucji i module
Name:		perl-File-ShareDir
Version:	1.118
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0084f730f4e3d4d89703d92b3ea82f54
URL:		https://metacpan.org/release/File-ShareDir
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(File::Path) >= 2.08
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-Class-Inspector >= 1.12
BuildRequires:	perl-File-ShareDir-Install >= 0.13
BuildRequires:	perl-Params-Util >= 0.07
BuildRequires:	perl-Test-Simple >= 0.90
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

On a Linux-like system, this would be in a place such as /usr/share,
however Perl runs on a wide variety of different systems, and so the
use of any one location is unreliable.

Perl provides a little-known method for doing this, but almost nobody
is aware that it exists. As a result, module authors often go through
some very strange ways to make the data available to their code.

%description -l pl.UTF-8
Celem File::ShareDir jest zapewnienie modułu towarzyszącego modułom
Class::Inspector oraz File::HomeDir (wykonujących zadania dobrze znane
zaawansowanym programistom Perla, ale wymagających sztuczek), będącego
bardziej przystępnym dla społeczności Perla.

Często istnieje potrzeba, aby moduł Perla (z CPAN lub innego źródła)
miał dostęp do dużych ilości danych tylko do odczytu, przechowywanych
w systemie plików.

Na systemach linuksowych takie dane zwykle znajdują się miejscu typu
/usr/share, ale Perla działa na wielu różnych systemach i użycie
jednego miejsca nie jest wiarygodne.

Perl udostępnia w takim celu mało znaną metodę, ale mało kto o niej
wie. W efekcie autorzy modułów w różny dziwny sposób sprawiają, by ich
dane były dostępne dla kodu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/auto/share/{dist/File-ShareDir/{sample.txt,subdir/sample.txt},module/File-ShareDir/test_file.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/File/ShareDir.pm
%dir %{perl_vendorlib}/auto/share/module
%{_mandir}/man3/File::ShareDir.3pm*
