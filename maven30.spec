%{!?scl:%global scl maven30}
%scl_package %scl

Name:       %scl_name
Version:    1
Release:    4%{?dist}
Summary:    Package that installs %scl

License:    GPLv2+
#URL:         
Source1:    macros.%{scl_name}
Source2:    %{scl_name}-javapackages-provides-wrapper
Source3:    %{scl_name}-javapackages-requires-wrapper

BuildRequires:    scl-utils-build

# This should eventually pull in maven itself
Requires:         %{name}-runtime

%description
This is the main package for the %scl Software Collection.

%package common
Summary:          Package containing common parts of %{scl}-runtime and %{scl}-build sub packages.

%description common
%{summary}

%package runtime
Summary:    Package that handles %scl Software Collection.
Requires:   scl-utils
Requires:   %{name}-common = %{version}-%{release}

%description runtime
Package shipping essential scripts to work with the %scl Software Collection.

%package build
Requires:   scl-utils-build
Requires:   %{name}-scldevel = %{version}-%{release}
Summary:    Build support tools for the %scl Software Collection.

# provide this to workaround problems with initial build deps
Provides:   java = 1:1.7.0

%description build
Package shipping essential configuration marcros/files in order to be able
to build %scl Software Collection.

%package scldevel
Requires:   %{name}-common = %{version}-%{release}
Summary:    Package shipping development files for %scl

%description scldevel
Package shipping development files, especially useful for development of
packages depending on %scl Software Collection.

%prep
%setup -c -T
#===================#
# SCL enable script #
#===================#
cat <<EOF >enable
# Generic variables
export PATH="%{_bindir}:\${PATH:-/bin:/usr/bin}"
export MANPATH="%{_mandir}:\${MANPATH}"

# Needed by Java Packages Tools to locate java.conf
export JAVACONFDIRS="%{_sysconfdir}/java:\${JAVACONFDIRS:-/etc/java}"

# Required by XMvn to locate its configuration file(s)
export XDG_CONFIG_DIRS="%{_sysconfdir}/xdg:\${XDG_CONFIG_DIRS:-/etc/xdg}"

# Not really needed by anything for now, but kept for consistency with
# XDG_CONFIG_DIRS.
export XDG_DATA_DIRS="%{_datadir}:\${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"
EOF

#===========#
# java.conf #
#===========#
cat <<EOF >java.conf
# Java configuration file for %{scl} software collection.
JAVA_LIBDIR=%{_javadir}
JNI_LIBDIR=%{_jnidir}
JVM_ROOT=%{_jvmdir}
EOF

#=============#
# XMvn config #
#=============#
cat <<EOF >configuration.xml
<!-- XMvn configuration file for %{scl} software collection -->
<configuration>
  <resolverSettings>
    <prefixes>
      <prefix>/opt/rh/%{scl}/root</prefix>
    </prefixes>
  </resolverSettings>
  <installerSettings>
    <metadataDir>opt/rh/%{scl}/root/usr/share/maven-fragments</metadataDir>
  </installerSettings>
  <repositories>
    <repository>
      <id>%{scl}-resolve</id>
      <type>compound</type>
      <properties>
        <prefix>opt/rh/%{scl}/root</prefix>
        <namespace>%{scl}</namespace>
      </properties>
      <configuration>
        <repositories>
          <repository>base-resolve</repository>
        </repositories>
      </configuration>
    </repository>
    <repository>
      <id>resolve-system</id>
      <type>compound</type>
      <properties>
        <prefix>/</prefix>
      </properties>
      <configuration>
        <repositories>
          <repository>%{scl}-resolve</repository>
          <repository>base-resolve</repository>
        </repositories>
      </configuration>
    </repository>
    <repository>
      <id>install</id>
      <type>compound</type>
      <properties>
        <prefix>opt/rh/%{scl}/root</prefix>
        <namespace>%{scl}</namespace>
      </properties>
      <configuration>
        <repositories>
          <repository>base-install</repository>
        </repositories>
      </configuration>
    </repository>
    <repository>
      <id>install-raw-pom</id>
      <type>compound</type>
      <properties>
        <prefix>opt/rh/%{scl}/root</prefix>
        <namespace>%{scl}</namespace>
      </properties>
      <configuration>
        <repositories>
          <repository>base-raw-pom</repository>
        </repositories>
      </configuration>
    </repository>
    <repository>
      <id>install-effective-pom</id>
      <type>compound</type>
      <properties>
        <prefix>opt/rh/%{scl}/root</prefix>
        <namespace>%{scl}</namespace>
      </properties>
      <configuration>
        <repositories>
          <repository>base-effective-pom</repository>
        </repositories>
      </configuration>
    </repository>
  </repositories>
</configuration>
EOF

%install
# Parentheses are needed here as workaround for rhbz#1017085
(%scl_install)

install -d -m 755 %{buildroot}%{_scl_scripts}
install -p -m 755 enable %{buildroot}%{_scl_scripts}/

install -d -m 755 %{buildroot}%{_sysconfdir}/java
install -p -m 644 java.conf %{buildroot}%{_sysconfdir}/java/

install -d -m 755 %{buildroot}%{_sysconfdir}/xdg/xmvn
install -p -m 644 configuration.xml %{buildroot}%{_sysconfdir}/xdg/xmvn/

# install rpm magic
install -Dpm0644 %{SOURCE1} %{buildroot}%{_root_sysconfdir}/rpm/macros.%{name}
install -Dpm0755 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/%{name}-javapackages-provides-wrapper
install -Dpm0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/%{name}-javapackages-requires-wrapper

# Empty package (no file content).  The sole purpose of this package
# is collecting its dependencies so that the whole SCL can be
# installed by installing %{name}.
%files

# Runtime doesn't have files, they are owned by the shared subpackage.
# Why? Because we need enable and other config files in the build package
# as well. It would be bad for build to require runtime.
%files runtime

%files common
%{scl_files}
%{_sysconfdir}/java/java.conf
%{_sysconfdir}/xdg/xmvn/configuration.xml

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name}
%{_root_prefix}/lib/rpm/%{name}-javapackages-provides-wrapper
%{_root_prefix}/lib/rpm/%{name}-javapackages-requires-wrapper

%changelog
* Fri Feb 07 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-4
- Add epoch to provides to match original

* Fri Feb 07 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-3
- Build-provide java 1.7.0

* Wed Feb 05 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-2
- Make scl-utils requires unversioned

* Wed Feb 05 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-1
- Initial maven30 scl metapackage

