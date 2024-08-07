# This metadata goes unused. We are just reusing the .spec file format as a way
# to declare requirements basically. Note that everything here must be
# BuildRequires as we use `dnf builddep` to install things.
Name:           fedora-cosmic
Version:        0
Release:        0
Summary:        Base image
License:        ASL 2.0

BuildRequires: kernel
BuildRequires: kernel-modules
BuildRequires: kernel-modules-extra
BuildRequires: git-core
BuildRequires: git-core-doc
BuildRequires: lvm2
BuildRequires: nss-altfiles
BuildRequires: buildah
BuildRequires: podman
BuildRequires: skopeo
BuildRequires: slirp4netns
BuildRequires: systemd-container
BuildRequires: ncurses
BuildRequires: flatpak
BuildRequires: xdg-desktop-portal
BuildRequires: hfsplus-tools
BuildRequires: fedora-repos-ostree
BuildRequires: fedora-repos-archive
BuildRequires: langpacks-en

BuildRequires: NetworkManager
BuildRequires: NetworkManager-bluetooth
BuildRequires: NetworkManager-config-connectivity-fedora
BuildRequires: NetworkManager-wifi
BuildRequires: NetworkManager-wwan
BuildRequires: acl
BuildRequires: alsa-ucm
BuildRequires: alsa-utils
BuildRequires: amd-gpu-firmware
BuildRequires: at-spi2-atk
BuildRequires: at-spi2-core
BuildRequires: atheros-firmware
BuildRequires: attr
BuildRequires: audit
BuildRequires: b43-fwcutter
BuildRequires: b43-openfwwf
BuildRequires: basesystem
BuildRequires: bash
BuildRequires: bash-color-prompt
BuildRequires: bash-completion
BuildRequires: bc
BuildRequires: bind-utils
BuildRequires: bluez-cups
BuildRequires: brcmfmac-firmware
BuildRequires: brltty
BuildRequires: btrfs-progs
BuildRequires: bzip2
BuildRequires: chrony
BuildRequires: cifs-utils
BuildRequires: colord
BuildRequires: compsize
BuildRequires: coreutils
BuildRequires: cpio
BuildRequires: cryptsetup
BuildRequires: cups
BuildRequires: cups-browsed
BuildRequires: cups-filters
BuildRequires: curl
BuildRequires: cyrus-sasl-plain
BuildRequires: default-editor
BuildRequires: default-fonts-cjk-mono
BuildRequires: default-fonts-cjk-sans
BuildRequires: default-fonts-cjk-serif
BuildRequires: default-fonts-core-emoji
BuildRequires: default-fonts-core-math
BuildRequires: default-fonts-core-mono
BuildRequires: default-fonts-core-sans
BuildRequires: default-fonts-core-serif
BuildRequires: default-fonts-other-mono
BuildRequires: default-fonts-other-sans
BuildRequires: default-fonts-other-serif
BuildRequires: dhcp-client
BuildRequires: dnsmasq
BuildRequires: e2fsprogs
BuildRequires: ethtool
BuildRequires: exfatprogs
BuildRequires: fedora-bookmarks
BuildRequires: fedora-chromium-config
BuildRequires: fedora-flathub-remote
BuildRequires: fedora-workstation-backgrounds
BuildRequires: fedora-workstation-repositories
BuildRequires: file
BuildRequires: filesystem
BuildRequires: firefox
BuildRequires: firewalld
BuildRequires: fpaste
BuildRequires: fros-gnome
BuildRequires: fwupd
BuildRequires: gamemode
BuildRequires: glibc
BuildRequires: glibc-all-langpacks
BuildRequires: gnupg2
BuildRequires: gstreamer1-plugin-libav
BuildRequires: gstreamer1-plugins-bad-free
BuildRequires: gstreamer1-plugins-good
BuildRequires: gstreamer1-plugins-ugly-free
BuildRequires: gutenprint
BuildRequires: gutenprint-cups
BuildRequires: hostname
BuildRequires: hplip
BuildRequires: hunspell
BuildRequires: ibus-anthy
BuildRequires: ibus-chewing
BuildRequires: ibus-gtk3
BuildRequires: ibus-gtk4
BuildRequires: ibus-hangul
BuildRequires: ibus-libpinyin
BuildRequires: ibus-m17n
BuildRequires: ibus-typing-booster
BuildRequires: intel-gpu-firmware
BuildRequires: iproute
BuildRequires: iptables-nft
BuildRequires: iptstate
BuildRequires: iputils
BuildRequires: iwlegacy-firmware
BuildRequires: iwlwifi-dvm-firmware
BuildRequires: iwlwifi-mvm-firmware
BuildRequires: kbd
BuildRequires: less
BuildRequires: libertas-firmware
BuildRequires: libglvnd-gles
BuildRequires: linux-firmware
BuildRequires: logrotate
BuildRequires: lrzsz
BuildRequires: lsof
BuildRequires: man-db
BuildRequires: man-pages
BuildRequires: mdadm
BuildRequires: mesa-dri-drivers
BuildRequires: mesa-vulkan-drivers
BuildRequires: mpage
BuildRequires: mt7xxx-firmware
BuildRequires: mtr
BuildRequires: nfs-utils
BuildRequires: nss-altfiles
BuildRequires: nss-mdns
BuildRequires: ntfs-3g
BuildRequires: ntfsprogs
BuildRequires: nvidia-gpu-firmware
BuildRequires: nxpwireless-firmware
BuildRequires: opensc
BuildRequires: openssh-clients
BuildRequires: openssh-server
BuildRequires: orca
BuildRequires: pam_afs_session
BuildRequires: paps
BuildRequires: passwdqc
BuildRequires: pciutils
BuildRequires: pinfo
BuildRequires: pipewire-alsa
BuildRequires: pipewire-gstreamer
BuildRequires: pipewire-pulseaudio
BuildRequires: pipewire-utils
BuildRequires: plocate
BuildRequires: plymouth
BuildRequires: plymouth-system-theme
BuildRequires: policycoreutils
BuildRequires: policycoreutils-python-utils
BuildRequires: procps-ng
BuildRequires: psmisc
BuildRequires: qemu-guest-agent
BuildRequires: qt5-qtbase
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtdeclarative
BuildRequires: qt5-qtxmlpatterns
BuildRequires: quota
BuildRequires: realmd
BuildRequires: realtek-firmware
BuildRequires: rootfiles
BuildRequires: rpm
BuildRequires: rpm-ostree
BuildRequires: rsync
BuildRequires: samba-client
BuildRequires: selinux-policy-targeted
BuildRequires: setup
BuildRequires: shadow-utils
BuildRequires: sos
BuildRequires: speech-dispatcher
BuildRequires: spice-vdagent
BuildRequires: spice-webdavd
BuildRequires: sssd-common
BuildRequires: sssd-kcm
BuildRequires: sudo
BuildRequires: system-config-printer-udev
BuildRequires: systemd
BuildRequires: systemd-oomd-defaults
BuildRequires: systemd-resolved
BuildRequires: systemd-udev
BuildRequires: tar
BuildRequires: time
BuildRequires: tiwilink-firmware
BuildRequires: toolbox
BuildRequires: tree
BuildRequires: unzip
BuildRequires: uresourced
BuildRequires: usb_modeswitch
BuildRequires: usbutils
BuildRequires: util-linux
BuildRequires: vim-minimal
BuildRequires: wget2-wget
BuildRequires: which
BuildRequires: whois
BuildRequires: wireplumber
BuildRequires: words
BuildRequires: wpa_supplicant
BuildRequires: zip
BuildRequires: zram-generator-defaults



