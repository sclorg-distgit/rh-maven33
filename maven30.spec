%{!?scl_name_base:%global scl_name_base maven}
%{!?scl_name_version:%global scl_name_version 30}
%{!?scl:%global scl %{scl_name_base}%{scl_name_version}}
%scl_package %scl

%global debug_package %{nil}

Name:       %scl_name
Version:    1.1
Release:    19%{?dist}
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
# Obsolete packages which were shipped in RHSCL 1.2, but removed in RHSCL 2.0
Obsoletes:  %{scl_name}-ant < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-antlr < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-apache-bcel < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-apache-bsf < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-apache-log4j < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-apache-oro < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-apache-regexp < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-apache-resolver < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-apache-xalan2 < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-commons-logging < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-commons-net < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-javadoc < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-javamail < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-jdepend < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-jmf < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-jsch < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-junit < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-manual < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-swing < 1.9.2-9.21
Obsoletes:  %{scl_name}-ant-testutil < 1.9.2-9.21
Obsoletes:  %{scl_name}-antlr-C++ < 2.7.7-29.15.el7.x86_64
Obsoletes:  %{scl_name}-antlr-C++-doc < 2.7.7-29.15
Obsoletes:  %{scl_name}-antlr-javadoc < 2.7.7-29.15
Obsoletes:  %{scl_name}-antlr-manual < 2.7.7-29.15
Obsoletes:  %{scl_name}-antlr-tool < 2.7.7-29.15
Obsoletes:  %{scl_name}-apache-commons-beanutils < 1.8.3-14.12
Obsoletes:  %{scl_name}-apache-commons-beanutils-javadoc < 1.8.3-14.12
Obsoletes:  %{scl_name}-apache-commons-cli < 1.2-13.11
Obsoletes:  %{scl_name}-apache-commons-cli-javadoc < 1.2-13.11
Obsoletes:  %{scl_name}-apache-commons-codec < 1.8-7.11
Obsoletes:  %{scl_name}-apache-commons-codec-javadoc < 1.8-7.11
Obsoletes:  %{scl_name}-apache-commons-collections < 3.2.1-21.11
Obsoletes:  %{scl_name}-apache-commons-collections-javadoc < 3.2.1-21.11
Obsoletes:  %{scl_name}-apache-commons-collections-testframework < 3.2.1-21.11
Obsoletes:  %{scl_name}-apache-commons-collections-testframework-javadoc < 3.2.1-21.11
Obsoletes:  %{scl_name}-apache-commons-compress < 1.5-4.11
Obsoletes:  %{scl_name}-apache-commons-compress-javadoc < 1.5-4.11
Obsoletes:  %{scl_name}-apache-commons-dbcp < 1.4-17.11
Obsoletes:  %{scl_name}-apache-commons-dbcp-javadoc < 1.4-17.11
Obsoletes:  %{scl_name}-apache-commons-io < 1:2.4-12.10
Obsoletes:  %{scl_name}-apache-commons-io-javadoc < 1:2.4-12.10
Obsoletes:  %{scl_name}-apache-commons-lang < 2.6-15.10
Obsoletes:  %{scl_name}-apache-commons-lang-javadoc < 2.6-15.10
Obsoletes:  %{scl_name}-apache-commons-logging < 1.1.2-7.14
Obsoletes:  %{scl_name}-apache-commons-logging-javadoc < 1.1.2-7.14
Obsoletes:  %{scl_name}-apache-commons-net < 3.2-8.10
Obsoletes:  %{scl_name}-apache-commons-net-javadoc < 3.2-8.10
Obsoletes:  %{scl_name}-apache-commons-pool < 1.6-9.11
Obsoletes:  %{scl_name}-apache-commons-pool-javadoc < 1.6-9.11
Obsoletes:  %{scl_name}-atinject < 1-13.20100611svn86.8
Obsoletes:  %{scl_name}-atinject-javadoc < 1-13.20100611svn86.8
Obsoletes:  %{scl_name}-atinject-tck < 1-13.20100611svn86.8
Obsoletes:  %{scl_name}-batik < 1.8-0.12.svn1230816.12
Obsoletes:  %{scl_name}-batik-demo < 1.8-0.12.svn1230816.12
Obsoletes:  %{scl_name}-batik-javadoc < 1.8-0.12.svn1230816.12
Obsoletes:  %{scl_name}-batik-rasterizer < 1.8-0.12.svn1230816.12
Obsoletes:  %{scl_name}-batik-slideshow < 1.8-0.12.svn1230816.12
Obsoletes:  %{scl_name}-batik-squiggle < 1.8-0.12.svn1230816.12
Obsoletes:  %{scl_name}-batik-svgpp < 1.8-0.12.svn1230816.12
Obsoletes:  %{scl_name}-batik-ttf2svg < 1.8-0.12.svn1230816.12
Obsoletes:  %{scl_name}-bcel < 5.2-18.11
Obsoletes:  %{scl_name}-bcel-javadoc < 5.2-18.11
Obsoletes:  %{scl_name}-bea-stax < 1.2.0-9.12
Obsoletes:  %{scl_name}-bea-stax-api < 1.2.0-9.12
Obsoletes:  %{scl_name}-bea-stax-javadoc < 1.2.0-9.12
Obsoletes:  %{scl_name}-bsf < 2.4.0-19.11
Obsoletes:  %{scl_name}-bsf-javadoc < 2.4.0-19.11
Obsoletes:  %{scl_name}-dom4j < 1.6.1-20.10
Obsoletes:  %{scl_name}-dom4j-demo < 1.6.1-20.10
Obsoletes:  %{scl_name}-dom4j-javadoc < 1.6.1-20.10
Obsoletes:  %{scl_name}-dom4j-manual < 1.6.1-20.10
Obsoletes:  %{scl_name}-easymock < 1.2-22.13
Obsoletes:  %{scl_name}-easymock-javadoc < 1.2-22.13
Obsoletes:  %{scl_name}-easymock2 < 2.5.2-12.14
Obsoletes:  %{scl_name}-easymock2-javadoc < 2.5.2-12.14
Obsoletes:  %{scl_name}-ecj < 1:4.2.1-8.12.el7.x86_64
Obsoletes:  %{scl_name}-felix-framework < 4.2.1-5.10
Obsoletes:  %{scl_name}-felix-framework-javadoc < 4.2.1-5.10
Obsoletes:  %{scl_name}-geronimo-annotation < 1.0-15.11
Obsoletes:  %{scl_name}-geronimo-annotation-javadoc < 1.0-15.11
Obsoletes:  %{scl_name}-geronimo-jaspic-spec < 1.1-9.10
Obsoletes:  %{scl_name}-geronimo-jaspic-spec-javadoc < 1.1-9.10
Obsoletes:  %{scl_name}-geronimo-jta < 1.1.1-17.10
Obsoletes:  %{scl_name}-geronimo-jta-javadoc < 1.1.1-17.10
Obsoletes:  %{scl_name}-glassfish-el < 2.2.5-6.11
Obsoletes:  %{scl_name}-glassfish-el-api < 2.2.4-5.10
Obsoletes:  %{scl_name}-glassfish-el-api-javadoc < 2.2.4-5.10
Obsoletes:  %{scl_name}-glassfish-el-javadoc < 2.2.5-6.11
Obsoletes:  %{scl_name}-glassfish-jsp < 2.2.6-11.10
Obsoletes:  %{scl_name}-glassfish-jsp-api < 2.2.1-9.10
Obsoletes:  %{scl_name}-glassfish-jsp-api-javadoc < 2.2.1-9.10
Obsoletes:  %{scl_name}-glassfish-jsp-javadoc < 2.2.6-11.10
Obsoletes:  %{scl_name}-guava < 13.0-6.10
Obsoletes:  %{scl_name}-guava-javadoc < 13.0-6.10
Obsoletes:  %{scl_name}-hamcrest < 1.3-6.12
Obsoletes:  %{scl_name}-hamcrest-demo < 1.3-6.12
Obsoletes:  %{scl_name}-hamcrest-javadoc < 1.3-6.12
Obsoletes:  %{scl_name}-hawtjni < 1.6-9.11
Obsoletes:  %{scl_name}-hawtjni-javadoc < 1.6-9.11
Obsoletes:  %{scl_name}-isorelax < 1:0-0.15.release20050331.11
Obsoletes:  %{scl_name}-isorelax-javadoc < 1:0-0.15.release20050331.11
Obsoletes:  %{scl_name}-ivy-local < 4.3.2-1.4
Obsoletes:  %{scl_name}-jai-imageio-core < 1.2-0.14.20100217cvs.13
Obsoletes:  %{scl_name}-jai-imageio-core-javadoc < 1.2-0.14.20100217cvs.13
Obsoletes:  %{scl_name}-jakarta-commons-httpclient < 1:3.1-15.13
Obsoletes:  %{scl_name}-jakarta-commons-httpclient-demo < 1:3.1-15.13
Obsoletes:  %{scl_name}-jakarta-commons-httpclient-javadoc < 1:3.1-15.13
Obsoletes:  %{scl_name}-jakarta-commons-httpclient-manual < 1:3.1-15.13
Obsoletes:  %{scl_name}-jakarta-oro < 2.0.8-16.11
Obsoletes:  %{scl_name}-jakarta-oro-javadoc < 2.0.8-16.11
Obsoletes:  %{scl_name}-jakarta-taglibs-standard < 1.1.2-11.12
Obsoletes:  %{scl_name}-jakarta-taglibs-standard-javadoc < 1.1.2-11.12
Obsoletes:  %{scl_name}-jansi < 1.9-7.11
Obsoletes:  %{scl_name}-jansi-javadoc < 1.9-7.11
Obsoletes:  %{scl_name}-jansi-native < 1.4-10.11.el7.x86_64
Obsoletes:  %{scl_name}-jansi-native-javadoc < 1.4-10.11.el7.x86_64
Obsoletes:  %{scl_name}-java_cup < 1:0.11a-16.12
Obsoletes:  %{scl_name}-java_cup-javadoc < 1:0.11a-16.12
Obsoletes:  %{scl_name}-java_cup-manual < 1:0.11a-16.12
Obsoletes:  %{scl_name}-javamail < 1.4.6-8.11
Obsoletes:  %{scl_name}-javamail-javadoc < 1.4.6-8.11
Obsoletes:  %{scl_name}-javapackages-local < 4.3.2-1.4
Obsoletes:  %{scl_name}-javapackages-tools < 4.3.2-1.4
Obsoletes:  %{scl_name}-jaxen < 1.1.3-11.11
Obsoletes:  %{scl_name}-jaxen-demo < 1.1.3-11.11
Obsoletes:  %{scl_name}-jaxen-javadoc < 1.1.3-11.11
Obsoletes:  %{scl_name}-jcl-over-slf4j < 1.7.4-3.17
Obsoletes:  %{scl_name}-jdepend < 2.9.1-10.13
Obsoletes:  %{scl_name}-jdepend-demo < 2.9.1-10.13
Obsoletes:  %{scl_name}-jdepend-javadoc < 2.9.1-10.13
Obsoletes:  %{scl_name}-jdom < 1.1.3-6.12
Obsoletes:  %{scl_name}-jdom-demo < 1.1.3-6.12
Obsoletes:  %{scl_name}-jdom-javadoc < 1.1.3-6.12
Obsoletes:  %{scl_name}-jetty-annotations < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-ant < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-client < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-continuation < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-deploy < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-http < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-io < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-jaas < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-jaspi < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-javadoc < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-jmx < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-jndi < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-jsp < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-jspc-maven-plugin < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-maven-plugin < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-monitor < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-plus < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-project < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-proxy < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-rewrite < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-runner < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-security < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-server < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-servlet < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-servlets < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-start < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-util < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-util-ajax < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-webapp < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-websocket-api < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-websocket-client < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-websocket-common < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-websocket-parent < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-websocket-server < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-websocket-servlet < 9.0.3-8.14
Obsoletes:  %{scl_name}-jetty-xml < 9.0.3-8.14
Obsoletes:  %{scl_name}-jsch < 0.1.50-5.12
Obsoletes:  %{scl_name}-jsch-demo < 0.1.50-5.12
Obsoletes:  %{scl_name}-jsch-javadoc < 0.1.50-5.12
Obsoletes:  %{scl_name}-jsoup < 1.6.1-10.9
Obsoletes:  %{scl_name}-jsoup-javadoc < 1.6.1-10.9
Obsoletes:  %{scl_name}-jul-to-slf4j < 1.7.4-3.17
Obsoletes:  %{scl_name}-junit < 4.11-8.12
Obsoletes:  %{scl_name}-junit-demo < 4.11-8.12
Obsoletes:  %{scl_name}-junit-javadoc < 4.11-8.12
Obsoletes:  %{scl_name}-junit-manual < 4.11-8.12
Obsoletes:  %{scl_name}-jzlib < 1.1.1-6.9
Obsoletes:  %{scl_name}-jzlib-demo < 1.1.1-6.9
Obsoletes:  %{scl_name}-jzlib-javadoc < 1.1.1-6.9
Obsoletes:  %{scl_name}-log4j < 1.2.17-15.13
Obsoletes:  %{scl_name}-log4j-javadoc < 1.2.17-15.13
Obsoletes:  %{scl_name}-log4j-manual < 1.2.17-15.13
Obsoletes:  %{scl_name}-log4j-over-slf4j < 1.7.4-3.17
Obsoletes:  %{scl_name}-maven-hawtjni-plugin < 1.6-9.11
Obsoletes:  %{scl_name}-maven-local < 4.3.2-1.4
Obsoletes:  %{scl_name}-msv-demo < 1:2013.5.1-6.13
Obsoletes:  %{scl_name}-msv-javadoc < 1:2013.5.1-6.13
Obsoletes:  %{scl_name}-msv-manual < 1:2013.5.1-6.13
Obsoletes:  %{scl_name}-msv-msv < 1:2013.5.1-6.13
Obsoletes:  %{scl_name}-msv-rngconv < 1:2013.5.1-6.13
Obsoletes:  %{scl_name}-msv-xmlgen < 1:2013.5.1-6.13
Obsoletes:  %{scl_name}-msv-xsdlib < 1:2013.5.1-6.13
Obsoletes:  %{scl_name}-nekohtml < 1.9.14-13.12
Obsoletes:  %{scl_name}-nekohtml-demo < 1.9.14-13.12
Obsoletes:  %{scl_name}-nekohtml-javadoc < 1.9.14-13.12
Obsoletes:  %{scl_name}-objectweb-asm < 3.3.1-9.13
Obsoletes:  %{scl_name}-objectweb-asm-javadoc < 3.3.1-9.13
Obsoletes:  %{scl_name}-python-javapackages < 4.3.2-1.4
Obsoletes:  %{scl_name}-qdox < 1.12.1-9.12
Obsoletes:  %{scl_name}-qdox-javadoc < 1.12.1-9.12
Obsoletes:  %{scl_name}-regexp < 1.5-13.13
Obsoletes:  %{scl_name}-regexp-javadoc < 1.5-13.13
Obsoletes:  %{scl_name}-relaxngDatatype < 1.0-11.10
Obsoletes:  %{scl_name}-relaxngDatatype-javadoc < 1.0-11.10
Obsoletes:  %{scl_name}-slf4j < 1.7.4-3.17
Obsoletes:  %{scl_name}-slf4j-api < 1.7.4-3.17
Obsoletes:  %{scl_name}-slf4j-javadoc < 1.7.4-3.17
Obsoletes:  %{scl_name}-slf4j-jdk14 < 1.7.4-3.17
Obsoletes:  %{scl_name}-slf4j-migrator < 1.7.4-3.17
Obsoletes:  %{scl_name}-slf4j-nop < 1.7.4-3.17
Obsoletes:  %{scl_name}-slf4j-parent < 1.7.4-3.17
Obsoletes:  %{scl_name}-slf4j-simple < 1.7.4-3.17
Obsoletes:  %{scl_name}-slf4j-site < 1.7.4-3.17
Obsoletes:  %{scl_name}-tomcat-el-2.2-api < 7.0.42-1.17
Obsoletes:  %{scl_name}-tomcat-javadoc < 7.0.42-1.17
Obsoletes:  %{scl_name}-tomcat-jsp-2.2-api < 7.0.42-1.17
Obsoletes:  %{scl_name}-tomcat-lib < 7.0.42-1.17
Obsoletes:  %{scl_name}-tomcat-servlet-3.0-api < 7.0.42-1.17
Obsoletes:  %{scl_name}-ws-commons-util < 1.0.1-29.11
Obsoletes:  %{scl_name}-ws-commons-util-javadoc < 1.0.1-29.11
Obsoletes:  %{scl_name}-ws-jaxme < 0.5.2-10.10
Obsoletes:  %{scl_name}-ws-jaxme-javadoc < 0.5.2-10.10
Obsoletes:  %{scl_name}-ws-jaxme-manual < 0.5.2-10.10
Obsoletes:  %{scl_name}-xalan-j2 < 2.7.1-23.6
Obsoletes:  %{scl_name}-xalan-j2-demo < 2.7.1-23.6
Obsoletes:  %{scl_name}-xalan-j2-javadoc < 2.7.1-23.6
Obsoletes:  %{scl_name}-xalan-j2-manual < 2.7.1-23.6
Obsoletes:  %{scl_name}-xalan-j2-xsltc < 2.7.1-23.6
Obsoletes:  %{scl_name}-xbean < 3.13-6.10
Obsoletes:  %{scl_name}-xbean-javadoc < 3.13-6.10
Obsoletes:  %{scl_name}-xerces-j2 < 2.11.0-17.6
Obsoletes:  %{scl_name}-xerces-j2-demo < 2.11.0-17.6
Obsoletes:  %{scl_name}-xerces-j2-javadoc < 2.11.0-17.6
Obsoletes:  %{scl_name}-xml-commons-resolver < 1.2-15.12
Obsoletes:  %{scl_name}-xml-commons-resolver-javadoc < 1.2-15.12
Obsoletes:  %{scl_name}-xmlrpc-client < 1:3.1.3-8.12
Obsoletes:  %{scl_name}-xmlrpc-common < 1:3.1.3-8.12
Obsoletes:  %{scl_name}-xmlrpc-javadoc < 1:3.1.3-8.12
Obsoletes:  %{scl_name}-xmlrpc-server < 1:3.1.3-8.12
Obsoletes:  %{scl_name}-xpp3 < 1.1.3.8-11.11
Obsoletes:  %{scl_name}-xpp3-javadoc < 1.1.3.8-11.11
Obsoletes:  %{scl_name}-xpp3-minimal < 1.1.3.8-11.11
Obsoletes:  %{scl_name}-xz-java < 1.3-3.11
Obsoletes:  %{scl_name}-xz-java-javadoc < 1.3-3.11

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
%{_javaconfdir}/*
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

