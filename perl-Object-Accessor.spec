#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Object
%define		pnam	Accessor
Summary:	Object::Accessor - interface to create per object accessors
Name:		perl-Object-Accessor
Version:	0.48
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Object/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	46a3ce50d8817938cecbb8e02eda9500
URL:		https://metacpan.org/release/Object-Accessor
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object::Accessor provides an interface to create per object accessors
(as opposed to per Class accessors, as, for example, Class::Accessor
provides).

You can choose to either subclass this module, and thus using its
accessors on your own module, or to store an Object::Accessor object
inside your own object, and access the accessors from there. See the
SYNOPSIS for examples.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Object/Accessor.pm
%{_mandir}/man3/Object::Accessor.3*
