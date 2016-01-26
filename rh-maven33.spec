%{!?scl_name_base:%global scl_name_base rh-maven}
%{!?scl_name_version:%global scl_name_version 33}
%{!?scl:%global scl %{scl_name_base}%{scl_name_version}}
%scl_package %scl

%global debug_package %{nil}

Name:       %scl_name
Version:    1
Release:    9%{?dist}
Summary:    Package that installs %scl

License:    GPLv2+
#URL:
Source1:    macros.%{scl_name}
Source2:    javapackages-config.json
Source3:    xmvn-configuration.xml
Source4:    README
Source5:    LICENSE

BuildRequires:  help2man
BuildRequires:  scl-utils-build

Requires:         %{name}-runtime = %{version}-%{release}
Requires:         %{scl_name}-maven

%description
This is the main package for the %scl Software Collection.

%package runtime
Summary:    Package that handles %scl Software Collection.
Requires:   scl-utils
Requires:   java-1.7.0-openjdk-devel
# XXX remove when BRs are fixed in all rh-maven33 packages
Requires:   %{name}-maven-local = %{version}-%{release}
Requires:   %{name}-ivy-local = %{version}-%{release}
Requires:   %{name}-javapackages-local = %{version}-%{release}

%description runtime
Package shipping essential scripts to work with the %scl Software Collection.

%package build
Summary:    Build support tools for the %scl Software Collection.
Requires:   scl-utils-build
Requires:   %{name}-scldevel = %{version}-%{release}

%description build
Package shipping essential configuration marcros/files in order to be able
to build %scl Software Collection.

%package scldevel
Summary:    Package shipping development files for %scl
Requires:   %{name}-maven-local = %{version}-%{release}
Requires:   %{name}-runtime = %{version}-%{release}
Requires:   %{?scl_prefix_java_common}scldevel

%description scldevel
Package shipping development files, especially useful for development of
packages depending on %scl Software Collection.

# javapackages-tools counterparts for rh-maven33 collection
%package maven-local
Summary:        Support for Maven packaging
Requires:       %{?scl_prefix_java_common}javapackages-tools
Requires:       %{name}-javapackages-local = %{version}-%{release}
Requires:       %{?scl_prefix}maven
Requires:       %{?scl_prefix}xmvn >= 2
Requires:       %{?scl_prefix}xmvn-mojo >= 2
Requires:       %{?scl_prefix}xmvn-connector-aether >= 2
# POM files needed by maven itself
Requires:       %{?scl_prefix}apache-commons-parent
Requires:       %{?scl_prefix}apache-parent
Requires:       %{?scl_prefix}geronimo-parent-poms
Requires:       %{?scl_prefix}httpcomponents-project
Requires:       %{?scl_prefix}jboss-parent
Requires:       %{?scl_prefix}jvnet-parent
Requires:       %{?scl_prefix}maven-parent
Requires:       %{?scl_prefix}maven-plugins-pom
Requires:       %{?scl_prefix}mojo-parent
Requires:       %{?scl_prefix}plexus-components-pom
Requires:       %{?scl_prefix}plexus-pom
Requires:       %{?scl_prefix}plexus-tools-pom
Requires:       %{?scl_prefix}sonatype-oss-parent
Requires:       %{?scl_prefix}weld-parent
# Common Maven plugins required by almost every build. It wouldn't make
# sense to explicitly require them in every package built with Maven.
Requires:       %{?scl_prefix}maven-assembly-plugin
Requires:       %{?scl_prefix}maven-compiler-plugin
Requires:       %{?scl_prefix}maven-enforcer-plugin
Requires:       %{?scl_prefix}maven-jar-plugin
Requires:       %{?scl_prefix}maven-javadoc-plugin
Requires:       %{?scl_prefix}maven-resources-plugin
Requires:       %{?scl_prefix}maven-surefire-plugin
# Tests based on JUnit are very common and JUnit itself is small.
# Include JUnit provider for Surefire just for convenience.
Requires:       %{?scl_prefix}maven-surefire-provider-junit
# testng is quite common as well
Requires:       %{?scl_prefix}maven-surefire-provider-testng
Requires:       %{?scl_prefix_java_common}maven-local-support

