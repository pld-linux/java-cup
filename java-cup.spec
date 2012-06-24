%define		ver		0.11a
%define		pkgver		0.11a-20060912

Summary:	Java-based Constructor of Useful Parsers
Summary(pl):	Javowy konstruktor przydatnych analizator�w
Name:		java_cup
Version:	%{ver}
Release:	1
License:	BSD-like
Group:		Development/Languages/Java
Source0:	%{name}-%{pkgver}.tar.gz
# Source0-md5:	c9b26e0e6c1c02f2b37148c54b28cd8d
URL:		http://www2.cs.tum.edu/projects/cup/
BuildRequires:	ant >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java CUP is a the Java(TM)-based Constructor of Useful Parsers (CUP
for short). CUP is a system for generating LALR parsers from simple
specifications. It serves the same role as the widely used program
YACC and in fact offers most of the features of YACC. However, CUP is
written in Java, uses specifications including embedded Java code, and
produces parsers which are implemented in Java.

%description -l pl
Java CUP to oparty na Javie(TM) konstruktor u�ytecznych analizator�w
(Constructor of Useful Parsers - w skr�cie CUP). CUP to system s�u��cy
do generowania analizator�w LALR z prostych wyra�e�. S�u�y do tego
samego celu co szeroko u�ywany YACC i w wi�kszo�ci ma te same
mo�liwo�ci. Jednak CUP jest napisany w Javie, u�ywa specyfikacji
do��czaj�cej osadzony kod w Javie i tworzy analizatory
zaimplementowane w Javie.

%package javadoc
Summary:	Java CUP API documentation
Summary(pl):	Dokumentacja API Java CUP
Group:		Documentation

%description javadoc
Java CUP API documentation.

%description javadoc -l pl
Dokumentacja API Java CUP.

%prep
%setup -q -n develop

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"

%{ant} dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

cp dist/java-cup-11a.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cp dist/java-cup-11a-runtime.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-runtime-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -sf %{name}-runtime-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-runtime.jar

#cp -R dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.txt manual.html 
%{_javadir}/*.jar

#%files javadoc
#%defattr(644,root,root,755)
#%doc %{_javadocdir}/%{name}-%{version}
