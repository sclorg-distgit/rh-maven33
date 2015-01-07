%{!?scl_name_base:%global scl_name_base maven}
%{!?scl_name_version:%global scl_name_version 30}
%{!?scl:%global scl %{scl_name_base}%{scl_name_version}}
%scl_package %scl

%global debug_package %{nil}

Name:       %scl_name
Version:    1.1
Release:    11%{?dist}
Summary:    Package that installs %scl

License:    GPLv2+
#URL:         
Source1:    macros.%{scl_name}
Source2:    javapackages-config.json
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
Requires:   %{scl_java_common}-maven-local
Requires:   %{name}-runtime = %{version}-%{release}
Requires:   %{scl_java_common}-scldevel

%description scldevel
Package shipping development files, especially useful for development of
packages depending on %scl Software Collection.

%prep
%setup -c -T
#===================#
# SCL enable script #
#===================#
cat <<EOF >enable
. /opt/rh/%{scl_java_common}/enable

# Generic variables
export PATH="%{_bindir}:\${PATH:-/bin:/usr/bin}"
export MANPATH="%{_mandir}:\${MANPATH}"
export PYTHONPATH="%{_scl_root}%{python_sitelib}\${PYTHONPATH:+:}\${PYTHONPATH:-}"

export JAVACONFDIRS="%{_sysconfdir}/java:\$JAVACONFDIRS"
export XDG_CONFIG_DIRS="%{_sysconfdir}/xdg:\$XDG_CONFIG_DIRS"
export XDG_DATA_DIRS="%{_datadir}:\$XDG_DATA_DIRS"
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

%build
# generate a helper script that will be used by help2man
cat >h2m_helper <<'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo "%{scl_name} %{version} Software Collection" || cat README
EOF
chmod a+x h2m_helper

# generate the man page
help2man -N --section 7 ./h2m_helper -o %{scl_name}.7

%install
# Parentheses are needed here as workaround for rhbz#1017085
(%scl_install)

install -d -m 755 %{buildroot}%{_scl_scripts}
install -p -m 755 enable %{buildroot}%{_scl_scripts}/

# install rpm magic
install -Dpm0644 %{SOURCE1} %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

# install dirs used by some deps
install -dm0755 %{buildroot}%{_prefix}/lib/rpm
install -dm0755 %{buildroot}%{_scl_root}%{python_sitelib}

# install generated man page
mkdir -p %{buildroot}%{_mandir}/man7/
install -m 644 %{scl_name}.7 %{buildroot}%{_mandir}/man7/%{scl_name}.7

# eclipse.conf, java.conf and javapackages-config.json
install -m 755 -d %{buildroot}%{_javaconfdir}
install -m 644 -p eclipse.conf %{buildroot}%{_javaconfdir}/
install -m 644 -p %{SOURCE2} %{buildroot}%{_javaconfdir}/
install -m 644 -p java.conf %{buildroot}%{_javaconfdir}/

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
%{_javaconfdir}/*

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

%changelog
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

