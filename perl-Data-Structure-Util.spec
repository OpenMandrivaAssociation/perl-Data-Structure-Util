%define upstream_name	 Data-Structure-Util
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Change nature of data within a structure
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-devel
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Clone)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
%{_mandir}/man?/*	       
