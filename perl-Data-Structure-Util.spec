%define upstream_name	 Data-Structure-Util
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.150.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.150.0-3
+ Revision: 681382
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-2mdv2011.0
+ Revision: 555781
- rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 403086
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.15-3mdv2009.0
+ Revision: 256479
- rebuild

* Tue Mar 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.1
+ Revision: 185217
- new version

* Sun Mar 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2008.1
+ Revision: 183113
- update to new version 0.13

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.12-3mdv2008.1
+ Revision: 135831
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-3mdv2007.0
+ Revision: 73484
- import perl-Data-Structure-Util-0.12-3mdv2007.1

* Tue Jul 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-2mdv2007.0
- switch to Module::Build build
- spec cleanup
- rpmbuildupdate aware
- fix directory ownership
- fix license
- non-redundant summary
- drop redundant perl buildrequires
- better URL

* Mon Jul 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.12-1mdv2007.0
- initial Mandriva package

