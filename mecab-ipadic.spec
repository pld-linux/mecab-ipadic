Summary:	IPA dictionary for Mecab
Summary(pl.UTF-8):	Słownik IPA dla biblioteki Mecab
Name:		mecab-ipadic
Version:	2.7.0
%define	subver	20070801
# base 1 as it's post-release, not pre-release
Release:	1.%{subver}.1
License:	BSD-like
Group:		Libraries
# original dictionary:
#Download: http://sourceforge.jp/projects/ipadic/
#Source:	http://dl.sourceforge.jp/ipadic/24435/ipadic-%{ipadicversion}.tar.gz
# mecab-modified version:
#Source0Download: http://code.google.com/p/mecab/downloads/list
Source0:	http://mecab.googlecode.com/files/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	e09556657cc70e45564c6514a6b08495
URL:		http://code.google.com/p/mecab/
BuildRequires:	mecab-devel >= 0.994
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPA dictionary for Mecab.

%description -l pl.UTF-8
Słownik IPA dla biblioteki Mecab.

%prep
%setup -q -n %{name}-%{version}-%{subver}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%{_libdir}/mecab/dic/ipadic
