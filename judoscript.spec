Summary:	JudoScript programming language
Summary(pl):	J�zyk programowania JudoScript
Name:		judoscript
Version:	0.9
Release:	1
License:	LGPL
Group:		Development/Languages
Source0:	http://www.judoscript.com/store/judoscript-0.9.zip
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

%description -l pl
JudoScript to j�zyk skryptowy og�lnego przeznaczenia dla Javy o wielu
zastosowaniach. To oznacza, �e ma trzy �ci�le zintegrowane cz�ci: a)
j�zyk skryptowy og�lnego przeznaczenia, b) w pe�ni funkcjonalne
narz�dzie skryptowe dla Javy, c) obs�ug� wielu cech zale�nych od
zastosowania. JudoScript jest zaprojektowany i zaimplementowany w
czystej Javie, narodzi� si� z potrzeb u�ywania bogactwa w platformach
Javy (J2SE i J2EE). Jego projekt obejmuje filozofie 3GL i 4GL,
dostarczaj�c nie tylko silne wsparcie dla programowania, ale tak�e
specjalne mechanizmy do programowania WYSIWYG dla wi�kszo�ci teraz
popularnych zastosowa�, co czyni u�ywanie j�zyka �atwym, efektywnym i
eleganckim. Jest to j�zyk wy�szego poziomu zintegrowany w silnym
�rodowisku skryptowym Javy og�lnego przeznaczenia.

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