%description maven-local
This package provides tools to support packaging Maven artifacts.

%package ivy-local
Summary:        Support for Apache Ivy packaging
Requires:       %{?scl_prefix_java_common}javapackages-tools
Requires:       %{name}-javapackages-local = %{version}-%{release}
Requires:       %{?scl_prefix}apache-ivy
Requires:       %{?scl_prefix}xmvn-connector-ivy >= 2
Requires:       %{?scl_prefix_java_common}ivy-local-support

%description ivy-local
This package provides tools to support Apache Ivy packaging.

%package javapackages-local
Summary:        Non-essential tools for Java packaging
Requires:       %{?scl_prefix_java_common}javapackages-tools
Requires:       %{?scl_prefix}xmvn-install >= 2
Requires:       %{?scl_prefix}xmvn-subst >= 2
Requires:       %{?scl_prefix}xmvn-resolve >= 2
Requires:       %{?scl_prefix_java_common}javapackages-local-support

%description javapackages-local
This package provides non-essential tools for Java packaging.

%prep
%setup -c -T
#===================#
# SCL enable script #
#===================#
cat <<EOF >enable
. /opt/rh/%{scl_java_common}/enable

# Generic variables
export PATH="%{_bindir}:\${PATH:-/bin:/usr/bin}"
export MANPATH="%{_mandir}\${MANPATH:+:}\${MANPATH:-}"
export PYTHONPATH="%{_scl_root}%{python_sitelib}\${PYTHONPATH:+:}\${PYTHONPATH:-}"

export JAVACONFDIRS="%{_sysconfdir}/java\${JAVACONFDIRS:+:}\${JAVACONFDIRS:-}"
export XDG_CONFIG_DIRS="%{_sysconfdir}/xdg\${XDG_CONFIG_DIRS:+:}\${XDG_CONFIG_DIRS:-}"
export XDG_DATA_DIRS="%{_datadir}\${XDG_DATA_DIRS:+:}\${XDG_DATA_DIRS:-}"
EOF

# Generate Eclipse configuration file
cat <<EOF >eclipse.conf
eclipse.bundles=%{_javadir},%{_jnidir}
scl.namespace=%{?scl}
scl.root=%{?_scl_root}
EOF

# Generate java.conf
cat <<EOF >java.conf
JAVA_LIBDIR=/opt/rh/%{scl_name}/root/usr/share/java
JNI_LIBDIR=/opt/rh/%{scl_name}/root/usr/lib/java
JVM_ROOT=/opt/rh/%{scl_name}/root/usr/lib/jvm
EOF

# This section generates README file from a template and creates man page
# from that file, expanding RPM macros in the template file.
cat >README <<'EOF'
%{expand:%(cat %{SOURCE4})}
EOF

# copy the license file so %%files section sees it
cp %{SOURCE5} .

cp %{SOURCE1} macros.%{scl_name}
cat >> macros.%{scl_name} << EOF
%%_sysconfdir_maven %_sysconfdir
%%_prefix_maven %_prefix
%%_exec_prefix_maven %_exec_prefix
%%_bindir_maven %_bindir
%%_libdir_maven %_libdir
%%_libexecdir_maven %_libexecdir
%%_sbindir_maven %_sbindir
%%_sharedstatedir_maven %_sharedstatedir
%%_datarootdir_maven %_datarootdir
%%_datadir_maven %_datadir
%%_includedir_maven %_includedir
%%_infodir_maven %_infodir
%%_mandir_maven %_mandir
%%_localstatedir_maven %_localstatedir
%%_initddir_maven %_initddir
%%_javadir_maven %_javadir
%%_jnidir_maven %_jnidir
%%_javadocdir_maven %_javadocdir
%%_mavenpomdir_maven %_mavenpomdir
%%_jvmdir_maven %_jvmdir
%%_jvmsysconfdir_maven %_jvmsysconfdir
%%_jvmcommonsysconfdir_maven %_jvmcommonsysconfdir
%%_jvmjardir_maven %_jvmjardir
%%_jvmprivdir_maven %_jvmprivdir
%%_jvmlibdir_maven %_jvmlibdir
%%_jvmdatadir_maven %_jvmdatadir
%%_jvmcommonlibdir_maven %_jvmcommonlibdir
%%_jvmcommondatadir_maven %_jvmcommondatadir
%%_javaconfdir_maven %_javaconfdir
EOF

