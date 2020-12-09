##Init variables

%global packageVer 1.4

## Package info declaration

Name:           multimc
Version:        %{packageVer}
Release:        1%{?dist}
Summary:        Free, open source launcher and instance manager for Minecraft

License:        ASL 2.0
URL:            https://multimc.org/
Source0:        %{name}-%{packageVer}.tar.gz

ExclusiveArch:  %{ix86} x86_64

Requires:       bash wget qt5-qtbase zenity

%description
Free, open source launcher and instance manager for Minecraft.

%prep

%setup -q

%install
##Installs directories
install -dm 755 %{buildroot}/usr/{bin,share/{applications,MultiMC,icons/hicolor/scalable/apps}}

##Installs icon and run.sh
install -m 644 %{_builddir}/multimc-%{packageVer}/multimc.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/multimc.svg
install -m 755 %{_builddir}/multimc-%{packageVer}/run.sh %{buildroot}%{_datadir}/MultiMC/run.sh

##Generates and installs desktop file to /usr/share/applications
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF

## Desktop File

[Desktop Entry]
Version=%{packageVer}
Name=MultiMC
GenericName=MultiMC Launcher
Comment=Free, open source launcher and instance manager for Minecraft.
Type=Application
Terminal=false
Exec=%{_datadir}/MultiMC/run.sh
Icon=multimc
Categories=Game
Keywords=game;minecraft;
EOF

%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/multimc.svg
%{_datadir}/MultiMC/
%{_datadir}/MultiMC/run.sh

%changelog
* Wed Dec 09 2020 Jack Greiner <jack@emoss.org> - 1.4-1%{?dist}
- Changed from installing into opt.
* Thu Jun 18 2020 Jack Greiner <jack@emoss.org> - 1.3-1%{?dist}
- Fixed builds in Copr.
* Mon Jun 8 2020 Jack Greiner <jack@emoss.org> - 1.2-1%{?dist}
- Updated in-line documentation
* Fri Jun 5 2020 Jack Greiner <jack@emoss.org> - 1.0-1%{?dist}
- Updated in-line documentation
* Mon Jun 1 2020 Jack Greiner <jack@emoss.org> - 1.0-1%{?dist}
- Created initial spec file.
