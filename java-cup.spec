%define		ver		0.10k
%define		pkgver		v10k

Summary:	Java-based Constructor of Useful Parsers
Summary(pl):	Javowy konstruktor przydatnych analizatorów
Name:		java_cup
Version:	%{ver}
Release:	1
License:	BSD-like
Group:		Development/Languages/Java
Source0:	http://www.cs.princeton.edu/~appel/modern/java/CUP/%{name}_%{pkgver}.tar.gz
# Source0-md5:	8b11edfec13c590ea443d0f0ae0da479
Source1:	%{name}-build.xml
URL:		http://www.cs.princeton.edu/~appel/modern/java/CUP/
BuildRequires:	jakarta-ant >= 1.5
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java CUP is a the Java(TM)-based Constructor of Useful Parsers (CUP
for short). CUP is a system for generating LALR parsers from simple
specifications. It serves the same role as the widely used program
YACC and in fact offers most of the features of YACC. However, CUP is
written in Java, uses specifications including embedded Java code, and
produces parsers which are implemented in Java.

%description -l pl
Java CUP to oparty na Javie(TM) konstruktor u¿ytecznych analizatorów
(Constructor of Useful Parsers - w skrócie CUP). CUP to system s³u¿±cy
do generowania analizatorów LALR z prostych wyra¿eñ. S³u¿y do tego
samego celu co szeroko u¿ywany YACC i w wiêkszo¶ci ma te same
mo¿liwo¶ci. Jednak CUP jest napisany w Javie, u¿ywa specyfikacji
do³±czaj±cej osadzony kod w Javie i tworzy analizatory
zaimplementowane w Javie.

%prep
%setup -q -c -n %{name}-%{version}
cp %{SOURCE1} build.xml

%build
ant
ant javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
cp dist/lib/%{name}.jar $RPM_BUILD_ROOT%{_javalibdir}
cp dist/lib/%{name}-runtime.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}-%{version}.jar
ln -sf %{name}-runtime.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}-runtime-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE CHANGELOG cup_logo.gif manual.html dist/javadoc/*
%{_javadir}/*.jar
