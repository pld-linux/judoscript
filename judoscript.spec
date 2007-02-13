Summary:	JudoScript programming language
Summary(pl.UTF-8):	Język programowania JudoScript
Name:		judoscript
Version:	0.9
Release:	1
License:	LGPL
Group:		Development/Languages
Source0:	http://www.judoscript.com/store/%{name}-%{version}.zip
# Source0-md5:	0b0ebf98e2bf25e0404dd1acb3554b92
URL:		http://www.judoscript.com/
BuildRequires:	unzip
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JudoScript is a general-purpose, Java scripting and multi-domain
language. What this means is, it has three tightly integrated parts:
a) a general-purpose scripting language, b) a fully capable Java
scripting tool, and c) support for multiple domain-specific features.
It is designed and implemented in pure Java, born out of the needs of
using the riches in the Java platforms (J2SE and J2EE) and beyond.
Its design embraces both 3GL and 4GL philosophies, providing not only
strong programming support but also special mechanisms of "WYSIWYG"
programming for most of today's popular computing areas, making their
uses easy, effective and elegant. It is a higher-level language
integrated in a robust, general-purpose Java scripting environment.

%description -l pl.UTF-8
JudoScript to język skryptowy ogólnego przeznaczenia dla Javy o wielu
zastosowaniach. To oznacza, że ma trzy ściśle zintegrowane części: a)
język skryptowy ogólnego przeznaczenia, b) w pełni funkcjonalne
narzędzie skryptowe dla Javy, c) obsługę wielu cech zależnych od
zastosowania. JudoScript jest zaprojektowany i zaimplementowany w
czystej Javie, narodził się z potrzeb używania bogactwa w platformach
Javy (J2SE i J2EE). Jego projekt obejmuje filozofie 3GL i 4GL,
dostarczając nie tylko silne wsparcie dla programowania, ale także
specjalne mechanizmy do programowania WYSIWYG dla większości teraz
popularnych zastosowań, co czyni używanie języka łatwym, efektywnym i
eleganckim. Jest to język wyższego poziomu zintegrowany w silnym
środowisku skryptowym Javy ogólnego przeznaczenia.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_examplesdir}}

install judo.jar $RPM_BUILD_ROOT%{_javadir}
cp -rf examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc articles ref share relnote.html
%{_javadir}/*.jar
%{_examplesdir}/%{name}-%{version}
