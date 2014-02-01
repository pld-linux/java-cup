#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
#
%define		_ver		11a
%define		ver		0.%{_ver}
%define		pkgver		%{ver}-20060912
%define		srcname		cup
%include	/usr/lib/rpm/macros.java
Summary:	Java-based Constructor of Useful Parsers
Summary(pl.UTF-8):	Javowy konstruktor przydatnych analizatorów
Name:		java-cup
Version:	%{ver}
Release:	4
License:	BSD-like
Group:		Development/Languages/Java
Source0:	java_cup-%{pkgver}.tar.gz
# Source0-md5:	c9b26e0e6c1c02f2b37148c54b28cd8d
URL:		http://www2.cs.tum.edu/projects/cup/
BuildRequires:	ant >= 1.5
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Obsoletes:	javacup
Obsoletes:	java_cup
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java CUP is a the Java(TM)-based Constructor of Useful Parsers (CUP
for short). CUP is a system for generating LALR parsers from simple
specifications. It serves the same role as the widely used program
YACC and in fact offers most of the features of YACC. However, CUP is
written in Java, uses specifications including embedded Java code, and
produces parsers which are implemented in Java.

%description -l pl.UTF-8
Java CUP to oparty na Javie(TM) konstruktor użytecznych analizatorów
(Constructor of Useful Parsers - w skrócie CUP). CUP to system służący
do generowania analizatorów LALR z prostych wyrażeń. Służy do tego
samego celu co szeroko używany YACC i w większości ma te same
możliwości. Jednak CUP jest napisany w Javie, używa specyfikacji
dołączającej osadzony kod w Javie i tworzy analizatory
zaimplementowane w Javie.

%package javadoc
Summary:	Java CUP API documentation
Summary(pl.UTF-8):	Dokumentacja API Java CUP
Group:		Documentation
Obsoletes:	java_cup-javadoc

%description javadoc
Java CUP API documentation.

%description javadoc -l pl.UTF-8
Dokumentacja API Java CUP.

%prep
%setup -qc
mv develop/* .

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"

%ant dist

%if %{with javadoc}
%javadoc -d dist/javadoc src/java_cup/*.java
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

cp dist/java-cup-%{_ver}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
cp dist/java-cup-%{_ver}-runtime.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-runtime-%{version}.jar
ln -sf %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar
ln -sf %{srcname}-runtime-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-runtime.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.txt manual.html
%{_javadir}/cup-%{version}.jar
%{_javadir}/cup.jar
%{_javadir}/cup-runtime-%{version}.jar
%{_javadir}/cup-runtime.jar

# javadoc
%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
