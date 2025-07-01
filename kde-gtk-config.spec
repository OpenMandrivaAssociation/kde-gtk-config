%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	GTK2 and GTK3 configurator for KDE
Name:		kde-gtk-config
Version:	6.4.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		System/Libraries
Url:		https://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kde-gtk-config/-/archive/%{gitbranch}/kde-gtk-config-%{gitbranchd}.tar.bz2#/kde-gtk-config-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/kde-gtk-config-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KDecoration3)
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(pango)
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	xsettingsd
BuildRequires:	sassc
Requires:	plasma6-kde-cli-tools
Requires:	xsettingsd
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed after 6.0 2026-05-01
%rename plasma6-kde-gtk-config

%description
Configuration dialog to adapt GTK applications appearance to your taste
under KDE. Among its many features, it lets you:
- Choose which theme is used for GTK2 and GTK3 applications.
- Tweak some GTK applications behaviour.
- Select what icon theme to use in GTK applications.
- Select GTK applications default fonts.
- Easily browse and install new GTK2 and GTK3 themes.

%files
%{_libdir}/libexec/*
%{_libdir}/kconf_update_bin/gtk_theme
%{_qtdir}/plugins/kf6/kded/gtkconfig.so
%{_datadir}/kconf_update/gtkconfig.upd
%{_libdir}/gtk-3.0/modules/libcolorreload-gtk-module.so
%{_libdir}/gtk-3.0/modules/libwindow-decorations-gtk-module.so
%{_datadir}/themes/Breeze/window_decorations.css
%{_datadir}/kconf_update/remove_window_decorations_from_gtk_css.sh
%{_datadir}/kcm-gtk-module/preview.ui
%{_datadir}/qlogging-categories6/kde-gtk-config.categories
%{_libdir}/kconf_update_bin/remove_deprecated_gtk4_option
