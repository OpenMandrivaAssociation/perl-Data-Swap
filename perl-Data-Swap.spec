%define upstream_name    Data-Swap
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:	Data-Swap module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:     Data-Swap-0.08-fix-format-security.patch

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module allows you to swap the contents of two referenced variables,
even if they have different types.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -b .format

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*/Data/Swap.pm
%{perl_vendorlib}/*/auto/Data/Swap
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.80.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.80.0-4
+ Revision: 681383
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-3mdv2011.0
+ Revision: 555783
- rebuild for perl 5.12

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-2mdv2010.0
+ Revision: 405949
- adding patch to fix format security error
- bump mkrel to force rebuild
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.1
+ Revision: 292102
- update to new version 0.08

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.07-3mdv2009.0
+ Revision: 256481
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2008.1
+ Revision: 152943
- update to new version 0.07
- update to new version 0.07

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.06-2mdv2008.1
+ Revision: 152049
- rebuild

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2008.1
+ Revision: 139189
- update to new version 0.06

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-2mdv2008.0
+ Revision: 86329
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdk
- initial Mandriva package

