%global giturl  https://github.com/kokoko3k/xt7-player-mpv
%global commit 6e211dfbc6af44f3f68e1d6da3f1c27db6c329fd
%global gitdate 20191030
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitrelease .%{gitdate}.git%{shortcommit}

Name:           xt7-player-mpv
Version:        0.31.3143
#Release:        0.1%%{?gitrelease}%%{?dist}
Release:        1%{?dist}
Summary:        Qt/Gambas gui to mpv media player
License:        GPLv3+
URL:            http://xt7-player.sourceforge.net/xt7forum/
#Source0:        %%{giturl}/archive/%%{commit}/%%{name}-%%{shortcommit}.tar.gz
Source0:        %{giturl}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gambas3-devel >= 3.8.4
BuildRequires:  gambas3-gb-args
BuildRequires:  gambas3-gb-compress
BuildRequires:  gambas3-gb-db
BuildRequires:  gambas3-gb-db-form
BuildRequires:  gambas3-gb-dbus
BuildRequires:  gambas3-gb-desktop
BuildRequires:  gambas3-gb-form
BuildRequires:  gambas3-gb-form-dialog
BuildRequires:  gambas3-gb-form-mdi
BuildRequires:  gambas3-gb-form-stock
BuildRequires:  gambas3-gb-gui
BuildRequires:  gambas3-gb-image
BuildRequires:  gambas3-gb-image-imlib
BuildRequires:  gambas3-gb-image-io
BuildRequires:  gambas3-gb-net
BuildRequires:  gambas3-gb-net-curl
BuildRequires:  gambas3-gb-qt5-ext
BuildRequires:  gambas3-gb-settings
BuildRequires:  gambas3-gb-signal
BuildRequires:  gambas3-gb-util-web
BuildRequires:  gambas3-gb-web
BuildRequires:  gambas3-gb-libxml
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  ImageMagick
Requires:       ffmpeg
Requires:       gambas3-gb-args
Requires:       gambas3-gb-compress
Requires:       gambas3-gb-dbus
Requires:       gambas3-gb-desktop
Requires:       gambas3-gb-form
Requires:       gambas3-gb-form-dialog
Requires:       gambas3-gb-form-mdi
Requires:       gambas3-gb-form-stock
Requires:       gambas3-gb-gui
Requires:       gambas3-gb-image
Requires:       gambas3-gb-net
Requires:       gambas3-gb-net-curl
Requires:       gambas3-gb-qt5-ext
Requires:       gambas3-gb-settings
Requires:       gambas3-gb-signal
Requires:       gambas3-gb-util-web
Requires:       gambas3-gb-web
Requires:       gambas3-gb-libxml
Requires:       gambas3-runtime >= 3.8.4
Requires:       hicolor-icon-theme
Requires:       mpv >= 0.14.0
Requires:       wget
Requires:       youtube-dl
BuildArch:      noarch

%description
Aims to be an (in)complete graphical interface to mpv, focused on
usability. It also provides extra features like youtube and shoutcast
integration, dvbt, media tagging, library and playlist managment and a lot
more.

%prep
%autosetup -p1 -n %{name}-%{version}
#%%autosetup -p1 -n %%{name}-%%{?commit}%%{?!commit:%%{version}}
sed -i '/project_group/d' xt7-player-mpv.appdata.xml

%build
gbc3 -e -a -g -t -p -m
gba3

%install
# executable
mkdir -p %{buildroot}%{_bindir}
# install -m755 %{name}-%{commit}.gambas %{buildroot}%{_bindir}/%{name}.gambas
install -m755 %{name}-%{version}.gambas %{buildroot}%{_bindir}/%{name}.gambas

#icons
for size in 256 48 32 16; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
  convert %{name}.png -resize ${size} %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

#menu entry
desktop-file-install %{name}.desktop\
       --dir %{buildroot}%{_datadir}/applications

mkdir -p %{buildroot}%{_datadir}/{applications,metainfo}
install -Dm 0644 xt7-player-mpv.appdata.xml %{buildroot}%{_metainfodir}/xt7-player-mpv.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%doc CHANGELOG_GIT
%license LICENSE.TXT
%{_bindir}/%{name}.gambas
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}*.xml

%changelog
* Wed Jan 29 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.31.3143-1
- Update to 0.31.3143

* Fri Nov 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.30.3140-0.1.20191030.git6e211df
- Update to 0.30.3140-0.1.20191030.git6e211df

* Sun Oct 27 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.29.3142-0.1.20191016.git3fac617
- Update to the latest git snapshot to fix compatibility with new mpv

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.29.3122-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.29.3122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Feb 25 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.29.3122-1
- Update to 0.29.3122

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.28.3100-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.28.3100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.28.3100-1
- Update to 0.28.3100
- Remove scriptlets

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.27.392-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.27.392-1
- Update to 27-392

* Thu Jul 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.26.392-1
- Update to 26-392

* Mon May 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.25.392-1
- Update to 25-392

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.24.392-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.24.392-1
- Update to 24-392

* Wed Nov 23 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.22.391-1
- Update to 0.22.391
- Update license tag to GPLv3+

* Thu Nov 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.21.384-1
- Update to 0.21.384
- remove gambas3-gb-qt4-ext 
- Add gambas3-gb-qt5-ext 

* Thu Sep 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.20.384-1
- Update to 0.20.384

* Mon Jul 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.18.1384-1
- Update to 0.18.1384

* Wed Jun 29 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.18.384-1
- Update to 0.18.384

* Sun Apr 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.17.384-1
- Update to 0.17.384

* Thu Mar 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.14.384-1
- Initial release
