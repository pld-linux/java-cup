%define		ver		0.10k
%define		pkgver		v10k

Summary:	Java source interpreter
Name:		java_cup
Version:	%{ver}
Release:	1
License:	Free
Group:		Development/Languages/Java
Source0:	http://www.cs.princeton.edu/~appel/modern/java/CUP/%{name}_%{pkgver}.tar.gz
# Source0-md5:	8b11edfec13c590ea443d0f0ae0da479
Source1:	%{name}-build.xml
URL: 		http://www.cs.princeton.edu/~appel/modern/java/CUP/
BuildRequires:	jakarta-ant >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
java_cup is a LALR Parser Generator for Java

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
