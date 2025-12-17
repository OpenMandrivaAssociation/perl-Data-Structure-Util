%define upstream_name	 Data-Structure-Util

Name:		perl-%{upstream_name}
Version:	0.16
Release:	7

Summary:	Change nature of data within a structure
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Data::Structure::Util
Source0:	https://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Clone)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(ExtUtils::CBuilder)

%description
"Data::Structure::Util" is a toolbox to manipulate the data inside a
data structure. It can process an entire tree and perform the
operation requested on each appropriate element.

For example: It can transform all strings within a data structure to
utf8 or transform any utf8 string back to the default encoding. It can
remove the blessing on any reference. It can collect all the objects
or detect if there is a circular reference.

It is written in C for decent speed.


%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%check
%make_build test

%install
%make_install

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
%{_mandir}/man?/*	       