%build
# generate a helper script that will be used by help2man
cat >h2m_helper <<'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo "%{scl_name} %{version} Software Collection" || cat README
EOF
chmod a+x h2m_helper

# generate the man page
help2man -N --section 7 ./h2m_helper -o %{scl_name}.7
# Fix single quotes in man page.
sed -i "s/'/\\\\(aq/g" %{scl_name}.7

%install
# Parentheses are needed here as workaround for rhbz#1017085
(%scl_install)

install -d -m 755 %{buildroot}%{_scl_scripts}
install -p -m 755 enable %{buildroot}%{_scl_scripts}/

# install rpm magic
install -Dpm0644 macros.%{scl_name} %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

# install dirs used by some deps
install -dm0755 %{buildroot}%{_prefix}/lib/rpm
install -dm0755 %{buildroot}%{_scl_root}%{python_sitelib}

# install generated man page
mkdir -p %{buildroot}%{_mandir}/man7/
install -m 644 %{scl_name}.7 %{buildroot}%{_mandir}/man7/%{scl_name}.7

# eclipse.conf, java.conf, javapackages-config.json and XMvn config
install -m 755 -d %{buildroot}%{_javaconfdir}
install -m 644 -p eclipse.conf %{buildroot}%{_javaconfdir}/
install -m 644 -p %{SOURCE2} %{buildroot}%{_javaconfdir}/
install -m 644 -p java.conf %{buildroot}%{_javaconfdir}/
install -m 755 -d %{buildroot}%{_sysconfdir}/xdg/xmvn
install -m 644 -p %{SOURCE3} %{buildroot}%{_sysconfdir}/xdg/xmvn/configuration.xml

install -m 755 -d %{buildroot}%{_jnidir}
install -m 755 -d %{buildroot}%{_javadir}
install -m 755 -d %{buildroot}%{_javadocdir}
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 755 -d %{buildroot}%{_mandir}/man7
install -m 755 -d %{buildroot}%{_datadir}/maven-metadata
install -m 755 -d %{buildroot}%{_mavenpomdir}
install -m 755 -d %{buildroot}%{_datadir}/xmvn

# Empty package (no file content).  The sole purpose of this package
# is collecting its dependencies so that the whole SCL can be
# installed by installing %{name}.
%files

%files runtime
%doc README LICENSE
%{scl_files}
%{_prefix}/lib/python2.*
%{_prefix}/lib/rpm
%{_mandir}/man7/%{scl_name}.*
%{_javaconfdir}/
%dir %{_jnidir}
%dir %{_javadir}
%dir %{_javadocdir}
%dir %{_mandir}/man1
%dir %{_mandir}/man7
%dir %{_datadir}/maven-metadata
%dir %{_mavenpomdir}
%dir %{_datadir}/xmvn

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

%files maven-local
%files ivy-local
%files javapackages-local

%changelog
* Tue Jan 26 2016 Michal Srb <msrb@redhat.com> - 1-9
- Fix R on javapackages-tools

* Tue Jan 19 2016 Michal Srb <msrb@redhat.com> - 1-8
- Introduce maven33-specific "local" subpackages
- Drop temp requires

* Mon Jan 18 2016 Michal Srb <msrb@redhat.com> - 1-7
- Remove fake sonatype provides
- Partially remove maven-wagon requires

* Mon Jan 18 2016 Michal Srb <msrb@redhat.com> - 1-6
- Fix R on rh-java-common packages

