Summary:	GTK2 and GTK3 configurator for KDE
Name:		kde-gtk-config
Version:	5.5.0
Release:	1
License:	GPLv3
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/base/kde-gtk-config
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Core)

%description
Configuration dialog to adapt GTK applications appearance to your taste
under KDE. Among its many features, it lets you:
- Choose which theme is used for GTK2 and GTK3 applications.
- Tweak some GTK applications behaviour.
- Select what icon theme to use in GTK applications.
- Select GTK applications default fonts.
- Easily browse and install new GTK2 and GTK3 themes.

%prep
%setup -q

%build
export CC=gcc
export CXX=g++
%cmake_kde5
%ninja

%install
%ninja_install -C build

%files
%doc README COPYING ChangeLog
%{_kde5_libdir}/libexec/gtk_preview
%{_kde5_libdir}/libexec/gtk3_preview
%{_kde5_libdir}/libexec/reload_gtk_apps
%{_kde5_datadir}/kcm-gtk-module/preview.ui
%{_sysconfdir}/xdg/cgcgtk3.knsrc
%{_sysconfdir}/xdg/cgcicon.knsrc
%{_sysconfdir}/xdg/cgctheme.knsrc
%{_kde5_iconsdir}/hicolor/*/apps/kde-gtk-config.*
%{_kde5_services}/kde-gtk-config.desktop
%{_libdir}/qt5/plugins/kcm_kdegtkconfig.so
