%{!?scl:%global scl maven30}
%scl_package %scl

Name:       %scl_name
Version:    1
Release:    19%{?dist}
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
Requires:   %{scl_name}-maven-local

%description runtime
Package shipping essential scripts to work with the %scl Software Collection.

%package build
Requires:   scl-utils-build
Requires:   %{name}-scldevel = %{version}-%{release}
Requires:   java-1.7.0-openjdk-devel
Summary:    Build support tools for the %scl Software Collection.

# provide these to workaround problems with initial build deps
Provides:   java = 1:1.7.0
Provides:   java-devel = 1:1.7.0
Provides:   javapackages-tools = 666
Provides:   jpackage-utils = 666
Provides:   mvn(com.sun:tools) = SYSTEM
Provides:   mvn(sun.jdk:jconsole) = SYSTEM

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
export PYTHONPATH="%{_scl_root}%{python_sitelib}\${PYTHONPATH:+:}\${PYTHONPATH:-}"

export JAVACONFDIRS="%{_sysconfdir}/java"
export XDG_CONFIG_DIRS="%{_sysconfdir}/xdg"
export XDG_DATA_DIRS="%{_datadir}"
EOF

%install
# Parentheses are needed here as workaround for rhbz#1017085
(%scl_install)

install -d -m 755 %{buildroot}%{_scl_scripts}
install -p -m 755 enable %{buildroot}%{_scl_scripts}/

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

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name}
%{_root_prefix}/lib/rpm/%{name}-javapackages-provides-wrapper
%{_root_prefix}/lib/rpm/%{name}-javapackages-requires-wrapper

%changelog
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