* Mon Jan 18 2016 Michal Srb <msrb@redhat.com> - 1-5
- Remove maven30 from PATH

* Thu Jan 14 2016 Michal Srb <msrb@redhat.com> - 1-4
- Reduce number of fake provides

* Tue Jan 12 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-3
- Temporarly add maven30 to PATH

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1-2
- Temporarily require all maven33 packages

* Fri Jan 08 2016 Michal Srb <msrb@redhat.com> 1-1
- Alter for rh-maven33

* Tue Jul 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-27
- Fix syntax errors in manpage

* Wed Jun 10 2015 Michal Srb <msrb@redhat.com> - 1.1-26
- Convert back to arch

* Tue Jun  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-25
- Convert to noarch

* Mon Feb  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-24
- Be more careful when setting env variables in enable script

* Fri Jan 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-23
- Obsolete xml-commons-apis

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-22
- Remove temp provides

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-21
- Add temp provides to fix Thermostat bulid

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 1.1-20
- Own %%{_javaconfdir}

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-19
- Revert adding directory ownership

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-18
- Add explicit directory attributes

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-17
- Own directories created by other packages

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-16
- Obsolete packages removed in RHSCL 2.0

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.1-15
- Mass rebuild 2015-01-13

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com>
- Generates macros for directories

* Wed Jan  7 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-13
- Fix XMvn config location

* Wed Jan  7 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-12
- Install XMvn configuration

* Wed Jan  7 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-11
- Don't use scl_source to enable %{scl_java_common}

* Tue Jan 06 2015 Michal Srb <msrb@redhat.com> - 1.1-10
- Add java.conf for maven30

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.1-9
- Mass rebuild 2015-01-06

* Wed Dec 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8
- Avoid generating requires on java-headless

* Thu Dec 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-7
- Add eclipse.conf file
- Add javapackages-config.json

* Wed Dec 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-6
- Switch to dependency generator from rh-java-common

* Wed Dec 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-5
- Add dependency on rh-java-common

* Thu Jul 31 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-4
- Add %%scl_maven and %%scl_prefix_maven macros to scldevel package
- Resolves: rhbz#1125274

* Mon Jun  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3
- Update README file

* Mon Jun  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-2
- Disable debuginfo

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Set metapackage version to 1.1

* Tue May 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.5-5
- Use python_sitelib marco

* Tue May 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.5-4
- Re-enable Python auto-requires

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.5-3
- Temporarly disable Python auto-requires

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.5-2
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.5-1
- Remove common subpackage
- Fix up requires in subpackages on various parts of SCL and deps
- Own a few unowned directories

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-22
- Ultimately remove provides for java and java-devel

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-21
- Restore provides for java and java-devel

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-20
- Remove bogus provides

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-19
- Don't install java.conf for base RHEL

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-18
- Add requires on maven30-maven-local to maven30-runtime

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-17
- Install java.conf for base RHEL

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-16
- Add jpackage-utils provides

* Wed Feb 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-15
- Provide java-devel in addition to java

* Wed Feb 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-14
- Temporally add base RHEL to javapackages search path

* Wed Feb 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-13
- Set PYTHONPATH in requires/provides wrapper scripts

* Wed Feb 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-12
- Fix requires/provides wrapper scripts

* Wed Feb 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-11
- Temporarly add XMvn config variables to enable script

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-10
- Provide and obsolete javapackages-tools

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-9
- Don't install XMvn configuration files

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-8
- Avoid trailing colon in PYTHONPATH

* Tue Feb 11 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-7
- Prefix PYTHONPATH with _scl_root

* Tue Feb 11 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-6
- Fix PYTHONPATH to root of python_sitelib instead of subdir

* Fri Feb 07 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-5
- Extend PYTHONPATH in enable scriptlet

* Fri Feb 07 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-4
- Add epoch to provides to match original

* Fri Feb 07 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-3
- Build-provide java 1.7.0

* Wed Feb 05 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-2
- Make scl-utils requires unversioned

* Wed Feb 05 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-1
- Initial maven30 scl metapackage

