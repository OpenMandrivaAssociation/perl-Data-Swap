%define upstream_name    Data-Swap
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

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
