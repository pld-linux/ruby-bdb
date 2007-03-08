%define		tarname		bdb
Summary:	An interface to Berkeley DB
Summary(pl.UTF-8):	Interfejs do Berkeley DB
Name:		ruby-bdb
Version:	0.6.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	ftp://moulon.inra.fr/pub/ruby/bdb-0.6.0.tar.gz
# Source0-md5:	75ed9523bc695beb2bf2c9bea2676b87
URL:		http://moulon.inra.fr/ruby/bdb.html
BuildRequires:	db-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface to Berkeley DB.

%description -l pl.UTF-8
Interfejs do Berkeley DB.

%prep
%setup -q -n %{tarname}-%{version}

%build
ruby extconf.rb
%{__make}

rdoc --ri --op ri src
rdoc --op rdoc src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{ruby_archdir}/*.so
%{ruby_ridir}/BDB*
%{_examplesdir}/%{name}-%{version}
