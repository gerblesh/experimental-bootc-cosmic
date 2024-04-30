# This metadata goes unused. We are just reusing the .spec file format as a way
# to declare requirements basically. Note that everything here must be
# BuildRequires as we use `dnf builddep` to install things.
Name:           fedora-container-minimal
Version:        0
Release:        0
Summary:        Container minimal image
License:        ASL 2.0

# NOTE! This magical comment is interpreted to pass `--setopt=install_weak_deps=0` to dnf
# Recommends: false

BuildRequires: fedora-release-container
BuildRequires: rpm
BuildRequires: bash
BuildRequires: coreutils
BuildRequires: glibc-minimal-langpack
BuildRequires: util-linux-core

# SELinux workaround
# BuildRequires: policycoreutils


%description
%{summary}