BuildRequires: fedora-release
BuildRequires: fedora-release-ostree-desktop
BuildRequires: xorg-x11-server-Xwayland
BuildRequires: xdg-desktop-portal-gtk

BuildRequires: firewall-config
BuildRequires: glx-utils
BuildRequires: mesa-dri-drivers
BuildRequires: mesa-vulkan-drivers
BuildRequires: plymouth-system-theme

%ifarch x86_64
BuildRequires: alsa-sof-firmware
BuildRequires: amd-ucode-firmware
BuildRequires: cirrus-audio-firmware
BuildRequires: hyperv-daemons
BuildRequires: intel-audio-firmware
BuildRequires: libva-intel-media-driver
BuildRequires: mcelog
BuildRequires: microcode_ctl
BuildRequires: open-vm-tools-desktop
BuildRequires: thermald
BuildRequires: virtualbox-guest-additions
%endif

%ifarch aarch64
BuildRequires: hyperv-daemons
BuildRequires: open-vm-tools-desktop
BuildRequires: pd-mapper
BuildRequires: qcom-firmware
BuildRequires: qrtr
BuildRequires: rmtfs
%endif

%ifarch ppc64le
BuildRequires: lsvpd
BuildRequires: powerpc-utils
%endif

BuildRequires: cosmic-desktop

%description
%{summary}
