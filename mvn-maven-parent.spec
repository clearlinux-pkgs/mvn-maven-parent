#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-parent
Version  : 4
Release  : 3
URL      : https://github.com/apache/maven-parent/archive/maven-parent-4.tar.gz
Source0  : https://github.com/apache/maven-parent/archive/maven-parent-4.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/10/maven-parent-10.pom
Source2  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/11/maven-parent-11.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/13/maven-parent-13.pom
Source4  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/15/maven-parent-15.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/16/maven-parent-16.pom
Source6  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/19/maven-parent-19.pom
Source7  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/20/maven-parent-20.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/21/maven-parent-21.pom
Source9  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/22/maven-parent-22.pom
Source10  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/23/maven-parent-23.pom
Source11  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/24/maven-parent-24.pom
Source12  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/25/maven-parent-25.pom
Source13  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/26/maven-parent-26.pom
Source14  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/27/maven-parent-27.pom
Source15  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/30/maven-parent-30.pom
Source16  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/31/maven-parent-31.pom
Source17  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/33/maven-parent-33.pom
Source18  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/4/maven-parent-4.pom
Source19  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/5/maven-parent-5.pom
Source20  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/6/maven-parent-6.pom
Source21  : https://repo1.maven.org/maven2/org/apache/maven/maven-parent/8/maven-parent-8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-parent-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-parent package.
Group: Data

%description data
data components for the mvn-maven-parent package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/10

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/11
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/11

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/13
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/13

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/15
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/15

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/16
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/16

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/19
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/19

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/20
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/20

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/21
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/21

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/22
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/22

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/23
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/23

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/24
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/24

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/25
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/25

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/26
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/26

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/27
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/27

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/30
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/30

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/31
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/31

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/33
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/33

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/4
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/5
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/6
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/8
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-parent/8


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/10/maven-parent-10.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/11/maven-parent-11.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/13/maven-parent-13.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/15/maven-parent-15.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/16/maven-parent-16.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/19/maven-parent-19.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/20/maven-parent-20.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/21/maven-parent-21.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/22/maven-parent-22.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/23/maven-parent-23.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/24/maven-parent-24.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/25/maven-parent-25.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/26/maven-parent-26.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/27/maven-parent-27.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/30/maven-parent-30.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/31/maven-parent-31.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/33/maven-parent-33.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/4/maven-parent-4.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/5/maven-parent-5.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/6/maven-parent-6.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-parent/8/maven-parent-8.pom
