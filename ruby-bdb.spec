%define		ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define		ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define		ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define		ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')

%define		tarname		bdb

Summary:	An interface to Berkeley DB
Summary(pl):	Interfejs do Berkeley DB
Name:		ruby-bdb
Version:	0.5.6
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	ftp://moulon.inra.fr/pub/ruby/bdb.tar.gz
# Source0-md5:	b3b4fed73d7639f71e995e37a9f2a6bd
URL:		http://moulon.inra.fr/ruby/bdb.html
BuildRequires:	db-devel
BuildRequires:	make
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface to Berkeley DB.

%description -l pl
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

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{ruby_archdir}/*.so
%{ruby_ridir}/BDB*
%{_examplesdir}/%{name}-%{version}
