%{!?scl_name_base:%global scl_name_base rh-maven}
%{!?scl_name_version:%global scl_name_version 33}
%{!?scl:%global scl %{scl_name_base}%{scl_name_version}}
%scl_package %scl

%global debug_package %{nil}

Name:       %scl_name
Version:    1
Release:    7%{?dist}
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
# XXX remove
Requires:   rh-maven33
Requires:   rh-maven33-ant-antunit
Requires:   rh-maven33-ant-contrib
Requires:   rh-maven33-aopalliance
Requires:   rh-maven33-apache-commons-configuration
Requires:   rh-maven33-apache-commons-daemon
Requires:   rh-maven33-apache-commons-daemon-jsvc
Requires:   rh-maven33-apache-commons-digester
Requires:   rh-maven33-apache-commons-exec
Requires:   rh-maven33-apache-commons-jexl
Requires:   rh-maven33-apache-commons-jxpath
Requires:   rh-maven33-apache-commons-lang3
Requires:   rh-maven33-apache-commons-parent
Requires:   rh-maven33-apache-commons-validator
Requires:   rh-maven33-apache-commons-vfs
Requires:   rh-maven33-apache-commons-vfs-ant
Requires:   rh-maven33-apache-commons-vfs-examples
Requires:   rh-maven33-apache-ivy
Requires:   rh-maven33-apache-parent
Requires:   rh-maven33-apache-rat
Requires:   rh-maven33-apache-rat-core
Requires:   rh-maven33-apache-rat-plugin
Requires:   rh-maven33-apache-rat-tasks
Requires:   rh-maven33-apache-resource-bundles
Requires:   rh-maven33-aqute-bnd
Requires:   rh-maven33-aqute-bndlib
Requires:   rh-maven33-avalon-framework
Requires:   rh-maven33-avalon-logkit
Requires:   rh-maven33-base64coder
Requires:   rh-maven33-beust-jcommander
Requires:   rh-maven33-bsh
Requires:   rh-maven33-bsh-utils
Requires:   rh-maven33-build
Requires:   rh-maven33-buildnumber-maven-plugin
Requires:   rh-maven33-cal10n
Requires:   rh-maven33-cdi-api
Requires:   rh-maven33-cglib
Requires:   rh-maven33-cobertura
Requires:   rh-maven33-codehaus-parent
Requires:   rh-maven33-codemodel
Requires:   rh-maven33-color-filesystem
Requires:   rh-maven33-exec-maven-plugin
Requires:   rh-maven33-felix-bundlerepository
Requires:   rh-maven33-felix-osgi-compendium
Requires:   rh-maven33-felix-osgi-core
Requires:   rh-maven33-felix-osgi-foundation
Requires:   rh-maven33-felix-osgi-obr
Requires:   rh-maven33-felix-parent
Requires:   rh-maven33-felix-shell
Requires:   rh-maven33-felix-utils
Requires:   rh-maven33-fop
Requires:   rh-maven33-forge-parent
Requires:   rh-maven33-fusesource-pom
Requires:   rh-maven33-geronimo-jaxrpc
Requires:   rh-maven33-geronimo-jms
Requires:   rh-maven33-geronimo-osgi-support
Requires:   rh-maven33-geronimo-parent-poms
Requires:   rh-maven33-geronimo-saaj
Requires:   rh-maven33-gnu-getopt
Requires:   rh-maven33-google-guice
Requires:   rh-maven33-groovy
Requires:   rh-maven33-guice-parent
Requires:   rh-maven33-httpcomponents-client
Requires:   rh-maven33-httpcomponents-core
Requires:   rh-maven33-httpcomponents-project
Requires:   rh-maven33-httpunit
Requires:   rh-maven33-httpunit-doc
Requires:   rh-maven33-icc-profiles-openicc
Requires:   rh-maven33-istack-commons
Requires:   rh-maven33-istack-commons-maven-plugin
Requires:   rh-maven33-javacc
Requires:   rh-maven33-javacc-maven-plugin
Requires:   rh-maven33-javassist
Requires:   rh-maven33-jboss-ejb-3.1-api
Requires:   rh-maven33-jboss-el-2.2-api
Requires:   rh-maven33-jboss-interceptors-1.1-api
Requires:   rh-maven33-jboss-jaxrpc-1.1-api
Requires:   rh-maven33-jboss-parent
Requires:   rh-maven33-jboss-servlet-3.0-api
Requires:   rh-maven33-jboss-specs-parent
Requires:   rh-maven33-jboss-transaction-1.1-api
Requires:   rh-maven33-jdependency
Requires:   rh-maven33-jettison
Requires:   rh-maven33-jetty-artifact-remote-resources
Requires:   rh-maven33-jetty-assembly-descriptors
Requires:   rh-maven33-jetty-build-support
Requires:   rh-maven33-jetty-distribution-remote-resources
Requires:   rh-maven33-jetty-parent
Requires:   rh-maven33-jetty-test-policy
Requires:   rh-maven33-jetty-toolchain
Requires:   rh-maven33-jetty-version-maven-plugin
Requires:   rh-maven33-jflex
Requires:   rh-maven33-jline
Requires:   rh-maven33-jna
Requires:   rh-maven33-jna-contrib
Requires:   rh-maven33-joda-convert
Requires:   rh-maven33-joda-time
Requires:   rh-maven33-jsr-305
Requires:   rh-maven33-jtidy
Requires:   rh-maven33-jvnet-parent
Requires:   rh-maven33-keytool-maven-plugin
Requires:   rh-maven33-kxml
Requires:   rh-maven33-maven
Requires:   rh-maven33-maven-antrun-plugin
Requires:   rh-maven33-maven-archiver
Requires:   rh-maven33-maven-artifact
Requires:   rh-maven33-maven-artifact-manager
Requires:   rh-maven33-maven-artifact-resolver
Requires:   rh-maven33-maven-assembly-plugin
Requires:   rh-maven33-maven-cal10n-plugin
Requires:   rh-maven33-maven-changes-plugin
Requires:   rh-maven33-maven-clean-plugin
Requires:   rh-maven33-maven-common-artifact-filters
Requires:   rh-maven33-maven-compiler-plugin
Requires:   rh-maven33-maven-dependency-analyzer
Requires:   rh-maven33-maven-dependency-plugin
Requires:   rh-maven33-maven-dependency-tree
Requires:   rh-maven33-maven-deploy-plugin
Requires:   rh-maven33-maven-downloader
Requires:   rh-maven33-maven-doxia
Requires:   rh-maven33-maven-doxia-core
Requires:   rh-maven33-maven-doxia-logging-api
Requires:   rh-maven33-maven-doxia-module-apt
Requires:   rh-maven33-maven-doxia-module-confluence
Requires:   rh-maven33-maven-doxia-module-docbook-simple
Requires:   rh-maven33-maven-doxia-module-fml
Requires:   rh-maven33-maven-doxia-module-fo
Requires:   rh-maven33-maven-doxia-module-latex
Requires:   rh-maven33-maven-doxia-module-rtf
Requires:   rh-maven33-maven-doxia-modules
Requires:   rh-maven33-maven-doxia-module-twiki
Requires:   rh-maven33-maven-doxia-module-xdoc
Requires:   rh-maven33-maven-doxia-module-xhtml
Requires:   rh-maven33-maven-doxia-sink-api
Requires:   rh-maven33-maven-doxia-sitetools
Requires:   rh-maven33-maven-doxia-test-docs
Requires:   rh-maven33-maven-doxia-tests
Requires:   rh-maven33-maven-doxia-tools
Requires:   rh-maven33-maven-enforcer
Requires:   rh-maven33-maven-enforcer-api
Requires:   rh-maven33-maven-enforcer-plugin
Requires:   rh-maven33-maven-enforcer-rules
Requires:   rh-maven33-maven-error-diagnostics
Requires:   rh-maven33-maven-failsafe-plugin
Requires:   rh-maven33-maven-file-management
Requires:   rh-maven33-maven-filtering
Requires:   rh-maven33-maven-gpg-plugin
Requires:   rh-maven33-maven-install-plugin
Requires:   rh-maven33-maven-invoker
Requires:   rh-maven33-maven-invoker-plugin
Requires:   rh-maven33-maven-jar-plugin
Requires:   rh-maven33-maven-jarsigner-plugin
Requires:   rh-maven33-maven-jxr
Requires:   rh-maven33-maven-model
Requires:   rh-maven33-maven-monitor
Requires:   rh-maven33-maven-osgi
Requires:   rh-maven33-maven-parent
Requires:   rh-maven33-maven-plugin-annotations
Requires:   rh-maven33-maven-plugin-build-helper
Requires:   rh-maven33-maven-plugin-bundle
Requires:   rh-maven33-maven-plugin-descriptor
Requires:   rh-maven33-maven-plugin-jxr
Requires:   rh-maven33-maven-plugin-plugin
Requires:   rh-maven33-maven-plugin-registry
Requires:   rh-maven33-maven-plugins-pom
Requires:   rh-maven33-maven-plugin-testing
Requires:   rh-maven33-maven-plugin-testing-harness
Requires:   rh-maven33-maven-plugin-testing-tools
Requires:   rh-maven33-maven-plugin-tools
Requires:   rh-maven33-maven-plugin-tools-annotations
Requires:   rh-maven33-maven-plugin-tools-ant
Requires:   rh-maven33-maven-plugin-tools-api
Requires:   rh-maven33-maven-plugin-tools-beanshell
Requires:   rh-maven33-maven-plugin-tools-generators
Requires:   rh-maven33-maven-plugin-tools-java
Requires:   rh-maven33-maven-plugin-tools-model
Requires:   rh-maven33-maven-profile
Requires:   rh-maven33-maven-project
Requires:   rh-maven33-maven-project-info-reports-plugin
Requires:   rh-maven33-maven-release
Requires:   rh-maven33-maven-release-manager
Requires:   rh-maven33-maven-release-plugin
Requires:   rh-maven33-maven-remote-resources-plugin
Requires:   rh-maven33-maven-reporting-api
Requires:   rh-maven33-maven-reporting-exec
Requires:   rh-maven33-maven-reporting-impl
Requires:   rh-maven33-maven-repository-builder
Requires:   rh-maven33-maven-resources-plugin
Requires:   rh-maven33-maven-scm
Requires:   rh-maven33-maven-scm-test
Requires:   rh-maven33-maven-script
Requires:   rh-maven33-maven-script-ant
Requires:   rh-maven33-maven-script-beanshell
Requires:   rh-maven33-maven-script-interpreter
Requires:   rh-maven33-maven-settings
Requires:   rh-maven33-maven-shade-plugin
Requires:   rh-maven33-maven-shared
Requires:   rh-maven33-maven-shared-incremental
Requires:   rh-maven33-maven-shared-io
Requires:   rh-maven33-maven-shared-jar
Requires:   rh-maven33-maven-shared-utils
Requires:   rh-maven33-maven-site-plugin
Requires:   rh-maven33-maven-source-plugin
Requires:   rh-maven33-maven-surefire
Requires:   rh-maven33-maven-surefire-plugin
Requires:   rh-maven33-maven-surefire-provider-junit
Requires:   rh-maven33-maven-surefire-provider-testng
Requires:   rh-maven33-maven-surefire-report-parser
Requires:   rh-maven33-maven-surefire-report-plugin
Requires:   rh-maven33-maven-test-tools
Requires:   rh-maven33-maven-toolchain
Requires:   rh-maven33-maven-verifier
Requires:   rh-maven33-maven-wagon
Requires:   rh-maven33-maven-wagon-file
Requires:   rh-maven33-maven-wagon-ftp
Requires:   rh-maven33-maven-wagon-http
Requires:   rh-maven33-maven-wagon-http-lightweight
Requires:   rh-maven33-maven-wagon-http-shared
Requires:   rh-maven33-maven-wagon-provider-api
Requires:   rh-maven33-maven-wagon-providers
Requires:   rh-maven33-maven-wagon-scm
Requires:   rh-maven33-maven-wagon-ssh-common
Requires:   rh-maven33-maven-wagon-ssh-external
Requires:   rh-maven33-maven-war-plugin
Requires:   rh-maven33-modello
Requires:   rh-maven33-mojo-parent
Requires:   rh-maven33-munge-maven-plugin
Requires:   rh-maven33-objectweb-anttask
Requires:   rh-maven33-plexus-ant-factory
Requires:   rh-maven33-plexus-archiver
Requires:   rh-maven33-plexus-bsh-factory
Requires:   rh-maven33-plexus-build-api
Requires:   rh-maven33-plexus-cdc
Requires:   rh-maven33-plexus-cipher
Requires:   rh-maven33-plexus-classworlds
Requires:   rh-maven33-plexus-cli
Requires:   rh-maven33-plexus-compiler
Requires:   rh-maven33-plexus-compiler-extras
Requires:   rh-maven33-plexus-compiler-pom
Requires:   rh-maven33-plexus-component-api
Requires:   rh-maven33-plexus-component-factories-pom
Requires:   rh-maven33-plexus-components-pom
Requires:   rh-maven33-plexus-containers
Requires:   rh-maven33-plexus-containers-component-annotations
Requires:   rh-maven33-plexus-containers-component-metadata
Requires:   rh-maven33-plexus-containers-container-default
Requires:   rh-maven33-plexus-digest
Requires:   rh-maven33-plexus-i18n
Requires:   rh-maven33-plexus-interactivity
Requires:   rh-maven33-plexus-interactivity-api
Requires:   rh-maven33-plexus-interactivity-jline
Requires:   rh-maven33-plexus-interpolation
Requires:   rh-maven33-plexus-io
Requires:   rh-maven33-plexus-mail-sender
Requires:   rh-maven33-plexus-pom
Requires:   rh-maven33-plexus-resources
Requires:   rh-maven33-plexus-sec-dispatcher
Requires:   rh-maven33-plexus-tools-pom
Requires:   rh-maven33-plexus-utils
Requires:   rh-maven33-plexus-velocity
Requires:   rh-maven33-runtime
Requires:   rh-maven33-sac
Requires:   rh-maven33-saxon
Requires:   rh-maven33-saxon-scripts
Requires:   rh-maven33-scldevel
Requires:   rh-maven33-snakeyaml
Requires:   rh-maven33-sonatype-oss-parent
Requires:   rh-maven33-sonatype-plugins-parent
Requires:   rh-maven33-spice-parent
Requires:   rh-maven33-stax2-api
Requires:   rh-maven33-testng
Requires:   rh-maven33-velocity
Requires:   rh-maven33-weld-parent
Requires:   rh-maven33-woodstox-core
Requires:   rh-maven33-wsdl4j
Requires:   rh-maven33-xml-commons-apis12
Requires:   rh-maven33-xmlgraphics-commons
Requires:   rh-maven33-xml-maven-plugin
Requires:   rh-maven33-xml-stylebook
Requires:   rh-maven33-xmlunit
Requires:   rh-maven33-xmvn
Requires:   rh-maven33-xmvn-api
Requires:   rh-maven33-xmvn-bisect
Requires:   rh-maven33-xmvn-connector-aether
Requires:   rh-maven33-xmvn-connector-ivy
Requires:   rh-maven33-xmvn-core
Requires:   rh-maven33-xmvn-install
Requires:   rh-maven33-xmvn-launcher
Requires:   rh-maven33-xmvn-mojo
Requires:   rh-maven33-xmvn-parent-pom
Requires:   rh-maven33-xmvn-resolve
Requires:   rh-maven33-xmvn-subst
Requires:   rh-maven33-xmvn-tools-pom
Requires:   rh-maven33-xstream
Requires:   rh-maven33-xstream-benchmark

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
Requires:   %{?scl_prefix_java_common}maven-local
Requires:   %{name}-runtime = %{version}-%{release}
Requires:   %{?scl_prefix_java_common}scldevel

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

%changelog
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

